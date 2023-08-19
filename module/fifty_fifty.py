def fifty(que, price_list, i, columns, lifeline, used_lifeline):

    lifeline.remove("50:50(H)")
    used_lifeline.append("H")
    print()
    print()
    print("KBC".center(columns))
    print("_______________________________________________________________".center(columns))
    print("50:50 Lifeline used".center(columns))
    print("_______________________________________________________________".center(columns))
    print(f"Current price : {price_list[i]}                  After this question : {price_list[i + 1]}".center(columns))
    print("_______________________________________________________________".center(columns))
    print(f"Remaining Life line :- {lifeline}".center(columns))
    print("_______________________________________________________________".center(columns))
    print(("" + que[0]).center(columns))
    print()

    options = que[1].split(",")
    if que[2] == "A" or que[2] == "B":
        print(f"{options[0]}                  {options[1]}".center(columns))
    else:
        print(f"{options[2]}                  {options[3]}".center(columns))
    print()
    print("Select an Option : ".center(columns - 15))
    ans = input("".center(70)).upper()
    return ans
