# Relatório Técnico: Inteligência Preditiva Big Mart Sales
**Candidato:** Othon Vitor Castro Braga  
**Desafio:** DATA1 — Ciência de Dados  
**Data:** Junho de 2026  

---

## 1. Contextualização do Problema e Objetivo
No cenário varejista moderno, a previsão assertiva de demanda é um pilar estratégico para a ootimização de estoques, redução de desperdícios e maximização do faturamento bruto. O objetivo deste projeto consistiu em desenvolver um pipeline completo de Ciência de Dados — abrangendo desde a ingestão, tratamento estatístico e modelagem preditiva até a entrega de valor na ponta por meio de uma interface gráfica de utilizador (Data App).

O modelo foi treinado utilizando o histórico de dados da rede **Big Mart**, focando em prever o volume total de vendas de cada produto em filiais específicas (`Item_Outlet_Sales`), permitindo que gerentes simulem cenários de negócios em tempo real.

---

## 2. Abordagem Metodológica e Arquitetura da Solução

### 2.1 Engenharia de Recursos e Análise Exploratória (Passos 1 a 7)
* **Tratamento de Dados Omissos:** Identificação e imputação estatística de valores nulos para as variáveis críticas de peso (`Item_Weight`) e tamanho da filial (`Outlet_Size`).
* **Saneamento Estatístico:** Correção de inconsistências na visibilidade dos produtos (`Item_Visibility`), onde valores zerados (ficamente impossíveis) foram tratados.
* **Análise Exploratória de Dados (EDA):** Criação de visualizações gráficas avançadas para compreender a distribuição das vendas, a correlação entre o preço máximo de venda comercial (`Item_MRP`) e o volume de saída nas lojas.

### 2.2 Modelagem, Treinamento e Inferência (Passos 8 e 9)
* **Algoritmos Selecionados:** Foram testados e refinados dois modelos principais para o problema de regressão: **Regressão Linear** (como modelo de baseline estatístico) e **Random Forest Regressor** (para capturar relações não-lineares mais complexas entre as features).
* **Métricas de Desempenho:** Avaliação rigorosa utilizando as métricas RMSE (Root Mean Squared Error) e R² Score para garantir a capacidade de generalização e evitar cenários de Overfitting.

### 2.3 Camada de Entrega: Data App (Passo 10)
Construção de uma aplicação web responsiva em **Streamlit** focada na Experiência do Utilizador (UX), permitindo a inserção dinâmica de parâmetros (`Item_MRP`, `Item_Visibility` e `Outlet_Age`) e renderização em tempo real de um gráfico de elasticidade-preço.

---

## 3. Uso de Inteligência Artificial 

Em total conformidade com o **Item 2.4 do Edital de Onboarding**, documenta-se que este projeto contou com o suporte de ferramentas de Inteligência Artificial Generativa (LLM). O uso da tecnologia foi pautado pela governança, atuando como um acelerador de produtividade de engenharia.

* **Na Análise Exploratória (EDA):** A IA auxiliou na estruturação e sintaxe dos códigos de plotagem de gráficos complexos usando bibliotecas de visualização (como Matplotlib/Seaborn), agilizando a identificação visual de padrões.
* **No Treinamento do Modelo:** Utilizou-se o suporte da IA para revisar as melhores práticas de parametrização e preparação de dados para os algoritmos de **Regressão Linear** e **Random Forest**, garantindo um pipeline limpo com o Scikit-Learn.
* **No Desenvolvimento da Interface (Streamlit):** A IA foi aplicada no design de experiência (UX) da folha de estilos CSS injetada no Streamlit, na estruturação do código assíncrono para o carregamento do modelo com cache em memória (`@st.cache_resource`), e na lógica que gera a curva interativa no gráfico de elasticidade-preço.

**Validação Humana:** Cada linha de código sugerida por IA foi rigorosamente revisada, testada localmente no ambiente de desenvolvimento e adaptada para refletir fielmente o comportamento e as colunas do dataset da Big Mart, mitigando riscos de alucinação.

---

## 4. Dificuldades Encontradas e Mitigações

* **Divergência de Dimensionalidade (Shape Mismatch):** Durante os primeiros testes na interface gráfica, o modelo recusava predições isoladas devido à ausência das colunas binárias geradas pelo One-Hot Encoding no momento do treino. 
  * *Mitigação:* Exportou-se a lista exata com a assinatura das colunas de treino (`colunas-treino.pkl`). No arquivo `app.py`, o vetor de entrada passou a ser um DataFrame inicializado com zeros contendo todas as colunas necessárias, onde apenas as features simuladas pelo usuário são atualizadas dinamicamente antes da inferência.
* **Aderência Estrita às Normas de Escrita:** A adequação ao padrão de nomenclatura em minúsculas separadas por hífens (*kebab-case*) exigiu uma refatoração minuciosa na exportação dos artefatos serializados para garantir a conformidade absoluta com o item 2.2 do edital.

---

## 5. Conclusão

O projeto atingiu com êxito todos os objetivos propostos pelo desafio técnico **DATA1**, entregando um ecossistema preditivo maduro, funcional e visualmente sofisticado para tomadores de decisão corporativos, respeitando todas as diretrizes de governança e clean code estipuladas.