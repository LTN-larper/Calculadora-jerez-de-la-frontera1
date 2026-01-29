import streamlit as st

# 1. Configuración y Título
st.set_page_config(page_title="Salud 3º ESO", page_icon="🏥")
st.title("💪 Calculadora de IMC")
st.markdown("Introduce tus datos para calcular tu Índice de Masa Corporal.")

# 2. Entrada de Datos (En la barra lateral)
st.sidebar.header("Tus Datos")
peso = st.sidebar.number_input("Tu peso (kg)", min_value=0, max_value=200, value=60)
altura = st.sidebar.slider("Tu altura (metros)", 1.00, 2.30, 1.65)

# 3. Botón de Cálculo
if st.button("Calcular ahora"):
    
    # 4. Lógica Matemática
    imc = peso / (altura ** 2)
    
    # 5. Mostrar Resultado con ESTILO
    col1, col2 = st.columns(2)
    
    with col1:
        # Usamos metric para que el número se vea grande e importante
        st.metric(label="Tu IMC es:", value=f"{imc:.2f}")
        
    with col2:
        # Usamos condicionales y colores para el diagnóstico
        if imc < 18.5:
            st.warning("⚠️ Peso bajo")
            st.write("Consulta con un nutricionista.")
        elif 18.5 <= imc < 25:
            st.success("✅ Peso Saludable")
            st.balloons() # ¡Premio!
        elif 25 <= imc < 30:
            st.warning("🟠 Sobrepeso")
        else:
            st.error("🔴 Obesidad")
            st.write("Es importante cuidar tu salud.")
            
    # Extra: Fórmula matemática
    st.write("---")
    st.info("Fórmula utilizada:")
    st.latex(r''' IMC = \frac{peso}{altura^2} ''')
