import que
import time
from ask_que import ask_que
import shutil
    

questions = que.read_que()

prize_list = [
    "₹0",
    "₹1000",
    "₹2000",
    "₹5000",
    "₹10000",
    "₹20000",
    "₹40000",
    "₹80000",
    "₹160000",
    "₹320000",
    "₹640000",
    "₹1250000",
    "₹2500000",
    "₹5000000",
    "₹10000000",
    "₹70000000"
]

# Get windows size
terminal_size = shutil.get_terminal_size()
rows, columns = terminal_size.lines, terminal_size.columns

columns += 50


lifeline = ["50:50(H)", "Audience Poll(P)", "Switch the Question(Q)", "Double Dip(U)"]
used_lifeline = []

for i in range(15):

    question = [questions["Questions"][i], questions['Options'][i], questions['Answers'][i]]
    print()

    if ask_que(question, prize_list, i, columns, lifeline, used_lifeline):
        if i == 14:
            print("Correct Answer.".center(columns))
            print(f"Congratulations! You won {prize_list[i]}".center(columns))
            break
        print("Correct Answer. Next Question in 5 second".center(columns))
        time.sleep(5)

    else:
        print("Incorrect Answer!".center(columns))
        print(f"Correct Answer is option {question[2]}".center(columns))
        if i == 0:
            print("Unfortunately, you didn't win any prize. Better luck next time!".center(columns))
            break
        print(f"Congratulations! You won {prize_list[i]}".center(columns))
        break



if __name__ == '__main__':
    pass
