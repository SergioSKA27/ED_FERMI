import streamlit as st
import streamlit.components.v1 as components
#No sirve:(
st.set_page_config(layout="wide", page_title="Lluvia de ideas", page_icon=":books:", initial_sidebar_state="collapsed")

components.iframe("https://mm.tt/app/map/3027982220?t=3q6Lb9FeER", width=1200, height=675, scrolling=True)
