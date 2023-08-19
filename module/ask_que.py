from module import fifty_fifty


def ask_que(que, price_list, i, columns, lifeline, used_lifeline):

    print()
    print()
    print("KBC".center(columns))
    print("_______________________________________________________________".center(columns))
    print(f"Current price : {price_list[i]}                  After this question : {price_list[i+1]}".center(columns))
    print("_______________________________________________________________".center(columns))
    print(f"Remaining Life line :- {lifeline}".center(columns))
    print("_______________________________________________________________".center(columns))
    print(("" + que[0]).center(columns))
    print()

    options = que[1].split(",")

    print(f"{options[0]}                  {options[1]}".center(columns))
    print(f"{options[2]}                  {options[3]}".center(columns))
    print()
    print("Select an Option : ".center(columns-15))
    ans = input("".center(70)).upper()
    while True:
        if ans == que[2]:
            return True
        elif ans in used_lifeline:
            print("You already used this lifeline try a different one".center(columns))
            print("Select a different Option : ".center(columns - 15))
            ans = input("".center(70)).upper()
        elif ans == "H":
            ans = fifty_fifty.fifty(que, price_list, i, columns, lifeline, used_lifeline)
        else:
            return False
