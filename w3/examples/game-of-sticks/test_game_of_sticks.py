from game_of_sticks import ComputerPlayer, Player, Game


class DummyPlayer(Player):

    def choose_sticks_to_pick_up(self, current_sticks):
        return 1

    def report_win(self, won):
        self.won = won


def test_computer_player_num_of_sticks():
    player = ComputerPlayer("player1")
    for _ in range(100):
        assert player.choose_sticks_to_pick_up(10) in (1, 2, 3)
    assert player.choose_sticks_to_pick_up(4) == 3
    assert player.choose_sticks_to_pick_up(3) == 2
    assert player.choose_sticks_to_pick_up(2) == 1
    assert player.choose_sticks_to_pick_up(1) == 1


def test_player_who_picks_up_last_stick_loses():
    p1 = DummyPlayer("p1")
    p2 = DummyPlayer("p2")
    game = Game(p1, p2)
    game.run_game()
    assert p1.won
    assert not p2.won
