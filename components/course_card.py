import streamlit as st

def course_card(icon, title, chapter, description, button_key):

    with st.container(border=True):

        st.markdown(f"## {icon}")

        st.subheader(title)

        st.write(f"**{chapter}**")

        st.write(description)

        st.write("")

        st.button(
            "Mulai Belajar",
            key=button_key,
            use_container_width=True
        )