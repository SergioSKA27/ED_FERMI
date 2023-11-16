import streamlit as st
import graphviz
st.title("Diagrama de Nodos y Rutas")
st.divider()
st.graphviz_chart('''digraph {
  Modelo -> BetaNegativa
  Modelo -> BetaPositiva
  BetaNegativa -> InicioNegativa
  BetaNegativa -> ConservacionNegativa
  BetaNegativa -> VerificacionNegativa
  BetaPositiva -> InicioPositiva
  BetaPositiva -> ConservacionPositiva
  BetaPositiva -> VerificacionPositiva
  Modelo -> Congruencia
}''')
