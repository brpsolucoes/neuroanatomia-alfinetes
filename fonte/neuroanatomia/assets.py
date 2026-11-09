# -*- coding: utf-8 -*-
"""Processa as imagens do PDF: recortes, limpeza dos mapas, máscaras de destaque."""
import os, json, math, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
import pymupdf

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = HERE + '/brutos'            # imagens extraídas do PDF (geradas automaticamente, fora do git)
OUT = HERE + '/out'               # imagens processadas usadas pelo build.py (estas ficam no git)
PDF = os.environ.get('NEURO_PDF') or (sys.argv[1] if len(sys.argv) > 1 else '')
if not PDF or not os.path.exists(PDF):
    raise SystemExit('Uso: python assets.py "caminho/Neuroanatomia (2).pdf"  (ou defina NEURO_PDF)')
os.makedirs(RAW, exist_ok=True)
os.makedirs(OUT + '/img', exist_ok=True)
os.makedirs(OUT + '/areas', exist_ok=True)

GALLERY_MAX = 900
GALLERY_Q = 76

# ---------------- imagens da galeria (chave -> arquivo bruto) ----------------
RAWMAP = {
    'cerebro_3d': 'p102_x12237', 'encefalo_cabeca': 'p007_x866', 'cerebro_hemisferios': 'p103_x12357',
    'telencefalo_base': 'p115_x13785', 'telencefalo_cima': 'p115_x13787', 'telencefalo_nucleos': 'p129_x15499',
    'diencefalo_foto': 'p104_x12475', 'diencefalo_subtalamo': 'p114_x13666',
    'cerebelo_sup': 'p098_x11764', 'cerebelo_post': 'p098_x11765', 'cerebelo_inf': 'p097_x11645', 'cerebelo_divisao': 'p099_x11883',
    'tronco_sagital': 'p071_x8541', 'tronco_reticular': 'p081_x9750', 'tronco_base': 'p083_x9987',
    'mesencefalo_corte': 'p073_x8785', 'mesencefalo_ant': 'p072_x8665', 'mesencefalo_post': 'p072_x8664', 'mesencefalo_negra': 'p075_x9024',
    'ponte_ant': 'p076_x9142', 'ponte_base': 'p076_x9145', 'ponte_post': 'p076_x9144',
    'bulbo_ant': 'p077_x9270', 'bulbo_decussacao': 'p077_x9269', 'bulbo_post': 'p077_x9268',
    'cinzenta_branca': 'p018_x2196', 'medula_corte': 'p037_x4473', 'medula_sagital': 'p032_x3873', 'medula_cabo': 'p034_x3874',
    'medula_ressonancia': 'p033_x3995', 'plexo_lombossacral': 'p052_x6247',
    'ventriculos_axial': 'p119_x14284', 'liquor': 'p133_x15976',
    'frenico_pescoco': 'p044_x5301', 'frenico_torax': 'p045_x5420', 'frenico_esquema': 'p044_x5302',
    'braco_ant': 'p048_x5774', 'plexo_braquial': 'p047_x5656', 'braco_cutaneo': 'p050_x6010',
    'isquiatico_post': 'p056_x6727', 'isquiatico_coxa': 'p057_x6854', 'regiao_glutea': 'p058_x6981',
    'nervos_perna_rotulados': 'p053_x6366', 'fibular': 'p057_x6861',
    'femoral_musculos': 'p054_x6484', 'femoral_cutaneo': 'p054_x6485', 'femoral_plexo': 'p054_x6486',
    'obturatorio_musculos': 'p055_x6606', 'obturatorio_pelve': 'p055_x6608', 'obturatorio_cutaneo': 'p055_x6609',
    'meninges_camadas': 'p064_x7712', 'meninges_ingles': 'p065_x7830', 'meninges_espinal': 'p068_x8185',
    'vago': 'p093_x11168', 'cranianos_base': 'p083_x9987', 'optico': 'p085_x10223', 'olfatorio': 'p084_x10105',
    'epitalamo_pineal': 'p113_x13544', 'epitalamo_sagital': 'p113_x13545',
    'talamo_vias': 'p109_x13072', 'talamo_esquema': 'p109_x13073',
    'hipotalamo_azul': 'p112_x13426', 'hipotalamo_hipofise': 'p107_x12834',
    'lobos_cores': 'p121_x14522', 'lobos_slide120': 'p120_x14403', 'giros_areas': 'p122_x14640',
    'broca_wernicke': 'p123_x14764', 'linguagem_areas': 'p123_x14760', 'afasia_broca': 'p124_x14884', 'linguagem_cores': 'p123_x14763',
}

# recortes da página do slide (x0,y0,x1,y1 em pontos; o slide tem 720x540)
PAGEMAP = {
    'diencefalo_cores': (105, (30, 100, 720, 490)),
    'ventriculos_coronal': (22, (0, 3, 423, 280)),
    'ventriculo4': (22, (423, 3, 711, 280)),
    'medula_vias': (35, (10, 20, 710, 490)),
    'vago_coracao': (80, (195, 30, 550, 528)),
    'oculomotores': (86, (10, 60, 570, 480)),
    'hipofise_pineal': (106, (60, 80, 640, 530)),
}

# ---------------- bases dos mapas ----------------
# chave -> (arquivo bruto, [retângulos para branquear], [linhas para apagar])
MAPBASE = {
    'map_sagital': ('p105_x12595', [], []),
    'map_coronal': ('p022_x2688', [], []),
    'map_lobos': ('p121_x14522',
                  [(0.05, 0.06, 0.205, 0.235), (0.39, 0.0, 0.535, 0.125), (0.69, 0.015, 0.87, 0.172),
                   (0.0, 0.693, 0.285, 0.86), (0.25, 0.845, 0.425, 0.985), (0.835, 0.80, 0.985, 0.935), (0.80, 0.84, 0.99, 0.97)],
                  [(0.143, 0.235, 0.19, 0.354), (0.493, 0.121, 0.52, 0.178), (0.693, 0.157, 0.66, 0.214),
                   (0.20, 0.763, 0.28, 0.685), (0.36, 0.832, 0.395, 0.727), (0.905, 0.806, 0.868, 0.606)]),
    'map_ventral': ('p027_x3283', [], []),
    'map_medula': ('p034_x3874', [], []),
    'map_meninges': ('p064_x7712', [(0.05, 0.47, 0.195, 0.85), (0.0, 0.0, 1.0, 0.012)], []),
    'map_torax': ('p045_x5420', [], []),
    'map_braco': ('p048_x5774', [(0.2, 0.0, 0.62, 0.04)], []),
    'map_coxa': ('p054_x6484', [], []),
    'map_obturatorio': ('p055_x6608', [(0.0, 0.0, 1.0, 0.045)], []),
    'map_perna_post': ('p057_x6854', [(0.0, 0.0, 1.0, 0.045)], []),
    'map_perna_ant': ('p057_x6861', [(0.0, 0.0, 1.0, 0.045)], []),
}
MAP_MIN = 1000


def extract_raw(name):
    """Extrai do PDF a imagem embutida 'pPPP_xXREF' (página, xref) para brutos/."""
    import io as _io
    xref = int(name.split('_x')[1])
    doc = pymupdf.open(PDF)
    try:
        pix = pymupdf.Pixmap(doc, xref)
        if pix.alpha or pix.colorspace.n > 3:
            pix = pymupdf.Pixmap(pymupdf.csRGB, pix)
        info = doc.extract_image(xref)
        if info.get('smask'):
            pix = pymupdf.Pixmap(pix, pymupdf.Pixmap(doc, info['smask']))
        pix.save(f'{RAW}/{name}.png')
    except Exception:
        info = doc.extract_image(xref)
        im = Image.open(_io.BytesIO(info['image']))
        if info.get('smask'):
            m = Image.open(_io.BytesIO(doc.extract_image(info['smask'])['image'])).convert('L')
            im = im.convert('RGB'); im.putalpha(m.resize(im.size))
        if im.mode in ('RGBA', 'LA', 'P'):
            im = im.convert('RGBA'); bg = Image.new('RGB', im.size, 'white'); bg.paste(im, mask=im.split()[3]); im = bg
        else:
            im = im.convert('RGB')
        im.save(f'{RAW}/{name}.png')


def load_raw(name):
    if not os.path.exists(f'{RAW}/{name}.png'):
        extract_raw(name)
    im = Image.open(f'{RAW}/{name}.png')
    if im.mode != 'RGB':
        im = im.convert('RGB')
    return im


def inpaint(a, mask, iters=14):
    """preenche pixels mascarados com a média dos vizinhos conhecidos (difusão)."""
    a = a.astype(np.float32)
    known = ~mask
    for _ in range(iters):
        if known.all():
            break
        acc = np.zeros_like(a); cnt = np.zeros(mask.shape, np.float32)
        for dy in (-1, 0, 1):
            for dx in (-1, 0, 1):
                if dx == 0 and dy == 0:
                    continue
                sh = np.roll(np.roll(a * known[..., None], dy, 0), dx, 1)
                sk = np.roll(np.roll(known, dy, 0), dx, 1).astype(np.float32)
                acc += sh; cnt += sk
        fill = (~known) & (cnt > 0)
        a[fill] = acc[fill] / cnt[fill][:, None]
        known = known | fill
    return np.clip(a, 0, 255).astype(np.uint8)


def clean(im, rects, lines, r=3.2):
    a = np.array(im)
    H, W, _ = a.shape
    for (x0, y0, x1, y1) in rects:
        a[int(y0 * H):int(y1 * H), int(x0 * W):int(x1 * W)] = 255
    if lines:
        yy, xx = np.mgrid[0:H, 0:W]
        mask = np.zeros((H, W), bool)
        for (x0, y0, x1, y1) in lines:
            p0 = np.array([x0 * W, y0 * H]); p1 = np.array([x1 * W, y1 * H]); d = p1 - p0; L2 = (d ** 2).sum()
            t = np.clip(((xx - p0[0]) * d[0] + (yy - p0[1]) * d[1]) / L2, 0, 1)
            px = p0[0] + t * d[0]; py = p0[1] + t * d[1]
            mask |= ((xx - px) ** 2 + (yy - py) ** 2) <= r * r
        a = inpaint(a, mask)
    return Image.fromarray(a)


def save_jpg(im, key, maxdim, q, upscale_to=None):
    w, h = im.size
    m = max(w, h)
    if upscale_to and m < upscale_to:
        s = upscale_to / m
        im = im.resize((round(w * s), round(h * s)), Image.LANCZOS)
    elif m > maxdim:
        s = maxdim / m
        im = im.resize((round(w * s), round(h * s)), Image.LANCZOS)
    path = f'{OUT}/img/{key}.jpg'
    im.save(path, 'JPEG', quality=q, optimize=True, progressive=True)
    return im.size, os.path.getsize(path)


manifest = {}

# galeria (raw)
for key, raw in RAWMAP.items():
    im = load_raw(raw)
    manifest[key] = save_jpg(im, key, GALLERY_MAX, GALLERY_Q)

# galeria (recortes de página)
doc = pymupdf.open(PDF)
for key, (pg, clip) in PAGEMAP.items():
    page = doc[pg - 1]
    pix = page.get_pixmap(matrix=pymupdf.Matrix(3, 3), clip=pymupdf.Rect(*clip), alpha=False)
    im = Image.frombytes('RGB', (pix.width, pix.height), pix.samples)
    manifest[key] = save_jpg(im, key, GALLERY_MAX, GALLERY_Q)

# bases dos mapas
map_arrays = {}
for key, (raw, rects, lines) in MAPBASE.items():
    im = load_raw(raw)
    if rects or lines:
        im = clean(im, rects, lines)
    map_arrays[key] = np.array(im)
    size_before = im.size
    manifest[key] = save_jpg(im, key, 1400, 82, upscale_to=MAP_MIN)
    manifest[key] = list(manifest[key][0]) + [manifest[key][1]]
    print(key, size_before, '->', manifest[key])


# ---------------- máscaras de destaque ----------------
def poly_mask(size, rings, ss=3):
    w, h = size
    big = Image.new('L', (w * ss, h * ss), 0)
    d = ImageDraw.Draw(big)
    for i, r in enumerate(rings):
        d.polygon([(x * w * ss, y * h * ss) for x, y in r], fill=255 if i == 0 else 0)
    return np.array(big.resize((w, h), Image.LANCZOS)).astype(np.float32) / 255.0


def ellipse(cx, cy, rx, ry, n=28):
    return [(cx + rx * math.cos(2 * math.pi * i / n), cy + ry * math.sin(2 * math.pi * i / n)) for i in range(n)]


def components(binary):
    H, W = binary.shape
    lab = np.zeros((H, W), np.int32)
    n = 0
    sizes = {}
    for y0 in range(H):
        for x0 in range(W):
            if binary[y0, x0] and lab[y0, x0] == 0:
                n += 1
                stack = [(y0, x0)]
                lab[y0, x0] = n
                c = 0
                while stack:
                    y, x = stack.pop(); c += 1
                    for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        yy, xx = y + dy, x + dx
                        if 0 <= yy < H and 0 <= xx < W and binary[yy, xx] and lab[yy, xx] == 0:
                            lab[yy, xx] = n; stack.append((yy, xx))
                sizes[n] = c
    return lab, sizes


def biggest(binary):
    lab, sizes = components(binary)
    if not sizes:
        return binary
    k = max(sizes, key=sizes.get)
    return lab == k


def morph(binary, op, n):
    im = Image.fromarray((binary * 255).astype(np.uint8))
    f = ImageFilter.MaxFilter if op == 'dil' else ImageFilter.MinFilter
    im = im.filter(f(n))
    return np.array(im) > 127


def fill_holes(binary):
    inv = ~binary
    lab, sizes = components(inv)
    H, W = binary.shape
    border = set(lab[0, :]) | set(lab[-1, :]) | set(lab[:, 0]) | set(lab[:, -1])
    out = binary.copy()
    for k in sizes:
        if k not in border:
            out |= (lab == k)
    return out


def save_area(key, mask_f, size=(900, None)):
    """mask_f: float 0..1 (h,w). Salva PNG LA: alpha = preenchimento + contorno."""
    m = mask_f
    h, w = m.shape
    mi = Image.fromarray((m * 255).astype(np.uint8))
    er = np.array(mi.filter(ImageFilter.MinFilter(5))).astype(np.float32) / 255.0
    edge = np.clip(m - er, 0, 1)
    alpha = np.clip(0.34 * m + 0.95 * edge, 0, 1)
    la = Image.new('LA', (w, h), (255, 0))
    la.putdata([(255, int(v * 255)) for v in alpha.flatten()])
    path = f'{OUT}/areas/{key}.png'
    la.save(path, optimize=True)
    manifest[key] = [w, h, os.path.getsize(path)]


def mask_size(mapkey, maxdim=900):
    h, w, _ = map_arrays[mapkey].shape
    s = maxdim / max(w, h)
    return (round(w * s), round(h * s))


# --- sagital (polígonos desenhados sobre a grade) ---
SAG = {
    'a_sag_cerebro': [[(0.175, 0.47), (0.185, 0.38), (0.21, 0.29), (0.25, 0.21), (0.30, 0.15), (0.37, 0.11), (0.45, 0.085), (0.53, 0.075),
                       (0.61, 0.08), (0.69, 0.10), (0.77, 0.14), (0.84, 0.20), (0.89, 0.27), (0.915, 0.35), (0.925, 0.44), (0.915, 0.52),
                       (0.89, 0.575), (0.85, 0.59), (0.80, 0.555), (0.74, 0.525), (0.68, 0.505), (0.64, 0.495), (0.60, 0.485), (0.51, 0.49),
                       (0.48, 0.53), (0.44, 0.555), (0.40, 0.575), (0.34, 0.58), (0.27, 0.565), (0.215, 0.54)]],
    'a_sag_diencefalo': [[(0.465, 0.40), (0.52, 0.375), (0.575, 0.375), (0.615, 0.405), (0.625, 0.455), (0.615, 0.495), (0.56, 0.50),
                          (0.545, 0.535), (0.50, 0.55), (0.47, 0.53), (0.455, 0.48)]],
    'a_sag_talamo': [[(0.49, 0.395), (0.545, 0.38), (0.595, 0.40), (0.61, 0.445), (0.60, 0.475), (0.56, 0.485), (0.52, 0.485), (0.495, 0.465), (0.485, 0.43)]],
    'a_sag_hipotalamo': [[(0.465, 0.485), (0.52, 0.49), (0.545, 0.515), (0.53, 0.545), (0.495, 0.55), (0.47, 0.53)]],
    'a_sag_epitalamo': [[(0.575, 0.465), (0.605, 0.465), (0.615, 0.49), (0.595, 0.505), (0.575, 0.495)]],
    'a_sag_mesencefalo': [[(0.505, 0.495), (0.56, 0.49), (0.60, 0.485), (0.64, 0.50), (0.645, 0.535), (0.61, 0.56), (0.52, 0.56), (0.505, 0.53)]],
    'a_sag_ponte': [[(0.495, 0.565), (0.605, 0.56), (0.612, 0.64), (0.608, 0.72), (0.525, 0.73), (0.495, 0.665), (0.49, 0.60)]],
    'a_sag_bulbo': [[(0.525, 0.735), (0.608, 0.725), (0.603, 0.85), (0.55, 0.86), (0.525, 0.80)]],
    'a_sag_tronco': [[(0.505, 0.495), (0.56, 0.49), (0.60, 0.485), (0.64, 0.50), (0.645, 0.535), (0.61, 0.56), (0.612, 0.64), (0.608, 0.72),
                      (0.603, 0.85), (0.55, 0.86), (0.525, 0.80), (0.525, 0.735), (0.495, 0.665), (0.49, 0.60), (0.495, 0.565), (0.505, 0.53)]],
    'a_sag_cerebelo': [[(0.62, 0.54), (0.655, 0.505), (0.71, 0.51), (0.76, 0.535), (0.805, 0.57), (0.845, 0.62), (0.87, 0.67), (0.865, 0.72),
                        (0.825, 0.76), (0.77, 0.795), (0.70, 0.805), (0.65, 0.795), (0.625, 0.76), (0.615, 0.66)]],
    'a_sag_v4': [[(0.603, 0.56), (0.618, 0.575), (0.628, 0.60), (0.62, 0.65), (0.628, 0.69), (0.616, 0.72), (0.606, 0.70), (0.606, 0.62)]],
}
sz = mask_size('map_sagital')
for k, rings in SAG.items():
    save_area(k, poly_mask(sz, rings))
# telencéfalo = hemisfério menos diencéfalo
save_area('a_sag_telencefalo', poly_mask(sz, [SAG['a_sag_cerebro'][0], SAG['a_sag_diencefalo'][0]]))

# --- coronal (escuro conectado ao ponto semente, dentro de uma caixa) ---
arr = map_arrays['map_coronal'].astype(np.float32)
lum = arr.mean(axis=2)
H, W = lum.shape


def seeded_dark(seed, box, thr=65):
    x0, y0, x1, y1 = box
    sub = np.zeros((H, W), bool)
    sub[int(y0 * H):int(y1 * H), int(x0 * W):int(x1 * W)] = lum[int(y0 * H):int(y1 * H), int(x0 * W):int(x1 * W)] < thr
    lab, sizes = components(sub)
    k = lab[int(seed[1] * H), int(seed[0] * W)]
    if k == 0:
        raise SystemExit(f'semente fora do escuro: {seed}')
    m = fill_holes(lab == k)
    m = morph(morph(m, 'dil', 3), 'dil', 3)  # leve margem
    m = morph(m, 'ero', 3)
    return m


cz = mask_size('map_coronal')
for key, seed, box in (('a_cor_vld', (0.44, 0.47), (0.36, 0.36, 0.505, 0.62)),
                       ('a_cor_vle', (0.565, 0.46), (0.495, 0.36, 0.64, 0.62)),
                       ('a_cor_v3', (0.52, 0.72), (0.485, 0.62, 0.565, 0.80))):
    m = seeded_dark(seed, box)
    mi = Image.fromarray((m * 255).astype(np.uint8)).resize(cz, Image.LANCZOS)
    save_area(key, np.array(mi).astype(np.float32) / 255.0)

# --- lobos (classificação por cor) ---
arr = map_arrays['map_lobos']
H, W, _ = arr.shape
brain = ~((arr > 205).all(axis=2))
hsv = np.array(Image.fromarray(arr).convert('HSV')).astype(np.float32) / 255.0
hh, ss_, vv = hsv[..., 0], hsv[..., 1], hsv[..., 2]
cls_masks = {
    'frontal': brain & (hh > 0.52) & (hh < 0.80) & (ss_ > 0.08) & (vv > 0.10),
    'parietal': brain & (hh > 0.14) & (hh < 0.32) & (ss_ > 0.25),
    'occipital': brain & ((hh < 0.035) | (hh > 0.93)) & (ss_ > 0.45),
    'temporal': brain & (hh >= 0.035) & (hh < 0.10) & (ss_ > 0.55),
}
lz = mask_size('map_lobos')
for nome in ('frontal', 'parietal', 'occipital'):
    orig = cls_masks[nome]
    others = np.zeros_like(orig)
    for k, v in cls_masks.items():
        if k != nome:
            others |= v
    m = morph(orig, 'dil', 11); m = morph(m, 'ero', 11)
    m = (m & ~others) | orig
    m = biggest(m)
    m = fill_holes(m)
    m = morph(m, 'dil', 3); m = morph(m, 'ero', 3)
    mi = Image.fromarray((m * 255).astype(np.uint8)).resize(lz, Image.LANCZOS)
    save_area('a_lob_' + nome, np.array(mi).astype(np.float32) / 255.0)

LOB = {
    'a_lob_prefrontal': [[(0.12, 0.46), (0.14, 0.36), (0.19, 0.28), (0.26, 0.22), (0.30, 0.26), (0.29, 0.38), (0.28, 0.52), (0.23, 0.62), (0.17, 0.60)]],
    'a_lob_broca': [ellipse(0.325, 0.535, 0.05, 0.06)],
    'a_lob_wernicke': [ellipse(0.625, 0.535, 0.06, 0.05)],
}
for k, rings in LOB.items():
    save_area(k, poly_mask(lz, rings))

json.dump(manifest, open(OUT + '/manifest.json', 'w'), indent=1)
tot = sum(v[-1] if isinstance(v, list) else v[1] for v in manifest.values())
print('arquivos:', len(manifest), 'total KB:', tot // 1024)
