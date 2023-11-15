import streamlit as st
import streamlit.components.v1 as components


st.set_page_config(layout="wide", page_title="Infografía", page_icon=":books:", initial_sidebar_state="collapsed")

st.title("Infografía")


st.markdown(r'''
<div style="position: relative; width: 100%; height: 0; padding-top: 250.0000%;
 padding-bottom: 0; box-shadow: 0 2px 8px 0 rgba(63,69,81,0.16); margin-top: 1.6em; margin-bottom: 0.9em; overflow: hidden;
 border-radius: 8px; will-change: transform;">
  <iframe loading="lazy" style="position: absolute; width: 100%; height: 100%; top: 0; left: 0; border: none; padding: 0;margin: 0;"
    src="https:&#x2F;&#x2F;www.canva.com&#x2F;design&#x2F;DAF0IU9az4E&#x2F;view?embed" allowfullscreen="allowfullscreen" allow="fullscreen">
  </iframe>
</div>
<a href="https:&#x2F;&#x2F;www.canva.com&#x2F;design&#x2F;DAF0IU9az4E&#x2F;view?utm_content=DAF0IU9az4E&amp;utm_campaign=designshare&amp;utm_medium=embeds&amp;utm_source=link" target="_blank" rel="noopener">INFOGRAFIAFERMI</a> de Sergio Lopez

''', unsafe_allow_html=True)

#components.iframe("https:&#x2F;&#x2F;www.canva.com&#x2F;design&#x2F;DAF0IU9az4E&#x2F;view?embed", width=700, height=1000, scrolling=True)
