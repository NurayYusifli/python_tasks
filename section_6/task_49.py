students = []
for i in range(5):
    name = input(f"{i+1}. Student name: ")
    score = float(input(f"{name}'s score: "))
    status = "Pass" if score >= 51 else "Fail"
    if score >= 91: grade = "A"
    elif score >= 81: grade = "B"
    elif score >= 71: grade = "C"
    elif score >= 61: grade = "D"
    elif score >= 51: grade = "E"
    else: grade = "F"
    students.append({"name": name, "score": score, "grade": grade, "status": status})
for i in students:
    print(i)
