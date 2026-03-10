questions = [
    {"question": "Which keyword is used to define a function in Python?", "answer": "def"},
    {"question": "Which method is used to add an element to the end of a list?", "answer": "append"},
    {"question": "Which function is used to display output to the console?", "answer": "print"},
    {"question": "What is the return type of the expression 10 / 2?", "answer": "float"},
    {"question": "Which loop continues as long as a condition is true?", "answer": "while"}
]
score = 0
for i, item in enumerate(questions):
    print(f"\nQuestion {i+1}: {item['question']}")
    answer = input("Your answer: ").lower().strip()
    if answer == item['answer']:
        print("Correct!")
        score += 1
    else:
        print(f"Incorrect. The correct answer was: {item['answer']}")
print(f"Finished! Your final score is: {score}/{len(questions)}")