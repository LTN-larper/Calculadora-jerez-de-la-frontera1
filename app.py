import streamlit as st

# 1. Configuración de la página
st.set_page_config(page_title="Salud 3º ESO", page_icon="🏥")

# Título y Descripción
st.title("💪 Calculadora de IMC")
st.markdown("Bienvenido. Introduce tus datos para calcular tu Índice de Masa Corporal.")
st.write("---") # Línea separadora

# 2. Entrada de Datos (Barra Lateral)
st.sidebar.header("Tus Datos")
peso = st.sidebar.number_input("Tu peso (kg)", min_value=0, max_value=200, value=60)
altura = st.sidebar.slider("Tu altura (metros)", 1.00, 2.30, 1.65)

# 3. Botón de Cálculo y Lógica
if st.button("Calcular ahora"):
    
    # Fórmula Matemática: Peso entre altura al cuadrado
    imc = peso / (altura ** 2)
    
    # 4. Mostrar Resultado con Diseño
    col1, col2 = st.columns(2)
    
    with col1:
        # Usamos metric para que el número se vea grande
        st.metric(label="Tu IMC es:", value=f"{imc:.2f}")
        
    with col2:
        # Usamos condicionales (if/elif/else) para el diagnóstico
        if imc < 18.5:
            st.warning("⚠️ Peso bajo")
            st.write("Consulta con un nutricionista.")
        elif 18.5 <= imc < 25:
            st.success("✅ Peso Saludable")
            st.balloons() # ¡Premio!
        elif 25 <= imc < 30:
            st.warning("🟠 Sobrepeso")
            st.write("Te recomendamos hacer ejercicio.")
        else:
            st.error("🔴 Obesidad")
            st.write("Es importante cuidar tu salud.")
            
    # Extra: Mostrar la fórmula usada (LaTeX)
    st.write("---")
    st.info("Fórmula matemática utilizada:")
    st.latex(r''' IMC = \frac{peso}{altura^2} ''')
6. Ejercicio Propuesto (Deberes)
Para demostrar que dominas la materia, debes crear y entregar el siguiente proyecto.

Nombre del Proyecto: 🛍️ "La Calculadora de Rebajas"

Escenario: Llegan las rebajas y es difícil calcular mentalmente cuánto se queda un producto. Crea una app que ayude a los compradores a saber el precio final rápidamente.

Requisitos Obligatorios:

Inputs: El usuario debe introducir:
El Precio Original (€) (usando number_input).

El Descuento (%) (usando slider de 0 a 100).

Cálculo: Debes programar la lógica matemática para hallar el precio final.

Visualización:

Usa st.metric para mostrar el Precio Final.

Usa st.success (caja verde) para mostrar cuánto dinero te ahorras en total.

Bonus (Nota extra): Si el descuento es mayor del 50%, debe salir un mensaje especial ("¡Menudo Chollo!") o una animación.

Ayuda con las fórmulas:

ahorro = precio_original * (descuento / 100)
precio_final = precio_original - ahorro
