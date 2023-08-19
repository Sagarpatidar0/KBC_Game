def ask_que(que, price_list, i):
    print()
    print()
    print("KBC".center(175))
    print(f"Current price : {price_list[i]}                  After this question : {price_list[i+1]}".center(175))
    print("-------------------------------------------------------------".center(175))
    print(("" + que[0]).center(175))
    print()

    options = que[1].split(",")

    print(f"{options[0]}                  {options[1]}".center(175))
    print(f"{options[2]}                  {options[3]}".center(175))
    print()
    print("Select an Option : ".center(160))
    ans = input("".center(90)).upper()

    if ans == que[2]:
        return True
    else:
        return False

