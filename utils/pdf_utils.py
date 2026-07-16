import fitz
from PIL import Image
import streamlit as st 

@st.cache_data
def render_pdf_page(pdf_path, page_number):

    doc = fitz.open(pdf_path)

    page = doc.load_page(page_number)

    pix = page.get_pixmap(dpi=180)

    image = Image.frombytes(
        "RGB",
        [pix.width, pix.height],
        pix.samples
    )

    doc.close()

    return image


@st.cache_data
def get_total_pages(pdf_path):

    doc = fitz.open(pdf_path)

    total = len(doc)

    doc.close()

    return total