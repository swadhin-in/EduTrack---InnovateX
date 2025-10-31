 
from typing import Union

def calculate_risk(attendance: Union[float, int], gpa: Union[float, int]) -> float:
    """
    

    Example formula:
      - Attendance contribution: (100 - attendance) weighted 60%
      - GPA contribution: (4 - gpa) scaled to 0-100 then weighted 40%

    """
    try:
        attendance = float(attendance)
        gpa = float(gpa)
    except Exception:
        return 0.0

    attendance_component = max(0.0, min(100.0, 100.0 - attendance))  # 0..100
    # converting GPA difference to 0..100: (4 - gpa) / 4 * 100
    gpa_component = max(0.0, min(100.0, (4.0 - gpa) / 4.0 * 100.0))

    score = (0.6 * attendance_component) + (0.4 * gpa_component)
    # clamp
    score = max(0.0, min(100.0, score))
    return round(score, 2)

def is_at_risk(score: float, threshold: float = 50.0) -> bool:
    return score >= threshold
