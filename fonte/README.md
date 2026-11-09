# Código-fonte dos apps de estudo

Os arquivos publicados (`index.html`, `neuroanatomia/index.html`, `desenvolvimento/index.html`) são gerados a partir desta pasta. **Não edite os HTMLs publicados à mão**: edite o fonte e rode o comando de construção.

## Construir

Requer Python 3 com Pillow (`pip install -r fonte/requirements.txt`).

```bash
python fonte/construir.py
```

Gera o site na raiz do repositório. Para gerar os três arquivos de uso offline numa pasta:

```bash
python fonte/construir.py --local "C:/caminho/da/pasta"
```

## Onde mudar cada coisa

| Quero mudar… | Arquivo |
|---|---|
| Textos dos 43 alfinetes (função, onde fica, extras), respostas aceitas no simulado, posição dos alfinetes nos mapas | `neuroanatomia/data.py` |
| Interface do app de Neuroanatomia (e o CSS compartilhado pelos três) | `neuroanatomia/app.html` |
| Conceitos de Desenvolvimento Humano (definição, detalhes, idade, slides) | `desenvolvimento/psi_data.py` |
| Interface do app de Desenvolvimento Humano | `desenvolvimento/psi_app.html` |
| Página inicial (menu) | `menu/hub.html` |

## Imagens

As imagens já processadas estão no repositório, então o comando acima basta para reconstruir. Só é preciso voltar aos PDFs se mudar recortes, mapas ou slides:

- `neuroanatomia/assets.py "…/Neuroanatomia (2).pdf"` recria `neuroanatomia/out/` (galerias, bases dos mapas e máscaras de destaque). Requer também numpy e PyMuPDF.
- `desenvolvimento/extrair_slides.py "pasta dos PDFs"` recria `desenvolvimento/slides/`. Requer PyMuPDF.
- `desenvolvimento/ocr.ps1` é o OCR do Windows usado para ler o texto dos slides (que eram só imagem). O texto já está em `psi_data.py`.

Os PDFs originais não ficam no repositório. Ao reextrair, algumas imagens podem sair com diferenças de cor imperceptíveis (menos de 1 nível em média); as posições dos alfinetes não mudam.
