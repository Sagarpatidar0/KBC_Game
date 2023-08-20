import pandas as pd


def read_que():
    questions = pd.read_csv("Data/question_bank.csv")
    return questions

def read_que_switch():
    questions = pd.read_csv("Data/question_bank_switch.csv")
    return questions

def save_que(que_data):
    que_data.to_csv('question_bank.csv', index=False)



if __name__ == '__main__':
    pass

