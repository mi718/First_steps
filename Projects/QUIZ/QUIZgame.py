import json

with open("questions.json", "r") as file:
    content = file.read()


data = json.loads(content)


for questions in data:
    print(questions["Question_text"])
    for index, alternative in enumerate(questions["Alternatives"]):
        print(index +1 , "-", alternative)
    user_choice = int(input("Enter your answer: "))
    questions["user_choice"] = user_choice

score = 0
for index, questions in enumerate(data):
    if questions["user_choice"] == questions["correct_answer"]:
        score = score +1
        result = "Correct answer"
    else:
        result = "Wrong Answer"
    message = f"{index +1 } {result} - Your answer: {questions['user_choice']}, " \
              f"Correct answer: {questions['correct_answer']}"
    print(message)


print(score, "/", len(data))
