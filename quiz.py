import time
import json
from colorama import Fore, init
import os


# init colorama
init()

# colors
c = Fore.LIGHTCYAN_EX
r = Fore.LIGHTRED_EX
y = Fore.LIGHTYELLOW_EX
g = Fore.LIGHTGREEN_EX
re = Fore.RESET


class Quiz():
    def __init__(self):
        os.system("clear")
        print("MENU")
        print("")

        self.commands = [
            {
                "name": "add",
                "command": self.add,
                "description": "Adds a new quiz"
            },

            {
                "name": "show",
                "command": self.show,
                "description": "Shows all added quizzes"
            },

            {
                "name": "exit",
                "command": self.exit,
                "description": "Closes this program"
            }
        ]

        for command in self.commands:
            print("[*] " +  "{:<10}".format(command["name"]) + command["description"])

        print("")
        
        cmd = input(y + "[+] " + re)

        for command in self.commands:
            if cmd == command["name"]:
                command["command"]()


    def add(self):
        os.system("clear")
        print("ADD NEW QUIZ")
        print("")

        name = input("[+] Enter Name: ")

        if not os.path.exists("quizzes"):
            os.mkdir("quizzes")

        main_info = {
            "name": name,
            "questions": []
        }

        with open("quizzes/" + name + ".json", "w") as new_quiz:
            json.dump(main_info, new_quiz, indent=4)

        self.add_question(name)


    def add_question(self, filename):
        os.system("clear")
        print("ADD CONTENT TO " + filename.upper())
        print("")

        title = input(y + "[+] Title: " + re)
        
        print("")

        answer_a = input(y + "[+] Answer A: " + re)
        is_right_a = input(y + "[+] Is Answer A right? [true, false]: " + re)
        
        print("")

        answer_b = input(y + "[+] Answer B: " + re)
        is_right_b = input(y + "[+] Is Answer B right? [true, false]: " + re)

        question = {
            "title": title,

            "a": {
                "text": answer_a,
                "is_right": is_right_a
            },

            "b": {
                "text": answer_b,
                "is_right": is_right_b
            }
        }

        with open("quizzes/" + filename + ".json", "r") as read_file:
            data = json.load(read_file)

        data["questions"].append(question)

        with open("quizzes/" + filename + ".json", "w") as write_file:
            json.dump(data, write_file, indent=4)
        
        print("")

        print(c + "[*] " + re + "Done!")
        again = input(y +"[+] Again? [Y|n]: " + re)

        if again == "" or again == "Y" or again == "y":
            self.add_question(filename)
        else:
            self.__init__()

    
    def show(self):
        os.system("clear")
        print("SHOW ALL QUIZZES")
        print("")

        quizzes = []

        for quiz in os.scandir("quizzes"):
            quizzes.append(quiz.name)

        quizzes.sort()
    
        for index, q in enumerate(quizzes, 1):
            print(c + "[" + str(index) + "] " + re + q)
        
        print("")

        select = input("[+] Enter number to select: ")

        print("")
        print("[*] p = Play")
        print("[*] a = Add content")
        print("[*] s = Show content")
        print("[*] b = Back to menu")
        print("")

        action = input(y + "[+] Enter Action: " + re)

        if action == "p":
            self.play(quizzes[int(select) - 1])

        elif action == "a":
            self.add_question(quizzes[int(select) - 1].split(".")[0])

        elif action == "s":
            self.show_content(quizzes[int(select) - 1])

        elif action == "b":
            self.__init__()

        else:
            self.__init__()


    def play(self, filename):
        os.system("clear")
        print("PLAY " + filename.upper())

        with open("quizzes/" + filename, "r") as read_file:
            data = json.load(read_file)

        for question in data["questions"]:
            print("")

            print(c + "[?] " + question["title"] + re)
            print(c + "[a] " + re + question["a"]["text"])
            print(c + "[b] " + re + question["b"]["text"])

            print("")

            ans = input(y + "[+] Answer: " + re)

            if question[ans]["is_right"] == "true":
                print(g + "[*] " + re + "Right answer!")
            else:
                print(r + "[*] " + re + "Wrong answer!")
        
        print("")

        input(y + "[+] Press enter to go to start ..." + re)

        self.__init__()


    def show_content(self, filename):
        os.system("clear")
        print("SHOW " + filename.upper())
        
        with open("quizzes/" + filename, "r") as read_file:
            data = json.load(read_file)

        for question in data["questions"]:
            print("")

            print(c + "[?] " + question["title"] + re)
            print(c + "[a] " + re + question["a"]["text"])
            print(c + "[b] " + re + question["b"]["text"])

        print("")

        input(y + "[+] Press enter to go to start ..." + re)

        self.__init__()

    
    def exit(self):
        print("")
        print(r + "[!] " + re + "Program closed.")
        exit()


Quiz()
