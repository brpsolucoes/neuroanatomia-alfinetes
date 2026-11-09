# -*- coding: utf-8 -*-
import re, sys, os
HERE = os.path.dirname(__file__)
app1 = open(HERE + '/../neuroanatomia/app.html', encoding='utf-8').read()
css = re.search(r'<style>(.*?)</style>', app1, re.S).group(1)
tokens = css[:css.index('/* ---------- topo ---------- */')]
html = open(HERE + '/hub.html', encoding='utf-8').read().replace('/*__TOKENS__*/', tokens)
out, neuro, dev = sys.argv[1], sys.argv[2], sys.argv[3]
html = html.replace('__LINK_NEURO__', neuro).replace('__LINK_DEV__', dev)
os.makedirs(os.path.dirname(out), exist_ok=True)
open(out, 'w', encoding='utf-8').write(html)
print('hub ->', out, round(os.path.getsize(out) / 1024), 'KB')
