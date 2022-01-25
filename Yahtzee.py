import collections


class Game:
    def __init__(self):
        self.player_count = 0
        self.score = [[]]
        self.available_options = [[]]
        self.cut = [[]]
        self.count = 0
        self.players = []
        self.dice = []
        self.calculate = 0

    def start(self):
        # setting player count
        while True:
            try:
                self.player_count = int(input("how many players? "))
                if self.player_count > 10 or self.player_count < 2:
                    raise Exception
                break
            except Exception:
                print("Please enter a number between 2 and 10")
                continue

        # setting up 2d arrays for each player's score, available options and what they cut
        self.score = [[0 for i in range(14)] for j in range(self.player_count)]

        self.available_options = [
            [True for i in range(14)] for j in range(self.player_count)]
        # setting last element in the list to false for the bonus yahtzee
        for i in self.available_options:
            i[13] = False

        self.cut = [["" for i in range(13)] for j in range(self.player_count)]

        # for tracking which player's turn it is
        self.count = 0

        self.players = []
        # set the players' names
        for i in range(self.player_count):
            self.players.append(input(f"give player {i + 1} name: ").upper())

        print("Hello " + self.players[0], end="")
        for i in self.players:
            if i != self.players[0]:
                print(" and " + i, end="")

    def rules(self):
        print("\n\nYour turn " + self.players[self.count])
        # printing the scores for all the different options
        print(
            f"\n\Aces      .      {self.score[self.count][0]} {self.cut[self.count][0]}                      3 of a kind XXX                     {self.score[self.count][6]} {self.cut[self.count][6]}\n\n")
        print(
            f"        .                                4 of a kind XXXX                    {self.score[self.count][7]} {self.cut[self.count][7]}\nTwos             {self.score[self.count][1]} {self.cut[self.count][1]}\n            .")
        print(
            f"                                         Full House XXYYY                    {self.score[self.count][8]} {self.cut[self.count][8]}\n        .\nThrees    .      {self.score[self.count][2]} {self.cut[self.count][2]}\n            .                            Sm Straight x(x+1)(x+2)(x+3)        {self.score[self.count][9]} {self.cut[self.count][9]}\n")
        print(
            f"        .   .\nFours            {self.score[self.count][3]} {self.cut[self.count][3]}                      Lg Straight x(x+1)(x+2)(x+3)(x+4)   {self.score[self.count][10]} {self.cut[self.count][10]}\n        .   .\n")
        print(
            f"        .   .                            Yahtzee XXXXX                       {self.score[self.count][11]} {self.cut[self.count][11]}\nFives     .      {self.score[self.count][4]} {self.cut[self.count][4]}\n        .   .")
        print(
            f"                                         Chance (anything)                   {self.score[self.count][12]} {self.cut[self.count][12]}\n        .   .\nSixes   .   .    {self.score[self.count][5]} {self.cut[self.count][5]}\n        .   .                            Yahtzee BONUS XXXXX                 {self.score[self.count][13]}\n")
        upper_total = sum(self.score[self.count][:6])
        lower_total = sum(self.score[self.count][6:14])
        bonus_total = 0
        if upper_total >= 63:
            bonus_total += 35
        print("TOTAL SCORE = " + str(upper_total))
        print(
            f"TOTAL of upper section = {upper_total + bonus_total}               TOTAL of lower section = {lower_total}")
        print("BONUS +35 if total is 63 or over \n")

        total = sum(self.score[self.count]) + bonus_total
        print("\n                          GRAND TOTAL = " + str(total) + "\n")

    def dice_roll(self):
        while True:
            # try statement in case the user input is wrong
            try:
                # taking the user's dice as input and making sure it is 5 dice of value between 1 to 6
                dice_throw = input("\nWhat did you roll ")
                print("\n")
                self.dice = dice_throw.split()
                new_dice = []
                for i in self.dice:
                    if len(i) > 1:
                        for j in str(i):
                            new_dice.append(j)
                    else:
                        new_dice.append(i)

                self.dice = [int(i) for i in new_dice]
                for i in self.dice:
                    if i < 1 or i > 6 or len(self.dice) != 5:
                        raise Exception
                if not self.dice:
                    raise Exception
                break
            except Exception:
                print("Please enter the real dice value")
                continue

    # functions for checking whether each option is available or not for each player
    def one_er_availability(self):
        if not self.available_options[self.count][0]:
            return

        if 1 in self.dice:
            predict = 0
            for i in self.dice:
                if i == 1:
                    predict += 1
            print("(1) Aces is AVAILABLE  " + str(predict))
            return 1

        else:
            print("(1) Aces can be cut")

    def two_er_availability(self):
        if not self.available_options[self.count][1]:
            return

        if 2 in self.dice:
            predict = 0
            for i in self.dice:
                if i == 2:
                    predict += 2
            print("(2) Twos is AVAILABLE  " + str(predict))
            return 1

        else:
            print("(2) Twos can be cut")

    def three_er_availability(self):
        if not self.available_options[self.count][2]:
            return

        if 3 in self.dice:
            predict = 0
            for i in self.dice:
                if i == 3:
                    predict += 3
            print("(3) Threes is AVAILABLE  " + str(predict))
            return 1

        else:
            print("(3) Threes can be cut")

    def four_er_availability(self):
        if not self.available_options[self.count][3]:
            return

        if 4 in self.dice:
            predict = 0
            for i in self.dice:
                if i == 4:
                    predict += 4
            print("(4) Fours is AVAILABLE  " + str(predict))
            return 1

        else:
            print("(4) Fours can be cut")

    def five_er_availability(self):
        if not self.available_options[self.count][4]:
            return

        if 5 in self.dice:
            predict = 0
            for i in self.dice:
                if i == 5:
                    predict += 5
            print("(5) Fives is AVAILABLE  " + str(predict))
            return 1

        else:
            print("(5) Fives can be cut")

    def six_er_availability(self):
        if not self.available_options[self.count][5]:
            return

        if 6 in self.dice:
            predict = 0
            for i in self.dice:
                if i == 6:
                    predict += 6
            print("(6) Sixes is AVAILABLE  " + str(predict))
            return 1

        else:
            print("(6) Sixes can be cut")

    def triple_availability(self):
        if not self.available_options[self.count][6]:
            return

        coll = collections.Counter(self.dice)
        triples = [k for k, v in coll.items() if v >= 3]
        if triples:
            predict = 0
            for i in self.dice:
                predict += i
            print("(7) 3 of a kind is AVAILABLE  " + str(predict))
            return 1

        else:
            print("(7) 3 of a kind can be cut")

    def quadruple_availability(self):
        if not self.available_options[self.count][7]:
            return

        coll = collections.Counter(self.dice)
        quadruples = [k for k, v in coll.items() if v >= 4]
        if quadruples:
            predict = 0
            for i in self.dice:
                predict += i
            print("(8) 4 of a kind is AVAILABLE  " + str(predict))
            return 1

        else:
            print("(8) 4 of a kind can be cut")

    def full_house_availability(self):
        if not self.available_options[self.count][8]:
            return

        coll = collections.Counter(self.dice)
        doubles = [k for k, v in coll.items() if v == 2]
        triples = [k for k, v in coll.items() if v == 3]

        if doubles and triples:
            predict = 25
            print("(9) Full_house is AVAILABLE  " + str(predict))
            return 1

        else:
            print("(9) Full_house can be cut")

    def little_street_availability(self):
        if not self.available_options[self.count][9]:
            return

        count = 0
        s = list(set(self.dice))

        for i in range(len(s) - 1):
            if s[i] + 1 == s[i + 1]:
                count += 1
                if count == 3:
                    predict = 30
                    print("(10) Sm Straight is AVAILABLE  " + str(predict))
                    return 1

        print("(10) Sm Straight can be cut")

    def big_street_availability(self):
        if not self.available_options[self.count][10]:
            return

        count = 0
        s = list(set(self.dice))

        for i in range(len(s) - 1):
            if s[i] + 1 == s[i + 1]:
                count += 1
                if count == 4:
                    predict = 40
                    print("(11) Lg Straight is AVAILABLE  " + str(predict))
                    return 1

        print("(11) Lg Straight can be cut")

    def yahtzee_availability(self):
        if not self.available_options[self.count][11]:
            return

        coll = collections.Counter(self.dice)
        penta = [k for k, v in coll.items() if v == 5]

        if penta:
            predict = 50
            print("(12) Yahtzee is AVAILABLE  " + str(predict))
            return 1

        else:
            print("(12) Yahtzee can be cut")
            return False

    def chance_availability(self):
        if not self.available_options[self.count][12]:
            return

        predict = 0
        for i in self.dice:
            predict += i
        print("(13) Chance is AVAILABLE  " + str(predict))
        return 1

    def yahtzee_bonus_availability(self):
        yahtzee_taken = self.available_options[self.count][13]
        coll = collections.Counter(self.dice)
        penta = [k for k, v in coll.items() if v == 5]

        if penta and yahtzee_taken:
            predict = 100
            print("\n(69) YAHTZEE BONUS IS AVAILABLE!!!!!  " + str(predict) + "\n")
            return 1

    # run all the options to show the players what they can choose
    def give_options(self):
        self.one_er_availability()
        self.two_er_availability()
        self.three_er_availability()
        self.four_er_availability()
        self.five_er_availability()
        self.six_er_availability()
        self.triple_availability()
        self.quadruple_availability()
        self.full_house_availability()
        self.little_street_availability()
        self.big_street_availability()
        self.yahtzee_availability()
        self.chance_availability()
        self.yahtzee_bonus_availability()

    # functions for giving the new scores and setting the available options 2d array element to false
    def one_er(self):
        if self.one_er_availability():
            for i in self.dice:
                if i == 1:
                    self.calculate += 1
            self.score[self.count][0] = self.calculate
        else:
            self.cut[self.count][0] = "CUT"
        self.available_options[self.count][0] = False

    def two_er(self):
        if self.two_er_availability():
            for i in self.dice:
                if i == 2:
                    self.calculate += 2
            self.score[self.count][1] = self.calculate
        else:
            self.cut[self.count][1] = "CUT"
        self.available_options[self.count][1] = False

    def three_er(self):
        if self.three_er_availability():
            for i in self.dice:
                if i == 3:
                    self.calculate += 3
            self.score[self.count][2] = self.calculate
        else:
            self.cut[self.count][2] = "CUT"
        self.available_options[self.count][2] = False

    def four_er(self):
        if self.four_er_availability():
            for i in self.dice:
                if i == 4:
                    self.calculate += 4
            self.score[self.count][3] = self.calculate
        else:
            self.cut[self.count][3] = "CUT"
        self.available_options[self.count][3] = False

    def five_er(self):
        if self.five_er_availability():
            for i in self.dice:
                if i == 5:
                    self.calculate += 5
            self.score[self.count][4] = self.calculate
        else:
            self.cut[self.count][4] = "CUT"
        self.available_options[self.count][4] = False

    def six_er(self):
        if self.six_er_availability():
            for i in self.dice:
                if i == 6:
                    self.calculate += 6
            self.score[self.count][5] = self.calculate
        else:
            self.cut[self.count][5] = "CUT"
        self.available_options[self.count][5] = False

    def triple(self):
        if self.triple_availability():
            for i in self.dice:
                self.calculate += i
            self.score[self.count][6] = self.calculate
        else:
            self.cut[self.count][6] = "CUT"
        self.available_options[self.count][6] = False

    def quadruple(self):
        if self.quadruple_availability():
            for i in self.dice:
                self.calculate += i
            self.score[self.count][7] = self.calculate
        else:
            self.cut[self.count][7] = "CUT"
        self.available_options[self.count][7] = False

    def full_house(self):
        if self.full_house_availability():
            self.score[self.count][8] = 25
        else:
            self.cut[self.count][8] = "CUT"
        self.available_options[self.count][8] = False

    def little_street(self):
        if self.little_street_availability():
            self.score[self.count][9] = 30
        else:
            self.cut[self.count][9] = "CUT"
        self.available_options[self.count][9] = False

    def big_street(self):
        if self.big_street_availability():
            self.score[self.count][10] = 40
        else:
            self.cut[self.count][10] = "CUT"
        self.available_options[self.count][10] = False

    def yahtzee(self):
        if self.yahtzee_availability():
            self.score[self.count][11] = 50
            self.available_options[self.count][13] = True

        else:
            self.cut[self.count][11] = "CUT"
        self.available_options[self.count][11] = False

    def chance(self):
        if self.chance_availability():
            for i in self.dice:
                self.calculate += i
            self.score[self.count][12] = self.calculate
        else:
            self.cut[self.count][12] = "CUT"
        self.available_options[self.count][12] = False

    def yahtzee_bonus(self):
        self.score[self.count][13] += 100

    # giving the player the option to choose of the available options
    def choose(self):
        while True:
            # try statement in case the user input is wrong
            try:
                available_options = []
                count = 1

                coll = collections.Counter(self.dice)
                penta = [k for k, v in coll.items() if v == 5]

                for i in self.available_options[self.count]:
                    # if statement for the bonus yahtzee
                    if count == 14:
                        if i and penta:
                            available_options.append(69)
                    elif i:
                        available_options.append(count)
                    count += 1

                if not available_options:
                    choosing = 0
                    print("Sorry but there are no available options")
                    break

                choosing = int(
                    input(f"\nPick one of the options {available_options} "))
                if choosing not in available_options:
                    raise Exception
                break
            except Exception:
                print("Please enter one of the available options: ")
                continue

        # running which function according to the user input
        if choosing == 1:
            self.one_er()
        elif choosing == 2:
            self.two_er()
        elif choosing == 3:
            self.three_er()
        elif choosing == 4:
            self.four_er()
        elif choosing == 5:
            self.five_er()
        elif choosing == 6:
            self.six_er()
        elif choosing == 7:
            self.triple()
        elif choosing == 8:
            self.quadruple()
        elif choosing == 9:
            self.full_house()
        elif choosing == 10:
            self.little_street()
        elif choosing == 11:
            self.big_street()
        elif choosing == 12:
            self.yahtzee()
        elif choosing == 13:
            self.chance()
        elif choosing == 69:
            self.yahtzee_bonus()

        # making it the turn of the next player
        self.calculate = 0
        self.count += 1
        if self.count == self.player_count:
            self.count = 0

    def play(self):
        # running all the necessary functions to play the game
        new_game.start()
        while True:
            new_game.rules()
            new_game.dice_roll()
            new_game.give_options()
            new_game.choose()

            # if all users do not have any more available options then end the game
            count = 0
            for i in self.available_options:
                for j in i[:13]:
                    if j:
                        count += 1

            if count == 0:
                break
        self.winner()

    def winner(self):
        # calculate the total of all the players
        total_list = []
        for i in range(self.player_count):
            total = 0
            if sum(self.score[i][:6]) >= 63:
                total += 35

            total += sum(self.score[i])
            total_list.append(total)
            print(f"\nTotal of {self.players[i]} is {str(total)} ")

        # from the total scores, find who has the highest score
        maxim = 0
        for i in total_list:
            if i > maxim:
                maxim = i

        winners = []
        for i, index in zip(total_list, range(len(total_list))):
            if i == maxim:
                winners.append(self.players[index])

        print(f"\n \nCONGRATULATIONS ", end="")
        for i in winners:
            print(f"{i} ", end="")
        print("YOU WON\n \n")


new_game = Game()

new_game.play()
