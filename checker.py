import sys

# --- KNOWLEDGE BASE (Declarative Knowledge) ---
# Maps a course to its list of prerequisites
KNOWLEDGE_BASE = {
    "CS101": {"name": "Intro to Programming", "prereqs": []},
    "CS102": {"name": "Formal Logic", "prereqs": []},
    "CS201": {"name": "Artificial Intelligence", "prereqs": ["CS101", "CS102"]},
    "CS301": {"name": "Advanced NLP", "prereqs": ["CS201"]}
}

# --- LOGIC ENGINE (Inference) ---
def check_eligibility(student_courses, target_course):
    """
    Uses First-Order Logic principles to verify if a student 
    meets all requirements (P AND Q AND R ... -> Eligible)
    """
    if target_course not in KNOWLEDGE_BASE:
        return False, "Course code not found."

    required = KNOWLEDGE_BASE[target_course]["prereqs"]
    
    # Check if all required courses exist in the student's completed list
    # This is a functional implementation of a logical 'AND' operation
    missing = [course for course in required if course not in student_courses]

    if not missing:
        return True, f"Eligible for {target_course}!"
    else:
        return False, f"Missing prerequisites: {', '.join(missing)}"

# --- MAIN INTERFACE ---
def main():
    print("--- Academic Logic Advisor ---")
    completed = input("Enter your completed courses (comma separated, e.g., CS101, CS102): ").upper().replace(" ", "").split(",")
    target = input("Which course do you want to take? (e.g., CS201): ").upper().strip()

    eligible, message = check_eligibility(completed, target)
    
    if eligible:
        print(f"\n SUCCESS: {message}")
    else:
        print(f"\n DENIED: {message}")

if __name__ == "__main__":
    main()