import json

def analyze_resume(resume_data, job_file="sample_job.json"):
    with open(job_file, "r") as f:
        job = json.load(f)

    required_skills = set([s.lower() for s in job["skills"]])
    resume_skills = set(resume_data["skills"])

    matched = required_skills.intersection(resume_skills)
    missing = required_skills - resume_skills

    score = (len(matched) / len(required_skills)) * 100

    return {
        "score": round(score, 2),
        "matched_skills": list(matched),
        "missing_skills": list(missing),
        "education": resume_data["education"],
        "experience": resume_data["experience"]
    }
