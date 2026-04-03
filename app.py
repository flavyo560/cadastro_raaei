import streamlit as st
import requests
from datetime import date

st.set_page_config(page_title="Cadastro RAAEI", layout="centered")

st.title("🏆 Cadastro de Atleta - RAAEI")
st.markdown("Preencha os dados abaixo para registrar um novo atleta.")

# ORGANIZAÇÃO EM ABAS (SEÇÕES)
tab1, tab2, tab3, tab4 = st.tabs(["Atleta", "Filiação", "Endereço", "Escola"])

with tab1:
    st.subheader("Dados do Atleta")
    nome = st.text_input("Nome Completo")
    col1, col2 = st.columns(2)
    cpf = col1.text_input("CPF (Somente números)")
    rg = col2.text_input("RG (Opcional)")
    
    col3, col4 = st.columns(2)
    data_nasc = col3.date_input("Data de Nascimento", min_value=date(1900, 1, 1))
    sexo = col4.selectbox("Sexo", ["Masculino", "Feminino"])
    
    inep_aluno = st.text_input("INEP do Aluno")
    cbat = st.text_input("CBAT (Opcional)")
    tel_atleta = st.text_input("Telefone Atleta")

with tab2:
    st.subheader("Dados da Mãe")
    m_nome = st.text_input("Nome da Mãe")
    col_m1, col_m2 = st.columns(2)
    m_cpf = col_m1.text_input("CPF da Mãe")
    m_tel = col_m2.text_input("Telefone da Mãe")
    m_email = st.text_input("E-mail da Mãe")
    
    st.divider()
    
    st.subheader("Dados do Pai")
    p_nome = st.text_input("Nome do Pai")
    col_p1, col_p2 = st.columns(2)
    p_cpf = col_p1.text_input("CPF do Pai")
    p_tel = col_p2.text_input("Telefone do Pai")
    p_email = st.text_input("E-mail do Pai")

with tab3:
    st.subheader("Endereço Residencial")
    cep = st.text_input("CEP")
    rua = st.text_input("Rua/Avenida")
    col_end1, col_end2 = st.columns([1, 3])
    num = col_end1.text_input("Nº")
    bairro = col_end2.text_input("Bairro")

with tab4:
    st.subheader("Dados Escolares")
    esc_nome = st.text_input("Nome da Escola")
    esc_cnpj = st.text_input("CNPJ da Escola")
    esc_inep = st.text_input("INEP da Escola")

# BOTÃO DE SALVAR
if st.button("FINALIZAR CADASTRO", type="primary"):
    # Aqui vamos montar o JSON para enviar para a sua API no Render
    dados = {
        "nome_atleta": nome,
        "cpf_atleta": cpf,
        "data_nascimento": str(data_nasc),
        "sexo": sexo,
        "mae_nome": m_nome,
        "endereco_cep": cep
        # ... adicionar os outros campos aqui
    }
    
    st.success(f"Atleta {nome} cadastrado com sucesso!")
    # r = requests.post("SUA_URL_DO_RENDER/atletas/", json=dados)