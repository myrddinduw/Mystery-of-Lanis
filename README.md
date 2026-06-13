# O Mistério de Lanis: O Bosque dos Axiomas

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://mystery-of-lanis.streamlit.app)

Ficção interativa de treino em **interpretação de texto** e **dedução lógica**, construída com Python + Streamlit.

## Sobre o jogo

A jogadora é **Lanis**, investigadora especializada na união entre natureza e matemática. Ela explora a **Estação de Pesquisa Botânica Épsilon**, abandonada, onde a flora obedece a regras matemáticas estritas.

Lendo diários de campo e registros científicos deixados pela antiga equipe, Lanis usa pura dedução lógica para destrancar os setores do laboratório e descobrir o destino dos pesquisadores.

A interface simula o **Terminal de Acesso da Estação Épsilon**: documentos antigos e envelhecidos surgem dentro de um terminal escuro. Lanis lê, anota no caderno físico, e insere suas deduções no terminal.

## Como rodar

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Progressão

| Setor | Nome | Status |
|---|---|---|
| 0 | Calibração do Terminal (5 salas) | ✅ v1.0 |
| 1 | Diário de Campo (2 salas) | ✅ v1.0 |
| 2 | Relatório Técnico | 🔜 futuro |
| 3 | Debate Acadêmico | 🔜 futuro |

## Estrutura

```
├── app.py                   # roteamento de fases
├── state.py                 # st.session_state — progressão e mutadores
├── engine.py                # validação + feedback socrático
├── ui.py                    # CSS do terminal, componentes de render
└── content/
    ├── schema.py            # dataclasses Sala e Documento
    ├── narrativa.py         # boot, transições, texto final
    ├── setor_0_treino.py    # salas 0.1–0.5
    ├── setor_1_diario.py    # salas 1.1–1.2
    ├── setor_2_relatorio.py # stub — futuro
    └── setor_3_debate.py    # stub — futuro
```

Para adicionar novas salas: edite apenas o arquivo `setor_X_*.py` correspondente. Nenhuma outra alteração é necessária.
