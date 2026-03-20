'''  Version 1: Parallel list-based questions, free text answers only, no multiple choice
                Data structure: three separate lists (questions, answers, points) accessed by index
                Answer format: free text input '''


# Use lists to store questions, answers and points and find them by index
questions = [
    'How many continents are there on Earth?',
    'Which planet in our solar system is known as the Red Planet?',
    'What is the chemical symbol for gold?',
    'What is the largest ocean on Earth?',
    'In which year did the Titanic sink?',
    'What is the smallest prime number greater than 100?',
    'Which element has the highest electrical conductivity at room temperature?']

answers = ['7', 'Mars', 'Au', 'Pacific Ocean', '1912', '101', 'Silver' ]
points = [1, 1, 1, 1, 2, 3, 3]

print("You'll get 7 questions, one at a time.")

score = 0

# Sum all point values upfront since structure is fixed
total_points = sum(points)

# Enumerate gives the index to look up the matching answer and points
for i, question in enumerate(questions):
    question_text = question
    question_answer = answers[i]
    question_points = points[i]

    print(question_text)

    # The strip() method in Python removes any leading and trailing whitespace (spaces, tabs, newlines) from a string
    user_answer = input("Insert your response here: ").lower().strip()

    if user_answer == question_answer:
        print("Correct!")
        score += question_points
    else:
        print(f"Wrong! Correct answer: {question_answer}")

print(f'Your final score is: {score} from {total_points}')

