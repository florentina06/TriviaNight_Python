'''  Version 3: JSON-based questions with multiple choice support
                Data structure: external JSON file loaded at runtime
                Answer format: multiple choice (multi-select or single) depending on the question '''


import json

# Check if file exists and handles the error if it doesn't
try:
    with open("questions.json", 'r') as f:
        questions = json.load(f)  # Read the JSON file and convert it into a Python list
except FileNotFoundError:
    print("Error! questions.json file not found. Make sure it's in the same folder as your script." )
except Exception as err:
    print(err)


print("You'll get 8 questions, one at a time.")

score = 0

for id, question in enumerate(questions, start=1):
    print(f'{id}: {question['text']}')
    print(question['options'])

    # Check if it's a multiple choice question
    if len(question['answer']) > 1:
        question_answer = question['answer']
        question_score = question['points']

        # User inputs multiple choices
        user_answer = []
        print('Insert your response here. When you want to stop press q: ')

        # Keep collecting answers until the user types 'q' to quit
        while True:
            # The strip() method removes any leading and trailing whitespace (spaces, tabs, newlines) from a string
            user = input("Insert a letter:").upper().strip()
            if user == 'Q':
                break
            user_answer.append(user)

        # Use set() to compare answers so order doesn't matter and duplicates are ignored
        user_answer = set(user_answer)
        question_answer = set(question_answer)

        # Find how many correct answers the user guessed
        user_correct_count = 0
        for answer in user_answer:
            if answer in question_answer:
                user_correct_count += 1

        total_correct_answer = len(question_answer)

        if user_answer == question_answer:
            print("Correct!")
            score += question['points']

        elif user_correct_count > 0:
            partial = user_correct_count / total_correct_answer * question['points']
            score += partial
            print(
                f'Partially correct! {user_correct_count} / {total_correct_answer} answers right. Correct answer: {question_answer}')

        else:
            print(f"Wrong! Correct answer: {question_answer}")


    else:  # If it's not a multiple choice question
        user_answer = input("Insert your answer here: ").upper().strip()
        question_answer = question['answer'][0]
        question_score = question['points']
        if user_answer == question_answer:
            print("Correct!")
            score += question_score
        else:
            print(f"Wrong! The correct answer is: {question_answer}")


# Calculate total possible points from all questions
total_points = sum(q['points'] for q in questions)

print(f'Your final score is: {score} from {total_points}')
