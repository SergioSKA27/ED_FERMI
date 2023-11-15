import streamlit as st
from st_pages import Page, show_pages, add_page_title

# Optional -- adds the title and icon to the current page
add_page_title()

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
        Page("pages/Modeldesc1.py","8. Formulación del modelo",":books:" ),
        Page("pages/preguntas.py","9. Respuesta a las preguntas",":books:" ),
        Page("pages/nodosyrutas.py","10. Nodos y rutas",":books:" ),
        Page("pages/Infografia.py","11. Infografía",":books:" ),
        Page("pages/actualtec.py","12. Relación del modelo con la tecnología actual",":books:" ),
        Page("pages/conclusiones.py","13. Conclusiones",":books:" ),
        Page("pages/videos.py","14. Video",":books:" ),
        Page("pages/referencias.py","15. Referencias",":books:" ),


    ]
)
