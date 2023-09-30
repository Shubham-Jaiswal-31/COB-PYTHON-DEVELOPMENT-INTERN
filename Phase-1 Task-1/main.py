# A Quiz Program where that will give a random quiz from a set of 30 questions.
# Written by Shubham Anand Jaiswal

# Importing the question data from data.py
from data import question_data

# Creating the Question Model class to hold the question and answer
class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

# Creating the QuizBrain class to handle the quiz 
class QuizBrain:
    # Initialize the attributes of class 
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    # A function to ask the question and receive the user's answer
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        print(f"Q.{self.question_number}: {current_question.text}")
        
        user_answer = input("Choose (True, False): ")
        self.check_answer(user_answer, current_question.answer)

    # A function to check if questions are left
    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    # A function to check the answer and display a message
    def check_answer(self, user_answer, correct_answer):
        
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You are correct!")
        else:
            print(f"You are wrong! The correct answer was: {correct_answer}.")
            
        print(f"Score: {self.score}/{self.question_number}", end="\n\n")

# Intializing an empty question bank
question_bank = []

# Reading the questions from question_data 
for data in question_data:
    
    # Creating a question model with its text and answer
    question = Question(data["question"], data["correct_answer"])
    
    # Adding the question model to the question bank
    question_bank.append(question)

# Initialize the quiz using QuizBrain class
quiz = QuizBrain(question_bank)

# Only asking till the questions exist
while quiz.still_has_questions():
    quiz.next_question()

# Displaying the final result
print(f"You have completed the quiz. Final score: {quiz.score}/{quiz.question_number}")
