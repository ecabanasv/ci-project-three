import pytest

from functions import Functions

# test print intro


def test_print_intro():
    """
    Test print intro
    """
    result = Functions.print_intro()
    assert result == print(
        "Are you a procrastinator? The following questionnaire",
        " will let you know if you are a born procrastinator.\n",
        "Please, take your time to answer the questions.",
        "Choose options A, B or C.\n"
        "At the end of questionary we will show the results,",
        "and the total results.\n",
    )


# test print options


def test_print_options():
    """
    Test print options
    """
    result = Functions.print_options()
    assert result == print(
        "(A) Never or seldom", "(B) Sometimes", "(C) Always or almost always\n"
    )


# test shuffle questions


def test_shuffle_questions():
    """
    Test shuffle questions
    Expected results: 30 (total number of questions in the file)
    """
    list_questions = Functions.shuffle_questions()
    assert len(list_questions) == 30


# test questionary choices


def test_input_question_choice_a():
    """
    Test choice A and sum of points 0
    Expect return of 0
    """
    points = Functions.questionary_total("a", 0)
    assert points == 0


def test_input_question_choice_b():
    """
    Test choice B and sum of points 0
    Expect return of 0.5
    """
    points = Functions.questionary_total("b", 0)
    assert points == 0.5


def test_input_question_choice_c():
    """
    Test choice C and sum of points 0
    Expect return of 1
    """
    points = Functions.questionary_total("c", 0)
    assert points == 1


# test questionary results


def test_questionary_result_low():
    """
    Points: 0
    Expected Low result
    """
    result = Functions.questionary_result(0)
    assert result == print(
        "YOUR RESULTS:\n (Low) You scored " + str(0) + "",
        "points. You are the new Terminator model Roomba TX6000",
    )


def test_questionary_result_medium():
    """
    Points: 3
    Expected Medium result
    """
    result = Functions.questionary_result(3)
    assert result == print(
        "YOUR RESULTS:\n (Medium) You scored " + str(3) + "",
        " points. We suppose that you are 'normal'",
    )


def test_questionary_result_high():
    """
    Points: 6
    Expected High result
    """
    result = Functions.questionary_result(6)
    assert result == print(
        "YOUR RESULTS:\n (High) You scored " + str(6) + "",
        " points. Don't do today what you can do tomorrow!",
    )


def test_questionary_result_extreme():
    """
    Points: 9
    Expected Extreme result
    """
    result = Functions.questionary_result(9)
    assert result == print(
        "YOUR RESULTS:\n (Extreme) You scored " + str(9) + "",
        " points. You even procrastinate this questionary for hours!",
    )
