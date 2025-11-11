import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Título
st.title("Modelo de Rendimientos Crecientes y Decrecientes con Precios Medios")


def calcular_Q(x, L, K, l, k):
    return x * (L ** l) * (K ** k)

def calcular_costos_y_beneficios(Q, L, w, P):
    CT = w * L                   # Costo total
    CM = CT / Q                  # Costo medio
    IT = P * Q                   # Ingreso total
    Ganancia = IT - CT           # Ganancia total
    return CT, CM, IT, Ganancia


with st.sidebar.expander("Función de Producción"):
    x = st.number_input("Productividad total (x)", value=10.0)
    K = st.number_input("Capital (K)", value=10.0)
    L_max = st.number_input("Rango máximo de trabajo (L)", value=50.0)

with st.sidebar.expander("Elasticidad de la producción"):
    l = st.number_input("Elasticidad del trabajo (L^)", value=0.5)
    k = st.number_input("Elasticidad del capital (K^)", value=0.5)

with st.sidebar.expander("Precios y Costos"):
    w = st.number_input("Costo por trabajador (w)", value=100.0)
    P = st.number_input("Precio del producto (P)", value=50.0)

# --- CÁLCULOS ---
L_vals = np.linspace(1, L_max, 100)
Q_vals = calcular_Q(x, L_vals, K, l, k)
CT_vals, CM_vals, IT_vals, G_vals = calcular_costos_y_beneficios(Q_vals, L_vals, w, P)

# --- TABLA DE RESULTADOS ---
data = pd.DataFrame({
    'L': L_vals,
    'Producción (Q)': Q_vals,
    'Costo Total (CT)': CT_vals,
    'Costo Medio (CM)': CM_vals,
    'Ingreso Total (IT)': IT_vals,
    'Ganancia (IT - CT)': G_vals
})

st.subheader("Resultados numéricos")
st.dataframe(data.round(2))

# --- GRÁFICAS ---
st.subheader("Curvas de Producción, Costos y Ganancias")

fig, ax = plt.subplots(3, 1, figsize=(7, 12))

# Producción
ax[0].plot(L_vals, Q_vals, color='blue')
ax[0].set_title("Función de Producción")
ax[0].set_xlabel("Trabajo (L)")
ax[0].set_ylabel("Producción (Q)")
ax[0].grid(True)

# Costos Medios
ax[1].plot(L_vals, CM_vals, color='orange', label='Costo Medio (CM)')
ax[1].axhline(y=P, color='green', linestyle='--', label='Precio Medio (P)')
ax[1].set_title("Costo Medio vs Precio Medio")
ax[1].set_xlabel("Trabajo (L)")
ax[1].set_ylabel("Costo / Precio")
ax[1].legend()
ax[1].grid(True)

# Ganancia Total
ax[2].plot(L_vals, G_vals, color='purple')
ax[2].axhline(y=0, color='black', linestyle='--')
ax[2].set_title("Ganancia Total")
ax[2].set_xlabel("Trabajo (L)")
ax[2].set_ylabel("Ganancia (IT - CT)")
ax[2].grid(True)

st.pyplot(fig)


st.markdown("""
### Interpretación:
- Cuando la función de producción es **creciente**, la **productividad media aumenta** y el **costo medio baja**.
- En esa fase, si el **precio medio (P)** se mantiene, la **empresa gana más**.
- Cuando la función entra en fase **decreciente**, la **productividad baja**, el **costo medio sube** y las **ganancias disminuyen**.
""")
