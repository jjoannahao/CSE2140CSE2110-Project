"""
title: Cannonball Distance Calculator
author: Joanna Hao
date-created: 2022-09-23
"""
# math library trig functions in radians (need to convert to degrees)
import math

"""
scenario 1: horizontal projectile
- calc air time (using height above water)
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
    scenario = input("Enter the scenario number: ")
    if scenario.isnumeric():
        scenario = int(scenario)
        return scenario
    else:
        return menu()


def calculateTime(height):
    time = math.sqrt(2 * height / 9.81)
    return time

def scenario1():
    # INPUTS
    speed = input("What is the speed of the cannonball (m/s)? ")
    height = input("What is the height of the cannonball above the water? ")

    # PROCESSING
    # checking validity of inputs
    if speed.isnumeric():
        speed = int(speed)
    else:
        print("Please enter a valid speed.")
        return scenario1()

    if height.isnumeric():
        height = int(height)
    else:
        print("Please enter a valid height.")
        return scenario1()



def scenario2():
    # INPUTS
    speed = input("What is the speed of the cannonball (m/s)? ")
    angle = input("What is the angle along the horizontal (degrees)? ")

    # PROCESSING
    # checking validity of inputs
    if speed.isnumeric():
        speed = int(speed)
    else:
        print("Please enter a valid speed.")
        return scenario2()

    if angle.isnumeric():
        angle_rads = math.radians(int(angle))
    else:
        print("Please enter a valid angle.")
        return scenario2()


def scenario3():
    # INPUTS
    speed = input("What is the speed of the cannonball (m/s)? ")
    angle = input("What is the angle along the horizontal (degrees)? ")
    height = input("What is the height of the cannonball above the water? ")

    # PROCESSING
    # checking validity of inputs
    if speed.isnumeric():
        speed = int(speed)
    else:
        print("Please enter a valid speed.")
        return scenario3()

    if angle.isnumeric():
        angle_rads = math.radians(int(angle))
    else:
        print("Please enter a valid angle.")
        return scenario3()

    if height.isnumeric():
        height = int(height)
    else:
        print("Please enter a valid height.")
        return scenario3()


def scenario4():
    pass
    # INPUTS

    # PROCESSING


# --- PROCESSING
def calculateDistance(scenario, height_above, angle, speed): # (#, height, angle_rads, speed)
    if scenario == 1:
        time = calculateTime(height_above)
        distance = speed * time
        return distance

    if scenario == 2:
        horizontal_speed = speed * math.cos(angle)
        vertical_speed = speed * math.sin(angle)
        time = 2 * (vertical_speed/9.81)
        distance = horizontal_speed * time
        return distance

    if scenario == 3:
        # scenario 2 part
        horizontal_speed = speed * math.cos(angle)
        vertical_speed = speed * math.sin(angle)
        time_to_peak = vertical_speed/9.81
        max_height = (vertical_speed ** 2)/(2 * 9.81)

        # scenario 1 part
        remaining_time = calculateTime(height_above)
        total_time = time_to_peak + remaining_time
        distance1 = remaining_time * speed

    if scenario == 4:
        pass


# --- OUTPUTS


# ----- MAIN PROGRAM CODE ----- #
if __name__ == "__main__":
    pass
