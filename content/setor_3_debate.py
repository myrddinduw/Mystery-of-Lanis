from content.schema import Sala, Documento

SALAS: list[Sala] = [
    Sala(
        id="3.1",
        setor=3,
        habilidade="aplicar exceção de fonte secundária sobre axioma de fonte primária",
        tutorial=False,
        ambiente=(
            "> SETOR 3 — DEBATE ACADÊMICO\n"
            "> dois documentos recuperados sobre o mesmo tema.\n"
            "> aviso: os documentos não concordam integralmente entre si.\n"
            "> leia os dois antes de concluir."
        ),
        documentos=[
            Documento(
                titulo="Protocolo de Contenção por Temperatura — Art. Téc. Nº 004",
                corpo=(
                    "Com base nos resultados da Análise de Fatores (Art. Téc. Nº 003), "
                    "o Protocolo de Contenção por Temperatura estabelece o seguinte axioma operacional:\n\n"
                    "Uma vez que o espécime Ômega é submetido a temperatura sustentada abaixo de 15°C, "
                    "ele entra em estado de dormência permanente e não retoma atividade espontaneamente. "
                    "A contenção por frio é, portanto, definitiva e irreversível nas condições "
                    "padrão da Estação Épsilon.\n\n"
                    "Recomenda-se a instalação de sistema de refrigeração autônomo no Setor Delta "
                    "como medida de contenção de longo prazo."
                ),
                tipo="artigo",
                autor="Dr. C. Andrade",
                data_campo="Estação Épsilon — Ciclo 47, Dia 16",
                registro="Art. Téc. Nº 004",
            ),
            Documento(
                titulo="Revisão por Pares — Art. Téc. Nº 004",
                corpo=(
                    "Concordo com a premissa geral e recomendo a instalação do sistema de refrigeração.\n\n"
                    "Ressalva técnica (ver Art. Téc. Nº 003, Hipótese Nula 2): em condições de solo "
                    "alcalino (pH > 7,5), a dormência por frio mostrou-se reversível em 58% dos "
                    "espécimes testados. Nesse subconjunto, o frio apenas suspende a atividade — "
                    "a Ômega retoma o crescimento quando a temperatura volta a subir.\n\n"
                    "Recomendo verificar o pH do solo do canteiro 12 antes de declarar a contenção "
                    "definitiva. Se o solo for alcalino, a refrigeração deve ser mantida de forma "
                    "contínua e permanente — nunca interrompida."
                ),
                tipo="artigo",
                autor="Dra. R. Vello",
                data_campo="Estação Épsilon — Ciclo 47, Dia 19",
                registro="Rev. Nº 004-A",
            ),
        ],
        desafio=(
            "O canteiro 12 do Setor Delta tem solo alcalino (pH 8,1). "
            "A Ômega entrou em dormência após a queda de temperatura. "
            "Se o sistema de refrigeração for desligado e a temperatura subir, "
            "a contenção se mantém?"
        ),
        tipo_input="single",
        opcoes=[
            "Sim — pelo Protocolo de Andrade, a dormência por frio é definitiva e irreversível",
            "Não — em solo alcalino a dormência por frio é reversível, conforme a ressalva de Vello",
            "Sim — a revisão de Vello confirma o axioma de Andrade sem ressalvas",
            "Não há informação suficiente nos documentos para concluir",
        ],
        correto=["Não — em solo alcalino a dormência por frio é reversível, conforme a ressalva de Vello"],
        diagnosticos={
            "Sim — pelo Protocolo de Andrade, a dormência por frio é definitiva e irreversível": (
                "Você aplicou o axioma de Andrade como regra absoluta — mas qual é o pH do canteiro 12? "
                "E o que a revisão de Vello estabelece especificamente para solos com pH acima de 7,5?"
            ),
            "Sim — a revisão de Vello confirma o axioma de Andrade sem ressalvas": (
                "Releia a seção de ressalva técnica da revisão de Vello. "
                "Ela concorda com o axioma de Andrade em todos os casos, "
                "ou aponta uma condição específica em que a regra não se aplica?"
            ),
            "Não há informação suficiente nos documentos para concluir": (
                "Os dois documentos juntos fornecem: o axioma geral (Andrade), "
                "a exceção para solo alcalino (Vello), e o pH do canteiro 12 (8,1). "
                "Com essas três informações, é possível chegar a uma conclusão. "
                "O que cada documento diz sobre cada um desses pontos?"
            ),
        },
        diagnostico_padrao=(
            "Uma fonte apresenta uma regra geral; a outra apresenta uma exceção para uma condição específica. "
            "Qual é a condição de solo do canteiro 12? Essa condição está coberta pela exceção de Vello?"
        ),
        texto_sucesso=(
            "Dedução correta. O axioma de Andrade vale para condições padrão — "
            "mas a ressalva de Vello cobre exatamente o solo alcalino do canteiro 12. "
            "Em pH 8,1, o frio apenas suspende. Se a temperatura subir, a Ômega retoma. "
            "Arquivo validado."
        ),
        log_narrativo=(
            "LOG RECUPERADO — Dra. R. Vello, Ciclo 47, Dia 22 (última entrada antes do Protocolo Ômega):\n"
            "\"Confirmado: pH 8,1. Andrade não viu a ressalva a tempo. "
            "O sistema de refrigeração está instalado — mas se a energia cair uma vez, "
            "a contenção falha. Só há uma solução que não depende da rede principal.\""
        ),
    ),

    Sala(
        id="3.2",
        setor=3,
        habilidade="síntese de múltiplas fontes para conclusão sobre estado atual",
        tutorial=False,
        ambiente=(
            "> três arquivos recuperados — últimos registros antes do silêncio.\n"
            "> leia os três. a conclusão sobre o destino da equipe e da contenção\n"
            "> só pode ser sustentada pelo cruzamento das fontes."
        ),
        documentos=[
            Documento(
                titulo="Memo Final de Evacuação",
                corpo=(
                    "Marina e eu estamos evacuando o Setor Alpha conforme protocolo.\n\n"
                    "Confiei no Art. Téc. Nº 004 para declarar a contenção do canteiro 12 suficiente. "
                    "O sistema de refrigeração foi instalado. A Ômega está em dormência.\n\n"
                    "Não consegui contato com Rafaela nas últimas três horas. "
                    "Se estiver lendo isto: evacue. A contenção está ativa."
                ),
                tipo="diario",
                autor="Dr. C. Andrade",
                data_campo="Estação Épsilon — Ciclo 47, Dia 23, 02h15",
                registro="Memo Nº 012 — URGENTE",
            ),
            Documento(
                titulo="Log Final — Setor Delta",
                corpo=(
                    "Confirmei: pH do canteiro 12 = 8,1. O Protocolo de Andrade não se sustenta aqui. "
                    "Se o sistema de refrigeração for interrompido por qualquer motivo — "
                    "falha de energia, manutenção, intervenção externa — a Ômega retoma.\n\n"
                    "Tomei uma decisão.\n\n"
                    "Estou no Setor Delta. Trancando o acesso por dentro. "
                    "Reprogramei o sistema de refrigeração para operação autônoma contínua: "
                    "ele se mantém ativo independentemente da rede principal, "
                    "com bateria de reserva suficiente para décadas.\n\n"
                    "A Ômega vai permanecer dormente enquanto o frio se mantiver. "
                    "E o frio vai se manter.\n\n"
                    "Não é uma tragédia. É a solução mais limpa que os dados me deram."
                ),
                tipo="diario",
                autor="Dra. R. Vello",
                data_campo="Estação Épsilon — Ciclo 47, Dia 23, 03h38",
                registro="Log Nº 089 [acesso restrito]",
            ),
            Documento(
                titulo="Status do Sistema — Setor Delta",
                corpo=(
                    "REFRIGERAÇÃO DELTA: ATIVA\n"
                    "Temperatura atual: 8,4°C (±0,2°C)\n"
                    "Fonte de energia: bateria autônoma (carga: 94%)\n"
                    "Última verificação automática: Ciclo 47, Dia 22\n"
                    "Breach detectado: NÃO\n"
                    "Status da contenção: ESTÁVEL"
                ),
                tipo="artigo",
                autor="Terminal Épsilon — consulta automatizada",
                data_campo="Data de consulta: acesso atual de Lanis",
                registro="Sis. Nº 099",
            ),
        ],
        desafio=(
            "Cruzando os três documentos, qual conclusão sobre o destino da equipe "
            "e o estado da contenção é sustentada pelas fontes?"
        ),
        tipo_input="single",
        opcoes=[
            "Andrade e Marina evacuaram; Vello selou Delta por dentro e mantém o frio ativo de forma autônoma — a Ômega segue dormente e a contenção está estável.",
            "A contenção falhou — a Ômega superou o frio e pode ter cruzado os portões do Setor Delta.",
            "Todos os membros evacuaram e o Setor Delta foi deixado sem supervisão ou contenção ativa.",
            "Vello destruiu permanentemente a Ômega com um composto químico antes de evacuar.",
        ],
        correto=[
            "Andrade e Marina evacuaram; Vello selou Delta por dentro e mantém o frio ativo de forma autônoma — a Ômega segue dormente e a contenção está estável."
        ],
        diagnosticos={
            "A contenção falhou — a Ômega superou o frio e pode ter cruzado os portões do Setor Delta.": (
                "O Documento C registra o status atual do sistema. "
                "O que ele diz sobre temperatura e sobre breach detectado? "
                "Esses dados são compatíveis com contenção falha?"
            ),
            "Todos os membros evacuaram e o Setor Delta foi deixado sem supervisão ou contenção ativa.": (
                "O Documento B descreve a decisão de Vello. "
                "Ela descreve evacuar — ou descreve outra ação? "
                "O que ela diz que fez com o acesso ao Setor Delta e com o sistema de refrigeração?"
            ),
            "Vello destruiu permanentemente a Ômega com um composto químico antes de evacuar.": (
                "O Documento B descreve alguma intervenção química? "
                "O que Vello realmente descreve como solução para o problema do pH alcalino?"
            ),
        },
        diagnostico_padrao=(
            "Cada documento oferece uma peça diferente: quem fez o quê (A e B), e o estado atual (C). "
            "Leia cada um separadamente: o que Andrade e Marina fizeram? "
            "O que Vello fez e o que ela garantiu antes de selar a porta? "
            "O que o sistema confirma sobre o estado atual da contenção?"
        ),
        texto_sucesso=(
            "Dedução correta. As três fontes se encaixam: Andrade e Marina evacuaram (A); "
            "Vello selou Delta por dentro e configurou refrigeração autônoma permanente (B); "
            "o sistema confirma temperatura estável e contenção ativa, sem breach (C). "
            "Arquivo final desbloqueado."
        ),
        log_narrativo=(
            "ARQUIVO FINAL DESBLOQUEADO — Sistema Épsilon:\n"
            "Refrigeração do Setor Delta: ATIVA — operação autônoma.\n"
            "Temperatura: 8,4°C — ESTÁVEL.\n"
            "Localização de R. Vello: Setor Delta — STATUS DESCONHECIDO.\n"
            "A Ômega permanece em dormência."
        ),
    ),
]
