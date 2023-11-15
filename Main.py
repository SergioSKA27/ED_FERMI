import streamlit as st
from st_pages import Page, show_pages, add_page_title
import base64

# Optional -- adds the title and icon to the current page
#add_page_title()
st.set_page_config(layout="wide", page_title="Desintegración de Partículas", page_icon=":books:", initial_sidebar_state="collapsed")
# Specify what pages should be shown in the sidebar, and what their titles and icons
# should be
show_pages(
    [
        Page("Main.py", "Inicio", "🏠"),
        Page("pages/Modeldesc1.py", "1. Descripción del modelo", ":books:"),
        Page("pages/DocDef.py", "2. Definiciones documentadas",":books:" ),
        Page('pages/MindMap.py',"3. Lluvia de ideas",":books:" ),
        Page("pages/Lotus.py", "4. Diagrama Lotus Blossom", ":books:"),
        Page("pages/IshikawaD.py", "5. Diagrama Ishikawa", ":books:"),
        Page("pages/Contexto.py","6. Contexto del modelo",":books:" ),
        Page("pages/Utilidad.py","7. Utilidad del modelo",":books:" ),
        Page("pages/formulacion.py","8. Formulación del modelo",":books:" ),
        Page("pages/preguntas.py","9. Respuesta a las preguntas",":books:" ),
        Page("pages/nodosyrutas.py","10. Nodos y rutas",":books:" ),
        Page("pages/Infografia.py","11. Infografía",":books:" ),
        Page("pages/actualtec.py","12. Relación del modelo con la tecnología actual",":books:" ),
        Page("pages/conclusiones.py","13. Conclusiones",":books:" ),
        Page("pages/videos.py","14. Video y Presentación",":books:" ),
        Page("pages/referencias.py","15. Referencias",":books:" ),


    ]
)

st.title("Inicio :house:")
st.header("Desintegración de Partículas y el Modelo de Fermi.")
cols = st.columns(2)
with cols[0]:
    st.write("Integrantes:")
    st.write("Escalante Leon Diego Armando")
    st.write("Fernández Castañeda Alexia")
    st.write("López Martinez Sergio Demis")

with cols[1]:
    st.write("Grupo:")
    st.write("")
    st.write("Profesor:")
    st.write("")

st.divider()
'''
La desintegración beta es un fenómeno nuclear fascinante que ha sido objeto de estudio durante décadas.

Este proceso, que implica la emisión de partículas beta y neutrinos de un núcleo atómico inestable, es un ejemplo de la
interacción débil, una de las cuatro fuerzas fundamentales de la naturaleza. A través del estudio de la desintegración
beta, los científicos han podido desentrañar muchos de los misterios de las partículas subatómicas y las fuerzas
fundamentales que rigen el universo.


El modelo de Fermi de la desintegración beta ha sido instrumental en este entendimiento. Proporciona el marco teórico
que nos permite comprender cómo y por qué ocurre la desintegración beta, permitiendo a los científicos predecir la
probabilidad de desintegración y la energía de las partículas emitidas. Además, el modelo de Fermi ha sido fundamental
para el desarrollo de la teoría electrodébil, una parte esencial del Modelo Estándar de la física de partículas.

Discutiremos cómo ocurre la desintegración beta, qué partículas se emiten y por qué, y cómo el modelo de Fermi nos ayuda
a entender este proceso. También discutiremos las aplicaciones prácticas de la desintegración beta y el modelo de Fermi
en la medicina, la energía y otras áreas.

En resumen, este documento proporcionará una visión general completa y detallada de la desintegración beta y
el modelo de Fermi. Esperamos que este documento sea de interés para cualquier persona interesada en la física de
partículas, la tecnología nuclear o la ciencia en general.

'''





st.write("Si desea puede descargar el documento en pdf en el siguiente enlace:")
with open("fermi.pdf", "rb") as f:
    bytes = f.read()
    b64 = base64.b64encode(bytes).decode()
    st.download_button(label='Descargar PDF',data=f,mime='application/pdf',help='Descargar el documento en pdf')
