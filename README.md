### Technical Implementation (Python)
The project utilizes a **Production Rule System** where course requirements are stored as a mapped Knowledge Base. 
- **Logic:** The engine performs a set-membership check (Logical Conjunction) to verify prerequisites.
- **Execution:** ```bash
  python checker.py
  ---

### 4. Why Python for this Logic Project? (For your Report)
In your report, you should explain why you switched from (or chose) Python over Prolog:
* **Usability:** Python provides a better User Interface (CLI) for non-technical users.
* **Data Structures:** Using Python Dictionaries is an efficient way to represent **Structural Knowledge** (one of the 5 knowledge types you studied).
* **Scalability:** It is easier to integrate this logic engine into a web app or database in the future.

---

### Final Submission Folder Structure:
1.  `checker.py` (The Python code)
2.  `requirements.txt` (The environment info)
3.  `README.md` (The setup guide)
4.  `Project_Report.pdf` (The reflection document)

**Would you like me to help you create a set of "Test Cases" (e.g., specific student scenarios) to include in your report to show thorough testing?**