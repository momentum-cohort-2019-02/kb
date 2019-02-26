from game_of_sticks import ComputerPlayer


def test_computer_player_num_of_sticks():
    player = ComputerPlayer()
    for _ in range(100):
        assert player.choose_sticks_to_pick_up(10) in (1, 2, 3)
    assert player.choose_sticks_to_pick_up(4) == 3
    assert player.choose_sticks_to_pick_up(3) == 2
    assert player.choose_sticks_to_pick_up(2) == 1
    assert player.choose_sticks_to_pick_up(1) == 1
