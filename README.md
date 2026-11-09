# Menu de estudos

Página inicial com dois apps de estudo, cada um em um único arquivo HTML (funcionam offline e no celular):

- `neuroanatomia/` — **Neuroanatomia · Alfinetes**: mapas anatômicos com os 43 alfinetes dos roteiros de aula prática, cartões de estudo (Nome → Função → Imagem → Onde fica), prova, simulado da prova prática (você escreve o nome do alfinete, com tempo) e lista.
- `desenvolvimento/` — **Desenvolvimento Humano**: 185 conceitos de nascimento e primeira infância (físico, perceptual, cognitivo e linguagem), com linha do tempo por idade, cartões, prova e glossário.

Os dois apps têm revisão espaçada: cada acerto leva o item para uma caixa com intervalo maior (volta em 1, 3, 7, 14 e 30 dias); um erro faz o item voltar no dia seguinte. A aba Estudar abre na "Revisão de hoje" e o menu mostra quantos itens estão para revisar.

O progresso de estudo (dominado/revisar e a agenda de revisão) fica salvo apenas no navegador de quem usa.

O código-fonte está em `fonte/` (veja `fonte/README.md`). Para reconstruir tudo: `python fonte/construir.py`.

Textos e imagens vêm dos slides das disciplinas (Neuroanatomia; Desenvolvimento Humano, Prof. Me. Carlos Eduardo Simonelli). Funções, localizações e alguns complementos foram acrescentados com conteúdo padrão da área e estão sinalizados nos cartões. Confira sempre com o professor.