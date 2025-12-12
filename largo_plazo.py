import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Costo Medio de Largo Plazo – Gráfica 6")

# ===========================================
#       SIDEBAR EXPANDER (ACOMODO EXACTO)
# ===========================================

with st.sidebar.expander("Parámetros de la gráfica"):

    st.subheader("CM1")
    a1 = st.number_input("a₁ (nivel CM1)", value=120.0)
    b1 = st.number_input("b₁ (pendiente CM1)", value=9)
    tp1 = st.number_input("TP1 (posición)", value=30)
    p1 = st.number_input("P1 (precio)", value=60)

    st.subheader("CM2")
    a2 = st.number_input("a₂ (nivel CM2)", value=90.0)
    b2 = st.number_input("b₂ (pendiente CM2)", value=6)
    tp2 = st.number_input("TP2 (posición)", value=70)
    p2 = st.number_input("P2 (precio)", value=40)

    st.subheader("CM3")
    a3 = st.number_input("a₃ (nivel CM3)", value=70.0)
    b3 = st.number_input("b₃ (pendiente CM3)", value=0.8)
    tp3 = st.number_input("TP3 (posición)", value=110)
    p3 = st.number_input("P3 (precio)", value=20)

    Qmax = st.number_input("Máximo del eje X", value=120)

# ===========================================
#            ECUACIONES DE COSTO MEDIO
# ===========================================

q = np.linspace(1, Qmax, 400)

CM1 = a1 / q + b1
CM2 = a2 / q + b2
CM3 = a3 / q + b3

# Costo medio de largo plazo (envolvente)
CMLP = np.minimum.reduce([CM1, CM2, CM3])

# ===========================================
#                  GRÁFICA
# ===========================================

fig, ax = plt.subplots(figsize=(10, 6))

# Curvas de costo medio
ax.plot(q, CM1, linewidth=3, color="black")
ax.text(tp1 + 2, CM1.min() + 20, "CM1", fontsize=12)

ax.plot(q, CM2, linewidth=3, color="black")
ax.text(tp2 + 2, CM2.min() + 15, "CM2", fontsize=12)

ax.plot(q, CM3, linewidth=3, color="black")
ax.text(tp3 + 2, CM3.min() + 10, "CM3", fontsize=12)

# Curva de largo plazo
ax.plot(q, CMLP, linewidth=4, color="black")

# Líneas verticales TP
ax.axvline(tp1, linestyle="--", color="black")
ax.axvline(tp2, linestyle="--", color="black")
ax.axvline(tp3, linestyle="--", color="black")

# Líneas horizontales de precio
ax.hlines(p1, tp1 - 10, tp1 + 10, color="black", linewidth=3)
ax.text(tp1, p1 + 3, "P1", fontsize=12)

ax.hlines(p2, tp2 - 10, tp2 + 10, color="black", linewidth=3)
ax.text(tp2, p2 + 3, "P2", fontsize=12)

ax.hlines(p3, tp3 - 10, tp3 + 10, color="black", linewidth=3)
ax.text(tp3, p3 + 3, "P3", fontsize=12)

ax.set_xlabel("Cantidad")
ax.set_ylabel("Precios, valores, costos")
ax.set_title("Costo Medio de Largo Plazo – Técnicas TP1, TP2, TP3")

ax.set_xlim(0, Qmax * 1)
ax.set_ylim(min(CM3) * 0.95, max(CM1) * .8)


st.pyplot(fig)
