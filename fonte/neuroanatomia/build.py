# -*- coding: utf-8 -*-
import json, base64, os, sys
sys.path.insert(0, os.path.dirname(__file__))
import data as D

HERE = os.path.dirname(__file__)
OUT = HERE + '/out'
manifest = json.load(open(OUT + '/manifest.json', encoding='utf-8'))
TARGET = sys.argv[1] if len(sys.argv) > 1 else r'C:/Users/User/Downloads/Material Duda/Neuroanatomia - Alfinetes.html'
HOME = sys.argv[2] if len(sys.argv) > 2 else 'Menu de Estudos.html'

AREA_MAP = {'a_sag': 'sagital', 'a_cor': 'coronal', 'a_lob': 'lobos'}
TOL = {'sagital': 0.05, 'coronal': 0.06, 'lobos': 0.07, 'ventral': 0.06, 'medula': 0.07, 'meninges': 0.04,
       'torax': 0.07, 'braco': 0.07, 'coxa': 0.08, 'obturatorio': 0.08, 'perna_post': 0.07, 'perna_ant': 0.07}

used = set()
structs = []
ids = [s['id'] for s in D.S]
assert ids == list(range(1, 44)), ids
for s in D.S:
    areas = {}
    for k in s.get('area', []):
        areas.setdefault(AREA_MAP[k[:5]], []).append(k)
        used.add(k)
    for key, _ in s['imgs']:
        assert key in manifest, f'imagem faltando: {key} ({s["nome"]})'
        used.add(key)
    for p in [s['pin']] + s.get('alt', []):
        assert p['mapa'] in D.MAPS, p
    structs.append({
        'id': s['id'], 'nome': s['nome'], 'grupo': s['grupo'], 'funcao': s['funcao'], 'onde': s['onde'],
        'extra': s.get('extra', []), 'imgs': s['imgs'], 'pin': s['pin'], 'alt': s.get('alt', []),
        'areas': areas, 'fonte': s['fonte'],
    })

sizes = {}
for m in D.MAPS.values():
    assert m['img'] in manifest, m['img']
    used.add(m['img'])
    sizes[m['img']] = manifest[m['img']][:2]

data = {'groups': D.GROUPS, 'maps': D.MAPS, 'mapOrder': D.MAP_ORDER, 'structs': structs, 'sizes': sizes, 'tol': TOL, 'home': HOME}


def uri(key):
    if key.startswith('a_'):
        f, mime = f'{OUT}/areas/{key}.png', 'image/png'
    else:
        f, mime = f'{OUT}/img/{key}.jpg', 'image/jpeg'
    return f'data:{mime};base64,' + base64.b64encode(open(f, 'rb').read()).decode()


imgs = {k: uri(k) for k in sorted(used)}


def jdump(o):
    return json.dumps(o, ensure_ascii=False, separators=(',', ':')).replace('<', '\\u003c').replace('\u2028', '\\u2028')


html = open(HERE + '/app.html', encoding='utf-8').read()
html = html.replace('__DATA__', jdump(data)).replace('__IMAGES__', jdump(imgs))
os.makedirs(os.path.dirname(TARGET), exist_ok=True)
open(TARGET, 'w', encoding='utf-8').write(html)
unused = [k for k in manifest if k not in used]
print('ok ->', TARGET, round(os.path.getsize(TARGET) / 1e6, 2), 'MB; imagens:', len(imgs), '; não usadas:', unused)
