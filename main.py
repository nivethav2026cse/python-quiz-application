
print("===== PYTHON QUIZ APPLICATION =====")

score = 0

questions = [
    "1. Which language is used for web development?",
    "2. Which keyword is used to define a function in Python?",
    "3. What is the output of 5 + 3?",
    "4. Which data type stores True or False?",
    "5. Which symbol is used for comments in Python?"
]

options = [
    ["A. HTML", "B. Python", "C. C++", "D. Java"],
    ["A. function", "B. def", "C. fun", "D. define"],
    ["A. 6", "B. 7", "C. 8", "D. 9"],
    ["A. int", "B. str", "C. float", "D. bool"],
    ["A. //", "B. /*", "C. #", "D. !"]
]

answers = ["A", "B", "C", "D", "C"]

for i in range(5):

    print("\n", questions[i])

    for option in options[i]:
        print(option)

    user_answer = input("Enter your answer: ").upper()

    if user_answer == answers[i]:
        print("Correct answer!")
        score = score + 1
    else:
        print("Wrong answer!")

print("\n===== QUIZ RESULT =====")

print("Your Score:", score, "/ 5")

if score == 5:
    print("Excellent performance!")
elif score >= 3:
    print("Good job!")
else:
    print("Keep practising!")
