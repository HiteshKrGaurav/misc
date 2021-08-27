import time


# Some variables

Times = 5

# Welcome Function


def welcome():
    level = 20
    print("\nWelcome to Meditation timer Program\n")
    print("Enter your Level of Nadi Shodhan")
    print("1. level 1 (10-10-10)")
    print("2. level 2 (10-20-10)")
    print("3. level 3 (10-20-20)")
    print("4. level pro (10-40-20)")

    level = int(input("\nlevel :"))
    print("\n")

    if(level == 1):
        l1()
    elif(level == 2):
        l2()
    elif(level == 3):
        l3()
    elif(level == 4):
        l4()


# Required functions

def l1():
    print("Level 1\n")
    for i in range(Times):
        for j in range(5):
            for k in range(3):
                time.sleep(10)
                print("\a")


def l2():
    print("Level 2\n")
    for i in range(Times):
        for j in range(5):
            print("Breath in")
            time.sleep(10)
            print("\a")
            print("Hold")
            time.sleep(20)
            print("\a")
            print("Breath out")
            time.sleep(10)
            print("\a")


def l3():
    print("Level 3\n")
    for i in range(Times):
        for j in range(5):
            print("Breath in")
            time.sleep(10)
            print("\a")
            print("Hold")
            time.sleep(20)
            print("\a")
            print("Breath out")
            time.sleep(20)
            print("\a")


def l4():
    print("Level 4\n")
    for i in range(Times):
        for j in range(5):
            print("Breath in")
            time.sleep(10)
            print("\a")
            print("Hold")
            time.sleep(40)
            print("\a")
            print("Breath out")
            time.sleep(20)
            print("\a")


if __name__ == '__main__':
    welcome()
