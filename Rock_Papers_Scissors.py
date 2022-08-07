class Game():

    def logMe(self, s):
        """
        Docstring:
        This function log every thing in the log file
        :param s: s takes input of a String

        """
        import logging as lg
        lg.basicConfig(filename="game.log", level=lg.INFO, format='%(asctime)s %(message)s')
        lg.info(str(s))

    def startInterface(self):
        """
        Docstring:
        This is Starting User Inter Face of the game
        """
        print("---------------------------------------------------------------------")
        print("Lets Play Rock Paper Sissors game...")
        print("The game will have 5 rounds.")
        print("Lets start..")
        print("---------------------------------------------------------------------")

    def endInterface(self):
        """
        Docstring:
        This is Ending User Inter Face of the game
        """
        print("---------------------------------------------------------------------")

    def computerChoise(self):
        """
        Docstring:
        This function makes a choise out of the strings inside the list eg =l = ["R", "P", "S"]
        :return: It returns a choise.
        """
        try:
            from random import choice
            l = ["R", "P", "S"]
            return choice(l)

        except Exception as e:
            self.logMe(e)

    def returnChoise(self, comInput):
        """
        Docstring:
        It takes input as a parameter and returns the full form.
        :param comInput: It takes comInput as a parameter.
        :return: returns the full form
        """
        try:
            if comInput == "R":
                return "Rock"
            elif comInput == "P":
                return "Paper"
            elif comInput == "S":
                return "Scissors"

        except Exception as e:
            self.logMe(e)

    def gameResults(self, player, computer):
        """
        Docstring:
        This function will return the result of the game played by player and computer
        :param player: It is the count of points of player
        :param computer: It is the count of points of computer
        :return: results
        """
        try:
            if player > computer:
                return f"Player won the game your point is {player}"
            elif player < computer:
                return f"Computer won the game his point is {computer} and your point is {player}"
            else:
                return f"The game is a draw Computer point is {computer} and your point is {player}"
        except Exception as e:
            self.logMe(e)

    def game(self):
        """
        Docstring:
        This is the game funtion the main part of the game
        """
        try:
            self.startInterface()
            player = 0
            computer = 0
            for i in range(5):
                userInput = input("Enter R for Rock, P for Paper and S for Scissors :")
                comInput = self.computerChoise()
                s = f"User input is {userInput} and computer input is{comInput}"
                self.logMe(s)
                result = self.returnChoise(comInput)
                if (userInput == "R" and comInput == "R") or (userInput == "P" and comInput == "P") or (
                        userInput == "S" and comInput == "S"):
                    print(f"It is a Draw, He thew {result}")

                elif (userInput == "R" and comInput == 'S') or (userInput == "P" and comInput == "R") or (
                        userInput == "S" and comInput == "P"):
                    print(f"You Won the round, He thew {result}")
                    player += 1

                else:
                    print(f"Computer won the round, He thew {result}")
                    computer += 1

            self.endInterface()
            print(self.gameResults(player, computer))

        except Exception as e:
            self.logMe(e)


if __name__ == '__main__':
    object1 = Game()
    object1.game()
