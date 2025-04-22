import os
import base64
import streamlit as st
from utils import highlight_keywords, search_keywords

UPLOAD_FOLDER = "sample_cvs"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

st.set_page_config(page_title="AI Resume Scanner", layout="centered")
st.title("📄 Intelligent Resume Scanner (AI-powered)")

st.sidebar.header("Upload Resume(s)")
uploaded_files = st.sidebar.file_uploader("Choose PDF/DOCX files", type=["pdf", "docx"], accept_multiple_files=True)

# Handling uploaded files
if uploaded_files:
    for uploaded in uploaded_files:
        save_path = os.path.join(UPLOAD_FOLDER, uploaded.name)
        with open(save_path, "wb") as f:
            f.write(uploaded.read())
        st.sidebar.success(f"Uploaded: {uploaded.name}")

# Function to get file in base64 format
def get_file_base64(filename):
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# Search resumes by keyword(s)
st.write("### 🔍 Search Resumes by Keyword(s)")
keyword_input = st.text_input("Enter keyword(s) (e.g., python, project manager)")

if keyword_input:
    keywords = [k.strip() for k in keyword_input.split(",") if k.strip()]
    st.write("📂 Scanning uploaded resumes...")

    matched_files = []
    for filename in os.listdir(UPLOAD_FOLDER):
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        if filename.endswith((".pdf", ".docx")):
            matched_keywords, raw_text = search_keywords(file_path, keywords)
            if matched_keywords:
                matched_files.append((filename, matched_keywords, raw_text))

    # Displaying matched results
    if matched_files:
        st.success(f"✅ Found {len(matched_files)} matching resume(s):")
        for name, found_keywords, raw_text in matched_files:
            with st.expander(f"{name}"):
                st.write(f"Matched Keywords: `{', '.join(found_keywords)}`")

                # Highlight matched keywords in the resume
                highlighted_text = highlight_keywords(raw_text, found_keywords)

                # Display the highlighted text within the app
                st.markdown(f"### Resume Content with Keyword Highlights")
                st.markdown(highlighted_text, unsafe_allow_html=True)

                # Provide a button to view the resume in a new tab or download
                with open(os.path.join(UPLOAD_FOLDER, name), "rb") as f:
                    st.download_button("📥 Download Resume", f, file_name=name)

                # You can uncomment this to open the resume in a new tab (base64 option)
                # st.markdown(f"Or [click here to open the resume in a new tab](data:application/octet-stream;base64,{get_file_base64(name)})")
    else:
        st.warning("❌ No resumes matched the given keywords.")
