import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

st.title("Modelo Interactivo de Funciones de Producción")




opcion = st.sidebar.selectbox(
    "Tipo de función de producción:",
    [
     "Cobb-Douglas: Q = A · K^a · L^b"]
)

with st.sidebar.expander("Parámetros de Producción"):
    K = st.number_input("Capital (K)", value=10.0, min_value=0.0)
    L = st.number_input("Trabajo (L)", value=5.0, min_value=0.0)

if opcion == "Cobb-Douglas: Q = A · K^a · L^b":
    with st.sidebar.expander("Parámetros Cobb-Douglas"):
        A = st.number_input("A (Eficiencia total)", value=1.0, min_value=0.0)
        a = st.number_input("Elasticidad del Capital (a)", value=0.5, min_value=0.0)
        b = st.number_input("Elasticidad del Trabajo (b)", value=0.5, min_value=0.0)


#  FUNCIONES


def produccion_cobb(A, K, L, a, b):
    return A * (K**a) * (L**b)

def pmgL_cobb(A, K, L, a, b):
    return A * b * (K**a) * (L**(b-1))

def pmgK_cobb(A, K, L, a, b):
    return A * a * (K**(a-1)) * (L**b)






#   COBB-DOUGLAS


if opcion == "Cobb-Douglas: Q = A · K^a · L^b":
    Q = produccion_cobb(A, K, L, a, b)
    PMg_L = pmgL_cobb(A, K, L, a, b)
    PMg_K = pmgK_cobb(A, K, L, a, b)
    PMe_L = Q / L if L != 0 else 0
    PMe_K = Q / K if K != 0 else 0

    st.subheader("Resultados de la Producción")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(label="Producción total (Q)", value=f"{Q:.4f}")

    with col2:
        st.metric(label="PMg del Trabajo (PMg_L)", value=f"{PMg_L:.4f}")

    with col3:
        st.metric(label="PMg del Capital (PMg_K)", value=f"{PMg_K:.4f}")

    col4, col5 = st.columns(2)

    with col4:
        st.metric(label="PMe del Trabajo (PMe_L)", value=f"{PMe_L:.4f}")

    with col5:
        st.metric(label="PMe del Capital (PMe_K)", value=f"{PMe_K:.4f}")

    # Rango para gráficas
    L_vals = np.linspace(1, 20, 100)
    Q_vals = produccion_cobb(A, K, L_vals, a, b)

    # Gráfica Q vs L
    fig1, ax1 = plt.subplots()
    ax1.plot(L_vals, Q_vals, label="Q(L)")
    ax1.set_xlabel("Trabajo (L)")
    ax1.set_ylabel("Producción (Q)")
    ax1.set_title("Producción Cobb-Douglas con K fijo")
    ax1.grid(True)
    st.pyplot(fig1)

    # PMg(L)
    PMg_curve = pmgL_cobb(A, K, L_vals, a, b)

    fig2, ax2 = plt.subplots()
    ax2.plot(L_vals, PMg_curve, color='orange')
    ax2.set_title("Producto Marginal del Trabajo (PMg_L)")
    ax2.set_xlabel("Trabajo (L)")
    ax2.set_ylabel("PMg_L")
    ax2.grid(True)
    st.pyplot(fig2)

    # PMe(L)
    PMe_curve = Q_vals / L_vals

    fig3, ax3 = plt.subplots()
    ax3.plot(L_vals, PMe_curve, color='green')
    ax3.set_title("Producto Medio del Trabajo (PMe_L)")
    ax3.set_xlabel("Trabajo (L)")
    ax3.set_ylabel("PMe_L")
    ax3.grid(True)
    st.pyplot(fig3)

    # 3D Cobb-Douglas
    K_vals = np.linspace(1, 20, 40)
    L_vals2 = np.linspace(1, 20, 40)
    K_mesh, L_mesh = np.meshgrid(K_vals, L_vals2)
    Q_mesh = produccion_cobb(A, K_mesh, L_mesh, a, b)

    fig4 = plt.figure(figsize=(8, 6))
    ax4 = fig4.add_subplot(111, projection="3d")
    ax4.plot_surface(K_mesh, L_mesh, Q_mesh, cmap='viridis', alpha=0.9)
    ax4.set_title("Superficie 3D – Función Cobb-Douglas")
    ax4.set_xlabel("K")
    ax4.set_ylabel("L")
    ax4.set_zlabel("Q")
    st.pyplot(fig4)


    