# 🛒 Sistema de Vendas com Dashboard

> Projeto desenvolvido na **Jornada Python — Python Dev** (Hashtag Treinamentos)

Aplicação web em Python para **cadastrar vendas e acompanhar os resultados em tempo real**: faturamento total, número de vendas, ticket médio e gráficos por vendedor, produto e mês, tudo em uma única tela.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=flat-square&logo=plotly&logoColor=white)

### 🔗 [Testar o sistema online](https://sistema-vendas-alessandro.streamlit.app/)

[![Abrir no Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://sistema-vendas-alessandro.streamlit.app/)

![Tela do sistema de vendas](imagens/dashboard.png)

---

## 📌 O problema

Pequenas equipes de vendas costumam registrar as vendas em planilhas soltas, e quem precisa de um número (quanto vendemos este mês? quem vende mais? qual produto puxa o faturamento?) tem que montar a conta na mão.

## 💡 A solução

Um sistema web simples que junta o cadastro e a análise no mesmo lugar:

1. **Cadastro:** formulário na barra lateral com data, vendedor, produto, quantidade e valor, com validação dos campos
2. **Base de dados:** cada venda é salva no arquivo `vendas.csv`
3. **Indicadores:** faturamento total, quantidade de vendas e ticket médio, formatados em reais
4. **Dashboard:** faturamento por vendedor (separado por produto), participação de cada produto e evolução mensal
5. **Tabela:** todas as vendas cadastradas, das mais recentes para as mais antigas

Ao cadastrar uma venda, os indicadores e os gráficos são atualizados na hora.

## 📊 O que os dados de exemplo mostram

Com as 120 vendas da base de exemplo (junho a agosto de 2026):

- **Faturamento total:** R$ 383.050,00, com ticket médio de R$ 3.192,08
- **Notebooks** respondem por cerca de **68% do faturamento**, mesmo sendo 37% das vendas
- **Ana** é a vendedora com maior faturamento, puxada pela venda de notebooks
- O faturamento **cresceu mês a mês**: de R$ 114 mil em junho para R$ 143 mil em agosto

## 📁 Estrutura

```
sistema-vendas/
├── main.py            # aplicação (cadastro + dashboard)
├── vendas.csv         # base de vendas
├── requirements.txt   # bibliotecas necessárias
└── imagens/           # print da aplicação
```

A versão online está publicada no **Streamlit Community Cloud**. As vendas cadastradas por lá ficam salvas até o app reiniciar.

## ▶️ Como executar

```bash
git clone https://github.com/AlessandroMaxv10/sistema-vendas.git
cd sistema-vendas
pip install -r requirements.txt
streamlit run main.py
```

O sistema abre no navegador, em `http://localhost:8501`.

## 🛠️ Tecnologias

- **Python**
- **Streamlit** — interface web, formulário e indicadores
- **Pandas** — leitura, gravação e agregação das vendas
- **Plotly** — gráficos interativos

## 📚 O que aprendi

- Criar uma aplicação web completa em Python, sem precisar de HTML ou JavaScript
- Ler e gravar dados em arquivo a partir de um formulário
- Calcular indicadores de negócio (faturamento, ticket médio) com Pandas
- Montar um dashboard com gráficos interativos e cores consistentes
- Publicar uma aplicação na internet

---

👤 **Alessandro José dos Santos** · [LinkedIn](https://www.linkedin.com/in/alessandro-jos%C3%A9-dos-santos-01b87a127) · [Portfólio](https://alessandromaxv10.github.io)
