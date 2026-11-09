# -*- coding: utf-8 -*-
"""Conteúdo do app: mapas, grupos e as 43 estruturas (alfinetes) do roteiro."""

GROUPS = {
    "encefalo":   {"nome": "Divisões do encéfalo",   "cor": "#6d4aff"},
    "diencefalo": {"nome": "Partes do diencéfalo",   "cor": "#2b7de9"},
    "tecido":     {"nome": "Substâncias",            "cor": "#5b6676"},
    "medula":     {"nome": "Medula espinal",         "cor": "#b86e00"},
    "ventriculo": {"nome": "Ventrículos",            "cor": "#0a8aa8"},
    "periferico": {"nome": "Nervos periféricos",     "cor": "#2f9e44"},
    "meninge":    {"nome": "Meninges",               "cor": "#d6336c"},
    "craniano":   {"nome": "Nervos cranianos",       "cor": "#e8590c"},
    "cortex":     {"nome": "Lobos e áreas corticais", "cor": "#0e9f8e"},
}

# id do mapa -> título, chave da imagem-base, nota exibida sob o mapa
MAPS = {
    "sagital":   {"nome": "Encéfalo · corte sagital",       "img": "map_sagital",
                  "z": 2.2, "z": 1.7, "nota": "Corte mediano (sagital) do encéfalo. Amplie a região central (botões + / − ou pinça) para separar os alfinetes."},
    "coronal":   {"nome": "Corte coronal · ventrículos",    "img": "map_coronal",
                  "z": 1.6, "nota": "Corte coronal do cérebro: o ventrículo lateral direito aparece à esquerda de quem olha."},
    "lobos":     {"nome": "Lobos · vista lateral",          "img": "map_lobos",
                  "z": 1.4, "nota": "Hemisfério esquerdo visto de lado (frente do cérebro à esquerda)."},
    "ventral":   {"nome": "Base do encéfalo · n. cranianos", "img": "map_ventral",
                  "z": 1.8, "nota": "Face inferior (ventral) do encéfalo, com os nervos cranianos."},
    "medula":    {"nome": "Medula espinal",                 "img": "map_medula",
                  "nota": "Medula espinal com a dura-máter aberta, vista posterior (extremidade cervical no alto)."},
    "meninges":  {"nome": "Meninges · cobertura do SNC",    "img": "map_meninges",
                  "z": 2.6, "nota": "Corte através do couro cabeludo, crânio, meninges e córtex. Amplie para separar as três camadas."},
    "torax":     {"nome": "Pescoço e tórax",                "img": "map_torax",
                  "z": 1.6, "nota": "Vista anterior do tórax aberto: coração, pulmões e diafragma."},
    "braco":     {"nome": "Membro superior · vista anterior", "img": "map_braco",
                  "z": 1.6, "nota": "Face anterior do membro superior direito, com os nervos em amarelo."},
    "coxa":      {"nome": "Coxa anterior · n. femoral",     "img": "map_coxa",
                  "z": 1.5, "nota": "Face anterior da coxa: feixe vásculo-nervoso femoral."},
    "obturatorio": {"nome": "Pelve e coxa medial · n. obturatório", "img": "map_obturatorio",
                  "z": 1.5, "nota": "Plexo lombar na parede posterior do abdome e descida do n. obturatório pela coxa."},
    "perna_post": {"nome": "Membro inferior · vista posterior", "img": "map_perna_post",
                  "z": 1.7, "nota": "Região glútea, coxa e perna vistas por trás."},
    "perna_ant": {"nome": "Perna · vista anterior",          "img": "map_perna_ant",
                  "z": 1.6, "nota": "Face anterior da perna e dorso do pé, com os ramos do nervo fibular."},
}

# ordem dos mapas nos botões
MAP_ORDER = ["sagital", "coronal", "lobos", "ventral", "medula", "meninges",
             "torax", "braco", "coxa", "obturatorio", "perna_post", "perna_ant"]


def P(mapa, x, y, ang=0, z=None):
    d = {"mapa": mapa, "x": x, "y": y, "ang": ang}
    if z:
        d["z"] = z
    return d


# Cada estrutura: id (= nº do alfinete), nome, grupo, funcao[], onde[], extra[(rótulo,texto)],
# imgs[(chave, legenda)], pin (posição principal), alt[] (outras posições), area[] (máscaras destacadas)
S = []


def add(**k):
    S.append(k)


add(id=1, nome="Cérebro", grupo="encefalo",
    funcao=["Sede das funções nervosas superiores: percepção sensitiva, comando dos movimentos voluntários, linguagem, memória, emoção e raciocínio.",
            "Integra as informações que chegam do corpo e do ambiente e elabora as respostas."],
    onde=["Maior parte do encéfalo: ocupa quase toda a cavidade do crânio, acima do cerebelo e do tronco encefálico.",
          "Divide-se em diencéfalo e telencéfalo. Tem dois hemisférios, separados incompletamente pela fissura longitudinal do cérebro e unidos pelo corpo caloso."],
    extra=[("Compõe-se de", "Telencéfalo (hemisférios, córtex, núcleos da base) + diencéfalo (tálamo, hipotálamo, epitálamo, subtálamo).")],
    imgs=[("cerebro_3d", "Slide 102 · Cérebro"), ("encefalo_cabeca", "Slide 7 · Encéfalo: cérebro, cerebelo e tronco encefálico"),
          ("cerebro_hemisferios", "Slide 103 · Hemisférios cerebrais e fissura longitudinal")],
    pin=P("sagital", 0.60, 0.17, 0, 1.0), area=["a_sag_cerebro"], fonte="Slides 102–103")

add(id=2, nome="Telencéfalo", grupo="encefalo",
    funcao=["Processamento cortical superior: cognição, planejamento e início dos movimentos voluntários (lobo frontal).",
            "Projeção e interpretação da sensibilidade (lobo parietal), da audição e da memória (temporal) e da visão (occipital).",
            "Núcleos da base (controle do movimento) e sistema límbico (emoção e memória, hipocampo)."],
    onde=["Parte mais externa e volumosa do cérebro: dois hemisférios cerebrais separados pela fissura longitudinal do cérebro, cujo assoalho é formado pelo corpo caloso.",
          "Cada hemisfério tem os lobos frontal, parietal, temporal, occipital e a ínsula."],
    extra=[("Compõe-se de", "Substância cinzenta (córtex cerebral), substância branca (centro branco medular) e núcleos da base (núcleo caudado, putâmen, globo pálido e corpo amigdaloide).")],
    imgs=[("telencefalo_base", "Slide 115 · Telencéfalo"), ("telencefalo_cima", "Slide 115 · Fissura longitudinal do cérebro"),
          ("telencefalo_nucleos", "Slide 129 · Córtex, substância branca e núcleos da base")],
    pin=P("sagital", 0.27, 0.40, -35, 1.0), area=["a_sag_telencefalo"], fonte="Slides 115, 129")

add(id=3, nome="Diencéfalo", grupo="encefalo",
    funcao=["Estação de retransmissão e integração: o tálamo envia as informações sensitivas ao córtex.",
            "O hipotálamo controla o sistema nervoso autônomo e o sistema endócrino (hipófise).",
            "O epitálamo (glândula pineal) regula o ciclo circadiano; o subtálamo participa do controle motor."],
    onde=["Região central do cérebro, entre o telencéfalo e o mesencéfalo, ao redor do III ventrículo.",
          "Partes: tálamo, hipotálamo, subtálamo e epitálamo (T-H-S-E)."],
    extra=[("Para fixar", "T-H-S-E: Tálamo, Hipotálamo, Subtálamo, Epitálamo.")],
    imgs=[("diencefalo_cores", "Slide 105 · Partes do diencéfalo"), ("diencefalo_foto", "Slide 104 · Diencéfalo (T, H, S, E)"),
          ("diencefalo_subtalamo", "Slide 114 · Diencéfalo e subtálamo")],
    pin=P("sagital", 0.485, 0.47, -75), area=["a_sag_diencefalo"], fonte="Slides 104–105")

add(id=4, nome="Cerebelo", grupo="encefalo",
    funcao=["Equilíbrio e postura; coordenação dos movimentos.",
            "Movimentos finos e delicados, aprendizado motor e correção dos movimentos.",
            "Manutenção do tônus muscular."],
    onde=["Localizado na fossa cerebelar do osso occipital, posterior ao tronco encefálico e abaixo do lobo occipital.",
          "Formado por dois hemisférios cerebelares e uma parte mediana, o vermis (com folhas, lóbulos, sulcos e fissuras)."],
    extra=[("Divisão funcional", "Arquicerebelo (vestibulocerebelo): equilíbrio · Paleocerebelo (espinocerebelo): tônus muscular · Neocerebelo (cerebrocerebelo): movimentos coordenados."),
           ("Clínica", "Lesão: ataxia, dismetria, disdiadococinesia e perda de equilíbrio."),
           ("Núcleos", "Fastigial, interpósito (globoso e emboliforme) e denteado.")],
    imgs=[("cerebelo_sup", "Slide 98 · Cerebelo, vista superior"), ("cerebelo_post", "Slide 98 · Vermis e hemisférios cerebelares"),
          ("cerebelo_inf", "Slide 97 · Face inferior do encéfalo"), ("cerebelo_divisao", "Slide 99 · Divisão do cerebelo")],
    pin=P("sagital", 0.74, 0.66, 30, 1.7), alt=[P("ventral", 0.72, 0.85, 40)], area=["a_sag_cerebelo"], fonte="Slides 95–101")

add(id=5, nome="Tronco Encefálico", grupo="encefalo",
    funcao=["Via de passagem: conduz as vias ascendentes (sensitivas) e descendentes (motoras) entre a medula espinal e o cérebro.",
            "Origem aparente da maioria dos nervos cranianos.",
            "Centros vitais: controle cardiorrespiratório e do estado de consciência (formação reticular)."],
    onde=["Interpõe-se entre a medula espinal e o diencéfalo, situado ventralmente (à frente) do cerebelo.",
          "Formado, de cima para baixo, por mesencéfalo, ponte e bulbo."],
    extra=[("Formação reticular", "Controle do estado de alerta (SARA), do sistema nervoso autônomo, ativação do córtex, controle motor/sensorial e neuroendócrino-cardiorrespiratório.")],
    imgs=[("tronco_sagital", "Slide 71 · Tronco encefálico no corte sagital"), ("tronco_reticular", "Slide 81 · Formação reticular"),
          ("tronco_base", "Slide 83 · Tronco encefálico e nervos cranianos")],
    pin=P("sagital", 0.505, 0.60, -122, 1.8), area=["a_sag_tronco"], fonte="Slides 70–71, 81")

add(id=6, nome="Mesencéfalo", grupo="encefalo",
    funcao=["Reflexos visuais e auditivos: colículos superiores (via visual) e inferiores (via auditiva).",
            "Controle motor: substância negra (relacionada à doença de Parkinson) e núcleo rubro (musculatura distal dos membros).",
            "Origem dos nervos oculomotor (III) e troclear (IV)."],
    onde=["Parte mais superior do tronco encefálico, entre a ponte (abaixo) e o diencéfalo (acima).",
          "Face anterior: pedúnculos cerebrais e fossa interpeduncular (saída do n. oculomotor). Face posterior: colículos.",
          "É atravessado pelo aqueduto do mesencéfalo, que liga o III ao IV ventrículo."],
    extra=[("Partes", "Pedúnculos cerebrais · fossa interpeduncular · colículos · aqueduto do mesencéfalo · substância negra · núcleo rubro."),
           ("Clínica", "Degeneração da substância negra → doença de Parkinson.")],
    imgs=[("mesencefalo_corte", "Slide 73 · Corte transversal do mesencéfalo"), ("mesencefalo_ant", "Slide 72 · Vista anterior"),
          ("mesencefalo_post", "Slide 72 · Vista posterior (colículos)"), ("mesencefalo_negra", "Slide 75 · Substância negra")],
    pin=P("sagital", 0.555, 0.525, 105), area=["a_sag_mesencefalo"], fonte="Slides 72–75")

add(id=7, nome="Ponte", grupo="encefalo",
    funcao=["Faz a ligação entre o cérebro e o cerebelo, pelos pedúnculos cerebelares médios (braço da ponte).",
            "Área vestibular: equilíbrio e postura.",
            "Origem aparente do n. trigêmeo (V); no sulco bulbopontino emergem também VI, VII e VIII."],
    onde=["Parte média do tronco encefálico, entre o mesencéfalo (acima) e o bulbo (abaixo), à frente do cerebelo (o IV ventrículo fica entre eles).",
          "Na face anterior há o sulco da artéria basilar."],
    extra=[("Para fixar", "A ponte é a 'ponte' que liga os hemisférios do cerebelo e o cérebro; o braço da ponte = pedúnculo cerebelar médio.")],
    imgs=[("ponte_ant", "Slide 76 · Ponte, vista anterior"), ("ponte_base", "Slide 76 · Base do encéfalo"), ("ponte_post", "Slide 76 · Vista posterior")],
    pin=P("sagital", 0.545, 0.665, -100), alt=[P("ventral", 0.43, 0.63, -50)], area=["a_sag_ponte"], fonte="Slide 76")

add(id=8, nome="Bulbo", grupo="encefalo",
    funcao=["Pirâmides: via motora somática (trato corticoespinal), que cruza na decussação das pirâmides.",
            "Fascículos grácil e cuneiforme: tato epicrítico, propriocepção consciente, estereognosia e sensibilidade vibratória.",
            "Controle cardiorrespiratório (centros vitais).",
            "Região de emergência dos nervos cranianos IX, X, XI e XII (e, no sulco bulbopontino, VI, VII e VIII)."],
    onde=["Porção mais inferior do tronco encefálico, entre a ponte (acima) e a medula espinal (abaixo), com a qual se continua ao nível do forame magno.",
          "Situa-se à frente do cerebelo e forma parte do assoalho do IV ventrículo."],
    extra=[("Estruturas visíveis", "Pirâmides, oliva bulbar, decussação das pirâmides, fascículos grácil e cuneiforme (face posterior).")],
    imgs=[("bulbo_ant", "Slide 77 · Bulbo, vista anterior"), ("bulbo_decussacao", "Slide 77 · Decussação das pirâmides"),
          ("bulbo_post", "Slide 77 · Vista posterior")],
    pin=P("sagital", 0.565, 0.785, 80), alt=[P("ventral", 0.455, 0.86, -60)], area=["a_sag_bulbo"], fonte="Slides 77–79")

add(id=9, nome="Substância Cinzenta", grupo="tecido",
    funcao=["Contém os corpos celulares dos neurônios (e dendritos): é onde a informação é processada.",
            "Cor mais escura (cinzenta) por não ter mielina."],
    onde=["No cérebro e no cerebelo forma o córtex (superfície) e núcleos profundos (núcleos da base, tálamo).",
          "Na medula espinal fica no interior, em forma de 'H' ou borboleta (colunas ou cornos anterior, lateral e posterior)."],
    extra=[("Para comparar", "Cinzenta = corpos de neurônios, mais ao córtex, processamento. Branca = axônios mielínicos, mais ao interior, conexão.")],
    imgs=[("cinzenta_branca", "Slide 18 · Substâncias cinzenta e branca"), ("medula_corte", "Slide 37 · Corte transversal da medula"),
          ("telencefalo_nucleos", "Slide 129 · Córtex e núcleos da base")],
    pin=P("coronal", 0.135, 0.52, -70), fonte="Slides 18–19, 37")

add(id=10, nome="Substância Branca", grupo="tecido",
    funcao=["Formada por axônios mielínicos: conduz os impulsos entre regiões do sistema nervoso (função de conexão).",
            "A bainha de mielina (lipídios e proteínas) aumenta a velocidade de condução do impulso."],
    onde=["Cor clara, devido à mielina. No cérebro é o centro branco medular (sob o córtex); no cerebelo, o corpo medular.",
          "Na medula espinal é periférica: forma os funículos (anterior, lateral e posterior), com tratos ascendentes e descendentes."],
    extra=[("Clínica", "Esclerose múltipla: doença desmielinizante autoimune crônica.")],
    imgs=[("cinzenta_branca", "Slide 18 · Substâncias cinzenta e branca"), ("medula_corte", "Slide 37 · Corte transversal da medula"),
          ("telencefalo_nucleos", "Slide 129 · Substância branca")],
    pin=P("coronal", 0.30, 0.34, -30), fonte="Slides 10, 13–14, 18–19")

add(id=11, nome="Medula Espinal", grupo="medula",
    funcao=["Conduz informações motoras (vias descendentes) e sensitivas (vias ascendentes) entre o encéfalo e o corpo.",
            "Centro de reflexos medulares.",
            "Origina os 31 pares de nervos espinhais."],
    onde=["Localiza-se no canal vertebral (dentro da coluna vertebral), em continuação ao bulbo ao nível do forame magno.",
          "Termina em L1/L2 (cone medular). Abaixo, restam apenas as raízes nervosas da cauda equina."],
    extra=[("Organização", "Substância cinzenta: colunas (cornos). Substância branca: funículos."),
           ("Clínica", "Lesões da medula causam paraplegia ou tetraplegia, conforme o nível.")],
    imgs=[("medula_sagital", "Slide 32 · Medula no canal vertebral"), ("medula_cabo", "Slide 34 · Medula espinal e raízes nervosas"),
          ("medula_vias", "Slide 35 · Vias ascendente (sensitiva) e descendente (motora)"), ("medula_corte", "Slide 37 · Corte transversal")],
    pin=P("medula", 0.50, 0.30, 55), alt=[P("sagital", 0.578, 0.93, 80)], fonte="Slides 31–37")

add(id=12, nome="Intumescência Lombar", grupo="medula",
    funcao=["Alargamento da medula de onde saem as raízes dos plexos lombar e sacral, que inervam o membro inferior.",
            "Concentra mais neurônios porque é a região que comanda a musculatura e recebe a sensibilidade das pernas."],
    onde=["Parte inferior da medula espinal, acima do cone medular (aproximadamente no nível das vértebras T10 a T12).",
          "Na parte alta da medula existe também a intumescência cervical, origem do plexo braquial (membro superior)."],
    imgs=[("medula_cabo", "Slide 34 · Intumescência lombar, cone medular e cauda equina"), ("plexo_lombossacral", "Slide 52 · Plexos lombar e sacral"),
          ("medula_sagital", "Slide 32 · Medula no canal vertebral")],
    pin=P("medula", 0.53, 0.64, 70), fonte="Slides 34, 52")

add(id=13, nome="Cone Medular", grupo="medula",
    funcao=["Extremidade inferior afilada da medula, formada pelos segmentos sacrais e coccígeo.",
            "Contém centros que controlam bexiga, intestino e função sexual."],
    onde=["Termina ao nível de L1–L2 (adulto), logo abaixo da intumescência lombar e acima da cauda equina.",
          "Continua-se com o filamento terminal."],
    extra=[("Clínica", "Lesão do cone: disfunção de esfíncteres e anestesia em 'sela'.")],
    imgs=[("medula_cabo", "Slide 34 · Cone medular"), ("medula_sagital", "Slide 32 · Medula e coluna vertebral"),
          ("medula_ressonancia", "Slide 33 · Medula na ressonância (sagital)")],
    pin=P("medula", 0.50, 0.735, -70), fonte="Slides 32–34")

add(id=14, nome="Cauda Equina", grupo="medula",
    funcao=["Conduz fibras motoras e sensitivas dos nervos espinhais lombares, sacrais e coccígeo para o membro inferior, a pelve e o períneo.",
            "Inclui o controle de bexiga e intestino."],
    onde=["Conjunto de raízes nervosas no final da medula espinal: descem soltas no canal vertebral abaixo de L1–L2, dentro do espaço subaracnóideo (cisterna lombar).",
          "O nome vem do aspecto de 'cauda de cavalo'."],
    extra=[("Clínica", "Compressão grande (ex.: hérnia de disco) → síndrome da cauda equina."),
           ("Para fixar", "A punção lombar (abaixo de L2) coleta líquor onde só há raízes soltas, o que protege a medula.")],
    imgs=[("medula_cabo", "Slide 34 · Cauda equina"), ("medula_sagital", "Slide 32 · Coluna vertebral e medula"), ("plexo_lombossacral", "Slide 52 · Raízes lombares e sacrais")],
    pin=P("medula", 0.52, 0.875, 70), fonte="Slides 32–34")

add(id=15, nome="Ventrículo Lateral Direito", grupo="ventriculo",
    funcao=["Cavidade preenchida por líquor (LCR), produzido pelo plexo corióide: é o 1º ventrículo, início da circulação do líquor.",
            "Comunica-se com o III ventrículo pelo forame interventricular (de Monro).",
            "Amortece e nutre o tecido nervoso."],
    onde=["Dentro do hemisfério cerebral direito (telencéfalo), abaixo do corpo caloso.",
          "Tem forma de 'C': corno frontal, corpo, corno occipital e corno temporal. No corte coronal da figura, o direito fica à esquerda de quem olha."],
    extra=[("Circulação do líquor", "Ventrículos laterais → III ventrículo → aqueduto do mesencéfalo → IV ventrículo → espaço subaracnóideo → seios venosos da dura-máter → veia jugular interna."),
           ("Clínica", "Excesso de líquor ou bloqueio do fluxo → hidrocefalia.")],
    imgs=[("ventriculos_coronal", "Slide 22 · Ventrículos (01 a 03)"), ("ventriculos_axial", "Slide 119 · Ventrículos laterais"),
          ("liquor", "Slide 133 · Circulação do líquor")],
    pin=P("coronal", 0.435, 0.47, -45), area=["a_cor_vld"], fonte="Slides 20–22, 119, 133")

add(id=16, nome="Ventrículo Lateral Esquerdo", grupo="ventriculo",
    funcao=["Cavidade preenchida por líquor (LCR), produzido pelo plexo corióide: é o 2º ventrículo.",
            "Comunica-se com o III ventrículo pelo forame interventricular (de Monro).",
            "Amortece e nutre o tecido nervoso."],
    onde=["Dentro do hemisfério cerebral esquerdo (telencéfalo), abaixo do corpo caloso.",
          "No corte coronal da figura, o esquerdo fica à direita de quem olha."],
    extra=[("Circulação do líquor", "Ventrículos laterais → III ventrículo → aqueduto do mesencéfalo → IV ventrículo → espaço subaracnóideo."),
           ("Clínica", "Hidrocefalia: dilatação dos ventrículos por excesso de líquor.")],
    imgs=[("ventriculos_coronal", "Slide 22 · Ventrículos (01 a 03)"), ("ventriculos_axial", "Slide 119 · Ventrículos laterais"),
          ("liquor", "Slide 133 · Circulação do líquor")],
    pin=P("coronal", 0.565, 0.47, 45), area=["a_cor_vle"], fonte="Slides 20–22, 119, 133")

add(id=17, nome="III Ventrículo", grupo="ventriculo",
    funcao=["Cavidade mediana do diencéfalo por onde circula o líquor: recebe-o dos ventrículos laterais e o envia ao IV ventrículo pelo aqueduto do mesencéfalo."],
    onde=["Fenda estreita na linha média, entre os dois tálamos: suas paredes laterais são o tálamo e o hipotálamo.",
          "Comunica-se com os ventrículos laterais (forames interventriculares) e com o IV ventrículo (aqueduto do mesencéfalo)."],
    imgs=[("ventriculos_coronal", "Slide 22 · III ventrículo (03)"), ("liquor", "Slide 133 · Circulação do líquor"),
          ("ventriculos_axial", "Slide 119 · Ventrículos")],
    pin=P("coronal", 0.52, 0.72, 60), alt=[P("sagital", 0.527, 0.447, -35)], area=["a_cor_v3"], fonte="Slides 22, 74, 133")

add(id=18, nome="IV Ventrículo", grupo="ventriculo",
    funcao=["Recebe o líquor do aqueduto do mesencéfalo e o conduz ao canal central da medula e ao espaço subaracnóideo (pelas aberturas mediana e laterais)."],
    onde=["Entre o tronco encefálico (ponte e bulbo, que formam o assoalho) e o cerebelo (teto), na fossa posterior do crânio."],
    imgs=[("ventriculo4", "Slide 22 · IV ventrículo (04)"), ("liquor", "Slide 133 · Circulação do líquor")],
    pin=P("sagital", 0.617, 0.63, 80), area=["a_sag_v4"], fonte="Slides 22, 133")

add(id=19, nome="Nervo Frênico do Plexo Cervical", grupo="periferico",
    funcao=["Nervo motor do diafragma, principal músculo da respiração.",
            "Também leva sensibilidade do pericárdio, da pleura mediastinal e do próprio diafragma."],
    onde=["Origina-se do plexo cervical (raízes C3, C4 e C5; o plexo cervical vai de C1 a C5).",
          "Desce pelo pescoço sobre o músculo escaleno anterior, entra no tórax e passa entre o pericárdio e a pleura, ao lado do coração, até o diafragma."],
    extra=[("Para fixar", "'C3, C4, C5 mantêm o diafragma vivo.'"),
           ("Clínica", "Lesão → paralisia do hemidiafragma do mesmo lado.")],
    imgs=[("frenico_pescoco", "Slide 44 · Plexo cervical"), ("frenico_torax", "Slide 45 · Nervo frênico no tórax"), ("frenico_esquema", "Slide 44 · Trajeto do n. frênico")],
    pin=P("torax", 0.355, 0.52, -60), fonte="Slides 42–45")

add(id=20, nome="Nervo Radial", grupo="periferico",
    funcao=["Motor: extensão do cotovelo (tríceps braquial), do punho e dos dedos (extensores do antebraço) e supinação.",
            "Sensitivo: face posterior do braço e do antebraço e parte lateral do dorso da mão."],
    onde=["Ramo do plexo braquial (C5–T1, fascículo posterior).",
          "Desce pela face posterior do braço, no sulco do nervo radial do úmero, e passa à região lateral do cotovelo; no antebraço divide-se em ramo superficial (sensitivo) e profundo (motor)."],
    extra=[("Clínica", "Lesão → 'mão caída' (punho em gota): perda da extensão do punho e dos dedos.")],
    imgs=[("braco_ant", "Slide 48 · Nervos do membro superior"), ("plexo_braquial", "Slide 47 · Plexo braquial"),
          ("braco_cutaneo", "Slide 50 · Inervação cutânea do membro superior")],
    pin=P("braco", 0.43, 0.50, -55), fonte="Slides 46–48, 50")

add(id=21, nome="Nervo Ulnar", grupo="periferico",
    funcao=["Motor: flexão e adução do punho (flexor ulnar do carpo), flexão do 4º e 5º dedos e a maioria dos músculos intrínsecos da mão.",
            "Sensitivo: 5º dedo e metade medial do 4º dedo."],
    onde=["Ramo do plexo braquial (C8–T1, fascículo medial).",
          "Desce pela face medial do braço, passa atrás do epicôndilo medial do úmero ('nervo do cotovelo'), segue pelo lado medial do antebraço e entra na mão ao lado do pisiforme."],
    extra=[("Clínica", "Lesão → 'mão em garra' (garra ulnar).")],
    imgs=[("braco_ant", "Slide 48 · Nervos do membro superior"), ("plexo_braquial", "Slide 47 · Plexo braquial"),
          ("braco_cutaneo", "Slide 50 · Inervação cutânea do membro superior")],
    pin=P("braco", 0.40, 0.725, 75), fonte="Slides 46–48, 50")

add(id=22, nome="Nervo Mediano", grupo="periferico",
    funcao=["Motor: pronação do antebraço, flexão do punho e dos dedos (maior parte dos flexores do antebraço) e músculos da base do polegar (oposição).",
            "Sensitivo: palma (lado lateral), polegar, indicador, médio e metade lateral do anular."],
    onde=["Formado pelos fascículos medial e lateral do plexo braquial (C6–T1).",
          "Desce no braço junto à artéria braquial, cruza a fossa cubital, percorre o centro da face anterior do antebraço e entra na mão pelo túnel do carpo."],
    extra=[("Clínica", "Compressão no punho → síndrome do túnel do carpo. Lesão alta → 'mão de bênção'.")],
    imgs=[("braco_ant", "Slide 48 · Nervos do membro superior"), ("plexo_braquial", "Slide 47 · Plexo braquial"),
          ("braco_cutaneo", "Slide 50 · Inervação cutânea do membro superior")],
    pin=P("braco", 0.385, 0.655, -80), fonte="Slides 46–48, 50")

add(id=23, nome="Nervo Isquiático", grupo="periferico",
    funcao=["É o maior e mais espesso nervo do corpo.",
            "Motor: flexão do joelho (músculos posteriores da coxa) e, pelos ramos terminais, todos os músculos da perna e do pé.",
            "Sensitivo: pele da perna e do pé (pelos nervos tibial e fibular comum)."],
    onde=["Origina-se do plexo sacral (L4, L5, S1, S2, S3).",
          "Sai da pelve pelo forame isquiático maior, abaixo do músculo piriforme, atravessa a região glútea e desce pela face posterior da coxa.",
          "Divide-se em nervo tibial e nervo fibular comum, geralmente perto da fossa poplítea."],
    extra=[("Clínica", "Compressão/irritação → dor ciática (ciatalgia)."),
           ("Para fixar", "Injeções glúteas ficam no quadrante súpero-lateral para evitar o nervo.")],
    imgs=[("isquiatico_post", "Slide 56 · Plexo sacral, vista posterior"), ("isquiatico_coxa", "Slide 57 · N. isquiático"), ("regiao_glutea", "Slide 58 · Nervos da região glútea")],
    pin=P("perna_post", 0.48, 0.41, 60), fonte="Slides 56–58")

add(id=24, nome="Nervo Tibial", grupo="periferico",
    funcao=["Motor: flexão plantar do pé, inversão do pé e flexão dos dedos (compartimento posterior da perna).",
            "Sensitivo: planta do pé (nervos plantares medial e lateral) e, com o fibular comum, a borda lateral do pé (n. sural)."],
    onde=["Ramo medial do nervo isquiático (L4–S3).",
          "Desce pela fossa poplítea e pela face posterior da perna, profundo ao músculo tríceps sural, passa atrás do maléolo medial e chega à planta do pé."],
    imgs=[("isquiatico_coxa", "Slide 57 · N. tibial e n. sural"), ("isquiatico_post", "Slide 56 · Plexo sacral, vista posterior"),
          ("nervos_perna_rotulados", "Slide 53 · Nervos do membro inferior")],
    pin=P("perna_post", 0.45, 0.58, -70), fonte="Slides 56–57")

add(id=25, nome="Nervo Fibular Superficial", grupo="periferico",
    funcao=["Motor: eversão do pé (músculos fibulares longo e curto, do compartimento lateral da perna).",
            "Sensitivo: dorso do pé e dos dedos (exceto o espaço entre o hálux e o 2º dedo)."],
    onde=["Ramo do nervo fibular comum (que se divide em superficial e profundo).",
          "Desce no compartimento lateral da perna e perfura a fáscia no terço inferior para chegar ao dorso do pé."],
    imgs=[("fibular", "Slide 57 · N. fibular comum e seus ramos"), ("nervos_perna_rotulados", "Slide 53 · Nervos do membro inferior")],
    pin=P("perna_ant", 0.27, 0.53, -60), fonte="Slides 57")

add(id=26, nome="Nervo Fibular Profundo", grupo="periferico",
    funcao=["Motor: dorsiflexão do pé e extensão dos dedos (compartimento anterior da perna).",
            "Sensitivo: pele do primeiro espaço entre os dedos do pé (entre o hálux e o 2º dedo)."],
    onde=["Ramo do nervo fibular comum.",
          "Desce no compartimento anterior da perna, junto à artéria tibial anterior sobre a membrana interóssea, até o dorso do pé."],
    extra=[("Clínica", "Lesão do fibular (comum ou profundo) → pé caído, com marcha escarvante.")],
    imgs=[("fibular", "Slide 57 · N. fibular comum e seus ramos"), ("nervos_perna_rotulados", "Slide 53 · Nervos do membro inferior")],
    pin=P("perna_ant", 0.435, 0.575, 60), fonte="Slide 57")

add(id=27, nome="Nervo Femoral", grupo="periferico",
    funcao=["Motor: flexão do quadril (iliopsoas) e extensão do joelho (quadríceps femoral e sartório).",
            "Sensitivo: face anterior da coxa e, pelo nervo safeno, face medial da perna e do pé."],
    onde=["Ramo do plexo lombar (L2, L3, L4).",
          "Desce sobre o músculo psoas, passa sob o ligamento inguinal, lateral à artéria femoral (trígono femoral), e se ramifica na coxa anterior. O ramo mais longo é o nervo safeno."],
    extra=[("Clínica", "Lesão → fraqueza do quadríceps ('joelho que cede') e perda do reflexo patelar.")],
    imgs=[("femoral_musculos", "Slide 54 · N. femoral"), ("femoral_cutaneo", "Slide 54 · Inervação cutânea (n. safeno)"), ("femoral_plexo", "Slide 54 · Plexo lombar")],
    pin=P("coxa", 0.565, 0.17, 35), fonte="Slides 52, 54")

add(id=28, nome="Nervo Obturatório", grupo="periferico",
    funcao=["Motor: adução da coxa (músculos adutores: longo, curto, magno, grácil e pectíneo).",
            "Sensitivo: face medial da coxa."],
    onde=["Ramo do plexo lombar (L2, L3, L4).",
          "Desce medialmente ao psoas, percorre a pelve e sai pelo canal obturatório para o compartimento medial da coxa."],
    imgs=[("obturatorio_musculos", "Slide 55 · N. obturatório"), ("obturatorio_pelve", "Slide 55 · Do plexo lombar à coxa"),
          ("obturatorio_cutaneo", "Slide 55 · Inervação cutânea")],
    pin=P("obturatorio", 0.555, 0.60, 60), fonte="Slides 52, 55")

add(id=29, nome="Dura-máter", grupo="meninge",
    funcao=["Meninge mais externa, espessa e resistente: protege o encéfalo e a medula.",
            "Forma a foice do cérebro e a tenda do cerebelo (sustentação).",
            "Seus folhetos abrigam os seios venosos que drenam o sangue do encéfalo para as veias jugulares internas."],
    onde=["Camada mais externa das meninges, logo abaixo do crânio (aderida ao osso). Na coluna, separa-se das vértebras pelo espaço epidural.",
          "Fica por fora da aracnoide-máter."],
    extra=[("Clínica", "Hematoma epidural: entre o crânio e a dura (ex.: ruptura da a. meníngea média). Hematoma subdural: entre a dura e a aracnoide.")],
    imgs=[("meninges_camadas", "Slide 64 · Meninges e espaços"), ("meninges_ingles", "Slide 65 · Dura (interna e externa) e espaço subaracnóideo"),
          ("meninges_espinal", "Slide 68 · Meninges da medula espinal")],
    pin=P("meninges", 0.316, 0.407, -40), alt=[P("medula", 0.25, 0.43, -60)], fonte="Slides 63–69")

add(id=30, nome="Pia-máter", grupo="meninge",
    funcao=["Meninge mais interna, fina e transparente, aderida à superfície do encéfalo e da medula (acompanha giros e sulcos).",
            "Sustenta os vasos que nutrem o tecido nervoso e forma, com o epêndima, os plexos corióides."],
    onde=["Diretamente sobre o tecido nervoso, abaixo do espaço subaracnóideo (que a separa da aracnoide)."],
    imgs=[("meninges_camadas", "Slide 64 · Meninges e espaços"), ("meninges_ingles", "Slide 65 · Pia-máter e aracnoide"),
          ("meninges_espinal", "Slide 68 · Meninges da medula espinal")],
    pin=P("meninges", 0.316, 0.495, 150), fonte="Slides 63–69")

add(id=31, nome="Aracnóide", grupo="meninge",
    funcao=["Meninge intermediária, fina e sem vasos, com aspecto de 'teia de aranha'.",
            "Delimita o espaço subaracnóideo, preenchido por líquor, que amortece o sistema nervoso central.",
            "As granulações aracnóideas devolvem o líquor ao sangue dos seios venosos."],
    onde=["Entre a dura-máter (por fora) e a pia-máter (por dentro).",
          "O espaço subaracnóideo fica abaixo dela, entre ela e a pia-máter."],
    extra=[("Clínica", "Hemorragia subaracnóidea (HSA): sangramento no espaço subaracnóideo.")],
    imgs=[("meninges_camadas", "Slide 64 · Meninges e espaços"), ("meninges_ingles", "Slide 65 · Aracnoide e espaço subaracnóideo"),
          ("meninges_espinal", "Slide 68 · Meninges da medula espinal")],
    pin=P("meninges", 0.316, 0.447, -90), fonte="Slides 63–69")

add(id=32, nome="Nervo Vago", grupo="craniano",
    funcao=["X par craniano e principal nervo parassimpático: diminui a frequência cardíaca, estimula a digestão e a broncoconstrição.",
            "Motor da faringe e da laringe (deglutição e fala).",
            "Sensibilidade visceral do tórax e do abdome."],
    onde=["Emerge do bulbo, sai do crânio pelo forame jugular e desce no pescoço junto à artéria carótida e à veia jugular interna.",
          "Atravessa o tórax e passa ao abdome com o esôfago; distribui-se por coração, pulmões e órgãos abdominais."],
    imgs=[("vago", "Slide 93 · N. vago (X)"), ("cranianos_base", "Slide 83 · Emergência dos nervos cranianos"),
          ("vago_coracao", "Slide 80 · Inervação autônoma do coração")],
    pin=P("ventral", 0.585, 0.81, 80), fonte="Slides 82–83, 93")

add(id=33, nome="Nervo Óptico", grupo="craniano",
    funcao=["II par craniano: nervo sensitivo da visão.",
            "Conduz os impulsos da retina ao quiasma óptico, depois ao trato óptico, ao corpo geniculado lateral (tálamo) e ao córtex visual do lobo occipital."],
    onde=["Da retina, atravessa o canal óptico e forma o quiasma óptico, à frente da hipófise e do hipotálamo.",
          "É uma extensão do diencéfalo."],
    extra=[("Clínica", "Lesão no quiasma (ex.: tumor de hipófise) → perda do campo visual temporal (hemianopsia bitemporal).")],
    imgs=[("optico", "Slide 85 · N. óptico (II)"), ("cranianos_base", "Slide 83 · Emergência dos nervos cranianos"), ("oculomotores", "Slide 86 · Nervos dos músculos oculares")],
    pin=P("ventral", 0.43, 0.408, -55), fonte="Slides 82–83, 85")

add(id=34, nome="Nervo Olfatório", grupo="craniano",
    funcao=["I par craniano: nervo sensitivo do olfato.",
            "As fibras do epitélio olfatório atravessam a lâmina cribriforme do etmoide e fazem sinapse no bulbo olfatório; o trato olfatório leva a informação ao córtex.",
            "O olfato é o único sentido que não passa pelo tálamo."],
    onde=["Teto da cavidade nasal (epitélio olfatório) → lâmina cribriforme do osso etmoide → bulbo e trato olfatório, na face inferior do lobo frontal."],
    imgs=[("olfatorio", "Slide 84 · N. olfatório (I)"), ("cranianos_base", "Slide 83 · Emergência dos nervos cranianos")],
    pin=P("ventral", 0.395, 0.30, -50), fonte="Slides 82–84")

add(id=35, nome="Epitálamo", grupo="diencefalo",
    funcao=["Glândula pineal: secreta melatonina.",
            "Controle do ciclo circadiano (sono e vigília), regulado pela luz que chega pela retina.",
            "Ligado ao sistema límbico (emoções)."],
    onde=["Parte póstero-superior do diencéfalo, no teto do III ventrículo, acima do mesencéfalo.",
          "A glândula pineal projeta-se para trás a partir dele."],
    imgs=[("epitalamo_pineal", "Slide 113 · Glândula pineal e melatonina"), ("epitalamo_sagital", "Slide 113 · Localização da pineal"), ("hipofise_pineal", "Slide 106 · Hipófise e pineal")],
    pin=P("sagital", 0.60, 0.485, 75), area=["a_sag_epitalamo"], fonte="Slides 104–106, 113")

add(id=36, nome="Tálamo", grupo="diencefalo",
    funcao=["Controle sensorial: retransmite as informações sensoriais (exceto o olfato) ao córtex cerebral.",
            "Controle motor e ativação do córtex cerebral.",
            "Sistema límbico: emoções, consciência e cognição."],
    onde=["Duas massas ovais de substância cinzenta, uma de cada lado do III ventrículo, na parte dorsal do diencéfalo: acima do hipotálamo e medial à cápsula interna.",
          "As duas metades se tocam na linha média pela aderência intertalâmica."],
    imgs=[("talamo_vias", "Slide 109 · Tálamo e vias sensoriais"), ("talamo_esquema", "Slide 109 · Tálamo"), ("diencefalo_cores", "Slide 105 · Partes do diencéfalo")],
    pin=P("sagital", 0.575, 0.425, 30), area=["a_sag_talamo"], fonte="Slides 104–105, 109–110")

add(id=37, nome="Hipotálamo", grupo="diencefalo",
    funcao=["Controle do sistema nervoso autônomo e regulação da temperatura corporal.",
            "Regulação do comportamento emocional, do sono e da vigília.",
            "Regulação da ingestão de alimentos e de água e da diurese.",
            "Regulação do sistema endócrino (comanda a hipófise)."],
    onde=["Abaixo do tálamo, forma o assoalho e parte das paredes do III ventrículo, acima da hipófise, à qual se liga pelo infundíbulo.",
          "Inclui o quiasma óptico, o túber cinéreo e os corpos mamilares."],
    imgs=[("hipotalamo_azul", "Slide 112 · Hipotálamo"), ("hipotalamo_hipofise", "Slide 107 · Hipotálamo e hormônios da hipófise"), ("diencefalo_cores", "Slide 105 · Partes do diencéfalo")],
    pin=P("sagital", 0.497, 0.515, -88), area=["a_sag_hipotalamo"], fonte="Slides 104–107, 111–112")

add(id=38, nome="Lobo Frontal", grupo="cortex",
    funcao=["Processamentos complexos: cognição, planejamento e iniciação dos movimentos voluntários.",
            "O giro pré-central é a área motora do cérebro; o giro frontal inferior esquerdo é a área de Broca (fala)."],
    onde=["Parte anterior do hemisfério cerebral, à frente do sulco central (que o separa do lobo parietal) e acima do sulco lateral (que o separa do lobo temporal)."],
    imgs=[("lobos_cores", "Slide 121 · Lobos cerebrais"), ("lobos_slide120", "Slide 120 · Divisão em lobos"), ("giros_areas", "Slide 122 · Giros e áreas funcionais")],
    pin=P("lobos", 0.27, 0.40, -20, 1.0), area=["a_lob_frontal"], fonte="Slides 120–122")

add(id=39, nome="Lobo Parietal", grupo="cortex",
    funcao=["Área de projeção e processamento somestésico (sensibilidade geral).",
            "O giro pós-central é a área sensitiva do cérebro.",
            "Integra a orientação espacial."],
    onde=["Posterior ao sulco central, acima do sulco lateral e à frente do sulco parieto-occipital (que o separa do lobo occipital)."],
    extra=[("Clínica", "Lesão do lobo parietal direito → síndrome da heminegligência (o paciente ignora a metade esquerda do corpo e do espaço).")],
    imgs=[("lobos_cores", "Slide 121 · Lobos cerebrais"), ("lobos_slide120", "Slide 120 · Divisão em lobos"), ("giros_areas", "Slide 122 · Giros e áreas funcionais")],
    pin=P("lobos", 0.58, 0.30, 0, 1.0), area=["a_lob_parietal"], fonte="Slides 120–122, 125")

add(id=40, nome="Lobo Occipital", grupo="cortex",
    funcao=["Área de projeção e processamento visual (córtex visual)."],
    onde=["Parte posterior do hemisfério cerebral, atrás do sulco parieto-occipital, apoiada sobre a tenda do cerebelo."],
    imgs=[("lobos_cores", "Slide 121 · Lobos cerebrais"), ("lobos_slide120", "Slide 120 · Divisão em lobos"), ("giros_areas", "Slide 122 · Área visual")],
    pin=P("lobos", 0.85, 0.52, 40, 1.0), area=["a_lob_occipital"], fonte="Slides 120–122")

add(id=41, nome="Córtex Pré-frontal", grupo="cortex",
    funcao=["Funções executivas: planejamento, tomada de decisão, julgamento e controle de impulsos.",
            "Atenção, memória de trabalho e comportamento social (personalidade)."],
    onde=["Porção mais anterior do lobo frontal, à frente das áreas motoras (giro pré-central e área pré-motora), logo atrás da testa."],
    extra=[("Observação", "O slide 112 apenas indica o córtex pré-frontal no esquema do diencéfalo. A descrição das funções é conteúdo padrão de neuroanatomia, conferir com o seu professor.")],
    imgs=[("hipotalamo_azul", "Slide 112 · Córtex pré-frontal (no esquema)"), ("lobos_cores", "Slide 121 · Lobo frontal"), ("giros_areas", "Slide 122 · Giros e áreas funcionais")],
    pin=P("lobos", 0.17, 0.44, -60), area=["a_lob_prefrontal"], fonte="Slides 112, 121")

add(id=42, nome="Área de Broca", grupo="cortex",
    funcao=["Expressão da linguagem: produção da fala.",
            "Corresponde às áreas 44 e 45 de Brodmann."],
    onde=["Giro frontal inferior do hemisfério dominante (geralmente o esquerdo), no lobo frontal, à frente do giro pré-central e logo acima do sulco lateral."],
    extra=[("Clínica", "Lesão → afasia de Broca (de expressão): fala difícil e pouco fluente, com compreensão preservada.")],
    imgs=[("broca_wernicke", "Slide 123 · Áreas de Broca e Wernicke"), ("linguagem_areas", "Slide 123 · Áreas da linguagem"), ("afasia_broca", "Slide 124 · Afasia de Broca")],
    pin=P("lobos", 0.325, 0.535, -35), area=["a_lob_broca"], fonte="Slides 122–124")

add(id=43, nome="Área de Wernicke", grupo="cortex",
    funcao=["Compreensão (percepção) da linguagem.",
            "Corresponde à área 22 de Brodmann."],
    onde=["Junção dos lobos parietal e temporal (parte posterior do giro temporal superior), no hemisfério dominante (geralmente o esquerdo)."],
    extra=[("Clínica", "Lesão → afasia de Wernicke (receptiva): fala fluente, porém sem sentido, e compreensão prejudicada.")],
    imgs=[("broca_wernicke", "Slide 123 · Áreas de Broca e Wernicke"), ("linguagem_areas", "Slide 123 · Áreas da linguagem"), ("linguagem_cores", "Slide 123 · Mapa funcional do córtex")],
    pin=P("lobos", 0.625, 0.535, 35), area=["a_lob_wernicke"], fonte="Slides 122–123")
