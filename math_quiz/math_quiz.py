import random


def Random_Integer(min, max):
    """
    Generate a random integer between min and max.

    Args:
        min: Lower limit of the random integer.
        max: Upper limit of the random integer.

    Returns:
        random integer between min and max.

    Raises:
        KeyError: See random.randint error handling.
    """
    return random.randint(min, max)


def Operator_Selector():
    """
    Generate a random operator to be used in the quiz.

    Returns:
        random operator as a string.

    Raises:
        KeyError: no error expected.
    """
    return random.choice(['+', '-', '*'])


def Solver(n1, n2, o):
    """
    Calculates the result of the randomly generated quiz problem

    Args:
        n1: First random integer.
        n2: Second random integer.
        o: Operator

    Returns:
        resulting integer.

    Raises:
        KeyError: See random.randint error handling.
    """

    p = f"{n1} {o} {n2}"
    if o == '+': a = n1 + n2
    elif o == '-': a = n1 - n2
    else: a = n1 * n2
    return p, a

def math_quiz():
    """
    The main code managing the quiz. Generates random math operation and solution, prompts the user for input and compares and keeps score for 10 rounds.

    Function calls:
    	Random_Integer 
    	Operator_Selector
    	Solver
    	
    Returns:
        Interactive. 

    Raises:
        ValueError: If a non integer input is given by user.
    """

    Correct_Answers = 0
    Num_Questions = 10

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(Num_Questions):
        n1 = Random_Integer(1, 10); n2 = Random_Integer(1, 6); o = Operator_Selector()

        PROBLEM, ANSWER = Solver(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your answer: ")
        
        try:
            useranswer = int(useranswer)
        except:
            print("That was not an integer")

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            Correct_Answers += 1
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {Correct_Answers}/{Num_Questions}")

if __name__ == "__main__":
    math_quiz()
