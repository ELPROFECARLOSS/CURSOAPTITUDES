import streamlit as st
import pandas as pd
import io

st.set_page_config(page_title="Examen Diagnóstico - Cálculo Diferencial", layout="centered")

# Título principal
st.title("📘 EXAMEN DE DIAGNÓSTICO DE LA MATERIA CÁLCULO DIFERENCIAL")

# Integrantes del equipo de desarrollo
st.markdown("""
**Desarrollado por:**
- LINDALVA PONCE IBARRA  
- FABIOLA MARQUEZ BELTRAN  
- HECTOR FERNANDO FLORES CASILLAS  
- JOSE DEL CARMEN ARECHIGA MARAVILLAS  
- RICARDO OLIVERA GUERRERO  
- CARLOS ADOLFO HERNANDEZ GUTIERREZ
""")

# Datos del estudiante
st.markdown("### 🧑 Datos del estudiante")
nombre = st.text_input("Nombre completo")
num_cuenta = st.text_input("Número de cuenta")

if not nombre or not num_cuenta:
    st.warning("⚠️ Por favor, ingresa tu nombre y número de cuenta antes de continuar.")
    st.stop()

puntuacion = 0
respuestas = []
respuestas_correctas = []

# Preguntas
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
]

# Presentación de preguntas 1-6
st.markdown("---")
for i, p in enumerate(preguntas):
    st.markdown(f"**{p['enunciado']}**")
    seleccion = st.radio(
        label="Selecciona una opción:",
        options=p["opciones"],
        key=f"preg{i}"
    )
    respuestas.append(seleccion)
    respuestas_correctas.append(p["correcta"])
    if seleccion == p["correcta"]:
        puntuacion += 1

# 👉 Contexto para preguntas 7 a 9
st.markdown("---")
st.markdown("### Contexto para las preguntas 7 a 9")

st.info("""
Una empresa produce dos tipos de mochilas: Mochila A y Mochila B.  
Para su elaboración, se requieren dos tipos de materiales: **tela** y **cierres**.

- Cada **Mochila A** necesita **3 metros de tela** y **2 cierres**.  
- Cada **Mochila B** necesita **2 metros de tela** y **1 cierre**.  
- La empresa dispone de **60 metros de tela** y **40 cierres** en total.  

Con esta información, se desea saber cuántas mochilas de cada tipo se pueden producir sin exceder los recursos disponibles.
""")

preguntas_finales = [
    {
        "enunciado": "7. ¿Cuál es el sistema de ecuaciones que representa esta situación?",
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

for i, p in enumerate(preguntas_finales, start=6):
    st.markdown(f"**{p['enunciado']}**")
    seleccion = st.radio(
        label="Selecciona una opción:",
        options=p["opciones"],
        key=f"preg{i}"
    )
    respuestas.append(seleccion)
    respuestas_correctas.append(p["correcta"])
    if seleccion == p["correcta"]:
        puntuacion += 1

# Resultado y descarga
if st.button("📊 Enviar respuestas"):
    st.success(f"✅ {nombre}, obtuviste **{puntuacion} de 9** respuestas correctas.")
    if puntuacion == 9:
        st.balloons()

    # Crear DataFrame
    data = {
        "Nombre": [nombre],
        "Número de cuenta": [num_cuenta],
        "Puntuación": [puntuacion],
    }

    for i in range(len(respuestas)):
        data[f"R{i+1}"] = [respuestas[i]]
        data[f"R{i+1}_Correcta"] = [respuestas_correctas[i]]

    df = pd.DataFrame(data)

    # CSV descargable
    csv_buffer = io.StringIO()
    df.to_csv(csv_buffer, index=False)
    csv_bytes = csv_buffer.getvalue().encode()

    st.download_button(
        label="⬇️ Descargar resultados en CSV",
        data=csv_bytes,
        file_name=f"{nombre.replace(' ', '_')}_resultado.csv",
        mime="text/csv"
    )
