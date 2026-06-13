from content.schema import Sala, Documento

SALAS: list[Sala] = [
    Sala(
        id="0.1",
        setor=0,
        habilidade="localizar fato explícito",
        tutorial=True,
        ambiente=(
            "> calibração 0.1 iniciada — carregando arquivo de referência simples...\n"
            "> um único registro foi recuperado do arquivo morto."
        ),
        documentos=[
            Documento(
                titulo="Nota de Campo",
                corpo=(
                    "A flor Vela só abre suas pétalas durante a noite. "
                    "Ao nascer do sol, ela se fecha completamente e permanece assim até o anoitecer."
                ),
                tipo="diario",
                autor="Pesq. M. Luz",
                data_campo="Estação Épsilon — Ciclo 47, Dia 2",
                registro="Reg. Nº 001",
            )
        ],
        desafio="Com base no documento recuperado: quando a flor Vela abre suas pétalas?",
        tipo_input="single",
        opcoes=["De dia", "À noite", "Ao nascer do sol"],
        correto=["À noite"],
        diagnosticos={
            "De dia": (
                "Releia a única frase do documento. Ela usa a palavra 'noite' ou 'dia' para dizer "
                "quando a Vela abre? Localize essa palavra no texto antes de responder."
            ),
            "Ao nascer do sol": (
                "O texto menciona o amanhecer — mas o que acontece com a Vela nesse momento? "
                "Releia com atenção: o amanhecer é quando ela abre ou quando ela se fecha?"
            ),
        },
        diagnostico_padrao=(
            "Releia a única frase do documento. Ela afirma em que período a Vela abre. "
            "Qual palavra exata o texto usa para descrever esse momento?"
        ),
        texto_sucesso="Dedução correta. A Vela abre à noite. Calibração 0.1 validada.",
        log_narrativo=(
            "[SISTEMA] Calibração 0.1 concluída. Arquivo de referência validado.\n"
            "6 setores restantes bloqueados."
        ),
    ),

    Sala(
        id="0.2",
        setor=0,
        habilidade="rastrear dois fatos independentes",
        tutorial=True,
        ambiente=(
            "> calibração 0.2 — dois registros independentes detectados no mesmo arquivo.\n"
            "> cada um descreve uma planta diferente."
        ),
        documentos=[
            Documento(
                titulo="Nota de Campo",
                corpo=(
                    "A planta Âmbar se desenvolve exclusivamente em solo seco. "
                    "A planta Névoa, ao contrário, requer solo úmido para sobreviver."
                ),
                tipo="diario",
                autor="Pesq. M. Luz",
                data_campo="Estação Épsilon — Ciclo 47, Dia 3",
                registro="Reg. Nº 002",
            )
        ],
        desafio="Qual das plantas precisa de solo seco para se desenvolver?",
        tipo_input="single",
        opcoes=["Âmbar", "Névoa", "As duas"],
        correto=["Âmbar"],
        diagnosticos={
            "Névoa": (
                "Você trocou as plantas. O documento menciona as duas — mas cada uma tem uma condição diferente. "
                "Releia: qual palavra o texto usa para descrever o solo da Névoa?"
            ),
            "As duas": (
                "O documento descreve condições opostas para as duas plantas. "
                "Uma precisa de solo seco; a outra, de solo úmido. Releia cada frase separadamente."
            ),
        },
        diagnostico_padrao=(
            "O documento tem uma frase para cada planta. Leia a frase da Âmbar: "
            "que tipo de solo ela precisa? Agora leia a frase da Névoa: é o mesmo tipo?"
        ),
        texto_sucesso=(
            "Dedução correta. A Âmbar exige solo seco; a Névoa, solo úmido. "
            "Calibração 0.2 validada."
        ),
        log_narrativo=(
            "LOG RECUPERADO — Dr. C. Andrade, Ciclo 47, Dia 1:\n"
            "\"Chegamos à Épsilon. O sistema botânico está intacto. "
            "As plantas obedecem aos axiomas exatamente como os modelos previam.\""
        ),
    ),

    Sala(
        id="0.3",
        setor=0,
        habilidade="entender exclusão e negação",
        tutorial=True,
        ambiente=(
            "> calibração 0.3 — arquivo de restrições detectado.\n"
            "> atenção: o documento contém uma proibição explícita."
        ),
        documentos=[
            Documento(
                titulo="Nota de Campo",
                corpo=(
                    "Nunca plante a Crimson no mesmo canteiro que a Vela. "
                    "A presença da Crimson suprime o florescimento da Vela, "
                    "impedindo-a de abrir mesmo durante a noite."
                ),
                tipo="diario",
                autor="Pesq. M. Luz",
                data_campo="Estação Épsilon — Ciclo 47, Dia 4",
                registro="Reg. Nº 003",
            )
        ],
        desafio=(
            "Lanis quer cultivar a Vela em um canteiro. "
            "Com base no documento, o que ela NÃO pode colocar nesse mesmo canteiro?"
        ),
        tipo_input="single",
        opcoes=["Âmbar", "Névoa", "Crimson"],
        correto=["Crimson"],
        diagnosticos={
            "Âmbar": (
                "O documento não menciona a Âmbar. Releia: qual planta o texto afirma "
                "que nunca pode ficar junto da Vela? A palavra-chave é 'nunca'."
            ),
            "Névoa": (
                "O documento não menciona a Névoa. Releia com atenção: qual planta "
                "o texto coloca como proibida ao lado da Vela?"
            ),
        },
        diagnostico_padrao=(
            "Releia a primeira frase do documento. Ela começa com 'Nunca'. "
            "O que ela diz que nunca pode estar junto da Vela?"
        ),
        texto_sucesso=(
            "Dedução correta. A Crimson é proibida no canteiro da Vela. "
            "Calibração 0.3 validada."
        ),
        log_narrativo=(
            "LOG RECUPERADO — Pesq. M. Luz, Ciclo 47, Dia 3:\n"
            "\"Vello está obcecada com algo no Setor Delta. "
            "Pediu que ninguém entrasse lá até ela terminar a análise.\""
        ),
    ),

    Sala(
        id="0.4",
        setor=0,
        habilidade="condicional simples — SE → ENTÃO",
        tutorial=True,
        ambiente=(
            "> calibração 0.4 — arquivo condicional detectado.\n"
            "> o documento contém uma regra do tipo: se [condição], então [resultado]."
        ),
        documentos=[
            Documento(
                titulo="Nota de Campo",
                corpo=(
                    "Se o solo está úmido, a semente Âmbar não germina. "
                    "A germinação da Âmbar só ocorre em solo completamente seco."
                ),
                tipo="diario",
                autor="Pesq. M. Luz",
                data_campo="Estação Épsilon — Ciclo 47, Dia 5",
                registro="Reg. Nº 004",
            )
        ],
        desafio=(
            "O canteiro de teste tem solo úmido. "
            "Com base no documento, o que acontece com a semente Âmbar plantada ali?"
        ),
        tipo_input="single",
        opcoes=["Ela germina normalmente", "Ela não germina", "Ela germina mais lentamente"],
        correto=["Ela não germina"],
        diagnosticos={
            "Ela germina normalmente": (
                "Releia a primeira frase do documento. Ela descreve exatamente essa situação — "
                "solo úmido — e diz o que acontece com a Âmbar. Qual é o resultado descrito?"
            ),
            "Ela germina mais lentamente": (
                "O texto não menciona velocidade de germinação. Releia: quando o solo está úmido, "
                "a Âmbar germina de alguma forma, ou não germina de maneira alguma?"
            ),
        },
        diagnostico_padrao=(
            "O documento tem a forma 'se [condição], então [resultado]'. "
            "O canteiro tem solo úmido — a condição está presente. "
            "Qual resultado o texto descreve para essa condição?"
        ),
        texto_sucesso=(
            "Dedução correta. Solo úmido → Âmbar não germina. "
            "Calibração 0.4 validada."
        ),
        log_narrativo=(
            "LOG RECUPERADO — Dr. C. Andrade, Ciclo 47, Dia 7:\n"
            "\"As equações do Setor Delta não batem. "
            "Algo está quebrando o Axioma 3. Preciso falar com Vello.\""
        ),
    ),

    Sala(
        id="0.5",
        setor=0,
        habilidade="cruzar duas regras para uma decisão",
        tutorial=True,
        ambiente=(
            "> calibração 0.5 — arquivo cruzado detectado.\n"
            "> dois registros inter-relacionados. a dedução exige combinar as duas regras."
        ),
        documentos=[
            Documento(
                titulo="Nota de Campo",
                corpo=(
                    "A Névoa não se desenvolve em solo seco.\n\n"
                    "Nunca coloque a Crimson no mesmo canteiro que a Âmbar — "
                    "a presença da Âmbar inibe completamente o crescimento da Crimson."
                ),
                tipo="diario",
                autor="Pesq. M. Luz / Dr. C. Andrade",
                data_campo="Estação Épsilon — Ciclo 47, Dia 6",
                registro="Reg. Nº 005",
            )
        ],
        desafio=(
            "O canteiro 7 tem solo seco. "
            "Qual par de plantas pode ser cultivado ali com segurança?"
        ),
        tipo_input="single",
        opcoes=["Névoa e Vela", "Âmbar e Vela", "Crimson e Vela", "Névoa e Crimson"],
        correto=["Âmbar e Vela"],
        diagnosticos={
            "Névoa e Vela": (
                "Você verificou a exigência de solo da Névoa? "
                "Releia a primeira regra do documento: a Névoa pode estar em um canteiro com solo seco?"
            ),
            "Crimson e Vela": (
                "Nenhuma das duas regras proíbe Crimson com Vela diretamente — "
                "mas verifique o solo. A Névoa e a Crimson têm exigências de solo? "
                "Releia cada regra e aplique-a ao canteiro 7."
            ),
            "Névoa e Crimson": (
                "Esse par viola a primeira regra — a Névoa não pode estar em solo seco. "
                "Além disso, verifique a segunda regra: a Crimson tem alguma restrição de convivência? "
                "Quais plantas do par violam as regras do canteiro 7?"
            ),
        },
        diagnostico_padrao=(
            "Aplique cada regra ao canteiro 7 separadamente. "
            "Primeira: qual planta não pode estar em solo seco? Risque-a das opções. "
            "Segunda: qual par de plantas é proibido de conviver? Risque-o também. "
            "O que sobra?"
        ),
        texto_sucesso=(
            "Dedução correta. Solo seco exclui a Névoa. A segunda regra não proíbe Âmbar com Vela. "
            "Âmbar e Vela é a única combinação segura. Calibração 0.5 validada."
        ),
        log_narrativo=(
            "NOTA RECUPERADA — Dra. R. Vello, Ciclo 47, Dia 9 (manuscrita):\n"
            "\"Não posso deixar isso sair daqui. "
            "Preciso entender o que a Ômega está fazendo antes que alguém abra aquele portão.\""
        ),
    ),
]
