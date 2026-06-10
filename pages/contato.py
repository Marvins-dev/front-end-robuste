import streamlit as st

st.set_page_config(
    page_title="Contato | Robuste",
    page_icon="🏛️",
    layout="wide"
)

st.markdown("""
<style>

.main {
    background-color: #f7f4ef;
}

.logo {
    font-size: 30px;
    font-weight: 600;
    letter-spacing: 3px;
}

.hero {
    padding: 70px;
    background: linear-gradient(
        rgba(0,0,0,0.55),
        rgba(0,0,0,0.55)
    ),
    url('https://images.unsplash.com/photo-1486406146926-c627a92ad1ab');
    background-size: cover;
    background-position: center;
    border-radius: 20px;
    color: white;
    margin-top: 20px;
}

.hero h1 {
    font-size: 52px;
}

.hero p {
    font-size: 20px;
    max-width: 700px;
}

.contact-card {
    background: white;
    padding: 35px;
    border-radius: 20px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.08);
}

.info-card {
    background: #1f1f1f;
    color: white;
    padding: 35px;
    border-radius: 20px;
    height: 100%;
}

.section-title {
    font-size: 36px;
    margin-top: 50px;
    margin-bottom: 30px;
}

.footer {
    text-align: center;
    color: #777;
    margin-top: 40px;
}

</style>
""", unsafe_allow_html=True)

# MENU

col1, col2, col3, col4 = st.columns([2,1,1,1])

with col1:
    st.markdown('<div class="logo">ROBUSTE</div>', unsafe_allow_html=True)

with col2:
    if st.button("inicio"):
        st.switch_page("robuste.py")

with col3:
    if st.button("Comprar"):
        st.switch_page("pages/compras.py")

with col4:
    if  st.button("alugar"):
        st.switch_page("pages/aluguel.py")

# HERO

st.markdown("""
<div class="hero">
    <h1>Fale com a Robuste</h1>
    <p>
        Nossa equipe está pronta para ajudar você a encontrar
        o imóvel ideal para compra ou locação.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown(
    '<h2 class="section-title">Entre em contato</h2>',
    unsafe_allow_html=True
)

col1, col2 = st.columns([2,1])

# FORMULÁRIO

with col1:

    st.markdown('<div class="contact-card">', unsafe_allow_html=True)

    nome = st.text_input("Nome completo")

    email = st.text_input("E-mail")

    telefone = st.text_input("Telefone / WhatsApp")

    assunto = st.selectbox(
        "Assunto",
        [
            "Compra de imóvel",
            "Aluguel de imóvel",
            "Venda de imóvel",
            "Parcerias",
            "Outros"
        ]
    )

    mensagem = st.text_area(
        "Mensagem",
        height=180
    )

    if st.button("Enviar mensagem"):
        st.success(
            "Mensagem enviada com sucesso! Em breve entraremos em contato."
        )

    st.markdown('</div>', unsafe_allow_html=True)

# INFORMAÇÕES

with col2:

    st.markdown("""
    <div class="info-card">
        <h2>Robuste</h2>

<h4>Central de Atendimento</h4>
<p>(14) 3112-7070</p>

<h4>E-mail Corporativo</h4>
<p>contato@robusteimobiliaria.com.br</p>

<h4>Escritório Robuste</h4>
<p>
    Francisco Líra Brandão, 63 <br>
    Vila Sao Judas Thadeu<br>
    Botucatu - SP
</p>

<h4>Horário de Funcionamento</h4>
<p>
    Segunda a Sexta • 08h às 18h<br>
    Sábado • 09h às 13h
</p>
    </div>
    """, unsafe_allow_html=True)

# MAPA (placeholder)

st.markdown(
    '<h2 class="section-title">Nossa localização</h2>',
    unsafe_allow_html=True
)

st.map(
    {
        "lat": [-22.89145864357638],
        "lon": [-48.454378749796014]
    }
)

# RODAPÉ

st.markdown("""
<div class="footer">
    © 2026 ROBUSTE IMOBILIÁRIA • Todos os direitos reservados
</div>
""", unsafe_allow_html=True)