def calculate_score(skills):
    required_skills = ["sql", "python", "excel", "powerbi", "machine learning"]

    matched = []
    missing = []

    for skill in required_skills:
        if skill in [s.lower() for s in skills]:
            matched.append(skill)
        else:
            missing.append(skill)

    score = int((len(matched) / len(required_skills)) * 100)

    return score, matched, missing