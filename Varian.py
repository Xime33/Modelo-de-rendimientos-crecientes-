import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Gráficas Capítulos 16–19 (Varian)")


# FUNCIÓN DE PRODUCCIÓN


st.header("1. Función de producción (Cap. 16)")

L = np.linspace(0, 20, 200)
A = 10
b = 0.6   # rendimientos decrecientes
Y = A * (L ** b)

fig1, ax1 = plt.subplots()
ax1.plot(L, Y, linewidth=2)
ax1.set_xlabel("Trabajo (L)")
ax1.set_ylabel("Producto (Y)")
ax1.set_title("Función de Producción – Producto Total")
ax1.grid(True)

st.pyplot(fig1)


# DEMANDA DE TRABAJO – VPM


st.header("2. Demanda de trabajo (Cap. 17) – VPM y salario")

L = np.linspace(1, 20, 200)
precio = 10

PMg1 = 15 / L          # productividad marginal "alta"
PMg2 = 10 / L          # productividad marginal más baja
VPM1 = precio * PMg1
VPM2 = precio * PMg2

W1 = 25
W2 = 10

fig2, ax2 = plt.subplots()
ax2.plot(L, VPM1, label="VPM1", linewidth=2)
ax2.plot(L, VPM2, label="VPM2", linewidth=2)
ax2.axhline(W1, color="gray", linestyle="--", label="W1")
ax2.axhline(W2, color="black", linestyle="--", label="W2")
ax2.set_xlabel("Empleo")
ax2.set_ylabel("Salario / VPM")
ax2.set_title("Demanda de trabajo según VPM")
ax2.legend()
ax2.grid(True)

st.pyplot(fig2)


# COSTO FIJO MEDIO – CFM


st.header("3. Costo Fijo Medio – Gráfica 7")

y = np.linspace(1, 50, 200)
F = 200
CFM = F / y

fig3, ax3 = plt.subplots()
ax3.plot(y, CFM, linewidth=2)
ax3.set_xlabel("Producción (y)")
ax3.set_ylabel("CFM")
ax3.set_title("Costo Fijo Medio")
ax3.grid(True)

st.pyplot(fig3)


# CVM con capacidad máxima – Gráfica 8


st.header("4. Costo Variable Medio con capacidad máxima – Gráfica 8")

y = np.linspace(1, 50, 200)
CVM = np.piecewise(
    y,
    [y < 30, y >= 30],
    [lambda y: 20*np.ones_like(y), 
     lambda y: 20 + 2*(y - 30) ** 2]
)

fig4, ax4 = plt.subplots()
ax4.plot(y, CVM, linewidth=2)
ax4.axvline(30, color="black", linestyle="--")
ax4.text(30, 22, "Máxima capacidad", rotation=90)
ax4.set_xlabel("y")
ax4.set_ylabel("CVM")
ax4.set_title("Costo Variable Medio con capacidad máxima")
ax4.grid(True)

st.pyplot(fig4)


#  CVMe tradicional – Gráfica 9


st.header("5. CVMe tradicional – Gráfica 9")

y = np.linspace(1, 50, 200)
CVMe = 0.02*(y-20)**2 + 10

fig5, ax5 = plt.subplots()
ax5.plot(y, CVMe, linewidth=2)
ax5.set_xlabel("y")
ax5.set_ylabel("CVMe")
ax5.set_title("Costo Variable Medio (forma de U)")
ax5.grid(True)

st.pyplot(fig5)


#  Costo Medio – Gráfica 10


st.header("6. Costo Medio – Gráfica 10")

CMe = 0.02*(y-20)**2 + 15

fig6, ax6 = plt.subplots()
ax6.plot(y, CMe, linewidth=2)
ax6.set_xlabel("y")
ax6.set_ylabel("CMe")
ax6.set_title("Costo Medio con forma de U")
ax6.grid(True)

st.pyplot(fig6)


# 7) CM + CVMe – Gráfica 11


st.header("7. Costo Medio (CM) y Costo Variable Medio (CVMe) – Gráfica 11")

CMe2 = 0.02*(y-20)**2 + 15
CVMe2 = 0.03*(y-20)**2 + 10

fig7, ax7 = plt.subplots()
ax7.plot(y, CMe2, label="CM", linewidth=2)
ax7.plot(y, CVMe2, label="CVMe", linewidth=2)
ax7.set_xlabel("y")
ax7.set_ylabel("Coste")
ax7.set_title("CM y CVMe (Gráfica 11)")
ax7.legend()
ax7.grid(True)

st.pyplot(fig7)
