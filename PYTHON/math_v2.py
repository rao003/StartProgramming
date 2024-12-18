import random
import time

def generate_question():
    operations = ['+', '-', '*', '/']
    a = random.randint(0, 20)
    b = random.randint(1, 20)  # Avoid division by zero
    operation = random.choice(operations)
    if operation == '/':
        a = a * b  # Ensure the division is always an integer
    return a, b, operation

def calculate_answer(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        return a // b

score = 0
total_questions = 10

for _ in range(total_questions):
    a, b, operation = generate_question()
    print(f"{a} {operation} {b}")
    start_time = time.time()
    try:
        c = int(input("What is the result? "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        continue
    end_time = time.time()
    
    if c == calculate_answer(a, b, operation):
        score += 1
        print(f"Correct! Time taken: {end_time - start_time:.2f} seconds")
    else:
        print(f"Wrong! The correct answer was {calculate_answer(a, b, operation)}. Time taken: {end_time - start_time:.2f} seconds")

print(f"From {total_questions} questions, you got {score} correct.")
print(f"Your score is {score / total_questions * 100:.2f}%")