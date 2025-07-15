print("===Simple Quiz Game===")
questions = [
    "What is the capital of France?\n1. Rome \n2. Berlin \n3. Paris \n4. Lahore",
    "Which number is even?\n1. 3 \n2. 4 \n3. 9 \n4. 7",
    "Which language used in webpage?\n1. HTML \n2. JAVA \n3. PHP \n4. Python"
]
correctanswer = [3,2,1]
score = 0

for i in range(len(questions)):
    print(f"\nQ{i+1}:")
    print(questions[i])
    useranswer = int(input("Your Answer (1-4): "))

    if useranswer == correctanswer[i]:
        print("Correct")
        score += 1
    else:
        print(f"Wrong the correct answer is {correctanswer[i]}")

print("===Quiz Finished===")
print(f"Your Score: {score} out of {len(questions)}")