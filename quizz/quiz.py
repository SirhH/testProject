print("Choose your quiz, use the numbers 1,2,3 or 4 as input")
print("1. Let me guess your favourite color")
print("2. Are you in a good mood?")
print("3. Do you know your css?")
print("4. Let me guess your card")

quiz = input("please enter your choice: ")
questions_for_quiz_1 = ["Wich of these colors do you prefer?", "In case of brightness, what do you choose?",
                        "Please let me know of your prefered saturation:"]
questions_for_quiz_2 = ["", "", "", "", "", "", "", "", "", ""]
questions_for_quiz_3 = ["", "", "", "", "", "", "", "", "", ""]
questions_for_quiz_4 = ["Of the given suits, which one is the closest one to yours?",
                        "Of the given ranks, which one is the closest to yous?"]
print(quiz)