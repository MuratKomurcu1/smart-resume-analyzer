import streamlit as st
from cv_parser import extract_text_from_pdf, extract_text_from_docx
from nlp_analyzer import extract_named_entities, extract_keywords_yake, extract_skills
from rewriter import rewrite_experience

from rewriter import rewrite_experience


st.set_page_config(page_title="Smart Resume Analyzer", layout="wide")
st.title("📄 Smart Resume Analyzer & Rewriter")
st.write("Upload your CV and get AI-powered feedback to boost your career!")

uploaded_file = st.file_uploader("Upload your CV (PDF or DOCX)", type=["pdf", "docx"])

if uploaded_file:
    # Text extraction
    if uploaded_file.name.endswith(".pdf"):
        with open("temp.pdf", "wb") as f:
            f.write(uploaded_file.read())
        text = extract_text_from_pdf("temp.pdf")
    else:
        with open("temp.docx", "wb") as f:
            f.write(uploaded_file.read())
        text = extract_text_from_docx("temp.docx")

    st.subheader("📜 Extracted Text:")
    st.text_area("Raw CV Text", text, height=300)

    # NLP Analysis
    st.subheader("🔍 Named Entity Recognition:")
    st.write(extract_named_entities(text))

    st.subheader("💡 Keywords (YAKE):")
    st.write(extract_keywords_yake(text))

    st.subheader("🛠️ Skills Detected:")
    st.write(extract_skills(text))

    # Rewrite with GPT
    # Rewrite kısmı
st.subheader("🤖 Rewrite Suggestion:")
role = st.text_input("What role are you applying for?", "Data Scientist")

if st.button("Rewrite Experience"):
    try:
        rewritten = rewrite_experience(text, role_description=role)
        st.text_area("Rewritten Experience", rewritten, height=300)
    except Exception as e:
        st.error(f"Rewrite işlemi başarısız oldu: {e}")
