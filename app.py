# app.py: la pantalla de la app.
# Los resultados vienen de logica.py; aquí solo se muestran.
# La app tiene una página de inicio y una página por pregunta. El diseño es libre:
# los colores y las letras se cambian en .streamlit/config.toml, y aquí se puede
# agregar lo que haga falta para que la app se vea bien.

import streamlit as st

# Ejecutar este archivo en Thonny (F5) abre la app en el navegador
if not st.runtime.exists():
    import sys
    from streamlit.web import cli
    sys.argv = ["streamlit", "run", __file__, "--server.runOnSave", "true", "--server.showEmailPrompt", "false"]
    sys.exit(cli.main())

import logica

st.set_page_config(page_title="Nombre de la app", layout="wide")


def inicio():
    st.title("Nombre de la app")
    st.markdown("*Una frase que diga para qué sirve la app.*")
    st.divider()

    # Las tres respuestas, una por columna
    columna_1, columna_2, columna_3 = st.columns(3)
    with columna_1:
        st.caption("PREGUNTA 1")
        st.subheader("Respuesta")
        st.write("Una frase que explique la respuesta.")
    with columna_2:
        st.caption("PREGUNTA 2")
        st.subheader("Respuesta")
        st.write("Una frase que explique la respuesta.")
    with columna_3:
        st.caption("PREGUNTA 3")
        st.subheader("Respuesta")
        st.write("Una frase que explique la respuesta.")

    st.divider()
    st.caption(f"La app analiza las {len(logica.filas)} filas de {logica.ARCHIVO}.")

    # Muestra cómo es una fila de la base de datos mientras trabajas; quítalo al terminar
    st.write("Una fila de la base de datos:", logica.filas[0])


def pregunta_1():
    st.caption("PREGUNTA 1")
    st.title("La pregunta 1, escrita como pregunta")

    # La respuesta va en un recuadro, arriba de todo
    with st.container(border=True):
        st.caption("RESPUESTA")
        st.header("La respuesta")
        st.write("Una frase que explique la respuesta con sus números.")

    # La gráfica que respalda la respuesta. Cambia las dos listas por las de logica.py:
    # una con los nombres (por ejemplo, las aerolíneas) y otra con sus números.
    # "Grupo" y "Valor" son los títulos de los ejes. sort=False deja las barras
    # en el orden de las listas. Para una línea, usa st.line_chart con las mismas
    # listas, sin sort.
    st.subheader("Título de la gráfica")
    nombres = ["A", "B", "C"]
    valores = [10, 20, 15]
    st.bar_chart({"Grupo": nombres, "Valor": valores}, x="Grupo", y="Valor", sort=False)

    st.subheader("Cómo se calculó")
    st.markdown("""
1. El primer paso del proceso.
2. El segundo paso.
3. El último paso.
""")


def pregunta_2():
    st.caption("PREGUNTA 2")
    st.title("La pregunta 2, escrita como pregunta")

    with st.container(border=True):
        st.caption("RESPUESTA")
        st.header("La respuesta")
        st.write("Una frase que explique la respuesta con sus números.")

    # La gráfica que respalda la respuesta. Cambia las dos listas por las de logica.py:
    # una con los nombres (por ejemplo, las aerolíneas) y otra con sus números.
    # "Grupo" y "Valor" son los títulos de los ejes. sort=False deja las barras
    # en el orden de las listas. Para una línea, usa st.line_chart con las mismas
    # listas, sin sort.
    st.subheader("Título de la gráfica")
    nombres = ["A", "B", "C"]
    valores = [10, 20, 15]
    st.bar_chart({"Grupo": nombres, "Valor": valores}, x="Grupo", y="Valor", sort=False)

    st.subheader("Cómo se calculó")
    st.markdown("""
1. El primer paso del proceso.
2. El segundo paso.
3. El último paso.
""")


def pregunta_3():
    st.caption("PREGUNTA 3")
    st.title("La pregunta 3, escrita como pregunta")

    with st.container(border=True):
        st.caption("RESPUESTA")
        st.header("La respuesta")
        st.write("Una frase que explique la respuesta con sus números.")

    # La gráfica que respalda la respuesta. Cambia las dos listas por las de logica.py:
    # una con los nombres (por ejemplo, las aerolíneas) y otra con sus números.
    # "Grupo" y "Valor" son los títulos de los ejes. sort=False deja las barras
    # en el orden de las listas. Para una línea, usa st.line_chart con las mismas
    # listas, sin sort.
    st.subheader("Título de la gráfica")
    nombres = ["A", "B", "C"]
    valores = [10, 20, 15]
    st.bar_chart({"Grupo": nombres, "Valor": valores}, x="Grupo", y="Valor", sort=False)

    st.subheader("Cómo se calculó")
    st.markdown("""
1. El primer paso del proceso.
2. El segundo paso.
3. El último paso.
""")


# Las páginas de la app, en el orden del menú. El nombre de cada página se puede cambiar.
pagina = st.navigation([
    st.Page(inicio, title="Inicio", default=True),
    st.Page(pregunta_1, title="Pregunta 1"),
    st.Page(pregunta_2, title="Pregunta 2"),
    st.Page(pregunta_3, title="Pregunta 3"),
])

# La barra lateral presenta a la persona para quien es la app
with st.sidebar:
    with st.container(border=True):
        st.caption("ESTA APP ES PARA")
        st.markdown("**Nombre de la persona**")
        st.write("Quién es y en qué situación está.")
        st.caption("SU DECISIÓN")
        st.write("Lo que necesita decidir.")

pagina.run()
