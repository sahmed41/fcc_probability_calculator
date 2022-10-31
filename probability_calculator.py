import copy
import random


# Consider using the modules imported above.

class Hat:

    def __init__(self, **kwargs):
        # Remember to make the instetiation require at least one argument
        self.contents = []
        for k, i in kwargs.items():
            for i in range(i):
                self.contents.append(k)

    def draw(self, numberOfBalls):
        # Run the draw equal to numberOfBalls
        # Generate a random number that is withing the length of contents
        # Remove that ball and append it to a list called drawList
        # Return drawList
        # If numberOfBalls is larger than the length of contents return all of its itmes and then clear it
        drawList = []
        if numberOfBalls > len(self.contents):
            # for i in self.contents:
            #     drawList.append(i)
            # self.contents.clear()
            drawList = copy.deepcopy(self.contents)
            self.contents.clear()

        else:
            for i in range(numberOfBalls):
                r = random.randint(0, len(self.contents) - 1)
                drawList.append(self.contents.pop(r))
        return drawList


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    # Run the draw num_experiment times
    # Convert expected balls to a list
    # Compare the results with expected_balls and if they match increase m by one
    # Return m / num_experiments
    contents = copy.deepcopy(hat.contents)
    m = 0
    eb = []
    for k, i in expected_balls.items():
        for n in range(i):
            eb.append(k)
    for i in range(num_experiments):
        d = hat.draw(num_balls_drawn)  # Do not remove the balls after everyy draw
        if match_list(eb, d):
            m += 1
        hat.contents = copy.deepcopy(contents)
    return m / num_experiments


def match_list(listToMatch, listBase):  # This method ensures that a results of a draw contains expected outcome
    toMatch = len(listToMatch)
    for k, i in enumerate(listToMatch):
        for n, j in enumerate(listBase):
            if i == j:
                listBase.pop(n)
                toMatch -= 1
                break
    if toMatch == 0:
        return True
    else:
        return False
