import streamlit as st
import streamlit.components.v1 as components


st.set_page_config(layout="wide", page_title="Infografía", page_icon=":books:", initial_sidebar_state="collapsed")

st.title("Infografía")

components.iframe("https:&#x2F;&#x2F;www.canva.com&#x2F;design&#x2F;DAF0IU9az4E&#x2F;view?embed", width=700, height=1000, scrolling=True)
