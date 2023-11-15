import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide", page_title="Diagrama Lotus Blossom", page_icon=":books:", initial_sidebar_state="collapsed")
st.title('Diagrama Lotus Blossom')
st.divider()
components.iframe("https://miro.com/app/embed/uXjVNRv-mOQ=/?pres=1&frameId=3458764569686990929&embedId=234084969186", width=1200, height=675, scrolling=True)


