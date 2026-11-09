# -*- coding: utf-8 -*-
"""Conteúdo do app Desenvolvimento Humano (slides do Prof. Me. Carlos Eduardo Simonelli)."""

TEMAS = {
    "nasc": {"nome": "Nascimento e primeira infância", "cor": "#c2410c", "doc": "Nascimento e Primeira Infância"},
    "fis":  {"nome": "Desenvolvimento físico",         "cor": "#2f9e44", "doc": "Desenvolvimento físico"},
    "perc": {"nome": "Desenvolvimento perceptual",     "cor": "#2b7de9", "doc": "Desenvolvimento perceptual"},
    "cogn": {"nome": "Desenvolvimento cognitivo",      "cor": "#7c3aed", "doc": "Desenvolvimento cognitivo"},
    "ling": {"nome": "Desenvolvimento da linguagem",   "cor": "#d6336c", "doc": "Desenvolvimento da linguagem"},
}

# faixas etárias da linha do tempo (o marco entra na faixa em que começa)
BANDS = [
    ("nasc", "Nascimento (parto)"),
    ("rn", "Recém-nascido · 0 a 1 mês"),
    ("m1_3", "1 a 3 meses"),
    ("m4_6", "4 a 6 meses"),
    ("m7_12", "7 a 12 meses"),
    ("a1_2", "1 a 2 anos"),
    ("a2_4", "2 a 4 anos"),
    ("a4_6", "4 a 6 anos"),
    ("a6_9", "6 a 9 anos"),
    ("a9_12", "9 a 12 anos"),
    ("adol", "Adolescência · 12 anos ou mais"),
]

CONC = []


def C(tema, sub, nome, defs, det=None, quando=None, faixa=None, slides=None, curto=None, extra=None):
    CONC.append(dict(tema=tema, sub=sub, nome=nome, defs=defs if isinstance(defs, list) else [defs],
                     det=det or [], quando=quando, faixa=faixa, slides=slides or [], curto=curto, extra=extra or []))


# =====================================================================
# NASCIMENTO E PRIMEIRA INFÂNCIA
# =====================================================================
S = "Parto"
C("nasc", S, "Estágios do parto natural",
  "O parto natural progride, em geral, por três estágios: (1) dilatação e esvaecimento; (2) o parto propriamente dito; (3) liberação da placenta.",
  ["Para os pais, o parto combina grande estresse físico com uma ampla variedade de emoções.",
   "Para a criança, o nascimento marca sua entrada na família e na comunidade."],
  faixa="nasc", slides=["nasc_02"], curto="3 estágios do parto")
C("nasc", S, "Estágio 1: dilatação e esvaecimento",
  "Período em que ocorrem dois processos importantes: a dilatação e o esvaecimento do colo do útero.",
  ["No início (fase latente), as contrações são mais leves e espaçadas; no final (fase ativa), são mais frequentes e desconfortáveis.",
   "Ao final do estágio, a mãe normalmente terá o impulso de ajudar o bebê a sair “empurrando”. O atendente de parto (médico ou parteira) encoraja o impulso quando o colo do útero está totalmente dilatado."],
  quando="Duração média: cerca de 8 horas em primeiros partos e 6 horas em partos subsequentes.",
  faixa="nasc", slides=["nasc_02", "nasc_03"], curto="Estágio 1")
C("nasc", S, "Dilatação",
  "Processo em que o colo do útero se dilata o suficiente para permitir que a cabeça do feto passe pelo canal de nascimento.",
  ["A dilatação total é de 10 cm."],
  faixa="nasc", slides=["nasc_02"])
C("nasc", S, "Esvaecimento",
  "Achatamento do colo do útero.",
  ["O colo passa de longo para fino durante o primeiro estágio do parto."],
  faixa="nasc", slides=["nasc_02"])
C("nasc", S, "Estágio 2: o parto propriamente dito",
  "A cabeça do bebê move-se do colo do útero expandido para o canal de nascimento e, finalmente, para fora do corpo da mãe.",
  ["Na maioria dos partos, a cabeça sai primeiro, com o rosto voltado para a espinha da mãe.",
   "Em 3 a 4% dos partos a orientação é diferente: saem primeiro os pés ou as nádegas."],
  quando="Duração média: cerca de 50 minutos no primeiro parto e 20 minutos nos partos posteriores.",
  faixa="nasc", slides=["nasc_04"], curto="Estágio 2")
C("nasc", S, "Apresentação de nádegas",
  "Parto em que os pés ou as nádegas saem primeiro (3 a 4% dos partos).",
  ["No passado, a maioria era realizada com instrumentos médicos como fórceps.",
   "Hoje, quase quatro quintos dos partos com apresentação de nádegas são feitos por cesariana."],
  faixa="nasc", slides=["nasc_04", "nasc_05"])
C("nasc", S, "Estágio 3: liberação da placenta",
  "Estágio em geral bastante breve: é a liberação da placenta (também chamada de secundinas).",
  [], faixa="nasc", slides=["nasc_05"], curto="Estágio 3")
C("nasc", S, "Anoxia",
  "Carência de oxigênio (geralmente pelo cordão umbilical) durante o parto.",
  ["Pode resultar em dano cerebral se for prolongada."],
  faixa="nasc", slides=["nasc_06"])
C("nasc", S, "Outras complicações do parto",
  "Os bebês podem deslocar os ombros ou os quadris durante o parto, e alguns sofrem fraturas.",
  ["Em outros bebês, os nervos que controlam os músculos faciais são comprimidos, causando paralisia temporária de um lado do rosto."],
  faixa="nasc", slides=["nasc_06"])
C("nasc", S, "Parto por cesariana (secção-c)",
  "Retirada cirúrgica do bebê por incisões feitas nas paredes abdominal e uterina.",
  ["Cerca de 30% dos partos são realizados por cesariana.",
   "Os críticos da frequência com que esses partos ocorrem dizem que muitas dessas operações são desnecessárias."],
  faixa="nasc", slides=["nasc_07"], curto="Cesariana")
C("nasc", S, "Indicações da cesariana",
  "Situações que justificam a operação: sofrimento fetal, parto que não progride, feto muito grande, idade da mãe e condições de saúde maternas.",
  ["Condições maternas: doença cardiovascular, lesão espinhal etc."],
  faixa="nasc", slides=["nasc_07"])
C("nasc", S, "Riscos da cesariana para a mãe",
  "Reações alérgicas a anestésicos, infecção, lesões acidentais a outros órgãos (e ao feto) e perda excessiva de sangue.",
  ["Há uma hipótese de que, durante o trabalho de parto, a mãe produza hormônios que cruzam a placenta antes do nascimento e influenciam o funcionamento do sistema imunológico do recém-nascido."],
  faixa="nasc", slides=["nasc_07", "nasc_08"])

S = "Avaliação do recém-nascido"
C("nasc", S, "Escore de Apgar",
  "Sistema de avaliação do recém-nascido frequentemente usado. Cada critério recebe índice 0, 1 ou 2.",
  ["Cor da pele: cianose (0); cianose nas extremidades (1); corado/rosado (2).",
   "Irritabilidade reflexiva: ausência de estímulo (0); alguma resposta (1); choro vigoroso, tosse, espirro ou careta (2).",
   "Frequência cardíaca: não detectável (0); abaixo de 100 bpm (1); acima de 100 bpm (2).",
   "Respiração: ausente (0); fraca/lenta/irregular (1); choro forte e vigoroso (2).",
   "Tônus muscular: ausente (0); pouco movimento e flexão das extremidades (1); muito movimento, com flexão das extremidades que resiste à extensão de braços e pernas (2)."],
  faixa="nasc", slides=["nasc_09"], curto="Escore de Apgar")
C("nasc", S, "Interpretação do escore de Apgar",
  "7 ou acima: o bebê não corre risco. 4, 5 ou 6: o bebê precisa de ajuda. 3 ou abaixo: o bebê está em condições críticas.",
  [], faixa="nasc", slides=["nasc_09"])
C("nasc", S, "Escala de Brazelton",
  "Ferramenta que avalia as respostas físicas e neurológicas dos recém-nascidos com base em seus comportamentos e em suas diferenças individuais.",
  ["Orientação visual e auditiva (animada e inanimada).",
   "Capacidade da criança de se acostumar à estimulação.",
   "Resposta ao abraço, tônus muscular geral e mudança de humor da criança.",
   "Capacidade de se organizar para responder à estimulação.",
   "Regulação da respiração e da temperatura, variações na cor da pele e presença de tremor ou choque."],
  faixa="nasc", slides=["nasc_10"], curto="Escala de Brazelton")

S = "Reflexos"
C("nasc", S, "Reflexos do recém-nascido",
  "Respostas físicas desencadeadas involuntariamente por estímulos específicos. Uma grande coleção de reflexos é parte importante do repertório de comportamentos do bebê.",
  ["Os reflexos vistos nos slides: busca, apoio plantar, marcha reflexa, pressão palmar, pressão plantar, sucção reflexiva, galante, motor e tônico-cervical."],
  faixa="rn", slides=["nasc_11"], curto="Reflexos")
C("nasc", S, "Reflexo de busca",
  "O bebê vira a cabeça de lado em busca de algo (o seio da mãe).",
  [], quando="Vai até 4 meses.", faixa="rn", slides=["nasc_11"], curto="Busca · até 4 m")
C("nasc", S, "Apoio plantar",
  "O bebê estende as pernas quando os pés estão apoiados sobre uma superfície.",
  [], quando="Vai até 12 meses.", faixa="rn", slides=["nasc_11"], curto="Apoio plantar · até 12 m")
C("nasc", S, "Marcha reflexa",
  "Ao colocar o bebê em pé e inclinar o corpo para a frente, suas pernas e pés fazem um movimento como se estivesse andando.",
  [], quando="Vai até 2 meses.", faixa="rn", slides=["nasc_11"], curto="Marcha reflexa · até 2 m")
C("nasc", S, "Pressão palmar",
  "O bebê fecha a mão quando algo toca a palma da mão.",
  [], quando="Vai até 6 meses.", faixa="rn", slides=["nasc_12"], curto="Pressão palmar · até 6 m")
C("nasc", S, "Pressão plantar",
  "O bebê flexiona os dedos dos pés quando pressionado na base deles.",
  [], quando="Vai até 12 meses.", faixa="rn", slides=["nasc_12"], curto="Pressão plantar · até 12 m")
C("nasc", S, "Sucção reflexiva",
  "Quando os lábios são estimulados, o bebê suga qualquer coisa que tiver na frente.",
  [], quando="Vai até 4 meses.", faixa="rn", slides=["nasc_12"], curto="Sucção · até 4 m")
C("nasc", S, "Reflexo galante",
  "Um estímulo ao lado do tronco desencadeia a flexão para o mesmo lado.",
  [], quando="Vai até 2 meses.", faixa="rn", slides=["nasc_13"], curto="Galante · até 2 m")
C("nasc", S, "Reflexo motor (reflexo do susto)",
  "Também chamado de “reflexo do susto”: o bebê abre os braços de uma vez e pode chorar.",
  [], quando="Vai até 6 meses.", faixa="rn", slides=["nasc_13"], curto="Motor/susto · até 6 m",
  extra=[("Complemento", "Em muitos livros esse reflexo aparece como reflexo de Moro. O nome “Moro” não está nos slides.")])
C("nasc", S, "Reflexo tônico-cervical",
  "Quando se vira a cabeça do bebê para um lado, ele estende o braço do mesmo lado e flexiona o braço do lado oposto.",
  [], quando="Vai até 4 meses.", faixa="rn", slides=["nasc_13"], curto="Tônico-cervical · até 4 m")

S = "Estados comportamentais"
C("nasc", S, "Sono do bebê",
  "Os recém-nascidos dormem quase 90% do tempo, tanto de dia quanto de noite.",
  ["Aos 6 ou 8 semanas, a maioria dos bebês diminui um pouco a quantidade total de sono por dia e mostra sinais de ritmos de sono dia/noite.",
   "Aos 6 meses, ainda dormem pouco mais de 14 horas por dia, mas a regularidade e a previsibilidade do sono são mais perceptíveis."],
  quando="Recém-nascido: ~90% do tempo · 6–8 semanas: ritmo dia/noite · 6 meses: pouco mais de 14 h por dia.",
  faixa="rn", slides=["nasc_14"], curto="Sono")
C("nasc", S, "Choro",
  "Parte normal do ciclo de estados comportamentais. A função básica do choro de um bebê é sinalizar uma necessidade.",
  ["Os recém-nascidos normais choram de 2 a 11% do tempo.",
   "A porcentagem aumenta nas primeiras semanas, com pico de 2 a 3 horas de choro por dia, e depois cai."],
  quando="Pico nas primeiras semanas; menos de 1 hora por dia aos 3 meses.",
  faixa="m1_3", slides=["nasc_15"], curto="Choro")

S = "Habilidades motoras"
C("nasc", S, "Primeiras habilidades motoras do bebê",
  "As habilidades motoras do bebê surgem apenas gradualmente nas primeiras semanas.",
  ["Com 1 mês, o bebê consegue levantar o queixo do chão ou do colchão.",
   "Aos 2 meses, pode manter a cabeça firme enquanto está sendo segurado e começa a estender a mão para objetos perto dele."],
  quando="1 a 2 meses.", faixa="m1_3", slides=["nasc_16"], curto="Queixo (1 m) e cabeça firme (2 m)")
C("nasc", S, "Padrão céfalo-caudal",
  "O desenvolvimento motor prossegue da cabeça para baixo.",
  ["A mielinização e o desenvolvimento ósseo também seguem esse padrão.",
   "Acompanha o padrão próximo-distal."],
  faixa="rn", slides=["nasc_17", "fis_07", "fis_12"], curto="Céfalo-caudal")
C("nasc", S, "Padrão próximo-distal",
  "O desenvolvimento prossegue do tronco para fora (para as extremidades).",
  ["A mielinização e o desenvolvimento ósseo também seguem esse padrão.",
   "Acompanha o padrão céfalo-caudal."],
  faixa="rn", slides=["nasc_17", "fis_07", "fis_12"], curto="Próximo-distal")

S = "Capacidades sensoriais e perceptuais"
C("nasc", S, "Visão do recém-nascido",
  "O recém-nascido consegue focalizar os dois olhos no mesmo ponto e discriminar rostos.",
  ["A melhor distância de foco é de 20 a 25 cm.",
   "Em poucas semanas, consegue acompanhar um objeto com os olhos, embora não muito eficientemente."],
  faixa="rn", slides=["nasc_18"], curto="Visão do RN")
C("nasc", S, "Audição do recém-nascido",
  "Ouve facilmente sons dentro da variação de altura e intensidade da voz humana.",
  ["Localiza aproximadamente objetos por seus sons.",
   "Discrimina algumas vozes individuais, em particular a voz de sua mãe."],
  faixa="rn", slides=["nasc_18"], curto="Audição do RN")
C("nasc", S, "Paladar do recém-nascido",
  "Sente os quatro sabores básicos (doce, ácido, amargo e salgado) mais um quinto sabor, o umami.",
  ["O umami é evocado por um aminoácido encontrado na carne, no peixe e em legumes."],
  faixa="rn", slides=["nasc_18"], curto="Paladar do RN")
C("nasc", S, "Olfato do recém-nascido",
  "Identifica odores corporais familiares, incluindo discriminar o cheiro de sua mãe do cheiro de uma mulher estranha.",
  [], faixa="rn", slides=["nasc_19"], curto="Olfato do RN")

S = "Aprendizagem, temperamento e habilidades sociais"
C("nasc", S, "Aprendizagem na primeira infância",
  "Os bebês usam suas habilidades motoras, sensoriais e perceptuais para influenciar as pessoas e os objetos em seu ambiente.",
  ["Essas ações lhes permitem estabelecer um entendimento fundamental do mundo."],
  slides=["nasc_20"])
C("nasc", S, "Temperamento",
  "Diferenças individuais no estilo de resposta: todos os bebês choram, mas alguns choram mais; alguns se irritam facilmente com uma fralda molhada, enquanto outros toleram melhor os desconfortos físicos.",
  ["Há três categorias de temperamento do bebê: a criança fácil, a criança difícil e a criança lenta para responder.",
   "Essas diferenças tendem a persistir durante a infância, mas nenhum psicólogo sugere que sejam absolutamente fixas no nascimento."],
  slides=["nasc_20", "nasc_21"])
C("nasc", S, "Revezamento (turn-taking)",
  "Capacidade que o bebê traz para as interações: as pausas e ações nas interações.",
  [], slides=["nasc_21"])
C("nasc", S, "Emoção no bebê",
  "Não há uma forma de saber exatamente que emoção um bebê está sentindo.",
  ["A melhor maneira é tentar julgar que emoção o bebê parece expressar por meio de seu corpo e rosto."],
  slides=["nasc_21"])
C("nasc", S, "Emoções ao nascimento",
  "No nascimento aparecem interesse, sofrimento, aversão e o sorriso neonatal.",
  ["Interesse: ativado por novidade ou movimento.",
   "Sofrimento: ativado por dor.",
   "Aversão: ativada por substâncias ofensivas.",
   "Sorriso neonatal (um “meio-sorriso”): aparece espontaneamente, sem razão conhecida."],
  quando="No nascimento.", faixa="rn", slides=["nasc_22"], curto="Interesse, sofrimento, aversão")
C("nasc", S, "Sorriso de prazer/social",
  "Sorriso de prazer/social, precursor da alegria.",
  ["Estímulos: voz humana aguda; bater as mãos do bebê; uma voz familiar; um rosto inclinado em cumprimento."],
  quando="3 a 6 semanas.", faixa="m1_3", slides=["nasc_22"], curto="Sorriso social · 3–6 sem")
C("nasc", S, "Tristeza no bebê",
  "Emoção de tristeza, ativada por um procedimento médico doloroso.",
  [], quando="2 a 3 meses.", faixa="m1_3", slides=["nasc_22"], curto="Tristeza · 2–3 m")
C("nasc", S, "Emoções aos 7 meses",
  "Aos 7 meses aparecem cautela, frustração, surpresa, medo, raiva e alegria.",
  ["Cautela (precursor do medo): rosto de um estranho.",
   "Frustração (precursor da raiva): ser restringido ou impedido.",
   "Surpresa: caixa de surpresas.",
   "Medo: novidade extrema.",
   "Raiva: falha ou interrupção de algo.",
   "Alegria: experiência com significado positivo."],
  quando="7 meses.", faixa="m7_12", slides=["nasc_22"], curto="Cautela, frustração, medo, raiva…")

# =====================================================================
# DESENVOLVIMENTO FÍSICO
# =====================================================================
S = "Cérebro e sistema nervoso"
C("fis", S, "Cérebro ao nascimento",
  "Ao nascimento, o mesencéfalo e a medula são as partes mais completamente desenvolvidas; o córtex é a parte menos desenvolvida.",
  ["Mesencéfalo e medula regulam frequência cardíaca, respiração, atenção, sono, vigília, eliminação e movimento da cabeça e do pescoço.",
   "Córtex cerebral: substância cinzenta torcida que encobre o mesencéfalo; está envolvida na percepção, no movimento corporal, no pensamento e na linguagem.",
   "As mudanças no cérebro e no sistema nervoso continuam por toda a infância e a adolescência."],
  faixa="rn", slides=["fis_02"], curto="Cérebro ao nascimento",
  extra=[("No app de Neuroanatomia", "Veja Mesencéfalo (alfinete 6), Medula Espinal (11) e Telencéfalo (2).")])
C("fis", S, "Surtos de crescimento cerebral",
  "O cérebro cresce mais em surtos do que de maneira suave e contínua. Cada surto é acompanhado por um período de estabilidade.",
  ["Muitos surtos são localizados: restritos a uma ou a algumas partes do cérebro, em vez de se aplicarem ao cérebro inteiro.",
   "Surtos descritos nos slides: 20 meses, 4 anos, 6–8 anos, 10–12 anos, 13–15 anos e a partir dos 17 anos."],
  faixa="a1_2", slides=["fis_03"], curto="Surtos de crescimento")
C("fis", S, "Surto dos 20 meses",
  "Acontece ao mesmo tempo em que a maioria dos bebês mostra evidência de planejamento dirigido ao objetivo em seu comportamento.",
  [], quando="Cerca de 20 meses.", faixa="a1_2", slides=["fis_03"], curto="Surto · 20 meses")
C("fis", S, "Surto dos 4 anos",
  "É acompanhado por um nível impressionante de fluência tanto na fala quanto no entendimento da linguagem.",
  [], quando="Cerca de 4 anos.", faixa="a4_6", slides=["fis_04"], curto="Surto · 4 anos")
C("fis", S, "Surto dos 6 aos 8 anos",
  "Melhora das habilidades motoras finas e da coordenação olho-mão.",
  [], quando="6 a 8 anos.", faixa="a6_9", slides=["fis_04"], curto="Surto · 6–8 anos")
C("fis", S, "Surto dos 10 aos 12 anos",
  "Melhora na cognição lógica, no planejamento e na memória.",
  [], quando="10 a 12 anos.", faixa="a9_12", slides=["fis_04"], curto="Surto · 10–12 anos")
C("fis", S, "Surto dos 13 aos 15 anos",
  "Melhora na percepção espacial e nas funções motoras, além da consolidação do pensamento abstrato.",
  [], quando="13 a 15 anos.", faixa="adol", slides=["fis_05"], curto="Surto · 13–15 anos")
C("fis", S, "Surto a partir dos 17 anos",
  "Último surto de crescimento cerebral: começa por volta dos 17 anos e continua até o início da idade adulta, com melhora nas ações que requerem essas funções cognitivas.",
  [], quando="A partir de ~17 anos.", faixa="adol", slides=["fis_05"], curto="Surto · 17+ anos")
C("fis", S, "Sinaptogênese",
  "Processo de criar conexões (sinapses) entre neurônios; resulta do crescimento de dendritos e axônios.",
  ["Contribui para o crescimento cerebral e é seguida por um período de poda."],
  slides=["fis_06"])
C("fis", S, "Poda sináptica",
  "Período, depois da arrancada da sinaptogênese, em que as conexões desnecessárias são eliminadas, fazendo todo o sistema operar de maneira mais eficiente.",
  [], slides=["fis_06"])
C("fis", S, "Plasticidade cerebral",
  "Capacidade do cérebro de responder à experiência.",
  ["Está no auge nos primeiros anos de vida."],
  slides=["fis_06"])
C("fis", S, "Mielinização",
  "Criação de bainhas (coberturas) em torno dos axônios, que melhoram a condutividade dos nervos.",
  ["A sequência de mielinização segue padrões céfalo-caudal e próximo-distal.",
   "Impulsiona o desenvolvimento de funções sensoriais (atenção e atenção seletiva), motoras, de memória e intelectuais."],
  slides=["fis_07"],
  extra=[("No app de Neuroanatomia", "Veja Substância Branca (alfinete 10): axônios mielínicos.")])
C("fis", S, "Lateralização",
  "Especialização funcional que ocorre nos dois hemisférios do cérebro. Em 95% dos seres humanos as funções cerebrais são lateralizadas: dominância cerebral esquerda.",
  ["Hemisfério esquerdo (no esquema do slide): racional, cético e cauteloso, lógico, estatístico, linear, mecânico.",
   "Hemisfério direito: emocional, criativo e imaginativo, intuitivo, aventureiro, artístico, musical."],
  slides=["fis_08"],
  extra=[("No app de Neuroanatomia", "Veja Telencéfalo (alfinete 2) e os lobos (38 a 40).")])
C("fis", S, "Percepção espacial",
  "Capacidade de identificar e influenciar relacionamentos de objetos no espaço.",
  ["O desenvolvimento da percepção espacial está associado à lateralização."],
  slides=["fis_09"])
C("fis", S, "Lateralidade (dominância manual)",
  "Tendência a usar principalmente a mão direita ou a esquerda.",
  ["É outro aspecto importante da lateralização neurológica."],
  slides=["fis_09"])

S = "Tamanho, forma e habilidades"
C("fis", S, "Crescimento na infância",
  "Aos 2 anos, a criança tem aproximadamente metade da altura que terá quando adulta.",
  ["Nos primeiros dois anos, o bebê ganha altura muito rapidamente: acrescenta de 25 a 30 cm no primeiro ano e triplica o peso corporal no mesmo período.",
   "Em torno dos 2 anos, o ritmo fica mais lento, porém constante: de 5 a 7 cm e cerca de 2,72 kg por ano até a adolescência."],
  quando="Rápido até 2 anos; depois 5–7 cm e ~2,72 kg por ano.", faixa="a1_2", slides=["fis_10"], curto="Crescimento")
C("fis", S, "Fontanelas",
  "Espaços que separam os diversos ossos do crânio do recém-nascido.",
  ["Permitem que a cabeça seja comprimida sem ferimento durante o nascimento e dão ao cérebro espaço para crescer.",
   "Na maioria das crianças, são preenchidas por ossos, criando um único osso."],
  quando="Preenchidas entre 12 e 18 meses.", faixa="a1_2", slides=["fis_11"], curto="Fontanelas fecham · 12–18 m")
C("fis", S, "Ossificação",
  "Processo de endurecimento ósseo. Os ossos de um bebê são mais macios, com maior conteúdo de água do que os de um adulto.",
  ["Ocorre regularmente do nascimento até a puberdade.",
   "Mão, pulso, tornozelos e pé têm menos ossos no nascimento do que terão na maturidade. O adulto tem nove ossos no pulso; a criança de 1 ano tem apenas três, e os seis restantes se desenvolvem durante a infância."],
  quando="Do nascimento até a puberdade.", faixa="rn", slides=["fis_12"], curto="Ossificação")
C("fis", S, "Músculos e gordura",
  "Os músculos mudam em qualidade da infância à adolescência, tornando-se mais longos e mais compactos. A gordura é armazenada sobretudo sob a pele.",
  ["A espessura da camada de gordura diminui até aproximadamente os 6 ou 7 anos.",
   "Durante e após a puberdade, as proporções de gordura aumentam entre as meninas e diminuem entre os meninos, enquanto a proporção de peso muscular aumenta nos meninos e diminui nas meninas."],
  quando="Gordura diminui até ~6–7 anos.", faixa="a6_9", slides=["fis_13"], curto="Gordura diminui até 6–7 anos")

S = "Desenvolvimento motor"
C("fis", S, "Desenvolvimento motor",
  "Crescimento e mudança na capacidade de dominar habilidades motoras grosseiras (como caminhar ou correr) e habilidades motoras finas (como desenhar ou escrever).",
  [], slides=["fis_14"])
C("fis", S, "Motor: 1 a 3 meses",
  "Reflexo de passo; levanta a cabeça; senta com apoio.",
  ["Segura objetos se colocados na mão; começa a golpear objetos."],
  quando="1 a 3 meses.", faixa="m1_3", slides=["fis_14"], curto="Motor · 1–3 m")
C("fis", S, "Motor: 4 a 6 meses",
  "Rola sobre o corpo; senta com autoapoio; rasteja.",
  ["Estende a mão e segura objetos usando uma mão."],
  quando="4 a 6 meses.", faixa="m4_6", slides=["fis_14"], curto="Motor · 4–6 m")
C("fis", S, "Motor: 7 a 9 meses",
  "Senta-se sem apoio.",
  ["Transfere objetos de uma mão para a outra; pode segurar com polegar e indicador (“agarrar de pinça”)."],
  quando="7 a 9 meses.", faixa="m7_12", slides=["fis_14"], curto="Motor · 7–9 m")
C("fis", S, "Motor: 10 a 12 meses",
  "Dá impulso para levantar; caminha agarrando a mobília e depois caminha sem ajuda; agacha-se e inclina-se.",
  ["Segura uma colher atravessada na palma da mão."],
  quando="10 a 12 meses.", faixa="m7_12", slides=["fis_14"], curto="Motor · 10–12 m")
C("fis", S, "Motor: 13 a 18 meses",
  "Caminha para a frente e para trás; corre.",
  ["Empilha dois blocos; coloca objetos em pequenos recipientes e os despeja."],
  quando="13 a 18 meses.", faixa="a1_2", slides=["fis_14"], curto="Motor · 13–18 m")
C("fis", S, "Motor: 2 a 4 anos",
  "Corre facilmente; sobe escadas usando um pé por degrau; salta com os dois pés e pedala.",
  ["Pega objetos pequenos e corta papel com tesoura."],
  quando="2 a 4 anos.", faixa="a2_4", slides=["fis_15"], curto="Motor · 2–4 a")
C("fis", S, "Motor: 4 a 6 anos",
  "Caminha na ponta dos pés; caminha sobre uma linha fina; salta, atira e pega.",
  ["Enfia linha em contas e em agulhas; segura o lápis, mas escreve com rigidez e concentração."],
  quando="4 a 6 anos.", faixa="a4_6", slides=["fis_15"], curto="Motor · 4–6 a")
C("fis", S, "Motor: 6 a 9 anos",
  "Chuta e bate em objetos parados; intercepta objetos em movimento correndo; corre a 10 km/h.",
  ["Usa preensão madura ao escrever ou desenhar; usa martelo; rebate objeto."],
  quando="6 a 9 anos.", faixa="a6_9", slides=["fis_15"], curto="Motor · 6–9 a")
C("fis", S, "Motor: 9 a 12 anos",
  "Chuta, bate e pega objetos em movimento correndo; aumento significativo no pulo vertical; corre a 15 km/h.",
  ["Rebate objeto com uma mão com bom controle."],
  quando="9 a 12 anos.", faixa="a9_12", slides=["fis_15"], curto="Motor · 9–12 a")

S = "Puberdade"
C("fis", S, "Puberdade",
  "Série de alterações hormonais e físicas durante a adolescência que levam à maturidade sexual.",
  [], faixa="adol", slides=["fis_16"])
C("fis", S, "Puberdade nas meninas",
  "Alterações físicas nas meninas durante a puberdade.",
  ["Desenvolvimento dos seios: começa com um pequeno nódulo sob o mamilo, seguido de aumento gradual do volume da mama e da aréola.",
   "Pelos pubianos: inicialmente uma fina camada de pelos lisos e claros, que se tornam mais grossos e escuros com o tempo.",
   "Aumento do quadril e da cintura: a gordura corporal se redistribui, com quadris mais largos e cintura mais fina.",
   "Pelos nas axilas e nas pernas.",
   "Mudança na voz: a voz fica mais fina e aguda."],
  faixa="adol", slides=["fis_16", "fis_17"], curto="Puberdade: meninas")
C("fis", S, "Menarca",
  "A primeira menstruação.",
  [], quando="Geralmente entre 12 e 15 anos, mas pode variar.", faixa="adol", slides=["fis_16"], curto="Menarca · 12–15 a")
C("fis", S, "Puberdade nos meninos",
  "Alterações físicas nos meninos durante a puberdade.",
  ["Aumento dos testículos e do pênis: os testículos aumentam de tamanho e o pênis cresce em comprimento e diâmetro.",
   "Pelos pubianos, nas axilas e nas pernas; surgimento da barba.",
   "Aumento dos ombros e do tórax: a massa muscular se desenvolve, com ombros mais largos e tórax mais amplo.",
   "Mudança na voz: a voz fica mais grave e grossa."],
  faixa="adol", slides=["fis_18", "fis_19"], curto="Puberdade: meninos")
C("fis", S, "Primeira ejaculação",
  "Primeira ejaculação do menino na puberdade.",
  ["Ocorre durante o sono ou com a masturbação."],
  quando="Geralmente entre 12 e 14 anos.", faixa="adol", slides=["fis_18"], curto="1ª ejaculação · 12–14 a")

# =====================================================================
# DESENVOLVIMENTO PERCEPTUAL
# =====================================================================
S = "Visão"
C("perc", S, "Acuidade visual",
  "Diz respeito ao quanto uma pessoa pode enxergar bem.",
  ["É medida por uma fórmula: capacidade sensorial em pés ÷ distância do objeto em pés.",
   "Na visão normal, a pessoa enxerga bem um objeto que está a 20 pés (20/20).",
   "Na visão empobrecida, a pessoa precisa estar mais próxima do objeto: por exemplo, a 6 pés de um objeto que, em visão normal, seria visto a 20 pés (6/20)."],
  slides=["perc_02"])
C("perc", S, "Acuidade visual do bebê",
  "No nascimento, a acuidade visual está entre 20/200 e 20/400, mas melhora rapidamente no primeiro ano (mielinização, desenvolvimento dendrítico e poda).",
  ["A maioria dos bebês alcança o nível 20/20 por volta dos 2 anos.",
   "Enxergar mal de longe não é tão negativo: o bebê não enxerga claramente as coisas distantes, mas enxerga bem em curta distância."],
  quando="Nascimento: 20/200 a 20/400 · por volta de 2 anos: 20/20.", faixa="rn", slides=["perc_03"], curto="Acuidade: 20/200 → 20/20")
C("perc", S, "Rastreamento",
  "Capacidade visual de seguir um objeto em movimento com os olhos.",
  ["Inicialmente é ineficiente: bebês com menos de 2 meses mostram algum rastreamento por breves períodos se o alvo se move muito lentamente.",
   "Por volta de 6 a 10 semanas, o rastreamento passa a ser hábil muito rapidamente."],
  quando="Mudança por volta de 6 a 10 semanas.", faixa="m1_3", slides=["perc_04"], curto="Rastreamento · 6–10 sem")
C("perc", S, "Percepção de profundidade",
  "Capacidade necessária sempre que se tenta pegar alguma coisa ou se decide se há espaço para virar antes que um carro se aproxime.",
  ["Há três tipos de sugestões (pistas): binoculares, monoculares e cinéticas."],
  slides=["perc_05"])
C("perc", S, "Sugestões binoculares",
  "Envolvem os dois olhos, cada um recebendo uma imagem visual ligeiramente diferente do objeto.",
  ["Quanto mais perto o objeto está, mais diferentes são essas duas visões."],
  slides=["perc_05"])
C("perc", S, "Sugestões monoculares",
  "Requerem estímulo de apenas um olho.",
  ["Exemplo: quando um objeto está parcialmente na frente de outro, sabe-se que o objeto parcialmente oculto está mais longe."],
  slides=["perc_05"])
C("perc", S, "Sugestões cinéticas",
  "Vêm do próprio movimento ou do movimento de algum objeto.",
  ["Se você mover a cabeça, objetos próximos parecem se mover mais do que objetos distantes."],
  slides=["perc_06"])

S = "Audição"
C("perc", S, "Acuidade auditiva do bebê",
  "Embora a audição melhore até a adolescência, a acuidade auditiva dos recém-nascidos é, na verdade, melhor do que a sua acuidade visual.",
  ["Com sons agudos a acuidade é menor: sons agudos devem ser mais altos para um recém-nascido ouvir do que para crianças mais velhas ou adultos."],
  faixa="rn", slides=["perc_07"], curto="Audição > visão")
C("perc", S, "Atenção à língua",
  "Desde o nascimento (talvez antes), o bebê presta atenção a aspectos cruciais da língua que ouve, como ênfase e entonação.",
  [], faixa="rn", slides=["perc_07"], curto="Atenção à língua")
C("perc", S, "Reconhecimento de padrões de sons",
  "Os bebês reconhecem padrões de sons.",
  ["Aos 5 meses, podem reconhecer seus próprios nomes.",
   "Respondem a notas dissonantes (tons que não soam agradáveis quando tocados juntos) exatamente como os adultos.",
   "Reconhecem melodias familiares, não importa em que tom sejam tocadas, e percebem quando uma melodia familiar é tocada em um instrumento diferente."],
  quando="Reconhecem o próprio nome aos 5 meses.", faixa="m4_6", slides=["perc_08"], curto="Próprio nome · 5 m")
C("perc", S, "Cantigas e músicas",
  "Os bebês são capazes de diferenciar cantigas de músicas.",
  ["Seu comportamento acompanha a brincadeira da cantiga e a dança da música."],
  slides=["perc_09"])
C("perc", S, "Localização do som",
  "Habilidade auditiva básica que existe no nascimento e melhora com a idade: determinar a localização de um som.",
  ["Os sons chegam a um ouvido ligeiramente antes de chegar ao outro; isso permite determinar a localização."],
  faixa="rn", slides=["perc_09"], curto="Localização do som")

S = "Combinando informações de diversos sentidos"
C("perc", S, "Percepção intermodal",
  "Percepção que integra informações de diversos sentidos. Raramente se obtém informação de apenas um sentido de cada vez.",
  ["Piaget acreditava que a percepção intermodal não estava presente até quase o final do primeiro ano de vida, depois de o bebê acumular muitas experiências com objetos específicos.",
   "Outros teóricos afirmam que alguma integração está presente no nascimento.",
   "Em bebês de 5 meses, a percepção intermodal pode ser facilmente demonstrada."],
  quando="Demonstrável aos 5 meses (Piaget: quase no final do 1º ano).", faixa="m4_6", slides=["perc_10", "perc_11"], curto="Percepção intermodal · 5 m")

S = "Ignorando informação"
C("perc", S, "Constâncias perceptuais",
  "Conjunto de regras perceptuais que a criança deve adquirir para desenvolver a capacidade de ignorar alguns tipos de dados perceptuais.",
  ["Os quatro tipos dos slides: constância de forma, constância de cor, constância do objeto (objetal) e permanência do objeto."],
  slides=["perc_12"])
C("perc", S, "Constância de forma",
  "Capacidade de reconhecer e identificar um estímulo visual mesmo que seu tamanho, cor e direção tenham sido alterados.",
  [], quando="2 meses.", faixa="m1_3", slides=["perc_12"], curto="Constância de forma · 2 m")
C("perc", S, "Constância de cor",
  "Habilidade de ver a cor de um objeto como sendo a mesma, apesar de mudanças na iluminação ou na sombra.",
  [], quando="2 meses.", faixa="m1_3", slides=["perc_13"], curto="Constância de cor · 2 m")
C("perc", S, "Constância do objeto (objetal)",
  "Expressão geral que descreve a habilidade de ver que os objetos permanecem os mesmos, apesar de mudanças na informação sensorial sobre eles.",
  [], quando="De 3 meses a 1 ano.", faixa="m1_3", slides=["perc_13"], curto="Constância do objeto · 3 m–1 a")
C("perc", S, "Permanência do objeto",
  "Entendimento de que os objetos continuam a existir mesmo quando não podem ser percebidos diretamente.",
  [], quando="18 a 24 meses.", faixa="a1_2", slides=["perc_13"], curto="Permanência do objeto · 18–24 m")

S = "Percepção de sinais sociais"
C("perc", S, "Atenção a sinais sociais e emocionais",
  "Por volta dos 2 ou 3 meses, os bebês começam a prestar atenção a sinais sociais/emocionais nos rostos das pessoas e a responder diferentemente a variações nas expressões emocionais dos outros.",
  ["Inicialmente, discriminam melhor as emoções quando recebem informação por meio de muitos canais simultaneamente (tom de voz e expressão facial)."],
  quando="2 a 3 meses.", faixa="m1_3", slides=["perc_14"], curto="Sinais sociais · 2–3 m")
C("perc", S, "Leitura de um canal por vez",
  "Entre os 5 e os 7 meses, os bebês podem começar a “ler” um canal de cada vez: responder só à expressão facial ou só à expressão vocal.",
  ["Isso vale mesmo quando as emoções são exibidas por um estranho, em vez da mãe ou do pai."],
  quando="5 a 7 meses.", faixa="m4_6", slides=["perc_15"], curto="Um canal por vez · 5–7 m")
C("perc", S, "Expressão emocional e contexto",
  "No final do primeiro ano, os bebês associam a informação sobre a expressão emocional de uma pessoa ao contexto ambiental.",
  ["Além disso, bebês de 1 ano podem se acalmar quando seus cuidadores se comportam de formas esperadas."],
  quando="Final do primeiro ano.", faixa="m7_12", slides=["perc_15"], curto="Emoção + contexto · fim do 1º ano")

# =====================================================================
# DESENVOLVIMENTO COGNITIVO
# =====================================================================
S = "Cognição piagetiana"
C("cogn", S, "Teoria de Piaget (construtivismo)",
  "Para Piaget, o conhecimento não é passivamente recebido, mas construído ativamente pelo indivíduo a partir da interação com o meio (construtivismo).",
  ["O desenvolvimento cognitivo das crianças ocorre em quatro estágios distintos, cada um com características próprias."],
  slides=["cogn_02"], curto="Piaget · construtivismo")
C("cogn", S, "Estágio sensório-motor",
  "Até os 2 anos: a criança aprende por meio da exploração sensorial e motora do mundo.",
  [], quando="Até 2 anos.", faixa="rn", slides=["cogn_02"], curto="Sensório-motor · até 2 a")
C("cogn", S, "Estágio pré-operatório",
  "Dos 2 aos 7 anos: a criança desenvolve a linguagem e a capacidade de pensar simbolicamente, mas ainda é egocêntrica e tem dificuldade em compreender o ponto de vista dos outros.",
  [], quando="2 a 7 anos.", faixa="a2_4", slides=["cogn_03"], curto="Pré-operatório · 2–7 a")
C("cogn", S, "Estágio operatório concreto",
  "Dos 7 aos 11 anos: a criança torna-se capaz de pensar logicamente sobre objetos concretos, mas ainda tem dificuldade em lidar com abstrações.",
  [], quando="7 a 11 anos.", faixa="a6_9", slides=["cogn_03"], curto="Operatório concreto · 7–11 a")
C("cogn", S, "Estágio operatório formal",
  "A partir dos 11 anos: o adolescente desenvolve a capacidade de pensar abstrata e hipoteticamente.",
  [], quando="A partir de 11 anos.", faixa="a9_12", slides=["cogn_03"], curto="Operatório formal · 11+ a")
C("cogn", S, "Equilibração",
  "Processo de autorregulação interna do organismo, que consiste na busca sucessiva de reequilíbrio após cada desequilíbrio sofrido.",
  ["O desenvolvimento cognitivo é impulsionado pela busca de um estado de equilíbrio entre a assimilação e a acomodação."],
  slides=["cogn_04"])
C("cogn", S, "Assimilação",
  "Incorporação de esquemas mentais.",
  ["Juntamente com a acomodação, busca o equilíbrio."],
  slides=["cogn_04"])
C("cogn", S, "Acomodação",
  "Modificação de esquemas mentais.",
  ["Juntamente com a assimilação, busca o equilíbrio."],
  slides=["cogn_04"])
C("cogn", S, "Equilíbrio e desequilíbrio no desenvolvimento",
  "O desenvolvimento é propulsionado pelo movimento de equilíbrio e desequilíbrio.",
  ["Esquema do slide: desequilíbrio → assimilação (incorporação de esquemas) e acomodação (modificação de esquemas) → equilíbrio → novos esquemas."],
  slides=["cogn_05"])

S = "Memória"
C("cogn", S, "Memória (processos)",
  "Processo pelo qual codificamos, armazenamos e recuperamos informações.",
  ["Codificação: registro inicial da informação.",
   "Armazenamento: informação salva para uso futuro.",
   "Recuperação: recupera a informação armazenada."],
  slides=["cogn_06"])
C("cogn", S, "Memória sensorial",
  "Armazenamento momentâneo inicial da informação, que dura apenas um instante.",
  ["Se a informação não passa para a memória de curto prazo, ela se perde para sempre."],
  slides=["cogn_07"])
C("cogn", S, "Memória de curto prazo",
  "Memória que retém a informação por 15 a 25 segundos; é o local onde a informação adquire seu primeiro significado.",
  ["Armazena até sete agrupamentos de uma vez."],
  slides=["cogn_07"])
C("cogn", S, "Memória de trabalho",
  "Conjunto de armazenamentos temporários (visual e verbal) que manipulam e ensaiam as informações de maneira ativa.",
  ["Está relacionada à memória de curto prazo."],
  slides=["cogn_07"])
C("cogn", S, "Pista de recuperação",
  "Estímulo que nos permite recordar mais facilmente informações que se encontram na memória de longo prazo.",
  ["Exemplos: emoção, som, odor."],
  slides=["cogn_08"])
C("cogn", S, "Reconhecimento",
  "Tarefa de memória em que a pessoa é apresentada a um estímulo e perguntada se foi exposta a ele no passado, ou deve identificá-lo em uma lista de alternativas.",
  [], slides=["cogn_08"])
C("cogn", S, "Recordação",
  "Tarefa voluntária de memória em que uma informação específica deve ser recuperada.",
  ["É o processo mais difícil: envolve busca, recuperação e análise."],
  slides=["cogn_08"])
C("cogn", S, "Memória explícita",
  "Recordação intencional ou consciente da informação.",
  [], slides=["cogn_09"])
C("cogn", S, "Memória implícita",
  "Lembranças das quais as pessoas não têm consciência, mas que podem afetar o desempenho e o comportamento posterior.",
  [], slides=["cogn_09"])
C("cogn", S, "Priming",
  "Memória de uma palavra ou conceito ativada por uma pista de recuperação, sem que a pessoa tenha memória consciente da aquisição dessa palavra ou conceito.",
  [], slides=["cogn_09"])
C("cogn", S, "Memórias instantâneas",
  "Memórias relacionadas a um evento específico importante ou surpreendente, que são recordadas com facilidade e com imagens vívidas.",
  [], slides=["cogn_10"])
C("cogn", S, "Processos construtivos",
  "Processos em que as memórias são influenciadas pelo significado que atribuímos aos eventos (ressignificar o passado).",
  ["As crianças são altamente influenciadas por processos construtivos."],
  slides=["cogn_11"])
C("cogn", S, "Esquemas (na memória)",
  "Organização de informações armazenadas na memória que influenciam o modo como novas informações são interpretadas, armazenadas e recordadas.",
  ["Influenciam fortemente as nossas memórias autobiográficas."],
  slides=["cogn_11"])
C("cogn", S, "Pseudomemórias",
  "A memória humana não funciona como um gravador: é um processo construtivo, que às vezes leva a erros e pode até resultar na invenção de pseudomemórias de eventos que nunca aconteceram realmente.",
  ["Conforme o cérebro e o sistema nervoso se desenvolvem nos primeiros anos, a capacidade da memória de curto prazo aumenta (e isso pode também dever-se à amplitude das experiências)."],
  slides=["cogn_12"])

S = "Inteligência"
C("cogn", S, "Inteligência",
  "Conjunto de capacidades definidas de várias formas por diferentes psicólogos, que geralmente inclui a capacidade de raciocinar de maneira abstrata, de tirar proveito da experiência e de se adaptar a contextos ambientais variáveis.",
  [], slides=["cogn_13"])
C("cogn", S, "Fator g (inteligência geral)",
  "Visão dos primeiros psicólogos de que existe uma inteligência única, geral: a inteligência g ou fator-g.",
  ["Outros psicólogos veem a inteligência como um conceito multidimensional, que inclui diferentes tipos de inteligência."],
  slides=["cogn_13"])
C("cogn", S, "Teoria das inteligências múltiplas (Gardner)",
  "Teoria que propõe a existência de oito tipos distintos de inteligência.",
  ["Musical, espacial, corporal-cinestésica, interpessoal, naturalista, lógico-matemática, intrapessoal e linguística."],
  slides=["cogn_14", "cogn_15", "cogn_16"], curto="Gardner · 8 inteligências")
C("cogn", S, "Inteligência musical",
  "Habilidades em tarefas que envolvem música.", [], slides=["cogn_14"])
C("cogn", S, "Inteligência espacial",
  "Habilidades que envolvem configurações espaciais, como as usadas por artistas e arquitetos.", [], slides=["cogn_14"])
C("cogn", S, "Inteligência corporal-cinestésica",
  "Habilidade no uso de todo o corpo ou de várias partes dele na solução de problemas ou na construção de produtos ou apresentações.",
  ["Exemplificada por dançarinos, atletas, atores e cirurgiões."], slides=["cogn_15"])
C("cogn", S, "Inteligência interpessoal",
  "Habilidades de interação com os outros, como sensibilidade a seus estados de humor, temperamento, motivações e intenções.",
  [], slides=["cogn_15"])
C("cogn", S, "Inteligência naturalista",
  "Capacidade de identificar e classificar padrões na natureza.", [], slides=["cogn_15"])
C("cogn", S, "Inteligência lógico-matemática",
  "Habilidades na resolução de problemas e no pensamento científico.", [], slides=["cogn_16"])
C("cogn", S, "Inteligência intrapessoal",
  "Conhecimento dos aspectos internos de si mesmo; acesso aos próprios sentimentos e emoções.", [], slides=["cogn_16"])
C("cogn", S, "Inteligência linguística",
  "Habilidades envolvidas na produção e na utilização da língua.", [], slides=["cogn_16"])
C("cogn", S, "Inteligência fluida",
  "Inteligência que reflete a capacidade de raciocinar de maneira abstrata.", [], slides=["cogn_17"])
C("cogn", S, "Inteligência cristalizada",
  "Inteligência que abrange o acúmulo de informações, habilidades e estratégias aprendidas por meio da experiência e que podem ser aplicadas em situações de resolução de problemas.",
  [], slides=["cogn_17"])
C("cogn", S, "Abordagens de processamento de informações",
  "A inteligência reflete-se nos modos como as pessoas armazenam e usam material para resolver tarefas intelectuais.",
  [], slides=["cogn_18"])
C("cogn", S, "Teoria da inteligência prática",
  "A inteligência é vista em termos de sucesso não acadêmico, profissional e pessoal.", [], slides=["cogn_18"])
C("cogn", S, "Inteligência emocional",
  "Inteligência que fornece uma compreensão do que as outras pessoas estão sentindo e experimentando, permitindo responder adequadamente às necessidades dos outros.",
  [], slides=["cogn_18"])
C("cogn", S, "Testes de inteligência",
  "Testes que visam quantificar o nível de inteligência de uma pessoa.",
  ["O primeiro esforço de testar a inteligência baseou-se em uma premissa totalmente errônea: a de que o tamanho e a forma da cabeça de uma pessoa poderiam ser usados como uma medida objetiva da inteligência."],
  slides=["cogn_19"])
C("cogn", S, "Alfred Binet",
  "Psicólogo francês que desenvolveu os primeiros testes de inteligência reais.",
  ["Premissa simples: o desempenho em determinadas tarefas ou itens de teste melhorava com a idade cronológica."],
  slides=["cogn_19"])
C("cogn", S, "Quociente de inteligência (QI)",
  "Medida baseada nos testes de Binet que leva em conta a idade mental e a cronológica de um indivíduo; busca avaliar a capacidade cognitiva em relação à média da população.",
  ["Hoje, em geral, os testes seguem a mesma lógica (capacidade cognitiva em relação à média populacional), mas são compreendidos a partir da ideia de inteligências múltiplas (WAIS-IV e WISC-IV)."],
  slides=["cogn_20"])
C("cogn", S, "Testes de inteligência mais usados",
  "Os três testes mais usados hoje pelos psicólogos: Stanford-Binet V, Escala de Inteligência Wechsler Pré-Escolar e Primária (WPPSI-III) e Escalas Wechsler para Crianças (WISC-IV).",
  [], slides=["cogn_21"])
C("cogn", S, "Teoria triárquica da inteligência (Sternberg)",
  "Teoria de Sternberg que mede três aspectos da inteligência: analítica, criativa e prática.",
  [], slides=["cogn_22", "cogn_23"], curto="Sternberg · triárquica")
C("cogn", S, "Inteligência analítica",
  "Inclui a capacidade de planejar, lembrar fatos e organizar informação.", [], slides=["cogn_22"])
C("cogn", S, "Inteligência criativa",
  "Inclui discernimento e capacidade de ver novas relações entre eventos e experiências.", [], slides=["cogn_22"])
C("cogn", S, "Inteligência prática (Sternberg)",
  "Inclui habilidade em aplicar informação ao mundo real ou resolver problemas práticos.", [], slides=["cogn_23"])

S = "Comportamento respondente"
C("cogn", S, "Comportamento respondente",
  "Também chamado de comportamento reflexo: é o comportamento não voluntário e inclui as respostas eliciadas por estímulos antecedentes do ambiente.",
  ["Como a resposta é causada pelo evento ambiental antecedente, diz-se que o estímulo elicia a resposta, ou que ele é um eliciador.",
   "São interações estímulo-resposta (S-R) incondicionadas: certos eventos ambientais eliciam certas respostas do organismo que independem de aprendizagem."],
  slides=["cogn_27"])
C("cogn", S, "Características das relações respondentes",
  "As relações respondentes possuem quatro características: limiar, magnitude, duração e latência.",
  [], slides=["cogn_28", "cogn_29"])
C("cogn", S, "Limiar",
  "Intensidade mínima do estímulo necessária para que a resposta seja eliciada.", [], slides=["cogn_28"])
C("cogn", S, "Magnitude",
  "Amplitude da resposta.", [], slides=["cogn_28"])
C("cogn", S, "Duração",
  "Tempo que a resposta eliciada perdura.", [], slides=["cogn_28"])
C("cogn", S, "Latência",
  "Intervalo de tempo entre a apresentação do estímulo e a ocorrência da resposta.", [], slides=["cogn_29"])
C("cogn", S, "Condicionamento respondente",
  "Comportamentos a partir da história evolutiva podem ocorrer em novas situações, dependendo da história individual do organismo, por meio do condicionamento respondente.",
  ["Isso ocorre em comportamentos humanos que necessitam de intervenção, como ansiedade generalizada, pânico, enfraquecimento do sistema imunológico em situações de estresse, dependências químicas etc."],
  slides=["cogn_30"])
C("cogn", S, "Estímulo incondicionado, pareado e condicionado",
  "No esquema do condicionamento respondente, um estímulo incondicionado (S) elicia o comportamento (C); um estímulo pareado é apresentado junto dele; depois do pareamento, o estímulo condicionado passa a eliciar o comportamento.",
  [], slides=["cogn_24", "cogn_25", "cogn_26"],
  extra=[("Complemento", "Os slides mostram apenas o esquema (estímulo incondicionado, estímulo pareado, estímulo condicionado e comportamento). A frase que explica a sequência é um resumo padrão do condicionamento respondente.")])

S = "Comportamento operante"
C("cogn", S, "Comportamento operante",
  "Relação organismo-ambiente em que a emissão de respostas de um indivíduo afeta ou altera o ambiente.",
  ["O comportamento operante opera sobre o mundo, direta ou indiretamente.",
   "É fruto da aprendizagem: é a ação do organismo sobre o meio e o efeito dela resultante, e atende à satisfação de alguma necessidade."],
  slides=["cogn_34"])
_nota_op = [("Complemento", "O slide mostra o esquema (R, reforço/punição → comportamento aumenta ou diminui). A definição de positivo e negativo (apresentar ou retirar um estímulo) é conteúdo padrão de análise do comportamento. Confira com o professor.")]
C("cogn", S, "Reforço positivo",
  "Consequência que aumenta a frequência do comportamento. No esquema do slide, o comportamento (C) é seguido de reforço positivo (R) e aumenta a frequência.",
  ["Na definição padrão: um estímulo é apresentado depois do comportamento."],
  slides=["cogn_31"], extra=_nota_op)
C("cogn", S, "Reforço negativo",
  "Também aumenta a frequência do comportamento (esquema do slide: reforço negativo → aumenta a frequência).",
  ["Na definição padrão: um estímulo aversivo é retirado depois do comportamento."],
  slides=["cogn_31"], extra=_nota_op)
C("cogn", S, "Punição positiva",
  "Consequência que diminui a frequência do comportamento (esquema do slide: punição positiva → diminui a frequência).",
  ["Na definição padrão: um estímulo aversivo é apresentado depois do comportamento."],
  slides=["cogn_33"], extra=_nota_op)
C("cogn", S, "Punição negativa",
  "Também diminui a frequência do comportamento (esquema do slide: punição negativa → diminui a frequência).",
  ["Na definição padrão: um estímulo reforçador é retirado depois do comportamento."],
  slides=["cogn_33"], extra=_nota_op)
C("cogn", S, "Reforço contínuo",
  "Quando o reforço é apresentado pelo período todo de tempo.", [], slides=["cogn_32"])
C("cogn", S, "Reforço intermitente",
  "Quando o reforço é apresentado apenas em determinada parte do tempo.",
  ["O reforço intermitente costuma aumentar a ocorrência do comportamento."],
  slides=["cogn_32"])
C("cogn", S, "Operante discriminado",
  "O comportamento operante não ocorre a despeito do contexto em que o indivíduo está. Com o tempo, o operante passa a ocorrer só em determinadas situações.",
  ["Isso acontece porque só em determinadas situações a emissão da resposta produz o reforçador."],
  slides=["cogn_35", "cogn_36"])
C("cogn", S, "Generalização",
  "Um operante discriminado tende a ocorrer também diante de outros contextos semelhantes àquele inicialmente condicionado.",
  [], slides=["cogn_35"])

# =====================================================================
# DESENVOLVIMENTO DA LINGUAGEM
# =====================================================================
S = "Pensamento, linguagem e inteligência"
C("ling", S, "Linguagem",
  "Comunicação da informação por meio de símbolos organizados de acordo com regras sistemáticas.", [], slides=["ling_02"])
C("ling", S, "Gramática",
  "Sistema de regras que determina como nossos pensamentos podem ser expressos.", [], slides=["ling_02"])
C("ling", S, "Semântica",
  "Regras que orientam o significado das palavras e das sentenças (sentido).", [], slides=["ling_02"])
C("ling", S, "Fonologia",
  "Estudo das menores unidades da fala, chamadas de fonemas.", [], slides=["ling_02"])
C("ling", S, "Sintaxe",
  "Modo como palavras e frases podem ser combinadas para formar sentenças.", [], slides=["ling_02"])

S = "Comunicação pré-verbal"
C("ling", S, "Arrulho",
  "Sons vocálicos repetitivos, particularmente o som “uuu”.",
  [], quando="1 a 4 meses.", faixa="m1_3", slides=["ling_03"], curto="Arrulho · 1–4 m")
C("ling", S, "Balbucio",
  "Vocalização repetitiva de combinações consoante-vogal pelo bebê.",
  ["Sons de consoante aparecem apenas por volta dos 6 ou 7 meses, quando o bebê tem o controle muscular necessário para combinar o som de uma consoante com o de uma vogal.",
   "Os bebês começam a balbuciar experimentando todos os tipos de sons, incluindo alguns que não fazem parte da língua que estão ouvindo."],
  quando="Começa por volta dos 6 meses.", faixa="m4_6", slides=["ling_03", "ling_04"], curto="Balbucio · 6 m")
C("ling", S, "Repertório de sons aos 9 ou 10 meses",
  "A partir dos 9 ou 10 meses, o repertório de sons dos bebês muda gradualmente para um conjunto de sons que eles estão escutando, com o desaparecimento dos sons não ouvidos.",
  [], quando="9 a 10 meses.", faixa="m7_12", slides=["ling_05"], curto="Sons da língua · 9–10 m")
C("ling", S, "Gestos",
  "Tipo de linguagem gestual que se desenvolve próximo do final do primeiro ano: apontar é o gesto mais comum nos bebês.",
  ["Aproximadamente na mesma idade, os bebês entram nos jogos gestuais adorados pelos pais, como “dar tchauzinho”."],
  quando="Final do primeiro ano.", faixa="m7_12", slides=["ling_05"], curto="Gestos · apontar, tchau")
C("ling", S, "Fala telegráfica",
  "Sentenças nas quais as palavras que não são essenciais à mensagem são omitidas (economia de palavras ou letras).",
  [], quando="2 anos de idade.", faixa="a2_4", slides=["ling_04"], curto="Fala telegráfica · 2 a")
C("ling", S, "Supergeneralização",
  "Fenômeno pelo qual as crianças aplicam regras de linguagem mesmo quando a aplicação resulta em erro (generalização de regras gramaticais).",
  ["Exemplo do slide: “caminhou – escrevinhou”."],
  quando="3 anos de idade.", faixa="a2_4", slides=["ling_04"], curto="Supergeneralização · 3 a")

S = "Teorias da aquisição da linguagem"
C("ling", S, "Abordagem da teoria da aprendizagem",
  "Teoria de que a aquisição da linguagem segue os princípios de reforço e condicionamento.", [], slides=["ling_06"])
C("ling", S, "Abordagem nativista",
  "Teoria de que um mecanismo inato, geneticamente determinado, rege o desenvolvimento da linguagem.", [], slides=["ling_06"])
C("ling", S, "Abordagem interacionista",
  "Teoria de que o desenvolvimento da linguagem é produzido por uma combinação de predisposições geneticamente determinadas e circunstâncias ambientais que ajudam a ensinar a linguagem.",
  [], slides=["ling_06"])

S = "Linguagem receptiva"
C("ling", S, "Linguagem receptiva",
  "Compreensão da linguagem falada.",
  ["Os primeiros sinais de que o bebê entende o significado de determinadas palavras faladas para ele tornam-se evidentes por volta dos 9 ou 10 meses.",
   "Mães de bebês de 10 meses identificaram, em média, cerca de 30 palavras que seus bebês entendiam; para bebês de 13 meses, quase 100 palavras."],
  quando="9 a 10 meses: primeiros sinais · 13 meses: ~100 palavras.", faixa="m7_12", slides=["ling_07"], curto="Linguagem receptiva · 9–10 m")
C("ling", S, "Primeiras palavras",
  "Para os linguistas, palavra é qualquer som ou conjunto de sons usado consistentemente para se referir a alguma coisa, ação ou qualidade.",
  [], slides=["ling_07"])
C("ling", S, "Explosão de vocabulário",
  "Entre os 16 e os 24 meses, depois do lento período inicial de aprendizagem de palavras, a maioria das crianças começa a acrescentar palavras novas rapidamente, como se tivessem entendido que as coisas têm nomes.",
  ["Nesse primeiro período de rápido crescimento, a maioria das palavras novas são nomes para coisas ou pessoas.",
   "Verbos tendem a se desenvolver mais tarde, talvez porque rotulam mais relações entre objetos do que apenas objetos individuais."],
  quando="16 a 24 meses.", faixa="a1_2", slides=["ling_08"], curto="Explosão de vocabulário · 16–24 m")
C("ling", S, "Subextensão",
  "Uso de palavras para aplicar apenas a objetos específicos.",
  ["Exemplo do slide: a criança usa a palavra “xícara” para se referir apenas a uma determinada xícara."],
  slides=["ling_09"])
C("ling", S, "Superextensão",
  "Uso inadequado de uma palavra para designar uma categoria inteira de objetos.",
  ["Exemplo do slide: a criança usa a palavra “gato” para se referir a todos os brinquedos.",
   "À medida que a criança aprende os rótulos separados para os diferentes subtipos, a superextensão desaparece."],
  slides=["ling_09"])
C("ling", S, "Vocabulário aos 2 anos e meio",
  "Aos 2 anos e meio, o vocabulário médio é de aproximadamente 600 palavras, cerca de um quarto das quais são verbos.",
  ["Durante os anos de pré-escola, as crianças continuam a adicionar palavras a uma velocidade notável."],
  quando="2 anos e meio.", faixa="a2_4", slides=["ling_10"], curto="~600 palavras · 2,5 a")
C("ling", S, "Vocabulário aos 5 ou 6 anos",
  "Aos 5 ou 6 anos, o vocabulário total aumentou para cerca de 15.000 palavras.",
  [], quando="5 a 6 anos.", faixa="a4_6", slides=["ling_10"], curto="~15.000 palavras · 5–6 a")
C("ling", S, "Mapeamento rápido",
  "Capacidade de ligar categoricamente as palavras: nessa fase, as palavras começam a estar inseridas em categorias.",
  [], quando="Pré-escola (por volta de 5–6 anos).", faixa="a4_6", slides=["ling_10"], curto="Mapeamento rápido")
C("ling", S, "Vocabulário na meninice",
  "No começo da meninice (6 anos), as crianças continuam a adicionar vocabulário a uma taxa de 5 a 10 mil palavras por ano.",
  [], quando="A partir de 6 anos.", faixa="a6_9", slides=["ling_11"], curto="5–10 mil palavras por ano")
C("ling", S, "Adjetivos e advérbios (8 ou 9 anos)",
  "Em torno dos 8 ou 9 anos, a criança muda para um novo nível de entendimento da estrutura da língua: compreende as relações entre adjetivos e advérbios (feliz e felizmente, triste e tristemente).",
  ["Ciente dessas relações, a criança pode entender e criar conjuntos inteiros de palavras novas, e seu vocabulário daí em diante aumenta com grande rapidez."],
  quando="8 a 9 anos.", faixa="a6_9", slides=["ling_11"], curto="Adjetivos e advérbios · 8–9 a")
