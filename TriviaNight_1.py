'''  Version 1: Dictionary-based questions, free text answers only, no multiple choice
                Data structure: list of dictionaries
                Answer format: free text input '''


# Use a list of dictionaries to store questions, answers, points
questions = [
    {"question": "How many continents are there on Earth?", "answer": "7", "points": 1},
    {"question": "Which planet in our solar system is known as the Red Planet?", "answer": "Mars", "points": 1},
    {"question": "What is the chemical symbol for gold?", "answer": "Au", "points": 1},
    {"question": "What is the largest ocean on Earth?", "answer": "Pacific Ocean", "points": 1},
    {"question": "In which year did the Titanic sink?", "answer": "1912", "points": 2},
    {"question": "What is the smallest prime number greater than 100?", "answer": "101", "points": 3},
    {"question": "Which element has the highest electrical conductivity at room temperature?", "answer": "Silver", "points": 3},
]

print("You'll get 7 questions, one at a time.")

total_points = 0
score = 0

# Loop through the list and access the question, answer and points for each question using the keys of the dictionary
for q in questions:
    question_text = q['question']
    question_answer = q['answer'].lower()
    question_points = q['points']

    print(question_text)

    # The strip() method in Python removes any leading and trailing whitespace (spaces, tabs, newlines) from a string.
    user_answer = input("Insert your response here: ").lower().strip()

    if user_answer == question_answer:
        print("Correct!")
        score += question_points
    else:
        print(f"Wrong! Correct answer: {question_answer}")

    # Accumulate total possible points
    total_points += question_points

print(f'Your final score is: {score} from {total_points}')
