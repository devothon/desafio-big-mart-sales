import streamlit as st
import pandas as pd
import joblib
import numpy as np

# 1. Configuração de Marca Corporativa e Layout Fluido
st.set_page_config(
    page_title="Big Mart | Predictive System",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Injeção de CSS Premium Avançado (Sombras, Botões Modernos e Customização de Cards)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');

    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

    .main { background-color: #fcfdfe; }

    /* Estilização Premium do Botão de Execução */
    .stButton>button { 
        width: 100%; 
        border-radius: 8px; 
        height: 3.5em; 
        font-weight: 700; 
        font-size: 16px;
        letter-spacing: 0.5px;
        background: linear-gradient(135deg, #1E3A8A 0%, #3B82F6 100%);
        color: white;
        transition: all 0.3s ease;
        border: none;
        box-shadow: 0 4px 12px rgba(59, 130, 246, 0.2);
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(59, 130, 246, 0.3);
        background: linear-gradient(135deg, #1d4ed8 0%, #2563eb 100%);
    }

    /* Customização dos Cartões de Métricas */
    div[data-testid="stMetricValue"] { font-size: 32px; font-weight: 700; color: #1E3A8A; }
    div[data-testid="stMetricLabel"] { font-size: 13px; font-weight: 600; color: #64748B; text-transform: uppercase; }

    /* Bloco customizado para o resultado principal */
    .result-card {
        background-color: #ffffff;
        padding: 24px;
        border-radius: 12px;
        border-left: 5px solid #10B981;
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.05), 0 8px 10px -6px rgba(0, 0, 0, 0.05);
        margin-top: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# 2. Painel Lateral de Governança e Configurações de Sistema
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3081/3081648.png", width=65)
st.sidebar.title("Big Mart Analytics")
st.sidebar.markdown("Plataforma empresarial de inteligência integrada para previsão automatizada de demanda e otimização de faturamento de estoques.")
st.sidebar.markdown("---")
st.sidebar.subheader("📋 Status da Sessão")
st.sidebar.success("Servidor Operacional")
st.sidebar.caption("Pipeline de Produção • v2.1.0")

# 3. Carregamento de Artefatos Otimizado com Cache em Memória (Atualizado para kebab-case!)
@st.cache_resource
def carregar_artefatos_pipeline():
    modelo = joblib.load('modelo-big-mart.pkl')
    colunas = joblib.load('colunas-treino.pkl')
    return modelo, colunas

try:
    modelo_preditivo, colunas_alinhadas = carregar_artefatos_pipeline()

    # Título Principal do Executivo
    st.title("📊 Painel de Inteligência Preditiva")
    st.markdown("Simule cenários operacionais e analise previsões estatísticas de faturamento para produtos da rede Big Mart.")
    st.markdown("---")

    # Layout de Duas Colunas Principais (Painel de Configuração vs Painel Analítico)
    col_inputs, col_outputs = st.columns([1, 1.4], gap="large")

    with col_inputs:
        st.markdown("### ⚙️ Configuração do Cenário")

        # Agrupamento Visual das Opções de Entrada
        with st.container(border=True):
            mrp = st.number_input(
                "Preço Máximo de Venda Comercial (Item_MRP)", 
                min_value=1.0, max_value=600.0, value=145.0, step=0.5,
                help="Preço máximo tabelado de comercialização sugerido para o item."
            )

            visibility = st.slider(
                "Visibilidade na Área de Exposição (Item_Visibility)", 
                min_value=0.0, max_value=0.40, value=0.06, step=0.005,
                format="%.3f", help="Porcentagem de espaço físico de prateleira dedicado a este produto na loja."
            )

            age = st.slider(
                "Tempo de Atuação da Filial no Mercado (Anos)", 
                min_value=1, max_value=50, value=15, step=1,
                help="Quantidade de anos desde a fundação/abertura desta unidade comercial."
            )

        st.markdown("##")
        executar_previsao = st.button("🔮 Calcular Projeção de Vendas", type="primary")

    with col_outputs:
        # Criação do Sistema Moderno de Abas para Organização dos Resultados
        tab_analise, tab_grafico, tab_documentacao = st.tabs([
            "🎯 Resultado da Previsão", 
            "📈 Gráfico de Elasticidade", 
            "ℹ️ Variáveis do Modelo"
        ])

        with tab_analise:
            st.markdown("### 📊 Visão Geral dos Parâmetros Digitados")

            # Cards Rápidos de Monitoramento
            kpi_1, kpi_2, kpi_3 = st.columns(3)
            kpi_1.metric("Preço Base", f"${mrp:,.2f}")
            kpi_2.metric("Área Vitrine", f"{visibility:.2%}")
            kpi_3.metric("Tempo de Loja", f"{age} Anos")

            st.markdown("---")

            if executar_previsao:
                # Alinhamento exato de Features para o scikit-learn
                X_input = pd.DataFrame(0, index=[0], columns=colunas_alinhadas)

                # Mapeamento dinâmico e robusto independente da grafia pós-processamento
                for col in X_input.columns:
                    if 'MRP' in col:
                        X_input[col] = mrp
                    elif 'Visibility' in col or 'Vis' in col:
                        X_input[col] = visibility
                    elif 'Age' in col or 'Year' in col:
                        X_input[col] = age

                # Execução da Inferência
                resultado_vendas = modelo_preditivo.predict(X_input)[0]
                if resultado_vendas < 0: resultado_vendas = 0.0

                # Card customizado de alta fidelidade
                st.markdown(f"""
                    <div class="result-card">
                        <h4 style='margin-top:0; color:#10B981;'>✓ Processamento Finalizado</h4>
                        <p style='color:#475569; margin-bottom:5px;'>Volume de faturamento estimado para o item neste estabelecimento:</p>
                        <h2 style='margin:0; color:#1E3A8A; font-size:36px;'>$ {resultado_vendas:,.2f}</h2>
                        <p style='color:#94A3B8; font-size:12px; margin-top:10px;'>Cálculo estatístico processado via Inferência Supervisionada.</p>
                    </div>
                """, unsafe_allow_html=True)

                st.balloons()
            else:
                st.info("💡 Pronto para simular: Configure as variáveis à esquerda e clique no botão 'Calcular Projeção de Vendas'.")

        with tab_grafico:
            st.markdown("### 📈 Simulação Dinâmica de Elasticidade-Preço")
            st.markdown("Este gráfico simula em tempo real como o modelo responderia a oscilações no preço do produto, mantendo as outras variáveis fixas.")

            # Loop automático para criar um vetor de predições e montar a curva no gráfico
            faixa_precos = np.linspace(mrp * 0.5, mrp * 1.5, 20)
            lista_predicoes = []

            for p_teste in faixa_precos:
                X_simulacao = pd.DataFrame(0, index=[0], columns=colunas_alinhadas)
                for col in X_simulacao.columns:
                    if 'MRP' in col: 
                        X_simulacao[col] = p_teste
                    elif 'Visibility' in col or 'Vis' in col: 
                        X_simulacao[col] = visibility
                    elif 'Age' in col or 'Year' in col: 
                        X_simulacao[col] = age

                pred_teste = modelo_preditivo.predict(X_simulacao)[0]
                lista_predicoes.append(max(0.0, pred_teste))

            # Gerando o DataFrame do gráfico estruturado
            df_curva = pd.DataFrame({
                "Preço Simulado ($)": faixa_precos,
                "Previsão de Saída (Unidades)": lista_predicoes
            }).set_index("Preço Simulado ($)")

            # Exibe o gráfico interativo nativo do Streamlit
            st.line_chart(df_curva, color="#3B82F6")
            st.caption("Eixo X: Faixa simulada de preço (de -50% a +50% do valor atual) | Eixo Y: Volume de vendas predito.")

        with tab_documentacao:
            st.markdown("### 📝 Metadados Estruturais das Features")
            st.markdown("Dicionário corporativo das variáveis numéricas que alimentam a Inteligência Artificial:")

            with st.expander("📌 Item_MRP"):
                st.write("Representa o preço máximo de venda tabelado para o produto. Historicamente, é a variável com maior peso estatístico e correlação direta com o volume final de vendas.")

            with st.expander("📌 Item_Visibility"):
                st.write("A porcentagem de área total de exibição de todas as prateleiras da loja alocada especificamente para este item. Valores extremos podem indicar erros de inventário ou alta exposição planejada.")

            with st.expander("📌 Outlet_Age"):
                st.write("Calculado como o ano corrente menos o ano de estabelecimento da filial. Unidades mais antigas consolidam marcas e costumam possuir maior estabilidade em faturamentos de grande volume.")

except FileNotFoundError:
    st.error("❌ Erro Crítico: Os arquivos do modelo treinado (`modelo-big-mart.pkl` ou `colunas-treino.pkl`) não foram detectados no repositório.")
