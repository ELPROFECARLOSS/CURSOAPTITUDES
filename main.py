import streamlit as st
import pandas as pd
import io

st.set_page_config(page_title="Evaluación Diagnóstica", layout="centered")
st.title("🧮 Evaluación Diagnóstica - Cálculo Diferencial")

st.markdown("Por favor, completa tus datos antes de responder:")

# Datos del estudiante
nombre = st.text_input("🧑 Nombre completo")
num_cuenta = st.text_input("🆔 Número de cuenta")

# Validación de inicio
if not nombre or not num_cuenta:
    st.warning("⚠️ Por favor, ingresa tu nombre y número de cuenta antes de continuar.")
    st.stop()

puntuacion = 0
respuestas = []
respuestas_correctas = []

# Lista de preguntas
preguntas = [
    {
        "enunciado": "1. ¿Cuál es el resultado de: 5 - 7 + 12?",
        "opciones": ["a) 14", "b) 10", "c) 0", "d) No se/no recuerdo"],
        "correcta": "b) 10"
    },
    {
        "enunciado": "2. ¿Cuál es el resultado de: 3 - 5 + 1/2?",
        "opciones": ["a) -3/2", "b) 3/2", "c) 1", "d) No se/no recuerdo"],
        "correcta": "a) -3/2"
    },
    {
        "enunciado": "3. Resuelve: 1/2 + (1/3 + 1/2) - 3(1/2 + 1) - 5/2",
        "opciones": ["a) -6/29", "b) 29/6", "c) -29/6", "d) No se/no recuerdo"],
        "correcta": "c) -29/6"
    },
    {
        "enunciado": "4. Elige la forma reducida de: 4(x+2) + 2x",
        "opciones": ["a) 6x+8", "b) 6x-2", "c) 3x+2", "d) No se/no recuerdo"],
        "correcta": "a) 6x+8"
    },
    {
        "enunciado": "5. Reduce la siguiente expresión: (x^9 * x^-2 * x^8) / (x^6 * x^7)",
        "opciones": ["a) x^2", "b) x^9", "c) x^3", "d) No se/no recuerdo"],
        "correcta": "a) x^2"
    },
    {
        "enunciado": "6. ¿Cuál es el resultado de desarrollar: (x - 9)^2?",
        "opciones": ["a) x^2+18", "b) x^2+18x+81", "c) x^2-18x+81", "d) No se/no recuerdo"],
        "correcta": "c) x^2-18x+81"
    },
    {
        "enunciado": "7. ¿Cuál es el sistema de ecuaciones que representa la producción de mochilas?",
        "opciones": [
            "a. 3x + 2y = 60     2x + y = 40",
            "b. 3x + 2y = 40     2x + y = 60",
            "c. 3x + 2y = 60     2x + y = 40",
            "d. x + y = 100     x - y = 20"
        ],
        "correcta": "c. 3x + 2y = 60     2x + y = 40"
    },
    {
        "enunciado": "8. ¿Qué representa la variable X en el sistema planteado?",
        "opciones": [
            "A. El número total de mochilas.",
            "B. El número de mochilas tipo A.",
            "C. El número de metros de tela.",
            "D. No se/no recuerdo"
        ],
        "correcta": "B. El número de mochilas tipo A."
    },
    {
        "enunciado": "9. ¿Qué indica si el sistema tiene una única solución?",
        "opciones": [
            "A. Que hay múltiples combinaciones posibles.",
            "B. Que hay una combinación específica de mochilas A y B que satisface ambos recursos exactamente.",
            "C. Que no se pueden producir mochilas.",
            "D. No se/no recuerdo"
        ],
        "correcta": "B. Que hay una combinación específica de mochilas A y B que satisface ambos recursos exactamente."
    }
]

st.markdown("---")

# Recolectar respuestas
for i, p in enumerate(preguntas):
    st.markdown(f"**{p['enunciado']}**")
    seleccion = st.radio(
        label="Selecciona una opción:",
        options=p["opciones"],
        key=i
    )
    respuestas.append(seleccion)
    respuestas_correctas.append(p["correcta"])
    if seleccion == p["correcta"]:
        puntuacion += 1

# Mostrar resultado
if st.button("📊 Enviar respuestas"):
    st.success(f"✅ {nombre}, obtuviste **{puntuacion} de 9** respuestas correctas.")
    if puntuacion == 9:
        st.balloons()

    # Crear DataFrame con los resultados
    data = {
        "Nombre": [nombre],
        "Número de cuenta": [num_cuenta],
        "Puntuación": [puntuacion],
    }

    for i in range(len(preguntas)):
        data[f"R{i+1}"] = [respuestas[i]]
        data[f"R{i+1}_Correcta"] = [respuestas_correctas[i]]

    df = pd.DataFrame(data)

    # Convertir a CSV
    csv_buffer = io.StringIO()
    df.to_csv(csv_buffer, index=False)
    csv_bytes = csv_buffer.getvalue().encode()

    st.download_button(
        label="⬇️ Descargar resultados en CSV",
        data=csv_bytes,
        file_name=f"{nombre.replace(' ', '_')}_resultados.csv",
        mime="text/csv"
    )

