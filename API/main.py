import pandas as pd
import os
from datetime import datetime

# Nome do arquivo (deve ser exatamente como você salvou)

ARQUIVO_DB = 'planilha_dados.xlsx'
# app.py

print("--- CADASTRO DE CULTURA ---")

# 1. Coletando o Título
# O input() pausa o programa e espera o usuário digitar e dar Enter
Título = input("Qual o nome da Obra? ")

# 2. Coletando a Categoria
Categoria = input("O que é? É um Livro, Filme, etc? ")

# 3. Coletando o Status
Status = input("Status (Desejo, Lendo, Concluido): ")

# 4. Coletando a Data
Data = datetime.now().strftime("%d/%m/%Y")

# --- NOVO: PREPARANDO OS DADOS ---
# Criamos um dicionário. 
# IMPORTANTE: As chaves (ex: 'Título') devem ser IDÊNTICAS às colunas do Excel.
novo_dado = {
    'Título': [Título],
    'Categoria': [Categoria],
    'Status': [Status],
    'Data': [Data],
    # Se você criou uma coluna 'Data' no Excel, precisaria adicionar aqui também
}

# --- VERIFICAÇÃO (Debug) ---
# Vamos imprimir para ver se as variáveis guardaram o valor correto
print("\n--- Confira os dados ---")
print(f"Título: {Título}")
print(f"Categoria: {Categoria}")
print(f"Status: {Status}")
print(f"Data: {Data}")

# Transformamos o dicionário em um DataFrame do Pandas
novo_df = pd.DataFrame(novo_dado)

# --- NOVO: LÓGICA DE GRAVAÇÃO ---

# 1. Verifica se o arquivo existe para carregar os dados antigos
if os.path.exists(ARQUIVO_DB):
    df_existente = pd.read_excel(ARQUIVO_DB)
    # Junta o antigo com o novo
    df_final = pd.concat([df_existente, novo_df], ignore_index=True)
else:
    # Se o arquivo não existir (ou nome estiver errado), ele cria um novo só com o dado atual
    print("Aviso: Arquivo não encontrado. Criando um novo...")
    df_final = novo_df

# 2. Salva tudo no Excel (index=False remove a numeração automática do Pandas)
try:
    df_final.to_excel(ARQUIVO_DB, index=False)
    print("\n✅ Sucesso! Dados salvos na planilha.")
except PermissionError:
    print("\n❌ Erro: Feche o arquivo Excel antes de rodar o programa!")