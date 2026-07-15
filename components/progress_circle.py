import streamlit as st
import plotly.graph_objects as go

def progress_circle(progress):

    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=progress,
            number={"suffix": "%"},
            title={"text": "Progress Belajar"},
            gauge={
                "axis": {"range": [0, 100]},
                "bar": {"color": "#4F46E5"},
                "steps": [
                    {"range": [0, 30], "color": "#FEE2E2"},
                    {"range": [30, 70], "color": "#FEF3C7"},
                    {"range": [70, 100], "color": "#DCFCE7"},
                ],
            },
        )
    )

    fig.update_layout(
        height=280,
        margin=dict(l=10, r=10, t=40, b=10)
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
        config={"displayModeBar": False}
    )