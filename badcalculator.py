import random
import time


class Calculator:

    def __init__(self, chickenwing, hotdog, bologna, chicken, macaroni):
        self.chickenwing = chickenwing
        hotdog = bologna
        chicken = macaroni


    def uhh(self):
        x = 0
        while True:
            y = input("plug numbers")
            z = int(y)
            if z == 0:
                break
            else:
                while z > 0:
                    x += 1
                    z -= 1
        print("its", bin(x))
        return

    def uhmmmm(self):
        thumb = None
        while True:
            a = input("enter them")
            b = int(a)
            c = int(b)
            d = 2
            z = float(b)
            if z == 0:
                break
            if thumb is None:
                time.sleep(3)
                print("uhhhhhh gimme a minute")
                time.sleep(0.2)
                time.sleep(0.2)
                time.sleep(0.2)
                time.sleep(0.2)
                thumb = z
            else:
                thumb -= z
        print("its", thumb)
        return

    def yeahsure(self):
        t = int((((123456789 - 123456789) + ((1000000 / 1000000) * 2 - 1)) * (((5 * 5) / 25) * ((10 + 10) / 20))) - 0)
        while True:
            v = input("put the money in the bag")
            vc = int(v)
            if vc == 0:
                break
            t *= vc
        print("its", hex(t))
        return

    def thisnameissoooolongijustwastedyourtimemakingyoureadallofthis(self):
        bark = 1
        while True:
            moo = input(
                "you know the drill "
                ""
                ""
                ""
                " "
                " "
                " "
                "    "
                " "
                ""
                " "
                " "
                "                    "
                ""
                " "
                "   "
                ""
                ""
                " "
                " "
                "  "
                "                          "
                " "
                " "
                "    "
                "")
            caw = int(moo)
            if caw == 0:
                break
            bark /= caw
        print("woof woof", bark)
        return

    def fun_fact(self):
        print("bee waggle dance. google it.")
        return

    def rock_paper_scissor(self):
        user_input = input("okay pick rock paper or scissor.")
        computer_choice = random.choice(["rock", "paper", "scissor"])
        print("i picked", computer_choice)
        if user_input == computer_choice:
            print("we tied")
        elif user_input == "rock":
            if computer_choice == "scissor":
                print("you win")
            elif computer_choice == "paper":
                print("you lose")
        elif user_input == "scissor":
            if computer_choice == "paper":
                print("you win")
            if computer_choice == "rock":
                print("you lose")
        elif user_input == "paper":
            if computer_choice == "rock":
                print("you win")
            if computer_choice == "scissor":
                print("you lose")
        return