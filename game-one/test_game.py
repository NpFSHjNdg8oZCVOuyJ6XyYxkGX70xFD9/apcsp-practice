import pytest
import game

# Replace this template with at least three tests per game function:
# def test_describe_the_case():
#     assert game.your_function(chosen_input) == expected_result


def test_random_move():
    for i in range(0,1000,1):
        result = game.random_move()
        assert result >= 0 and result <= 2

def test_distrubution():
    counts = [0,0,0]
    for i in range(0,10000,1):
        result = game.random_move()
        counts[result] += 1
    assert counts == pytest.approx([3333,3333,3333], rel = 0.05)


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__, "-q"]))
