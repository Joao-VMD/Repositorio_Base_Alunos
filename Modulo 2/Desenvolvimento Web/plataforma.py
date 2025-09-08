import streamlit as st
import calculoimc as imc


st.title("Elite Life 😎")
st.caption("Feito com paciencia")
st.write("Bem Vindo")

with st.form("formulario_imc"):
    peso = st.number_input("peso em kg:", min_value=0.0,max_value=300.0)
    altura = st.number_input("Altura em metros:",min_value=0.1,max_value=4.0)

    calcular= st.form_submit_button("Calcular")

if calcular:
    valor_imc = imc.calculo_imc(peso=peso,altura=altura)
    categoria,status = imc.tabela_imc(valor_imc)
    st.progress(min(valor_imc/40,1.0))

    if status == "success":
        st.success(f"{valor_imc:.2f}")
    elif status == "info":
        st.info(f"{valor_imc:.2f}")
    elif status == "warning":
        st.warning(f"{valor_imc:.2f}")
    else:
        st.error(f"{valor_imc:.2f}")

    # st.success(f"{valor_imc}\n{msg}")
    








# with st.sidebar:
#     st.subheader("Programas")
