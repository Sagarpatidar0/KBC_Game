from module import que as ques, TextToSpeech


def switch(que, price_list, i, columns, lifeline, used_lifeline):

    questions = ques.read_que_switch()
    que = [questions["0"][i], questions["1"][i], questions["2"][i]]

    lifeline.remove("Switch the Question(Q)")
    used_lifeline.append("Q")
    print()
    print()
    print("KBC".center(columns))
    print("_______________________________________________________________".center(columns))
    print("Switch the Question Lifeline used".center(columns))
    TextToSpeech.play("You just use Switch the Question Lifeline, Question is changed, New question is :.")
    print("_______________________________________________________________".center(columns))
    print(f"Current price : {price_list[i]}                  After this question : {price_list[i + 1]}".center(columns))
    print("_______________________________________________________________".center(columns))
    print(f"Remaining Life line :- {lifeline}".center(columns))
    print("_______________________________________________________________".center(columns))
    print(("" + que[0]).center(columns))
    print()
    TextToSpeech.play(que[0])

    que[1] = que[1].replace("'", "")
    que[1] = que[1].replace("[", "")
    que[1] = que[1].replace("]", "")
    options = que[1].split(",")

    print(f"{options[0]}                  {options[1]}".center(columns))
    print(f"{options[2]}                  {options[3]}".center(columns))
    print()
    TextToSpeech.play(f"Your options are: {options}")

    print("Select an Option : ".center(columns - 15))
    print(que[2])

    ans = input("".center(70)).upper()
    return ans, que[2]
