"""
title: Cannonball Distance Calculator
author: Joanna Hao
date-created: 2022-09-23
"""
# math library trig functions in radians (need to convert to degrees)
"""
scenario 1: horizontal projectile
scenario 2: diagonal projectile (landing at same height as being shot from)
scenario 3: diagonal projectile (landing below initial height)
scenario 4: diagonal projectile (either before reaching peak or b/w peak and landing)

"""

# ----- SUBROUTINES ----- #
def scenario1Art():
    pass


def scenario2Art():
    pass


def scenario3Art():
    pass


def scenario4Art():
    pass

# --- INPUTS
def menu():
    print("Welcome to the Navy canon distance calculator. Find the total distance the cannonball travels away from the cannon. ")
    scenario1Art()
    scenario2Art()
    scenario3Art()
    scenario4Art()
    # INPUT
    scenario = input("Enter the scenario number: ")
    speed = input("What is the speed of the cannonball (m/s)? ")
    angle = input("What is the angle along the horizontal (degrees)? ")

    # PROCESSING
    if scenario.isnumeric():
        scenario = int(scenario)
    else:
        pass

# --- PROCESSING


# --- OUTPUTS


# ----- MAIN PROGRAM CODE ----- #
if __name__ == "__main__":
    pass
