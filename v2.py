import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

st.title("Modelo de Rendimientos Crecientes, Decrecientes y Producción Exponencial")


def calcular_Q(x, L, K, l, k):
    return x * (L ** l) * (K ** k)

def calcular_costos(Q, L, costo_insumo):
    costo_total = costo_insumo * L
    costo_medio = np.divide(costo_total, Q, out=np.zeros_like(costo_total), where=Q!=0)
    return costo_total, costo_medio

def calcular_exponencial(x, L, K, beta):
    return x * np.exp(beta * L) * K



with st.sidebar.expander("Parámetros de Producción"):
    x = st.number_input("x (Productividad total)", value=10.0)
    L_max = st.number_input("L (Trabajo máximo)", value=20.0)
    K = st.number_input("K (Capital)", value=10.0)

with st.sidebar.expander("Elasticidades"):
    l_crec = st.number_input("Elasticidad del trabajo (Creciente)", value=1.2)
    l_decr = st.number_input("Elasticidad del trabajo (Decreciente)", value=0.5)
    k = st.number_input("Elasticidad del capital (K^)", value=0.5)
    beta = st.number_input("Parámetro exponencial β", value=0.15)

with st.sidebar.expander("Costos e ingresos"):
    costo_insumo = st.number_input("Costo por unidad de trabajo (w)", value=100.0)
    precio = st.number_input("Precio del producto (P)", value=50.0)

L_vals = np.linspace(1, L_max, 50)

# Producción decreciente
Q_decr = calcular_Q(x, L_vals, K, l_decr, k)

# Producción creciente
Q_crec = calcular_Q(x, L_vals, K, l_crec, k)

# Producción exponencial
Q_exp = calcular_exponencial(x, L_vals, K, beta)

# Costos para el caso creciente
CT_vals, CM_vals = calcular_costos(Q_crec, L_vals, costo_insumo)
IT_vals = Q_crec * precio


data = pd.DataFrame({
    "Trabajo (L)": L_vals,
    "Producción Creciente (Q)": Q_crec,
    "Producción Decreciente (Q)": Q_decr,
    "Producción Exponencial (Q)": Q_exp,
    "Costo Total (w·L)": CT_vals,
    "Costo Medio (CT/Q)": CM_vals,
    "Ingreso Total (P·Q)": IT_vals,
    "Ganancia (IT - CT)": IT_vals - CT_vals
})

# Producto Marginal del Trabajo (PM_L) para el caso creciente
PM_L = x * l_crec * (L_vals ** (l_crec - 1)) * (K ** k)

# Costo Marginal (CMg)
CMg_vals = np.divide(costo_insumo, PM_L, out=np.zeros_like(PM_L), where=PM_L!=0)

# Agregar al DataFrame
data["Producto Marginal del Trabajo (PM_L)"] = PM_L
data["Costo Marginal (CMg)"] = CMg_vals

st.subheader("📊 Tabla de Resultados")
st.dataframe(data.round(2))

#decreciente
fig1, ax1 = plt.subplots()
ax1.plot(L_vals, Q_decr, color='red', label="Rendimientos Decrecientes")
ax1.set_xlabel('Trabajo (L)')
ax1.set_ylabel('Producción (Q)')
ax1.set_title('Función de Producción con Rendimientos Decrecientes')
ax1.legend()
ax1.grid(True)
st.pyplot(fig1)

#creciente
fig2, ax2 = plt.subplots()
ax2.plot(L_vals, Q_crec, color='green', label="Rendimientos Crecientes")
ax2.set_xlabel('Trabajo (L)')
ax2.set_ylabel('Producción (Q)')
ax2.set_title('Función de Producción con Rendimientos Crecientes')
ax2.legend()
ax2.grid(True)
st.pyplot(fig2)

#Costo Medio vs Precio del Producto
fig3, ax3 = plt.subplots()
ax3.plot(L_vals, CM_vals, color='orange', label='Costo Medio (CT/Q)')
ax3.axhline(y=precio, color='blue', linestyle='--', label='Precio del Producto (P)')
ax3.fill_between(L_vals, CM_vals, precio, where=CM_vals<precio, color='green', alpha=0.2, label="Beneficio")
ax3.fill_between(L_vals, CM_vals, precio, where=CM_vals>precio, color='red', alpha=0.2, label="Pérdida")
ax3.set_xlabel('Trabajo (L)')
ax3.set_ylabel('Costo / Precio')
ax3.set_title('Costo Medio vs Precio del Producto')
ax3.legend()
ax3.grid(True)
st.pyplot(fig3)

#exponencial
fig4, ax4 = plt.subplots()
ax4.plot(L_vals, Q_exp, color='purple', label=f"Producción Exponencial (β = {beta})")
ax4.set_xlabel('Trabajo (L)')
ax4.set_ylabel('Producción (Q)')
ax4.set_title('Crecimiento Exponencial de la Producción respecto al Trabajo')
ax4.legend()
ax4.grid(True)
st.pyplot(fig4)


# Costo Marginal y Costo Medio
fig5, ax5 = plt.subplots()
ax5.plot(L_vals, CM_vals, color='orange', label='Costo Medio (CT/Q)')
ax5.plot(L_vals, CMg_vals, color='blue', linestyle='--', label='Costo Marginal (w/PM_L)')
ax5.set_xlabel('Trabajo (L)')
ax5.set_ylabel('Costo')
ax5.set_title('Costo Medio y Costo Marginal')
ax5.legend()
ax5.grid(True)
st.pyplot(fig5)


st.markdown("""
### 
# Interpretación Económica:
1. **Rendimientos Decrecientes:**  
   Cuando el exponente del trabajo (L^) es menor que 1, cada unidad adicional de trabajo genera menos producción que la anterior.  
   Esto ocurre, por ejemplo, cuando la capacidad del capital no crece al mismo ritmo que el trabajo.

2. **Rendimientos Crecientes:**  
   Cuando L^ es mayor que 1, cada unidad adicional de trabajo aumenta la producción de forma acelerada.  
   Suele reflejar mejoras tecnológicas o alta complementariedad entre los factores.

3. **Costo Medio vs Precio:**  
   Si el costo medio (CT/Q) está por debajo del precio del producto (P), la empresa obtiene beneficios.  
   Si está por encima, hay pérdidas o ineficiencia.

4. **Producción Exponencial:**  
   Representa un crecimiento acelerado de la producción en función del trabajo, donde un cambio pequeño en L genera aumentos multiplicativos en Q.
""")
