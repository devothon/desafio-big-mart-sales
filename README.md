# 📈 Sistema Preditivo Big Mart Sales

Este repositório contém a solução para o desafio técnico **DATA01 (Ciência de Dados - Nível Avançado)**. A aplicação consiste em um pipeline de **Machine Learning** integrado a uma interface gráfica desenvolvida com **Streamlit** para previsão de faturamento de produtos da Big Mart.

## 📌 Sobre o Projeto

O objetivo deste projeto é estimar o faturamento de produtos com base em características dos itens e das lojas, utilizando técnicas de Ciência de Dados e Aprendizado de Máquina. A solução permite que usuários realizem previsões de forma simples através de uma interface web interativa.

## 🚀 Tecnologias Utilizadas

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Streamlit

## 🛠️ Instruções de Instalação e Execução

Para testar a aplicação em seu ambiente local, siga os passos abaixo no terminal:

### 1. Instalar as Dependências

Certifique-se de ter o Python instalado e execute o comando abaixo para instalar as bibliotecas necessárias:

```bash
pip install streamlit pandas numpy scikit-learn joblib
```

### 2. Executar a Aplicação

Após a instalação das dependências, inicie a aplicação com o comando:

```bash
streamlit run app.py
```

### 3. Acessar a Interface

Com o servidor em execução, abra o navegador e acesse:

```text
http://localhost:8503
```

## 📂 Estrutura do Projeto

```text
├── app.py
├── modelo_final.pkl
├── preprocessor.pkl
├── train.csv
└── README.md
```

## 🎯 Objetivo

Desenvolver um modelo preditivo capaz de estimar o faturamento de produtos com base em características dos itens e das lojas, auxiliando análises de desempenho e tomadas de decisão orientadas por dados.
