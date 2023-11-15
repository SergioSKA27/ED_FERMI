import streamlit as st


st.set_page_config(layout="wide", page_title="Formulación del modelo", page_icon=":books:", initial_sidebar_state="collapsed")
st.title("Formulación del modelo")
st.divider()

r'''
El modelo se basa en ecuaciones diferenciales parciales que describen la probabilidad de transición de una partícula de
un estado a otro a lo largo del tiempo.
$$
\frac{d N(t)}{d t}=-\lambda N(t)
$$

Donde:
- $N(t)$ : Número de partículas en el tiempo $t$
- $\lambda$ : Tasa de desintegración

La ecuación describe cómo cambia el número de partículas a lo largo del tiempo debido a la desintegración.
La solución general de esta ecuación es:
$$
N(t)=N_0 e^{-\lambda t}
$$

Donde:
- $N_0$ : Número inicial de partículas en $t=0$
- $t$ : Tiempo

La ecuación (2) nos permite calcular el número de partículas en un momento posterior, dado el número inicial y la tasa de desintegración.

'''
