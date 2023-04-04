def functional(resume):
    
    required_keywords = ["Python", "machine learning", "data analysis", "problem solving"]
    return all(keyword in resume.lower() for keyword in required_keywords)

