while True:
    name = input("Please enter a name: ")
    if name.isdigit():
        print("Invalid input! Please enter a valid name.")
    else:
        print("\n")
        break

print(f"\t Welcome! {name}\U0001F642 \n")
questions = [
    ["What is the capital of India?", "A. New Delhi", "B. Mumbai", "C. Kolkata", "D. Chennai", "a"],
    ["The International Literacy Day was observed on ?","A. Sep 8","B. Nov 28","C. May 2","D. Sep 22","a"],
    ["What is the capital of France?", "A. London", "B. Madrid", "C. Paris", "D. Rome", "c"],
    ["Which planet is known as the 'Red Planet'?", "A. Jupiter", "B. Mars", "C. Venus", "D. Saturn", "b"],
    ["Which of the following is a mammal?", "A. Frog", "B. Snake", "C. Dolphin", "D. Lizard", "c"],
    ["Who wrote the play 'Romeo and Juliet'?", "A. William Shakespeare", "B. Charles Dickens", "C. Jane Austen", "D. Leo Tolstoy", "a"],
    ["Which gas do plants absorb from the atmosphere?", "A. Carbon dioxide", "B. Oxygen", "C. Hydrogen", "D. Nitrogen", "a"],
    ["In which year did Christopher Columbus discover America?", "A. 1492", "B. 1776", "C. 1620", "D. 1848", "a"],
    ["Which planet is known as the 'Morning Star' or 'Evening Star'?", "A. Jupiter", "B. Mars", "C. Venus", "D. Saturn", "c"],
    ["What is the chemical symbol for gold?", "A. Go", "B. Gd", "C. Au", "D. Ag", "c"],
    ["Which country is known as the 'Land of the Rising Sun'?", "A. China", "B. South Korea", "C. Japan", "D. Thailand", "c"],
    ["Who is the author of 'The Catcher in the Rye'?", "A. J.D. Salinger", "B. F. Scott Fitzgerald", "C. Ernest Hemingway", "D. Mark Twain", "a"],
    ["What is the largest organ in the human body?", "A. Brain", "B. Heart", "C. Liver", "D. Skin", "d"],
    ["Which gas makes up the majority of the Earth's atmosphere?", "A. Oxygen", "B. Carbon dioxide", "C. Nitrogen", "D. Hydrogen", "c"],
    ["In the game of chess, which piece can move diagonally?", "A. Rook", "B. Bishop", "C. Knight", "D. Queen", "b"]
]

amount = [1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000]
sum = 0

for i, Question in enumerate(questions, start=1):
    print(f"Question {i}:\n \t{Question[0]} \n")
    print(f"\t{Question[1]}   {Question[2]} \n \t{Question[3]}    {Question[4]}")
    ans = input("\tEnter the correct option  : ")
    if(ans == Question[5]):
        sum = sum +  amount[0]
        print(f"\n correct answer you have won {sum}\n ")
    else:
        print("\n wrong answer ")
        print("Better Luck next time\n")
        if(i % 2 == 0):
            break
        break
    if(i == 15):
        break
        

print(f"Congatulations u have won Rs - ₹ {sum}")   
print("\n \t------------- THANK YOU ---------------- \n")

ans = input(" If u require the questions with ans for questions type y else type n (y/n)  :-- ")
if(ans == "y"):
    for i, question in enumerate(questions, start=1):
        print(f"Question {i}: \n{question[0]}")
        print(f"Options: {question[1]}, {question[2]}, {question[3]}, {question[4]}")
        match question[5]:
            case "a":
                print(f"\nCorrect Answer: {question[1]} \n")
            case "b":
                print(f"\nCorrect Answer: {question[2]} \n")
            case "c":
                print(f"\nCorrect Answer: {question[3]} \n")
            case "d":
                print(f"\nCorrect Answer: {question[4]} \n")
    print(f"\n \t Thank you for playing {name}\U0001F600 \n \n ")
else:
    print(f"\n \t Thank you for playing {name}\U0001F600 \n \n ")
    