from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
question_num = 0


for new_question in question_data:
    question_bank.append(Question(q_text=question_data[question_num]["text"], q_answer=question_data[question_num]["answer"]))
    question_num += 1

quizbrain = QuizBrain(question_bank)

while quizbrain.still_has_questions():
    quizbrain.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quizbrain.score} / {len(quizbrain.question_list)}")







