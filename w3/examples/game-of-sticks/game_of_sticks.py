import random


def pluralize(number, singular, plural=None):
    if plural is None:
        plural = singular + "s"

    if number == 1:
        return f"1 {singular}"

    return f"{number} {plural}"


class Player:

    def __init__(self, name):
        self.name = name

    def report_pick_up(self, num_sticks):
        pass

    def report_win(self, won):
        pass

    def __str__(self):
        return self.name


class ComputerPlayer(Player):
    """
    A player for the game of sticks. Chooses number of sticks to pick up randomly.
    """

    def __init__(self, name):
        """
        Our player will track its winning moves by adding winning moves to virtual "buckets"
        and removing losing moves from those buckets.
        """
        super().__init__(name)

        self.possible_choices = {}
        for num in range(5, 21):
            self.possible_choices[num] = [1, 2, 3]
        self.current_choices = {}

    def choose_sticks_to_pick_up(self, current_sticks):
        """
        Choose a random number (1-3) sticks to pick up. You cannot pick up
        more sticks than currently exist.
        """
        if current_sticks in (1, 2):
            return 1
        if current_sticks == 3:
            return 2
        if current_sticks == 4:
            return 3

        choice = random.choice(self.possible_choices[current_sticks])
        self.current_choices[current_sticks] = choice
        return choice

    def report_win(self, won):
        """
        When we win, we want to add back the current choices to the possible choice buckets.
        When we lose, we want to remove those choices.
        """
        if won:
            for count, choice in self.current_choices.items():
                self.possible_choices[count].append(choice)
        else:
            for count, choice in self.current_choices.items():
                self.possible_choices[count].remove(choice)
                if not self.possible_choices[count]:
                    self.possible_choices[count] = [1, 2, 3]

        self.current_choices = {}
        # print(self.possible_choices)


class HumanPlayer(Player):
    """
    A human player for the game of sticks.
    """

    def choose_sticks_to_pick_up(self, current_sticks):
        print(f'There are {pluralize(current_sticks, "stick")} left.')

        try:
            num_of_sticks = int(
                input("How many sticks (1-3) do you want to pick up? "))
        except ValueError:
            print("That was not a number. Try again.")
            return self.choose_sticks_to_pick_up(current_sticks)

        if num_of_sticks < 1:
            print("You can't pick up less than 1 stick!")
            return self.choose_sticks_to_pick_up(current_sticks)
        if num_of_sticks > min(3, current_sticks):
            print("You can't pick up that many sticks!")
            return self.choose_sticks_to_pick_up(current_sticks)

        return int(num_of_sticks)

    def report_pick_up(self, num_sticks):
        print(f"The other player picked up {pluralize(num_sticks, 'stick')}.")


class Game:

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.sticks = 20
        self.current_player = None

    def start_game(self):
        self.print_instructions()
        play_again = True
        while play_again:
            self.run_game()
            play_again = input("Would you like to play again?")
            play_again = play_again.lower().startswith("y")

    def run_game(self):
        self.sticks = 20
        self.current_player = None

        while self.sticks > 0:
            self.current_player = 1
            p1_sticks = self.player1.choose_sticks_to_pick_up(self.sticks)
            self.player2.report_pick_up(p1_sticks)
            self.sticks -= p1_sticks
            if self.sticks == 0:
                break
            self.current_player = 2
            p2_sticks = self.player2.choose_sticks_to_pick_up(self.sticks)
            self.player1.report_pick_up(p2_sticks)
            self.sticks -= p2_sticks

        if self.current_player == 2:
            print(f"{self.player1} wins!")
            self.player1.report_win(True)
            self.player2.report_win(False)
        else:
            print(f"{self.player2} wins!")
            self.player1.report_win(False)
            self.player2.report_win(True)

    def print_instructions(self):
        print(
            "Welcome to the Game of Sticks! Try not to be the person picking up the last stick."
        )
        print("Player 1 will start.")


if __name__ == "__main__":
    p1 = ComputerPlayer(name="Player 1")
    p2 = HumanPlayer(name="Player 2")

    game = Game(p1, p2)
    game.start_game()
