import parser
import analyzer

def run_resume_analyzer(file_path):
    text = parser.extract_text(file_path)
    resume_data = {
        "skills": parser.extract_skills(text),
        "education": parser.extract_education(text),
        "experience": parser.extract_experience(text)
    }
    result = analyzer.analyze_resume(resume_data)
    print("📊 Resume Analysis Report")
    print("Score:", result["score"], "%")
    print("Matched Skills:", result["matched_skills"])
    print("Missing Skills:", result["missing_skills"])
    print("Education:", result["education"])
    print("Experience:", result["experience"])

if __name__ == "__main__":
    run_resume_analyzer("resume.pdf")  # replace with your file
