# -*- coding: utf-8 -*-
"""Gera slides/*.jpg a partir dos PDFs de Desenvolvimento Humano (só é preciso se os slides mudarem).

Uso: python extrair_slides.py "pasta/com/os/PDFs"
"""
import os, sys
import pymupdf
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import psi_data as D

PDFS = {
    'nasc': 'Nascimento e Primeira Infância.pdf',
    'fis': 'Desenvolvimento físico.pdf',
    'perc': 'Desenvolvimento perceptual.pdf',
    'cogn': 'Desenvolvimento cognitivo.pdf',
    'ling': 'Desenvolvimento da linguagem.pdf',
}
W, Q = 880, 64

if len(sys.argv) < 2:
    raise SystemExit(__doc__)
pasta = sys.argv[1]
os.makedirs(HERE + '/slides', exist_ok=True)
usados = []
for c in D.CONC:
    for k in c['slides']:
        if k not in usados:
            usados.append(k)
docs = {}
for k in usados:
    tema, pg = k.split('_')
    if tema not in docs:
        docs[tema] = pymupdf.open(os.path.join(pasta, PDFS[tema]))
    pix = docs[tema][int(pg) - 1].get_pixmap(matrix=pymupdf.Matrix(2, 2), alpha=False)
    im = Image.frombytes('RGB', (pix.width, pix.height), pix.samples)
    im = im.resize((W, round(W * 9 / 16)), Image.LANCZOS)
    im.save(f'{HERE}/slides/{k}.jpg', 'JPEG', quality=Q, optimize=True, progressive=True)
print('slides gerados:', len(usados))
