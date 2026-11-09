# -*- coding: utf-8 -*-
"""Monta os apps a partir do fonte.

  python fonte/construir.py                 -> gera o site na raiz do repositório
                                               (index.html, neuroanatomia/, desenvolvimento/)
  python fonte/construir.py --local PASTA   -> gera os 3 arquivos para uso offline numa pasta
                                               (Menu de Estudos.html, Neuroanatomia - Alfinetes.html,
                                                Desenvolvimento Humano.html)
"""
import os, subprocess, sys

FONTE = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(FONTE)
PY = sys.executable


def run(script, *args):
    env = dict(os.environ, PYTHONIOENCODING='utf-8')
    r = subprocess.run([PY, '-X', 'utf8', os.path.join(FONTE, script), *args], capture_output=True, text=True, encoding='utf-8', env=env)
    if r.returncode != 0:
        print(r.stdout, r.stderr)
        raise SystemExit(f'falhou: {script}')
    print(r.stdout.strip())


def site():
    run('neuroanatomia/build.py', os.path.join(RAIZ, 'neuroanatomia', 'index.html'), '../')
    run('desenvolvimento/build_psi.py', os.path.join(RAIZ, 'desenvolvimento', 'index.html'), '../')
    run('menu/build_hub.py', os.path.join(RAIZ, 'index.html'), 'neuroanatomia/', 'desenvolvimento/')


def local(pasta):
    menu = 'Menu de Estudos.html'
    neuro = 'Neuroanatomia - Alfinetes.html'
    dev = 'Desenvolvimento Humano.html'
    run('neuroanatomia/build.py', os.path.join(pasta, neuro), menu)
    run('desenvolvimento/build_psi.py', os.path.join(pasta, dev), menu)
    run('menu/build_hub.py', os.path.join(pasta, menu), neuro, dev)


if __name__ == '__main__':
    if len(sys.argv) >= 3 and sys.argv[1] == '--local':
        local(sys.argv[2])
    elif len(sys.argv) == 1:
        site()
    else:
        raise SystemExit(__doc__)
