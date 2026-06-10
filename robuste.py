import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Imobiliária Robuste",
    page_icon="🏛️",
    layout="wide"
)

if "go_bottom" not in st.session_state:
    st.session_state.go_bottom = 0

st.markdown("""
<style>
body {
    background-color: #f7f4ef;
}
.main {
    background-color: #f7f4ef;
}
.hero {
    padding: 90px 40px;
    background: linear-gradient(rgba(10,10,10,.55), rgba(10,10,10,.55)),
    url('https://images.unsplash.com/photo-1600585154340-be6161a56a0c');
    background-size: cover;
    background-position: center;
    border-radius: 18px;
    color: white;
}
.hero h1 {
    font-size: 58px;
    font-weight: 500;
    letter-spacing: 2px;
}
.hero p {
    font-size: 20px;
    max-width: 700px;
}
.card {
    background-color: white;
    padding: 25px;
    border-radius: 16px;
    box-shadow: 0 10px 30px rgba(0,0,0,.08);
    margin-bottom: 20px;
}
.price {
    color: #8b6f47;
    font-size: 22px;
    font-weight: bold;
}
.section-title {
    font-size: 36px;
    margin-top: 50px;
    color: #1f1f1f;
}
.button {
    background-color: #1f1f1f;
    color: white;
    padding: 12px 26px;
    border-radius: 30px;
    text-decoration: none;
}
</style>
""", unsafe_allow_html=True)

# MENU
col1, col2, col3, col4 = st.columns([2,1,1,1])
with col1:
    st.markdown("## ROBUSTE")
with col2:
   if st.button("Comprar"):
    st.switch_page("pages/compras.py")
with col3:
   if  st.button("alugar"):
    st.switch_page("pages/aluguel.py")
with col4:
    if st.button("Contato"):
        st.session_state.go_bottom += 1


if st.session_state.go_bottom:
     components.html(
        f"""
        <script>
            setTimeout(() => {{
                parent.document
                    .getElementById('Fale')
                    ?.scrollIntoView({{
                        behavior:'smooth',
                        block:'start'
                    }});
            }}, 100);
        </script>
        <div>{st.session_state.go_bottom}</div>
        """,
        height=0,)

# HERO
st.markdown("""
<div class="hero">
    <h1>Imóveis exclusivos para viver com sofisticação</h1>
    <p>
    A Imobiliária Robuste oferece uma curadoria de casas, apartamentos e propriedades
    selecionadas para quem busca conforto, localização e alto padrão.
    </p>
    <br>
    <a class="button" href="#imoveis">Ver imóveis</a>
</div>
""", unsafe_allow_html=True)

# BUSCA
st.markdown('<h2 class="section-title">Encontre seu imóvel ideal</h2>', unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4)
with c1:
    cidade = st.selectbox("Cidade", ["São Paulo", "Rio de Janeiro", "Campinas", "Ribeirão Preto"])
with c2:
    tipo = st.selectbox("Tipo", ["Apartamento", "Casa", "Cobertura", "Casa de Campo"])
with c3:
    quartos = st.selectbox("Quartos", ["1+", "2+", "3+", "4+"])
with c4:
    valor = st.selectbox("Valor", ["Até R$ 800 mil", "Até R$ 1,5 mi", "Até R$ 3 mi", "Acima de R$ 3 mi"])

st.button("Buscar imóveis")

# IMÓVEIS
st.markdown('<h2 id="imoveis" class="section-title">Imóveis em destaque</h2>', unsafe_allow_html=True)

imoveis = [
    {
        "titulo": "Casa contemporânea no Jardim América",
        "local": "São Paulo, SP",
        "preco": "R$ 4.800.000",
        "detalhes": "420 m² • 4 suítes • 5 vagas",
        "img": "https://images.unsplash.com/photo-1600607687939-ce8a6c25118c"
    },
    {
        "titulo": "Cobertura com vista panorâmica",
        "local": "Rio de Janeiro, RJ",
        "preco": "R$ 6.200.000",
        "detalhes": "310 m² • 3 suítes • Piscina privativa",
        "img": "https://images.unsplash.com/photo-1600566753190-17f0baa2a6c3"
    },
    {
        "titulo": "Refúgio de campo exclusivo",
        "local": "Interior de SP",
        "preco": "R$ 3.500.000",
        "detalhes": "900 m² • Área verde • Arquitetura autoral",
        "img": "https://images.unsplash.com/photo-1600047509807-ba8f99d2cdde"
    }
]

cols = st.columns(3)

for col, imovel in zip(cols, imoveis):
    with col:
        st.image(imovel["img"], use_container_width=True)
        st.markdown(f"""
        <div class="card">
            <h3>{imovel['titulo']}</h3>
            <p>{imovel['local']}</p>
            <p>{imovel['detalhes']}</p>
            <p class="price">{imovel['preco']}</p>
        </div>
        """, unsafe_allow_html=True)

# SOBRE
st.markdown('<h2 class="section-title">A experiência Robuste</h2>', unsafe_allow_html=True)

st.markdown("""
<div class="card">
A Robuste nasceu para oferecer um atendimento imobiliário mais elegante, seguro e personalizado.
Nossa curadoria seleciona imóveis com localização privilegiada, arquitetura diferenciada e alto potencial
de valorização.
<br><br>
Trabalhamos com compra, venda, aluguel e avaliação de imóveis residenciais de médio e alto padrão.
</div>
""", unsafe_allow_html=True)

# CONTATO
st.markdown("<div id='Fale'></div>", unsafe_allow_html=True)
st.markdown('<h2 class="section-title">Fale com um consultor</h2>', unsafe_allow_html=True)

nome = st.text_input("Nome")
telefone = st.text_input("Telefone / WhatsApp")
mensagem = st.text_area("Mensagem")

if st.button("Enviar contato"):
    st.success("Contato enviado com sucesso! A equipe Robuste retornará em breve.")

st.markdown("---")
st.markdown("© 2026 Imobiliária Robuste | CRECI 00000-J | Atendimento personalizado em imóveis de alto padrão")