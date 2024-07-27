import json

with open("question_ans.json", 'r') as file:
    file_read = file.read()
    data = json.loads(file_read)

for question in data:
    print(question['question'])

    for index, ans in enumerate(question['option']):
        print(index+1,ans)
    user_choice = int(input("Enter your choice: "))
    question["user_choice"] = user_choice


score = 0
for index, value in enumerate(data):
    if value["correct_answer"] == value["user_choice"]:
        score = score + 1
    print(f"{index+1}. Question you answered {value['user_choice']} and the correct answer is {value['correct_answer']}")


print(f"Your Final Score is {score}/{len(data)}")

