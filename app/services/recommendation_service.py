def recommend_next_topic(student_id: int) -> str:
    """
    Placeholder  
    """
    sample_topics = ["Data Structures", "Algorithms", "DBMS", "OS", "Networks"]
    return sample_topics[student_id % len(sample_topics)]
