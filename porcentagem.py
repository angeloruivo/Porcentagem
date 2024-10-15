import streamlit as st

# Título da aplicação
st.title("Calculadora de Porcentagem de Aumento e Redução")

# Entrada de valores
valor_inicial = st.number_input("Digite o valor inicial", min_value=0.0, format="%.2f")
valor_final = st.number_input("Digite o valor final", min_value=0.0, format="%.2f")

# Função para calcular a porcentagem de aumento
def calcular_aumento(valor_inicial, valor_final):
    if valor_inicial == 0:
        return "Aumento indefinido (valor inicial é zero)"
    aumento = ((valor_final - valor_inicial) / valor_inicial) * 100
    return aumento

# Função para calcular a porcentagem de redução
def calcular_reducao(valor_inicial, valor_final):
    if valor_inicial == 0:
        return "Redução indefinida (valor inicial é zero)"
    reducao = ((valor_inicial - valor_final) / valor_inicial) * 100
    return reducao

# Verifica se os valores são válidos
if valor_inicial > 0 and valor_final > 0:
    # Calcula e exibe a porcentagem de aumento
    aumento = calcular_aumento(valor_inicial, valor_final)
    st.write(f"Aumento de {valor_inicial} para {valor_final}: {aumento:.2f}%")

    # Calcula e exibe a porcentagem de redução
    reducao = calcular_reducao(valor_final, valor_inicial)
    st.write(f"Redução de {valor_final} para {valor_inicial}: {reducao:.2f}%")
else:
    st.write("Insira valores maiores que zero para os cálculos.")
