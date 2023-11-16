import streamlit as st
import graphviz
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
