import streamlit as st

st.set_page_config(
    page_title="um cantinho pra você ☾",
    page_icon="☾"
)

# ==========================
# ESTILO
# ==========================

st.markdown("""
<style>

.stApp {
    background:
        radial-gradient(circle at 20% 20%, #171525 0, #08080d 45%, #050507 100%);
    color: #f4f1f8;
}

.block-container {
    max-width: 700px;
    padding-top: 10vh;
}

.big {
    font-size: clamp(2rem, 7vw, 4rem);
    line-height: 1.1;
    text-align: center;
    margin: 2rem 0;
}

.text {
    font-size: clamp(1.35rem, 4vw, 2rem);
    line-height: 1.5;
    text-align: center;
}

.small {
    text-align: center;
    color: #bdb6c8;
    font-size: 1.1rem;
}

.moon {
    text-align: center;
    font-size: 3.5rem;
    margin-bottom: 2rem;
}

.signature {
    text-align: center;
    margin-top: 2rem;
    font-size: 1.2rem;
    color: #c9c1d5;
}

.stButton > button {
    width: 100%;
    border-radius: 999px;
    background: rgba(255,255,255,.06);
    color: white;
    border: 1px solid rgba(255,255,255,.25);
    padding: 0.8rem;
}

</style>
""", unsafe_allow_html=True)


# ==========================
# CONTROLE DAS PÁGINAS
# ==========================

if "pagina" not in st.session_state:
    st.session_state.pagina = 0


def continuar():
    st.session_state.pagina += 1


pagina = st.session_state.pagina


# ==========================
# COMEÇO
# ==========================

if pagina == 0:

    st.markdown(
        '<div class="moon">☾</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="small">um cantinho que eu fiz pra você</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="big">eu queria te mostrar uma coisa.</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="small">não precisa ter pressa.</div>',
        unsafe_allow_html=True
    )

    st.write("")

    st.button(
        "continuar",
        on_click=continuar
    )


# ==========================
# PARTE 2
# ==========================

elif pagina == 1:

    st.markdown(
        '<div class="moon">✦</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="text">eu sei que você gosta da sua própria companhia.</div>',
        unsafe_allow_html=True
    )

    st.write("")

    st.button(
        "...",
        on_click=continuar
    )


# ==========================
# PARTE 3
# ==========================

elif pagina == 2:

    st.markdown(
        '<div class="moon">⋆</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="text">
        do silêncio.<br>
        do seu espaço.<br>
        de simplesmente ficar.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    st.button(
        "eu entendo.",
        on_click=continuar
    )


# ==========================
# PARTE 4
# ==========================

elif pagina == 3:

    st.markdown(
        '<div class="moon">☾</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="text">e eu não quero mudar isso.</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="small">de verdade.</div>',
        unsafe_allow_html=True
    )

    st.write("")

    st.button(
        "então...",
        on_click=continuar
    )


# ==========================
# PERGUNTA
# ==========================

elif pagina == 4:

    st.markdown(
        '<div class="moon">☾ ✦ ☾</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="text">eu só queria saber uma coisa...</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="big">posso ficar aqui calada com você?</div>',
        unsafe_allow_html=True
    )

    st.write("")

    st.button(
        "pode. ♡",
        on_click=continuar
    )


# ==========================
# MODO SILÊNCIO
# ==========================

elif pagina == 5:

    st.markdown(
        '<div class="moon">☾</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="text">então eu fico.</div>',
        unsafe_allow_html=True
    )

    st.write("")

    st.button("→", on_click=continuar)


elif pagina == 6:

    st.markdown(
        '<div class="moon">⋆</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="text">não precisa falar.</div>',
        unsafe_allow_html=True
    )

    st.write("")

    st.button("→", on_click=continuar)


elif pagina == 7:

    st.markdown(
        '<div class="moon">⋆</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="text">não precisa responder.</div>',
        unsafe_allow_html=True
    )

    st.write("")

    st.button("→", on_click=continuar)


elif pagina == 8:

    st.markdown(
        '<div class="moon">⋆</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="text">não precisa fazer nada.</div>',
        unsafe_allow_html=True
    )

    st.write("")

    st.button("→", on_click=continuar)


elif pagina == 9:

    st.markdown(
        '<div class="moon">☾</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="text">pode só ficar aqui.</div>',
        unsafe_allow_html=True
    )

    st.write("")

    st.button("→", on_click=continuar)


# ==========================
# FINAL
# ==========================

elif pagina == 10:

    st.markdown(
        '<div class="moon">✦</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="text">eu continuo aqui.</div>',
        unsafe_allow_html=True
    )

    st.write("")

    st.button(
        "última coisinha",
        on_click=continuar
    )


# ==========================
# FINALZINHO
# ==========================

else:

    st.markdown(
        '<div class="moon">☾ ✦ ☾</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="text">
        não precisa dizer nada.<br><br>
        pode só ficar.<br><br>
        eu fico também.
        </div>

        <div class="signature">
        — sua Bobona ♡
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")
    st.write("")

    if st.button("voltar pro começo"):
        st.session_state.pagina = 0
        st.rerun()