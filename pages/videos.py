import streamlit as st
import streamlit.components.v1 as components

#<div style="width: 100%;"><div style="position: relative; padding-bottom: 56.25%; padding-top: 0; height: 0;"><iframe title="FERMI" frameborder="0" width="1200" height="675" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;" src="https://view.genial.ly/65515eb911fd730011cbe8d6" type="text/html" allowscriptaccess="always" allowfullscreen="true" scrolling="yes" allownetworking="all"></iframe> </div> </div>

st.set_page_config(layout="wide", page_title="Presentación", page_icon=":books:", initial_sidebar_state="collapsed")
st.title("Presentación")
st.divider()
components.iframe("https://view.genial.ly/65515eb911fd730011cbe8d6", width=1200, height=675, scrolling=True)

st.header("Video")
st.divider()
st.video("https://youtu.be/FGQXE5UiCc4")
