import streamlit as st

st.set_page_config(
    page_title="Alugar Imóveis | Robuste",
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
    letter-spacing: 3px;
    font-weight: 600;
}
.hero-rent {
    padding: 70px 40px;
    background: linear-gradient(rgba(0,0,0,.55), rgba(0,0,0,.55)),
    url('https://images.unsplash.com/photo-1560184897-ae75f418493e');
    background-size: cover;
    background-position: center;
    border-radius: 18px;
    color: white;
    margin-top: 25px;
}
.hero-rent h1 {
    font-size: 52px;
    font-weight: 500;
}
.hero-rent p {
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
col1, col2, col3, col4= st.columns([2, 1, 1, 1])

with col1:
    st.markdown('<div class="logo">ROBUSTE</div>', unsafe_allow_html=True)
with col2:
     if st.button("inicio"):
        st.switch_page("robuste.py")
with col3:
    if st.button("Comprar"):
        st.switch_page("pages/compras.py")
with col4:
    if  st.button("Contato"):
        st.switch_page("pages/contato.py")

# HERO
st.markdown("""
<div class="hero-rent">
    <h1>Alugue imóveis com conforto e segurança</h1>
    <p>
    Encontre apartamentos, casas, coberturas e imóveis mobiliados selecionados
    pela curadoria da Imobiliária Robuste.
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
        "Studio",
        "Casa de campo"
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
    faixa_valor = st.selectbox("Valor do aluguel", [
        "Todos",
        "Até R$ 2.000",
        "R$ 2.000 a R$ 5.000",
        "R$ 5.000 a R$ 10.000",
        "Acima de R$ 10.000"
    ])

st.button("Buscar aluguel")

st.markdown('</div>', unsafe_allow_html=True)

# DADOS DOS IMÓVEIS
imoveis = [
    {
        "titulo": "Apartamento mobiliado em região nobre",
        "cidade": "São Paulo",
        "tipo": "Apartamento",
        "quartos": 2,
        "preco_num": 4800,
        "preco": "R$ 4.800/mês",
        "local": "Moema, São Paulo - SP",
        "detalhes": "95 m² • 2 dormitórios • 1 suíte • 2 vagas",
        "tag": "Mobiliado",
        "img": "https://images.unsplash.com/photo-1522708323590-d24dbb6b0267"
    },
    {
        "titulo": "Cobertura para locação com vista",
        "cidade": "Rio de Janeiro",
        "tipo": "Cobertura",
        "quartos": 3,
        "preco_num": 12500,
        "preco": "R$ 12.500/mês",
        "local": "Barra da Tijuca, Rio de Janeiro - RJ",
        "detalhes": "240 m² • 3 suítes • Terraço • Piscina",
        "tag": "Vista privilegiada",
        "img": "https://images.unsplash.com/photo-1505693416388-ac5ce068fe85"
    },
    {
        "titulo": "Studio moderno próximo ao centro",
        "cidade": "Campinas",
        "tipo": "Studio",
        "quartos": 1,
        "preco_num": 2100,
        "preco": "R$ 2.100/mês",
        "local": "Cambuí, Campinas - SP",
        "detalhes": "42 m² • 1 dormitório • Mobiliado • Lazer completo",
        "tag": "Compacto e moderno",
        "img": "https://images.unsplash.com/photo-1493809842364-78817add7ffb"
    },
    {
        "titulo": "Casa em condomínio fechado",
        "cidade": "Ribeirão Preto",
        "tipo": "Casa",
        "quartos": 4,
        "preco_num": 8900,
        "preco": "R$ 8.900/mês",
        "local": "Zona Sul, Ribeirão Preto - SP",
        "detalhes": "330 m² • 4 suítes • Área gourmet • 4 vagas",
        "tag": "Condomínio premium",
        "img": "https://images.unsplash.com/photo-1568605114967-8130f3a36994"
    },
    {
        "titulo": "Casa de campo para temporada",
        "cidade": "Interior de SP",
        "tipo": "Casa de campo",
        "quartos": 4,
        "preco_num": 15000,
        "preco": "R$ 15.000/mês",
        "local": "Interior de São Paulo",
        "detalhes": "800 m² • 4 suítes • Piscina • Área verde",
        "tag": "Temporada ou mensal",
        "img": "https://images.unsplash.com/photo-1600047509807-ba8f99d2cdde"
    },
    {
        "titulo": "Apartamento amplo com varanda gourmet",
        "cidade": "São Paulo",
        "tipo": "Apartamento",
        "quartos": 3,
        "preco_num": 6700,
        "preco": "R$ 6.700/mês",
        "local": "Vila Mariana, São Paulo - SP",
        "detalhes": "130 m² • 3 dormitórios • Varanda gourmet • 2 vagas",
        "tag": "Excelente localização",
        "img": "https://images.unsplash.com/photo-1502672260266-1c1ef2d93688"
    }
]

def valor_ok(preco):
    if faixa_valor == "Todos":
        return True
    if faixa_valor == "Até R$ 2.000":
        return preco <= 2000
    if faixa_valor == "R$ 2.000 a R$ 5.000":
        return 2000 <= preco <= 5000
    if faixa_valor == "R$ 5.000 a R$ 10.000":
        return 5000 <= preco <= 10000
    if faixa_valor == "Acima de R$ 10.000":
        return preco > 10000
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
st.markdown('<h2 class="section-title">Imóveis disponíveis para aluguel</h2>', unsafe_allow_html=True)

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

            if st.button("Quero alugar", key=imovel["titulo"]):
                st.success("Interesse registrado. Um consultor Robuste entrará em contato.")

            st.markdown('</div>', unsafe_allow_html=True)

# CTA FINAL
st.markdown("""
<div class="contact-box">
    <h2>Precisa de ajuda para encontrar o aluguel ideal?</h2>
    <p>
    A equipe Robuste seleciona imóveis de acordo com seu perfil, localização desejada,
    orçamento mensal e estilo de vida.
    </p>
</div>
""", unsafe_allow_html=True)

nome = st.text_input("Seu nome")
whatsapp = st.text_input("WhatsApp")
preferencia = st.text_area("Descreva o imóvel que você deseja alugar")

if st.button("Solicitar atendimento"):
    st.success("Solicitação enviada com sucesso!")