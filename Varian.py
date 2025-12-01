import streamlit as st
import numpy as np
import matplotlib.pyplot as plt



# ESTILO GLOBAL VARIAN

def estilo_varian():
    plt.rcParams['axes.edgecolor'] = 'black'
    plt.rcParams['axes.linewidth'] = 1.2
    plt.rcParams['font.size'] = 14
    plt.rcParams['font.family'] = 'serif'
    plt.rcParams['figure.figsize'] = (6, 4)
    plt.rcParams['axes.grid'] = False


st.title("Gráficas Capítulos 16–19 (Varian)")



# 1) FUNCIÓN DE PRODUCCIÓN


st.header("1. Función de Producción ")
estilo_varian()

with st.sidebar.expander("Parámetros Gráfica 1"):
    A = st.number_input("A (Productividad total)", value=10.0)
    b = st.number_input("b (Elasticidad)", value=0.6)
    Lmax = st.slider("Máximo de L", 10, 50, 20)

L = np.linspace(0, Lmax, 200)
Y = A * (L ** b)

fig1, ax1 = plt.subplots()
ax1.plot(L, Y, color="black")
ax1.set_xlabel("Trabajo (L)")
ax1.set_ylabel("Producto (Y)")
ax1.spines["right"].set_visible(False)
ax1.spines["top"].set_visible(False)
st.pyplot(fig1)




# 2) DEMANDA DE TRABAJO – VPM (Gráfica 6)


st.header("2. Demanda de trabajo  – Gráfica 6")
estilo_varian()

with st.sidebar.expander("Parámetros Gráfica 2"):
    m = st.number_input("Pendiente (negativa)", value=-0.6)
    b1 = st.number_input("Intercepto VPM1", value=18.0)
    b2 = st.number_input("Intercepto VPM2", value=16.0)
    W1 = st.number_input("Salario W1", value=12.0)
    W2 = st.number_input("Salario W2", value=8.0)
    Lmax2 = st.slider("Máximo del eje de empleo", 10, 50, 25)

L = np.linspace(0, Lmax2, 200)
VPM1 = m * L + b1
VPM2 = m * L + b2

E1 = (b1 - W1) / (-m)
E2 = (b2 - W2) / (-m)

fig2, ax2 = plt.subplots()
ax2.plot(L, VPM1, linewidth=1.4, color="black")
ax2.plot(L, VPM2, linewidth=1.4, color="black")

ax2.axhline(W1, color="black")
ax2.axhline(W2, color="black")
ax2.vlines(E1, 0, W1, color="black")
ax2.vlines(E2, 0, W2, color="black")

ax2.text(0.5, W1+0.3, "W1")
ax2.text(0.5, W2+0.3, "W2")
ax2.text(E1, -0.7, "E1", ha="center")
ax2.text(E2, -0.7, "E2", ha="center")
ax2.set_xlabel("Empleo")
ax2.set_ylabel("Salario")
ax2.spines["top"].set_visible(False)
ax2.spines["right"].set_visible(False)
st.pyplot(fig2)




# 3) CFM


st.header("3. Gráfica 7 – Costo Fijo Medio")
estilo_varian()

with st.sidebar.expander("Parámetros Gráfica 3"):
    CF = st.number_input("Costo Fijo (CF)", value=200.0)
    ymax = st.slider("Máximo de y", 20, 200, 50)

y = np.linspace(1, ymax, 200)
CFM = CF / y

fig3, ax3 = plt.subplots()
ax3.plot(y, CFM, color="black")
ax3.text(y[-1], CFM[-1], "CFM")
ax3.set_xlabel("y")
ax3.set_ylabel("CFM")
ax3.spines["top"].set_visible(False)
ax3.spines["right"].set_visible(False)
st.pyplot(fig3)




# 4) CVM – Máxima capacidad


st.header("4. Gráfica 8 – CVM con Máxima Capacidad")
estilo_varian()

with st.sidebar.expander("Parámetros Gráfica 4"):
    costo_base = st.number_input("Costo base", value=20.0)
    capacidad = st.slider("Máxima Capacidad", 10, 80, 40)
    potencia = st.slider("Exponente", 1, 3, 2)

y = np.linspace(1, 60, 300)
CVM = np.piecewise(
    y,
    [y < capacidad, y >= capacidad],
    [
        lambda y: costo_base * np.ones_like(y),
        lambda y: costo_base + 0.5 * (y - capacidad)**potencia
    ]
)

fig4, ax4 = plt.subplots()
ax4.plot(y, CVM, color="black")
ax4.axvline(capacidad, color="black")
ax4.text(capacidad+1, costo_base-1, "Máxima\ncapacidad")
ax4.set_xlabel("y")
ax4.set_ylabel("CVM")
ax4.spines["top"].set_visible(False)
ax4.spines["right"].set_visible(False)
st.pyplot(fig4)




# 5) CVMe (U)


st.header("5. Gráfica 9 – CVMe")
estilo_varian()

with st.sidebar.expander("Parámetros Gráfica 5"):
    a = st.number_input("Constante base", value=8.0)
    c = st.number_input("Pendiente cuadrática", value=0.015)

y = np.linspace(1, 60, 300)
CVMe = a + c * (y - 20)**2

fig5, ax5 = plt.subplots()
ax5.plot(y, CVMe, color="black")
ax5.text(55, CVMe[-1], "CVMe")
ax5.set_xlabel("y")
ax5.set_ylabel("CMe")
ax5.spines["top"].set_visible(False)
ax5.spines["right"].set_visible(False)
st.pyplot(fig5)




# 6) CMe – U pronunciada


st.header("6. Gráfica 10 – CMe (Curva en U)")
estilo_varian()

with st.sidebar.expander("Parámetros Gráfica 6"):
    c0 = st.number_input("Nivel base", value=10.0)
    c2 = st.number_input("Coeficiente cuadrático", value=0.02)

y = np.linspace(1, 60, 300)
CMe = c0 + c2*(y - 30)**2

fig6, ax6 = plt.subplots()
ax6.plot(y, CMe, color="black")
ax6.text(55, CMe[-1], "CMe")
ax6.set_xlabel("y")
ax6.set_ylabel("CMe")
ax6.spines["top"].set_visible(False)
ax6.spines["right"].set_visible(False)
st.pyplot(fig6)




# 7) CM + CVMe (Gráfica 11)


st.header("7. Gráfica 11 – CM y CVMe")
estilo_varian()

with st.sidebar.expander("Parámetros Gráfica 7"):
    cCM = st.number_input("CM — parámetro cuadrático", value=0.015)
    cCV = st.number_input("CVMe — parámetro cuadrático", value=0.008)
    shift_CM = st.number_input("Desplazamiento CM", value=28)
    shift_CV = st.number_input("Desplazamiento CVMe", value=38)

y = np.linspace(1, 60, 300)
CM = cCM*(y - shift_CM)**2 + 8
CVMe = cCV*(y - shift_CV)**2 + 9

fig7, ax7 = plt.subplots()
ax7.plot(y, CM, color="black")
ax7.plot(y, CVMe, color="black")
ax7.text(40, CM[200], "CM")
ax7.text(48, CVMe[-1], "CVMe")

ax7.set_xlabel("y")
ax7.set_ylabel("Costos")
ax7.spines["top"].set_visible(False)
ax7.spines["right"].set_visible(False)
st.pyplot(fig7)


