from content.schema import Sala, Documento

SALAS: list[Sala] = [
    Sala(
        id="1.1",
        setor=1,
        habilidade="mapear múltiplas premissas num parágrafo coeso",
        tutorial=False,
        ambiente=(
            "> SETOR 1 — DIÁRIO DE CAMPO\n"
            "> carregando registro do Dr. C. Andrade — Ciclo 47, Dia 9...\n"
            "> aviso: documento contém múltiplas premissas sobre o mesmo sistema."
        ),
        documentos=[
            Documento(
                titulo="Diário de Campo — Observações do Setor Gamma",
                corpo=(
                    "As espécies do Setor Gamma seguem padrões estáveis. "
                    "A Âmbar floresce apenas em solo seco e exige luz solar direta. "
                    "A Névoa precisa de solo úmido e tolera exclusivamente sombra — "
                    "a luz direta a resseca em dois dias. "
                    "A Crimson cresce em qualquer tipo de solo, mas nunca ao lado da Âmbar: "
                    "a presença da Âmbar inibe completamente seu crescimento. "
                    "A Vela também prefere sombra, mas diferente da Névoa, "
                    "suas raízes exigem solo seco."
                ),
                tipo="diario",
                autor="Dr. C. Andrade",
                data_campo="Estação Épsilon — Ciclo 47, Dia 9",
                registro="Diário de Campo, Vol. II — pág. 34",
            )
        ],
        desafio=(
            "Lanis precisa montar um canteiro sombrio com solo úmido. "
            "Quais plantas do Setor Gamma podem crescer juntas ali?"
        ),
        tipo_input="multi",
        opcoes=["Âmbar", "Névoa", "Crimson", "Vela"],
        correto=["Névoa", "Crimson"],
        diagnosticos={
            "Âmbar": (
                "A Âmbar tem dois requisitos de ambiente no diário. "
                "O canteiro sombrio com solo úmido satisfaz os dois ao mesmo tempo? "
                "Verifique cada condição da Âmbar separadamente."
            ),
            "Vela": (
                "A Vela e a Névoa têm algo em comum, mas também têm uma diferença. "
                "Releia o que o diário diz sobre o solo de cada uma. "
                "O canteiro úmido atende à exigência de solo da Vela?"
            ),
        },
        diagnostico_padrao=(
            "Aplique cada condição do diário ao canteiro em questão: sombrio, solo úmido. "
            "Para cada planta, pergunte: ela tolera sombra? ela tolera solo úmido? "
            "ela tem alguma restrição de convivência com as outras que passaram no teste?"
        ),
        texto_sucesso=(
            "Dedução correta. Névoa (úmido + sombra) e Crimson (qualquer solo, sem Âmbar) "
            "são as únicas compatíveis com o canteiro. Arquivo validado."
        ),
        log_narrativo=(
            "MENSAGEM DE EMERGÊNCIA — Sistema de broadcast, Ciclo 47, Dia 23, 03h44:\n"
            "\"ATENÇÃO: PROTOCOLO ÔMEGA ATIVO. EVACUAÇÃO TOTAL DA ESTAÇÃO ÉPSILON. "
            "TODOS OS SETORES EXCETUANDO DELTA SÃO CONSIDERADOS SEGUROS. "
            "REPITO: EVACUAR IMEDIATAMENTE.\""
        ),
    ),

    Sala(
        id="1.2",
        setor=1,
        habilidade="identificar fato correto em texto com múltiplas afirmações",
        tutorial=False,
        ambiente=(
            "> carregando último registro de campo antes do Protocolo Ômega...\n"
            "> arquivo classificado — Dra. R. Vello — acesso liberado por dedução anterior.\n"
            "> aviso: este documento contém a primeira menção à anomalia."
        ),
        documentos=[
            Documento(
                titulo="Diário de Campo — Anomalia no Setor Delta",
                corpo=(
                    "Encontrei um espécime desconhecido no canteiro 12 do Setor Delta. "
                    "Estou chamando-o provisoriamente de Ômega.\n\n"
                    "A Ômega cresce em qualquer tipo de solo — seco ou úmido, com luz ou sem. "
                    "Ela não é inibida pela Âmbar: os dois crescem lado a lado sem interferência mútua. "
                    "O que me preocupa é outro fenômeno: quando a Ômega está presente, "
                    "as regras das plantas vizinhas parecem se alterar. "
                    "A Âmbar ao lado da Ômega começou a germinar em solo úmido — "
                    "o que viola o Axioma 3 de maneira que ainda não consigo explicar.\n\n"
                    "A única limitação que identifiquei na Ômega até agora: "
                    "ela não tolera temperaturas abaixo de 15°C. "
                    "Abaixo disso, ela para de crescer completamente."
                ),
                tipo="diario",
                autor="Dra. R. Vello",
                data_campo="Estação Épsilon — Ciclo 47, Dia 11",
                registro="Diário de Campo, Vol. II — pág. 41 [CLASSIFICADO]",
            )
        ],
        desafio=(
            "Com base no diário de Vello, qual afirmação sobre a Ômega está correta?"
        ),
        tipo_input="single",
        opcoes=[
            "A Ômega só cresce em solo seco",
            "A Ômega não tolera temperaturas abaixo de 15°C",
            "A Ômega é inibida pela Âmbar",
            "A Ômega não afeta as plantas vizinhas",
        ],
        correto=["A Ômega não tolera temperaturas abaixo de 15°C"],
        diagnosticos={
            "A Ômega só cresce em solo seco": (
                "Releia o início do segundo parágrafo. Vello descreve o que a Ômega "
                "tolera em termos de solo. Ela limita a Ômega a um tipo específico, "
                "ou diz o oposto?"
            ),
            "A Ômega é inibida pela Âmbar": (
                "Vello descreve a relação entre Ômega e Âmbar — mas quem inibe quem, "
                "ou nenhuma inibe a outra? Releia a frase que menciona as duas juntas."
            ),
            "A Ômega não afeta as plantas vizinhas": (
                "Vello registra um fenômeno específico nas plantas ao redor da Ômega. "
                "O que ela observa que acontece com a Âmbar vizinha? "
                "Isso é 'não afetar' ou 'afetar'?"
            ),
        },
        diagnostico_padrao=(
            "Cada opção faz uma afirmação sobre a Ômega. Localize no texto a passagem "
            "que fala sobre cada característica e verifique se o que o texto diz confirma "
            "ou contradiz a opção."
        ),
        texto_sucesso=(
            "Dedução correta. A única limitação identificada por Vello: "
            "temperaturas abaixo de 15°C interrompem o crescimento da Ômega. "
            "Arquivo final desbloqueado."
        ),
        log_narrativo=(
            "ÚLTIMA TRANSMISSÃO — Dra. R. Vello, Ciclo 47, Dia 23, 03h41:\n"
            "\"Carlos, Marina — saiam agora. O Protocolo Ômega foi ativado. "
            "Tranquei o Setor Delta por dentro. Não é um erro. "
            "A anomalia não pode cruzar os portões. "
            "O bosque lá fora ainda segue os axiomas. Que continue assim.\""
        ),
    ),
]
