"""
Sistema de Vendas com Dashboard

Aplicação web em Streamlit para cadastrar vendas e acompanhar os
resultados em tempo real: faturamento, ticket médio e gráficos por
vendedor, produto e mês.

Projeto da Jornada Python (Hashtag Treinamentos) - Alessandro José dos Santos

Como rodar:  streamlit run main.py
"""

from datetime import date

import pandas as pd
import plotly.express as px
import streamlit as st

ARQUIVO = "vendas.csv"
VENDEDORES = ["Ana", "Bruno", "Carla"]
PRODUTOS = ["Notebook", "Celular", "Fone"]
CORES = {"Notebook": "#1F3A5F", "Celular": "#2E75B6", "Fone": "#9CC3E6"}  # mesma cor em todos os gráficos


def reais(valor):
    """Formata um número no padrão brasileiro: R$ 1.234,56"""
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def carregar_vendas():
    tabela = pd.read_csv(ARQUIVO)
    tabela["data"] = pd.to_datetime(tabela["data"]).dt.date
    return tabela


# Passo 1: tela do sistema
st.set_page_config(page_title="Sistema de Vendas", page_icon="🛒", layout="wide")
st.title("🛒 Sistema de Vendas")

tabela = carregar_vendas()

# Passo 2: formulário de cadastro
with st.sidebar.form("cadastro", clear_on_submit=True):
    st.header("Cadastrar venda")
    data = st.date_input("Data", value=date.today(), format="DD/MM/YYYY")
    vendedor = st.selectbox("Vendedor", VENDEDORES)
    produto = st.selectbox("Produto", PRODUTOS)
    quantidade = st.number_input("Quantidade", min_value=1, step=1)
    valor = st.number_input("Valor total da venda (R$)", min_value=0.0, step=50.0, format="%.2f")
    enviar = st.form_submit_button("Cadastrar venda", width="stretch")

# Passo 3: salvar a venda na base de dados
if enviar:
    if valor <= 0:
        st.sidebar.error("Informe o valor da venda.")
    else:
        tabela.loc[len(tabela)] = [data, vendedor, produto, int(quantidade), float(valor)]
        tabela.to_csv(ARQUIVO, index=False)
        st.sidebar.success(f"Venda de {reais(valor)} cadastrada!")

# Passo 4: indicadores principais
faturamento = tabela["valor"].sum()
n_vendas = len(tabela)
ticket_medio = faturamento / n_vendas if n_vendas else 0

col1, col2, col3 = st.columns(3)
col1.metric("Faturamento total", reais(faturamento))
col2.metric("Vendas realizadas", f"{n_vendas}")
col3.metric("Ticket médio", reais(ticket_medio))

# Passo 5: dashboard
st.subheader("Dashboard")
esquerda, direita = st.columns(2)

por_vendedor = tabela.groupby(["vendedor", "produto"], as_index=False)["valor"].sum()
grafico_vendedor = px.bar(por_vendedor, x="vendedor", y="valor", color="produto",
                          color_discrete_map=CORES, category_orders={"produto": PRODUTOS},
                          title="Faturamento por vendedor",
                          labels={"vendedor": "Vendedor", "valor": "Faturamento (R$)", "produto": "Produto"})
esquerda.plotly_chart(grafico_vendedor, width="stretch")

grafico_produto = px.pie(tabela, names="produto", values="valor", hole=0.45,
                         color="produto", color_discrete_map=CORES, category_orders={"produto": PRODUTOS},
                         title="Participação de cada produto no faturamento")
direita.plotly_chart(grafico_produto, width="stretch")

por_mes = (tabela.assign(mes=pd.to_datetime(tabela["data"]).dt.to_period("M").astype(str))
           .groupby("mes", as_index=False)["valor"].sum())
grafico_mes = px.bar(por_mes, x="mes", y="valor", title="Faturamento por mês", text_auto=".3s",
                     color_discrete_sequence=[CORES["Celular"]],
                     labels={"mes": "Mês", "valor": "Faturamento (R$)"})
st.plotly_chart(grafico_mes, width="stretch")

# Passo 6: base de dados
st.subheader("Vendas cadastradas")
st.dataframe(
    tabela.sort_values("data", ascending=False),
    width="stretch", hide_index=True,
    column_config={
        "data": st.column_config.DateColumn("Data", format="DD/MM/YYYY"),
        "vendedor": "Vendedor",
        "produto": "Produto",
        "quantidade": "Quantidade",
        "valor": st.column_config.NumberColumn("Valor (R$)", format="%.2f"),
    },
)
