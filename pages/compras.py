import streamlit as st

st.set_page_config(
    page_title="Comprar Imóveis | Robuste",
    page_icon="🏛️",
    layout="wide"
)

st.markdown("""
<style>
.main {
    background-color: #f7f4ef;
}
.header {
    padding: 30px 20px;
    border-bottom: 1px solid #ddd;
}
.logo {
    font-size: 30px;
    letter-spacing: 3px;
    font-weight: 600;
}
.hero-buy {
    padding: 70px 40px;
    background: linear-gradient(rgba(0,0,0,.55), rgba(0,0,0,.55)),
    url('https://images.unsplash.com/photo-1600607687920-4e2a09cf159d');
    background-size: cover;
    background-position: center;
    border-radius: 18px;
    color: white;
    margin-top: 25px;
}
.hero-buy h1 {
    font-size: 52px;
    font-weight: 500;
}
.hero-buy p {
    font-size: 20px;
    max-width: 720px;
}
.filter-box {
    background-color: white;
    padding: 25px;
    border-radius: 18px;
    box-shadow: 0 10px 25px rgba(0,0,0,.08);
    margin-top: -35px;
}
.card {
    background-color: white;
    border-radius: 18px;
    overflow: hidden;
    box-shadow: 0 10px 28px rgba(0,0,0,.08);
    margin-bottom: 30px;
}
.card-content {
    padding: 22px;
}
.card h3 {
    font-size: 24px;
    margin-bottom: 5px;
}
.location {
    color: #666;
    font-size: 15px;
}
.details {
    color: #333;
    font-size: 15px;
    margin-top: 12px;
}
.price {
    color: #8b6f47;
    font-size: 24px;
    font-weight: bold;
    margin-top: 15px;
}
.tag {
    display: inline-block;
    padding: 6px 12px;
    background-color: #efe6d8;
    color: #5e4728;
    border-radius: 20px;
    font-size: 13px;
    margin-bottom: 10px;
}
.section-title {
    font-size: 36px;
    margin-top: 50px;
    margin-bottom: 25px;
}
.contact-box {
    background-color: #1f1f1f;
    color: white;
    padding: 40px;
    border-radius: 20px;
    margin-top: 40px;
}
</style>
""", unsafe_allow_html=True)

# MENU
col1, col2, col3, col4 = st.columns([2, 1, 1, 1])

with col1:
    st.markdown('<div class="logo">ROBUSTE</div>', unsafe_allow_html=True)
with col2:
    if st.button("inicio"):
        st.switch_page("robuste.py")
with col3:
    if  st.button("alugar"):
        st.switch_page("pages/aluguel.py")
with col4:
    if  st.button("Contato"):
        st.switch_page("pages/contato.py")

# HERO
st.markdown("""
<div class="hero-buy">
    <h1>Comprar imóveis de alto padrão</h1>
    <p>
    Encontre casas, apartamentos, coberturas e propriedades exclusivas
    selecionadas pela curadoria da Imobiliária Robuste.
    </p>
</div>
""", unsafe_allow_html=True)

# FILTROS
st.markdown('<div class="filter-box">', unsafe_allow_html=True)

f1, f2, f3, f4 = st.columns(4)

with f1:
    cidade = st.selectbox("Cidade", [
        "Todas",
        "São Paulo",
        "Rio de Janeiro",
        "Campinas",
        "Ribeirão Preto",
        "Interior de SP"
    ])

with f2:
    tipo = st.selectbox("Tipo de imóvel", [
        "Todos",
        "Apartamento",
        "Casa",
        "Cobertura",
        "Casa de campo",
        "Terreno"
    ])

with f3:
    quartos = st.selectbox("Quartos", [
        "Qualquer",
        "1+",
        "2+",
        "3+",
        "4+"
    ])

with f4:
    faixa_valor = st.selectbox("Faixa de valor", [
        "Todos",
        "Até R$ 800 mil",
        "R$ 800 mil a R$ 1,5 mi",
        "R$ 1,5 mi a R$ 3 mi",
        "Acima de R$ 3 mi"
    ])

b1, b2, b3 = st.columns([1, 1, 4])
with b1:
    buscar = st.button("Buscar")
with b2:
    limpar = st.button("Limpar")

st.markdown('</div>', unsafe_allow_html=True)

# DADOS DOS IMÓVEIS
imoveis = [
    {
        "titulo": "Casa contemporânea no Jardim América",
        "cidade": "São Paulo",
        "tipo": "Casa",
        "quartos": 4,
        "preco_num": 4800000,
        "preco": "R$ 4.800.000",
        "local": "Jardim América, São Paulo - SP",
        "detalhes": "420 m² • 4 suítes • 5 vagas • Piscina",
        "tag": "Exclusivo Robuste",
        "img": "https://images.unsplash.com/photo-1600607687939-ce8a6c25118c"
    },
    {
        "titulo": "Cobertura duplex com vista panorâmica",
        "cidade": "Rio de Janeiro",
        "tipo": "Cobertura",
        "quartos": 3,
        "preco_num": 6200000,
        "preco": "R$ 6.200.000",
        "local": "Leblon, Rio de Janeiro - RJ",
        "detalhes": "310 m² • 3 suítes • Terraço • Piscina privativa",
        "tag": "Vista privilegiada",
        "img": "https://images.unsplash.com/photo-1600566753190-17f0baa2a6c3"
    },
    {
        "titulo": "Apartamento elegante em região nobre",
        "cidade": "Campinas",
        "tipo": "Apartamento",
        "quartos": 3,
        "preco_num": 1450000,
        "preco": "R$ 1.450.000",
        "local": "Cambuí, Campinas - SP",
        "detalhes": "180 m² • 3 dormitórios • 2 vagas • Varanda gourmet",
        "tag": "Pronto para morar",
        "img": "https://images.unsplash.com/photo-1600585154526-990dced4db0d"
    },
    {
        "titulo": "Casa de campo com arquitetura autoral",
        "cidade": "Interior de SP",
        "tipo": "Casa de campo",
        "quartos": 4,
        "preco_num": 3500000,
        "preco": "R$ 3.500.000",
        "local": "Interior de São Paulo",
        "detalhes": "900 m² • 4 suítes • Área verde • Espaço gourmet",
        "tag": "Natureza e privacidade",
        "img": "https://images.unsplash.com/photo-1600047509807-ba8f99d2cdde"
    },
    {
        "titulo": "Terreno em condomínio fechado",
        "cidade": "Ribeirão Preto",
        "tipo": "Terreno",
        "quartos": 0,
        "preco_num": 760000,
        "preco": "R$ 760.000",
        "local": "Zona Sul, Ribeirão Preto - SP",
        "detalhes": "520 m² • Condomínio de alto padrão • Segurança 24h",
        "tag": "Oportunidade",
        "img": "https://images.unsplash.com/photo-1500382017468-9049fed747ef"
    },
    {
        "titulo": "Casa térrea em condomínio premium",
        "cidade": "São Paulo",
        "tipo": "Casa",
        "quartos": 3,
        "preco_num": 2850000,
        "preco": "R$ 2.850.000",
        "local": "Alphaville, São Paulo - SP",
        "detalhes": "360 m² • 3 suítes • Jardim • 4 vagas",
        "tag": "Condomínio fechado",
        "img": "https://images.unsplash.com/photo-1605276374104-dee2a0ed3cd6"
    }
]

def valor_ok(preco):
    if faixa_valor == "Todos":
        return True
    if faixa_valor == "Até R$ 800 mil":
        return preco <= 800000
    if faixa_valor == "R$ 800 mil a R$ 1,5 mi":
        return 800000 <= preco <= 1500000
    if faixa_valor == "R$ 1,5 mi a R$ 3 mi":
        return 1500000 <= preco <= 3000000
    if faixa_valor == "Acima de R$ 3 mi":
        return preco > 3000000
    return True

def quartos_ok(qtd):
    if quartos == "Qualquer":
        return True
    minimo = int(quartos.replace("+", ""))
    return qtd >= minimo

imoveis_filtrados = [
    imovel for imovel in imoveis
    if (cidade == "Todas" or imovel["cidade"] == cidade)
    and (tipo == "Todos" or imovel["tipo"] == tipo)
    and quartos_ok(imovel["quartos"])
    and valor_ok(imovel["preco_num"])
]

# LISTAGEM
st.markdown('<h2 class="section-title">Imóveis disponíveis para compra</h2>', unsafe_allow_html=True)

st.write(f"{len(imoveis_filtrados)} imóveis encontrados")

for i in range(0, len(imoveis_filtrados), 3):
    cols = st.columns(3)

    for col, imovel in zip(cols, imoveis_filtrados[i:i+3]):
        with col:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.image(imovel["img"], use_container_width=True)

            st.markdown(f"""
            <div class="card-content">
                <span class="tag">{imovel['tag']}</span>
                <h3>{imovel['titulo']}</h3>
                <p class="location">{imovel['local']}</p>
                <p class="details">{imovel['detalhes']}</p>
                <p class="price">{imovel['preco']}</p>
            </div>
            """, unsafe_allow_html=True)

            if st.button("Tenho interesse", key=imovel["titulo"]):
                st.success("Interesse registrado. Um consultor Robuste entrará em contato.")

            st.markdown('</div>', unsafe_allow_html=True)

# CTA FINAL
st.markdown("""
<div class="contact-box">
    <h2>Não encontrou o imóvel ideal?</h2>
    <p>
    Conte para a Robuste o que você procura. Nossa equipe faz uma curadoria personalizada
    de imóveis de acordo com seu perfil, localização desejada e investimento.
    </p>
</div>
""", unsafe_allow_html=True)

nome = st.text_input("Seu nome")
whatsapp = st.text_input("WhatsApp")
preferencia = st.text_area("Descreva o imóvel que você procura")

if st.button("Solicitar curadoria personalizada"):
    st.success("Solicitação enviada com sucesso!")