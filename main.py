print("Добро пожаловать в викторину по школе")
print("Ответь на слейдущий вопрос.")
#question = "Как расшифровываеться Физ-ра"
#answer = 'Физическая культура'
#print(question)

#user = input("Ответ: ")
#if user.lower() == answer.lower():
#  print("Правильно")
#else:
#  print("Неправльно")

questions = [
"1. Как расшифровываеться Физ-ра?",
"2. В каком классе появляется Физика?(только число)",
"3. В каком классе появляется Информатика?(только число)",
"4. На какие предметы делится Окружающий мир в 5 классе(без запятых, по алфавиту, в И.П.)?",
"5. На какие два предметы делится Математика в 7 классе(без запятых, по алфавиту, в И.П.)?",
"6. В каком классе ученик переходит в старшую школу(только число)?",
"7. Самая худшая оценка(без минусов)"]

answers = [
"Физическая культура",
"7",
"7",
"Биология История Обществознание",
"Алгебра Геометрия",
"10",
"1"]

print(questions[0])
user = input("Ответ: ")
if user.lower() == answers[0].lower():
  print("Правильно")
else:
  print("Неправильно") 

print(questions[1])
user = input("Ответ: ")
if user.lower() == answers[1].lower():
  print("Правильно")
else:
  print("Неправильно")

print(questions[2])
user = input("Ответ: ")
if user.lower() == answers[2].lower():
  print("Правильно")
else:
  print("Неправильно")

print(questions[3])
user = input("Ответ: ")
if user.lower() == answers[3].lower():
  print("Правильно")
else:
  print("Неправильно")

print(questions[4])
user = input("Ответ: ")
if user.lower() == answers[4].lower():
  print("Правильно")
else:
  print("Неправильно")

print(questions[5])
user = input("Ответ: ")
if user.lower() == answers[5].lower():
  print("Правильно")
else:
  print("Неправильно")