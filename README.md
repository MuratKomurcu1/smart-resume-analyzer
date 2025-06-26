Smart Resume Analyzer - README
Smart Resume Analyzer
Smart Resume Analyzer is a lightweight yet powerful AI-based application that analyzes uploaded resumes and provides intelligent feedback tailored to a specific job role. Built with Streamlit and OpenAI's GPT models, it extracts resume content, evaluates its quality, and suggests improvements in skills, structure, and keyword usage to boost job matching performance.
✅ Upload your CV (PDF)  
🎯 Specify your target job role  
🤖 Get AI-powered suggestions & improvements instantly
Demo
Live demo (coming soon via Hugging Face Spaces...)
Features
📤 Upload your resume in PDF format  
🔍 Extract text using pdfplumber  
🧠 Analyze CV using GPT (OpenAI API)  
🎯 Customize based on your target role  
🧾 Get keyword suggestions and improvement tips  
🌐 Streamlit-based responsive UI
File Structure
smart-resume-analyzer/
├── streamlit_app.py       # Main app
├── requirements.txt       # Python dependencies
├── .env                   # API key config (excluded from repo)
├── assets/                # Images, demo content
└── README.md
Installation
1. Clone the repo
   git clone https://github.com/MuratKomurcu1/smart-resume-analyzer.git
   cd smart-resume-analyzer
2. Install dependencies
   pip install -r requirements.txt
3. Set your OpenAI API key in `.env`
   OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxxxxxxxxxxxxx
4. Run the app
   streamlit run streamlit_app.py
Built With
- Streamlit
- OpenAI GPT
- pdfplumber
- python-dotenv
Roadmap – v2 Plans
✅ Named Entity Recognition (NER) for skills, education, and experience  
✅ Resume Rewriting using LLM  
✅ Semantic job description matching  
✅ PDF export of suggestions  
✅ Hugging Face Spaces deployment  
✅ DOCX support
Contributing
Contributions, ideas, or issues? Feel free to open a pull request or contact via LinkedIn.
License
MIT License © 2025 Murat Kömürcü
