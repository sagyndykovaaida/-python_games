def functional(resume):
    
    required_keywords = ["Python", "machine learning", "data analysis", "problem solving"]
    return all(keyword in resume.lower() for keyword in required_keywords)

def non_functional(resume):
   
    print("This candidate has a degree in Computer Science and 3 years of experience in software development.")
    print("They are proficient in Python, Java, and C++, and have worked on several projects involving machine learning and data analysis.")