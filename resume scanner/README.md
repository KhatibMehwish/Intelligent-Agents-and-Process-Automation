#  Intelligent Resume Scanner (AI-Powered)

This Streamlit-based web application allows users to upload resumes in PDF or DOCX format and intelligently search them by keywords. It's designed to assist HR teams in filtering candidates quickly based on relevant skills.

##  Features

- Upload multiple resumes
- Search resumes by multiple keywords
- Highlight matched keywords in resume content
- ATS (Applicant Tracking System) style scoring
- Download and preview resume contents

## Project Structure

```
resume-scanner/

 app.py               # Main Streamlit app file
 utils.py             # Contains keyword search and text processing logic
 sample_cvs/          # Folder where uploaded resumes are saved
 __pycache__/         # Python bytecode cache
 requirements.txt     # Required Python packages
```

##  Why Streamlit?

- Easy to build interactive web apps for data applications.
- Real-time feedback and auto-refresh on changes.
- Ideal for internal tools and quick UI deployment for RPA use cases.

## ⚙️ Setting Up the Project (With Virtual Environment)

1. Unzip the project folder you already have.

2. Create a virtual environment (recommended):


python -m venv venv
```

3. Activate the virtual environment:

- On Windows:
  
  .\venv\Scripts\activate
  ```

- On macOS/Linux:
  ```bash
  source venv/bin/activate
  ```

4. Install required packages:


pip install -r requirements.txt

python -m spacy download en_core_web_sm

5. Run the app:


streamlit run app.py
```

##  How This Relates to RPA

This project fits perfectly into Robotic Process Automation (RPA) because:

- It automates the manual task of scanning and evaluating resumes.
- Increases efficiency in HR screening processes.
- Can be integrated with email bots to scan incoming resumes.
- Highlights decision-making data with keyword detection, making human-in-the-loop review faster.


## Author

Developed as part of an RPA learning and automation implementation activity.
