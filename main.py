import que
import time
from ask_que import ask_que

questions = que.read_que()

prize_list = [
    "₹0",
    "₹100",
    "₹200",
    "₹300",
    "₹500",
    "₹1000",
    "₹2000",
    "₹4000",
    "₹8000",
    "₹16000",
    "₹32000",
    "₹64000",
    "₹125000",
    "₹250000",
    "₹500000",
    "₹1000000"
]

for i in range(14):

    question = [questions["Questions"][i], questions['Options'][i], questions['Answers'][i]]
    print()
    if ask_que(question, prize_list, i):
        print("Correct Answer. Next Question in 5 second".center(175))
        time.sleep(5)

    else:
        print("Incorrect Answer!".center(175))
        print(f"Correct Answer is option {question[2]}".center(175))
        if i == 0:
            print("Unfortunately, you didn't win any prize. Better luck next time!".center(175))
            break
        print(f"Congratulations! You won {prize_list[i]}".center(175))
        break



if __name__ == '__main__':
    pass
