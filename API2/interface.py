import streamlit as st
import pandas as pd
import os
from datetime import datetime

# --- CONFIGURAÇÕES DA PÁGINA ---
st.set_page_config(page_title="Minha Biblioteca", page_icon="📚")

# Nome do arquivo
ARQUIVO_DB = 'dados_cultura.xlsx'

# --- FUNÇÕES DE BACK-END (A Lógica) ---
def carregar_dados():
    if os.path.exists(ARQUIVO_DB):
        return pd.read_excel(ARQUIVO_DB)
    else:
        return pd.DataFrame(columns=['Título', 'Categoria', 'Status', 'Continuidade', 'Número', 'Data'])

def salvar_novo_item(titulo, categoria, status, continuidade, numero):
    novo_dado = {
        'Título': [titulo],
        'Categoria': [categoria],
        'Status': [status],
        'Continuidade': [continuidade],
        'Numero': [numero],
        'Data': [datetime.now().strftime("%d/%m/%Y")]
    }
    
    try:
        df_atual = carregar_dados()
        novo_df = pd.DataFrame(novo_dado)
        df_final = pd.concat([df_atual, novo_df], ignore_index=True)
        df_final.to_excel(ARQUIVO_DB, index=False)
        return True, "Item salvo com sucesso!"
    except PermissionError:
        return False, "Erro: Feche o arquivo Excel aberto!"
    except Exception as e:
        return False, f"Erro desconhecido: {e}"

# --- INTERFACE (O Front-end) ---

st.title("📚 Gerenciador de Leitura & Filmes")
st.write("Adicione seus livros e filmes favoritos para acompanhar depois.")

# Área de Cadastro (Barra lateral ou topo)
with st.container():
    st.subheader("📝 Novo Cadastro")
    
    col1, col2 = st.columns(2)
    
    with col1:
        titulo = st.text_input("Nome da Obra")
        categoria = st.selectbox("Categoria", ["Livro", "Filme", "Série", "Mangá", "Anime"])
        status = st.selectbox("Status Atual", ["Desejo", "Lendo", "Assistindo", "Concluído"])
        
    with col2:
        continuidade = st.selectbox("Continuidade", ["Temporada", "Capítulo", "Episódio", "Concluído"])
        numero = st.text_input("Número")
        # O botão de salvar
        submit = st.button("Salvar na Planilha")

    # Lógica do Botão
    if submit:
        if titulo:
            sucesso, mensagem = salvar_novo_item(titulo, categoria, status, continuidade, numero)
            if sucesso:
                st.success(mensagem)
            else:
                st.error(mensagem)
        else:
            st.warning("Por favor, digite o nome da obra.")

# Área de Visualização (Tabela)
st.divider()
st.subheader("📂 Seus Itens Salvos")

df = carregar_dados()

if not df.empty:
    # Mostra a tabela interativa
    st.dataframe(df, use_container_width=True)
    
    # Estatísticas Rápidas
    st.metric(label="Total de Itens", value=len(df))
else:
    st.info("Nenhum item cadastrado ainda.")