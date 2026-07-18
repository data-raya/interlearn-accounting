import streamlit as st

def course_card(icon, title, chapter, progress, color, key, kategori):

    with st.container(border=True):

        # Header
        st.markdown(
            f"""
            <div style="
                background:{color};
                padding:18px;
                border-radius:12px;
                margin-bottom:20px;
            ">
                <h2 style="
                    color:#2E2E2E;
                    margin:0;
                    font-size:30px;
                ">
                    {icon} {title}
                </h2>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.progress(progress / 100)

        col1, col2 = st.columns([1,1])

        with col1:
            st.caption("Progress")

        with col2:
            st.caption(f"{progress:.0f}%")

        if st.button(
            "🚀 Buka Materi",
            key=key,
            use_container_width=True
        ):

            st.session_state.kategori = kategori
            st.session_state.page = "chapter"

            st.rerun()