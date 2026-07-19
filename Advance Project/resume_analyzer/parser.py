import re
import docx
import pdfplumber

def extract_text(file_path):
    if file_path.endswith(".pdf"):
        text = ""
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() + "\n"
        return text
    elif file_path.endswith(".docx"):
        doc = docx.Document(file_path)
        return "\n".join([p.text for p in doc.paragraphs])
    else:
        raise ValueError("Unsupported file format")

def extract_skills(text):
    # Simple regex-based skill extraction
    skills = re.findall(r"\b(Python|Java|SQL|Machine Learning|AI|C\+\+|HTML|CSS|JavaScript)\b", text, re.I)
    return list(set([s.lower() for s in skills]))

def extract_education(text):
    edu = re.findall(r"(Bachelor|Master|PhD|BSc|MSc|MBA)", text, re.I)
    return list(set(edu))

def extract_experience(text):
    exp = re.findall(r"(\d+)\s+years", text, re.I)
    return exp
