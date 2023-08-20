from module import fifty_fifty
from module import SwitchQuestion
from module import TextToSpeech

def ask_que(que, price_list, i, columns, lifeline, used_lifeline):

    print()
    print()
    print("KBC".center(columns))
    print("_______________________________________________________________".center(columns))
    TextToSpeech.play("Wellcome to Kooun Banegaa Crorepati")
    TextToSpeech.play("Lets play Kooun Banegaa Crorepati")
    print(f"Current price : {price_list[i]}                  After this question : {price_list[i+1]}".center(columns))
    print("_______________________________________________________________".center(columns))
    print(f"Remaining Life line :- {lifeline}".center(columns))
    print("_______________________________________________________________".center(columns))
    print(("" + que[0]).center(columns))
    TextToSpeech.play(que[0])
    print()

    options = que[1].split(",")

    print(f"{options[0]}                  {options[1]}".center(columns))
    print(f"{options[2]}                  {options[3]}".center(columns))

    TextToSpeech.play(f"Your options are: {options}")
    print()
    print("Select an Option : ".center(columns-15))
    ans = input("".center(70)).upper()

    while True:
        if ans == que[2]:
            return True
        elif ans in used_lifeline:
            print("You already used this lifeline try a different one".center(columns))
            print("Select a different Option : ".center(columns - 15))
            TextToSpeech.play("You already used this lifeline try a different one")
            ans = input("".center(70)).upper()
        elif ans == "H":
            ans = fifty_fifty.fifty(que, price_list, i, columns, lifeline, used_lifeline)
        elif ans == "Q":
            ans, que[2] = SwitchQuestion.switch(que, price_list, i, columns, lifeline, used_lifeline)
        else:
            return False
