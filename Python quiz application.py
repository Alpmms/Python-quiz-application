#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# quiz.py

questions = [
    {
        "question": "What is the output of print(2 * 3 ** 3)",
        "answers": ["18", "54", "6", "27"],
        "correct_answer": "54"
    },
    {
        "question": "Which of the following is not a Python data type?",
        "answers": ["str", "int", "float", "tuple"],
        "correct_answer": "tuple"
    },
    {
        "question": "What is the output of print(abs(-5))",
        "answers": ["5", "-5", "0", "None"],
        "correct_answer": "5"
    }
]

def ask_question(question):
    print(question["question"])
    for i, answer in enumerate(question["answers"], 1):
        print(f"{i}. {answer}")
    user_answer = input("Enter your answer (1-{}): ".format(len(question["answers"])))
    return user_answer

def check_answer(question, user_answer):
    if user_answer == "":
        return False
    if user_answer == question["correct_answer"]:
        print("Correct!")
        return True
    else:
        print("Incorrect. The correct answer is '{}'.".format(question["correct_answer"]))
        return False

def run_quiz():
    score = 0
    for question in questions:
        user_answer = ask_question(question)
        if check_answer(question, user_answer):
            score += 1
    print("Your final score is: {}/{}".format(score, len(questions)))

if __name__ == "__main__":
    run_quiz()


# In[ ]:




