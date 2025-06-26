import streamlit as st
import os
from dotenv import load_dotenv
import pdfplumber
import openai

# .env dosyasını yükle
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="Smart Resume Analyzer", layout="centered")

st.title("📄 Smart Resume Analyzer")
st.write("Yüklediğiniz özgeçmişi analiz edip, hedeflediğiniz pozisyona uygun hale getirmenize yardımcı olur.")

# Hedef pozisyon girişi
target_role = st.text_input("🎯 Hedeflediğiniz pozisyon nedir? (örn: Data Scientist)")

# CV yükleyici
uploaded_file = st.file_uploader("📎 Özgeçmişinizi yükleyin (PDF)", type=["pdf"])

if uploaded_file and target_role:
    st.info("Özgeçmiş işleniyor...")

    # PDF'ten metin çıkar
    with pdfplumber.open(uploaded_file) as pdf:
        text = "\n".join([page.extract_text() or "" for page in pdf.pages])

    # OpenAI'ya gönder
    with st.spinner("LLM önerileri hazırlanıyor..."):
        prompt = f"""
        Aşağıda bir özgeçmiş metni verilmiştir. Bu kişiyi '{target_role}' pozisyonu için değerlendir.
        1. Eksik veya geliştirilebilir yönleri belirt.
        2. Anahtar kelime önerileri sun ve bunları nasıl yapacağını anlat.
        3. Genel bir geliştirme önerisi ver fakat bu öneri sıradan olmasın bir işe alım yapan asistan gibi davran.

        Özgeçmiş:
        {text}
        """

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Sen profesyonel bir insan kaynakları kariyer danışmanısın. Kişilerin özgeçmişlerini analiz et ve geliştirme önerileri sun."},
                {"role": "user", "content": prompt}
            ]
        )

        output = response.choices[0].message["content"]
        st.success("Analiz tamamlandı!")
        st.markdown("### 🧠 Öneriler:")
        st.write(output)

elif not uploaded_file and target_role:
    st.warning("Lütfen bir özgeçmiş dosyası yükleyin.")
elif uploaded_file and not target_role:
    st.warning("Lütfen hedeflediğiniz pozisyonu yazın.")
