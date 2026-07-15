import streamlit as st

def stat_card(icon, title, value):

    with st.container(border=True):

        st.markdown(f"# {icon}")

        st.markdown(f"### {title}")

        st.markdown(
            f"<h2 style='text-align:center'>{value}</h2>",
            unsafe_allow_html=True
        )