# -*- coding: utf-8 -*-
import json, base64, os, re, sys, io
from collections import Counter
sys.path.insert(0, os.path.dirname(__file__))
import psi_data as D

HERE = os.path.dirname(os.path.abspath(__file__))
SLIDES = HERE + '/slides'          # slides já reduzidos (880 px, JPEG q64), gerados por extrair_slides.py
APP1 = HERE + '/../neuroanatomia/app.html'   # o CSS é compartilhado com o app de Neuroanatomia
TEMPLATE = HERE + '/psi_app.html'

# ---- valida e numera ----
names = [c['nome'] for c in D.CONC]
dup = [n for n, k in Counter(names).items() if k > 1]
assert not dup, f'nomes repetidos: {dup}'
defs0 = [c['defs'][0] for c in D.CONC]
dup = [n[:50] for n, k in Counter(defs0).items() if k > 1]
assert not dup, f'definições repetidas: {dup}'
bands = {b for b, _ in D.BANDS}
for c in D.CONC:
    assert c['tema'] in D.TEMAS, c['nome']
    assert c['faixa'] is None or c['faixa'] in bands, (c['nome'], c['faixa'])
    for s in c['slides']:
        assert os.path.exists(f'{SLIDES}/{s}.jpg'), f'slide ausente: {s} (rode extrair_slides.py)'


def slide_no(k):
    return int(k.split('_')[1])


def fonte(c):
    by = {}
    for s in c['slides']:
        by.setdefault(s.split('_')[0], []).append(slide_no(s))
    parts = []
    for k, nums in by.items():
        nums = sorted(set(nums))
        parts.append(f"{'Slide' if len(nums) == 1 else 'Slides'} {', '.join(map(str, nums))} · {D.TEMAS[k]['doc']}")
    return ' | '.join(parts) if parts else '—'


conc = []
used = []
for i, c in enumerate(D.CONC, 1):
    sl = []
    for s in c['slides']:
        sl.append([s, f"Slide {slide_no(s)} · {D.TEMAS[s.split('_')[0]]['doc']}"])
        if s not in used:
            used.append(s)
    conc.append({'id': i, 'nome': c['nome'], 'tema': c['tema'], 'sub': c['sub'], 'defs': c['defs'], 'det': c['det'],
                 'quando': c['quando'], 'faixa': c['faixa'], 'curto': c['curto'], 'extra': c['extra'],
                 'slides': sl, 'fonte': fonte(c)})

# ---- imagens dos slides ----
imgs = {}
total = 0
for k in used:
    raw = open(f'{SLIDES}/{k}.jpg', 'rb').read()
    total += len(raw)
    imgs[k] = 'data:image/jpeg;base64,' + base64.b64encode(raw).decode()

css = re.search(r'<style>(.*?)</style>', open(APP1, encoding='utf-8').read(), re.S).group(1)


def jdump(o):
    return json.dumps(o, ensure_ascii=False, separators=(',', ':')).replace('<', '\\u003c').replace('\u2028', '\\u2028')


def build(target, home):
    data = {'temas': D.TEMAS, 'bands': D.BANDS, 'conc': conc, 'home': home}
    html = open(TEMPLATE, encoding='utf-8').read()
    html = html.replace('/*__CSS__*/', css).replace('__DATA__', jdump(data)).replace('__IMAGES__', jdump(imgs))
    os.makedirs(os.path.dirname(target), exist_ok=True)
    open(target, 'w', encoding='utf-8').write(html)
    return round(os.path.getsize(target) / 1e6, 2)


if __name__ == '__main__':
    out = sys.argv[1]
    home = sys.argv[2]
    mb = build(out, home)
    cnt = Counter(c['tema'] for c in conc)
    print('conceitos:', len(conc), dict(cnt), '| com idade (linha do tempo):', sum(1 for c in conc if c['faixa']),
          '| slides usados:', len(used), '| imagens KB:', total // 1024, '| arquivo MB:', mb)
