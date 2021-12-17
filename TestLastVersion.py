from random import shuffle



        
        
def s1():
    try:
        print("What is the number of states in USA?")
        c1 = ['49', '50', '60']
        shuffle(c1)
        corr = "CORRECT"
        incorr = "INCORRECT"
        x = 0
        for i in c1:
            x = x+1
            print(str(x) + '. ' + i)
        cavab = input('My choice: ')
        if int(cavab) < 1 or int(cavab) > 3:
            print('☠ Pick a number between 1 and 3 ☠')
            s1()
        elif c1[int(cavab)-1] == '50':
            return (corr)
        else:
            return (incorr)
    except ValueError:
        print('☠ Enter only number of answer ☠')
        s1()

def s2():
    try:
        print("What is the capital of Azerbaijan?")
        c1 = ['Cairo', 'Kyiv', 'Baku']
        shuffle(c1)
        corr = "CORRECT"
        incorr = "INCORRECT"
        x = 0
        for i in c1:
            x = x+1
            print(str(x) + '. ' + i)
        cavab = input('My choice: ')
        if int(cavab) < 1 or int(cavab) > 3:
            print('☠ Pick a number between 1 and 3 ☠')
            s1()
        elif c1[int(cavab)-1] == 'Baku':
            return (corr)
        else:
            return (incorr)
    except ValueError:
        print('☠ Enter only number of answer ☠')
        s2()

def s3():
    try:
        print("What is the capital city of the Russian Federation?")
        c1 = ['St. Petersburg', 'Moscow', 'Geneva']
        shuffle(c1)
        corr = "CORRECT"
        incorr = "INCORRECT"
        x = 0
        for i in c1:
            x = x+1
            print(str(x) + '. ' + i)
        cavab = input('My choice: ')
        if int(cavab) < 1 or int(cavab) > 3:
            print('☠ Pick a number between 1 and 3 ☠')
            s1()
        elif c1[int(cavab)-1] == 'Moscow':
            return (corr)
        else:
            return (incorr)
    except ValueError:
        print('☠ Enter only number of answer ☠')
        s3()

def s4():
    try:
        print("What is the leader of Germany called?")
        c1 = ['President', 'Chancellor', 'Emperor']
        shuffle(c1)
        corr = "CORRECT"
        incorr = "INCORRECT"
        x = 0
        for i in c1:
            x = x+1
            print(str(x) + '. ' + i)
        cavab = input('My choice: ')
        if int(cavab) < 1 or int(cavab) > 3:
            print('☠ Pick a number between 1 and 3 ☠')
            s1()
        elif c1[int(cavab)-1] == 'Chancellor':
            return (corr)
        else:
            return (incorr)
    except ValueError:
        print('☠ Enter only number of answer ☠')
        s4()

def s5():
    try:
        print("Which countries are the Talysh Mountains in?")
        c1 = ['Azerbaijan & Iran', 'Georgia & Armenia', 'Turkey & Cyprus']
        shuffle(c1)
        corr = "CORRECT"
        incorr = "INCORRECT"
        x = 0
        for i in c1:
            x = x+1
            print(str(x) + '. ' + i)
        cavab = input('My choice: ')
        if int(cavab) < 1 or int(cavab) > 3:
            print('☠ Pick a number between 1 and 3 ☠')
            s1()
        elif c1[int(cavab)-1] == 'Azerbaijan & Iran':
            return (corr)
        else:
            return (incorr)
    except ValueError:
        print('☠ Enter only number of answer ☠')
        s5()



def go_back():
    try:
        print('Do you want to return to the quiz?')
        c1 = ['Yes', 'No']
        x = 0
        for i in c1:
            x = x+1
            print(str(x) + '. ' + i)
        cavab = input('My choice: ')
        if int(cavab) < 1 or int(cavab) > 2:
            print('☠ Pick a number between 1 and 2 ☠')
            go_back()
        elif c1[int(cavab)-1] == 'Yes':
            start()
        else:
            exit()
    except ValueError:
        print('☠ Enter only number of answer ☠')
        go_back()
    


def start():
    test = [s1, s2, s3, s4, s5]
    shuffle(test)
    corr = 0
    incorr = 0
    for i in test:
        if i() == 'CORRECT':
            print('Answer is correct')
            corr += 1
        else:
            print('Answer is incorrect')
            incorr += 1
    print(f"Total of correct answers:{corr}; Total of incorrect answers:{incorr}")
    go_back()



start()








