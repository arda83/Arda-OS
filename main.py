print("Welcome")

from alive_progress import alive_bar
from time import sleep
def smallprograms():
    print("Here are the smaller Programs")
    time.sleep(int(1))
    print("1.Number Sorter")
    time.sleep(int(1))
    print("2.Area Of A Triangle Calculator")
    time.sleep(int(1))
    print("3.Todays Date And Time")
    time.sleep(int(1))
    print("4.Random Number Generator")
    time.sleep(int(1))
    print("(Anything Else). Close Program And Return To Main Menu")

    print("Which One Would You Like To Choose")
    smallprogramchoice = input()
    while smallprogramchoice != "Z":
        if smallprogramchoice == "1":
            print("Number Sorter Selected")
            print("Please select a number")
            numbers = input()
            print("Please Select The Second Number")
            numbers2 = input()
            print("Please Select The Third Number")
            numbers3 = input()
            num_strings = [numbers,numbers2,numbers3]

            num_strings.sort(key=int)
            print(num_strings)

            smallprograms()
        if smallprogramchoice == "2":
            print("Triangle Area Solver Selected")
            time.sleep(int(1))
            a = float(input('Enter first side: '))
            b = float(input('Enter second side: '))
            c = float(input('Enter third side: '))
            s = (a + b + c) / 2
            area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
            print('The area of the triangle is %0.2f' % area)
            print("A Would you like to go back to the main menu?")
            print("B Use another smaller program?")
            mainmenuselection = input()
            if mainmenuselection == "A":
                programs()
            if mainmenuselection == "B":
                smallprograms()
            else:
                print("Incorrect Input, Going Back To Main Menu")
                programs()

        if smallprogramchoice == "3":
            from datetime import datetime
            now = datetime.now()
            print("now =", now)
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            print("date and time =", dt_string)
            smallprograms()

        if smallprogramchoice == "4":
            import random
            print(random.randint(0, 100))
            smallprograms()


        if smallprogramchoice == "Z":
            programs()
        else:
            programs()
    else:
        programs()

def forestgame():
    print("Game Opening! Get Ready")
    time.sleep(int(5))
    print("Welcome To ECM(Every Choice Matters)")
    print("Press enter to continue")
    input()
    print("Loading game.....")
    time.sleep(int(3))
    print(
        "You wake up In a dark forest you see a car that has one of its lights broken, what do you do? (go to car or explore the forest)")
    wakeup = input()
    if wakeup == "go to car":
        print(
            "You go near the car, you see an crowbar and a flashlight. You want to pick up both but dont have enough space for it What do you pick(Crowbar or Flashlight")
        item = input()
        if item == "Flashlight":
            print("You pick up the flashlight and open It, you go towards the door of the car ")
            time.sleep(int(3))
            print(
                "You open the door and see a person, you try to wake him up but you cant, you proceed near the back door and see a phone. You pick up the phone and dial 911")
            time.sleep(int(3))
            print(
                " 911, Whats your emergency?, You say that you are In a forest and dont know how you came here,The operator responds that they cant track your location and thinks you made a prank call. ")
            time.sleep(int(3))
            print("The operator hangs up the phone and you lie down, and start sleeping ")
            time.sleep(int(2))
            print(
                "You wake up to the sound of a police siren, and see a light. You try to speak but cant speak because you have a duct tape over your mouth.")
            time.sleep(int(2))
            print(
                "You get up and start running towards the light, a police officer sees you and starts running to you.")
            time.sleep(int(2))
            print("The officer gets you to his car and brings you to the police station")
            time.sleep(int(2))
            print("You call your father and go back to your home")
            time.sleep(int(2))
            print("Happy Ending Achieved")
            time.sleep(int(2))
            Happy_Ending = 1
            programs()
        if item == "Crowbar":
            print(
                "You pick up the crowbar and start trying to open the trunk of the car, after a few tries you get It open and see a child")
            time.sleep(int(3))
            print("He says that you should save him,")
            time.sleep(int(2))
            print("You ask where we are, he says that this forest Is 20 kilometers away from the city.")
            time.sleep(int(2))
            print("You remember that you could carry the child and bring him to the city")
            time.sleep(int(2))
            print(
                "You also remember that If you carry him to the city you might not make It out since you are starving already.")
            time.sleep(int(2))
            print("What will you do?, save the child or not save the child")
            whatdo = input()

            if whatdo == "save the child":
                print("You pick up the child and start walking towards the town, when you finally see the city lights you fall down, and start getting sleepy,you can feel that you are going to sleep forever")
                time.sleep(int(3))
                print("A life for a life Ending Achieved")
                print("Game Ended, Going back to AA-DOS")
                time.sleep(int(2))
                Hero = 1
                programs()

            elif whatdo == "not save the child":
                print("You both lie down and start sleeping, knowing you will not be able to wake up")
                time.sleep(int(2))
                print("Bad Ending Achieved")
                print("Game Ended, Going back to AA-DOS")
                time.sleep(int(2))
                Child_Murderer = 1
                programs()

            else:
                print("Wrong answer Going back to AA-DOS")
                programs()
        else:
            print("Wrong answer Going back to AA-DOS")
            programs()
    elif wakeup == "explore the forest":
        print("You start going towards the trees,until sometime you slip and fall Into a animal trap In the ground")
        time.sleep(int(2))
        print("You start screaming for help but no one responds, you start getting colder as the night progresses,")
        time.sleep(int(2))
        print("After sometime you close your eyes and hope for the best")
        time.sleep(int(2))
        print("Cold and Dark Ending Achieved")
        a = 1
        programs()
    else:
        print("Wrong Input Going Back To AA-DOS")
        programs()



def notepad():
    print("Notepad Opening....")
    time.sleep(int(1))
    print("If At Anytime You Want to Close The Program Type - ")
    time.sleep(1)
    notepadwriting = ""
    print("You Can Now Start Typing, If You Want to Save Your Changes And Close The Program Type - ")
    with open("Notepad.txt", "a+") as f:
        while notepadwriting != "-":
            print("-----------------------------------")
            notepadwriting = input()
            f.write("\n" + notepadwriting)
        if notepadwriting == "-":
            print("Closing Program/ Returning To Main Menu")
            f.close()
            programs()


def bankprogram():
    print("Welcome to the Bank of Simpletown")
    print("******************************************************************")
    print("Please Select an option from below")
    print("A) Register")
    print("B) Login")
    print("C) Exit")
    reglog = input()
    while reglog != "C":
        if reglog == "A":
            print("Registiration service selected, opening registiration form")
            time.sleep(int(2))
            print("Please start by telling us a username")
            username = input()
            if username == "Admin":
                print("You are trying to access the Admin Account")
                print("Failure In Doing So Will Close The Program")
                time.sleep(int(2))
                print("Please Write Your 5 Digit Master access code password (Admin password)")
                adminpass = input()
                if adminpass == "98543":
                    print("Welcome To The Admin Database")
                    time.sleep(int(2))
                    print("Would you like to see all the registered accounts? A")
                    print("Would you like to delete all the registered accounts? B")
                    print("Would you like to exit the aplication? C")
                    adminselection = input()
                    while adminselection != "C":
                        if adminselection == "A":
                            file1 = open("Arda.txt", "a+")
                            f = open("Arda.txt", "r")
                            print(f.read())
                            print("Action Completed, Returning to Admin Database")
                            adminselection = input()

                        if adminselection == "B":
                            print(
                                "Are you sure you want to delete all present accounts?, This will delete everything!")
                            file1 = open("Arda.txt", "a+")
                            file1.write(" ")
                            filedata = file1.read()
                            with open("Arda.txt", "w") as f:
                                f.write("")
                                f.close()
                            adminselection = input()
                    if adminselection == "C":
                        print("Closing Program")
                        programs()
                    else:
                        programs()

            else:
                file1 = open("Arda.txt", "a+")
                print("Please tell us a password")
                password = input()
                passuserfortxt = "\n" + username + " " + password
                file1.write(passuserfortxt)
                print(
                    "We have given you a starting balance of 1000, If you want to deposit/withdrawal/check balance please login.")
                initialbalance = " " + "1000"
                file1.write(str(initialbalance))
                file1.close()
                print("Thanks for Registering an account")
                print("A) Go Back To Main Menu")
                print("B) Exit the Program")
                regdesicion = input()
                if regdesicion == "A":
                    bankprogram()
                elif regdesicion == "B":
                    print("Bye Hope You Enjoyed Your Time")
                    programs()
                else:
                    print("Incorrect Input")
                    programs()


        elif reglog == "B":
            file1 = open("Arda.txt", "a+")
            print("Login services selected")
            time.sleep(int(1))
            print("Please enter your username")
            usernamelogon = input()
            print("Please tell us your password")
            passwordlogon = input()
            logon = usernamelogon + " " + passwordlogon
            file_name = "Arda.txt"

            def check_if_string_in_file(file_name, string_to_search):
                """ Check if any line in the file contains given string """

                with open("Arda.txt", 'r') as read_obj:

                    for line in read_obj:

                        if string_to_search in line:
                            return True
                return False

            if check_if_string_in_file('sample.txt', str(logon)):
                print('Account Found')
                time.sleep(int(1))
                print("Would you like to deposit or withdraw? To Check your balance type L")
                depodraw = input()
                if depodraw == "deposit":
                    print("Deposit selected")
                    programs()

                if depodraw == "withdraw":
                    print("This works with withdraw")
                    programs()
            else:
                print('Username or password Incorrect')
                programs()
    else:
        bankprogram()
    if reglog == "C":
        print("Bye")
        programs()

    else:
        print("Incorrect Input try again")
        bankprogram()

import time
time.sleep(int(1))
def Osstart():
    import time
    print("Booting Up....")
    time.sleep(int(2))
    print("AA-DOS Installing")
    time.sleep(int(2))
    print("Please Wait For Instillation")
    time.sleep(int(2))
    print("Instillation Complete.......")
    print("Os Loading.....")
    time.sleep(int(2))
    print("Welcome To Arda OS")
    time.sleep(int(1))
    print("The First Operating System Ever To Be Written In Python")
    time.sleep(int(2))
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print("                                                                 Arda Os                                                                                     ")
    print(" ")
    print(" ")

def start():
    import time
    print("Doing Diagnostics On The Operating System")
    time.sleep(2)
    print("Hard Disk Found")
    for x in 50, 60 :
        with alive_bar(x) as bar:
            for i in range(x):
                time.sleep(.001)
                bar()
    print("Cpu And Gpu, Is Working Properly")
    with alive_bar(100) as bar:
        for i in range(100):
            sleep(0.03)
            bar()
    print("System Files Are All Fine")
    with alive_bar(100) as bar:
        for i in range(100):
            sleep(0.03)
            bar()
    print("Initiating Arda-OS")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(":::'###::::'########::'########:::::'###::::::::::::::'#######:::'######::")
    print("::'## ##::: ##.... ##: ##.... ##:::'## ##::::::::::::'##.... ##:'##... ##:")
    print(":'##:. ##:: ##:::: ##: ##:::: ##::'##:. ##::::::::::: ##:::: ##: ##:::..::")
    print("'##:::. ##: ########:: ##:::: ##:'##:::. ##:'#######: ##:::: ##:. ######::")
    print(" #########: ##.. ##::: ##:::: ##: #########:........: ##:::: ##::..... ##:")
    print(" ##.... ##: ##::. ##:: ##:::: ##: ##.... ##:::::::::: ##:::: ##:'##::: ##:")
    print(" ##:::: ##: ##:::. ##: ########:: ##:::: ##::::::::::. #######::. ######::")
    print("..:::::..::..:::::..::........:::..:::::..::::::::::::.......::::......:::")
    print("")
    from tqdm import tqdm
    import time
    pbar = tqdm(total=100)

    for i in range(20):
        time.sleep(0.1)
        pbar.update(5)
    pbar.close

    print(" ")
    print("Please Wait Until The System Starts")

    time.sleep(20)
    print(" ")
    OsUserSelect()


def OsUserSelect():
    print("Please Select A User By Typing Its Full Name")
    time.sleep(int(1))
    print("Admin")
    OsUserSelection = input()
    if OsUserSelection == "Admin":
        print("Admin User Selected, Please Enter The Admin Password")
        Adminpass = input()
        if Adminpass == "7648":
            print("Password Is Correct, Booting Up Selected User")
            programs()
        if Adminpass != "7648":
            print("Wrong Password")
            time.sleep(int(1))
            print("Going Back To User Selection")
            OsUserSelect()
    else:
        print("Wrong Input Going Back To User Selection")
        time.sleep(int(1))
        OsUserSelect()

    #These Lines Represent The Programs And The User Will Make The Selection By Using Letters Assigned To The Programs
    print("Please Select The Program That You Will Be Using")
def programs():
    print("A Calculator")
    print("B Banking System")
    print("C Notepad")
    print("D Forest The Game")
    print("E Other Smaller Settings"),
    print("F Game Achievements")
    print("Anything Else Will Close The Operating System")
    ProgramSelection = input()
    while ProgramSelection != "L":
        if ProgramSelection == "A":
            print("Calculator")


            def add(x, y):
                return x + y


            def subtract(x, y):
                return x - y


            def multiply(x, y):
                return x * y


            def divide(x, y):
                return x / y


            print("Select operation.")
            print("1.Add")
            print("2.Subtract")
            print("3.Multiply")
            print("4.Divide")
            print("5.Close Program")

            while True:
                choice = input("Enter choice(1/2/3/4/5): ")
                if choice in ('1', '2', '3', '4'):
                    num1 = float(input("Enter first number: "))
                    num2 = float(input("Enter second number: "))

                    if choice == '1':
                        print(num1, "+", num2, "=", add(num1, num2))

                    elif choice == '2':
                        print(num1, "-", num2, "=", subtract(num1, num2))

                    elif choice == '3':
                        print(num1, "*", num2, "=", multiply(num1, num2))

                    elif choice == '4':
                        print(num1, "/", num2, "=", divide(num1, num2))

                    programs()
                if choice == "5":
                    programs()

                else:
                    print("Invalid Input")
                    break

        if ProgramSelection == "B":
            bankprogram()

        if ProgramSelection == "C":
            notepad()

        if ProgramSelection == "D":
            forestgame()

        if ProgramSelection == "E":
            smallprograms()

        if ProgramSelection == "F":

            programs()

        else:
            print("Wrong Input Closing System")
            break

def programstart():
    Osstart()
    start()
    OsUserSelect()
    programs()

programstart()




