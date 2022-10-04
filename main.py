"""
title: Cannonball Distance Calculator
author: Joanna Hao
date-created: 2022-09-23
"""
import math


# ----- SUBROUTINES ----- #
def scenario1Art():
    print("""
 ___
|   \\
|    \\
|     \\
1. Horizontal to the water
""")


def scenario2Art():
    print("""
   ___
  /   \\
 /     \\
/       \\
2. Parabolic to a level boat
""")


def scenario3Art():
    print("""
  ___
 /   \\
|     \\
|      \\
3. Parabolic to a smaller boat far away
""")


def scenario4Art():
    print("""
   ___
  /   \\_          _
 /               /
/          or   /
4. Parabolic to a boat higher above the water.
""")


# --- INPUTS
def menu():
    """
    Display starting text and ask user for scenario
    :return: int
    """
    print("""Welcome to the Navy canon distance calculator. 
Find the total distance the cannonball travels away from the cannon. """)
    scenario1Art()
    scenario2Art()
    scenario3Art()
    scenario4Art()
    scenario = input("Enter the scenario number: ")
    if scenario.isnumeric():
        return int(scenario)
    else:
        return menu()


def scenario1():
    """
    ask for inputs for scenario 1 and check their validity
    :return: floats
    """
    # INPUTS
    speed = input("What is the speed of the cannonball (m/s)? ")
    height = input("What is the height of the cannonball above the water? ")

    # PROCESSING
    # checking validity of inputs
    if speed.isnumeric():
        speed = float(speed)
    else:
        print("Please enter a valid speed.")
        return scenario1()

    if height.isnumeric():
        height = float(height)
    else:
        print("Please enter a valid height.")
        return scenario1()

    # OUTPUTS
    return speed, height


def scenario2():
    """
    ask for inputs of scenario 2 and check their validity
    :return: floats
    """
    # INPUTS
    speed = input("What is the speed of the cannonball (m/s)? ")
    angle = input("What is the angle along the horizontal (degrees)? ")

    # PROCESSING
    # checking validity of inputs
    if speed.isnumeric():
        speed = float(speed)
    else:
        print("Please enter a valid speed.")
        return scenario2()

    if angle.isnumeric():
        angle_rads = math.radians(float(angle))
    else:
        print("Please enter a valid angle.")
        return scenario2()

    # outputs
    return speed, angle_rads


def scenario3():
    """
    ask for inputs for scenario 3 and check their validity
    :return: floats
    """
    # INPUTS
    speed = input("What is the speed of the cannonball (m/s)? ")
    angle = input("What is the angle along the horizontal (degrees)? ")
    height = input("What is the height of the cannonball above the water? ")

    # PROCESSING
    # checking validity of inputs
    if speed.isnumeric():
        speed = float(speed)
    else:
        print("Please enter a valid speed.")
        return scenario3()

    if angle.isnumeric():
        angle_rads = math.radians(float(angle))
    else:
        print("Please enter a valid angle.")
        return scenario3()

    if height.isnumeric():
        height = float(height)
    else:
        print("Please enter a valid height.")
        return scenario3()

    # OUTPUTS
    return speed, angle_rads, height

def scenario4():
    """
    ask for inputs for scenario 4 and check their validity
    :return: floats
    """
    # INPUTS
    speed = input("What is the speed of the cannonball (m/s)? ")
    angle = input("What is the angle along the horizontal (degrees)? ")
    enemy_height = input("What is the height of the enemy ship above the water? ")

    # PROCESSING
    # checking validity of inputs
    if speed.isnumeric():
        speed = float(speed)
    else:
        print("Please enter a valid speed.")
        return scenario4()

    if angle.isnumeric():
        angle_rads = math.radians(float(angle))
    else:
        print("Please enter a valid angle.")
        return scenario4()

    if enemy_height.isnumeric():
        enemy_height = float(enemy_height)
    else:
        print("Please enter a valid enemy ship height.")
        return scenario4()

    # OUTPUTS
    return speed, angle_rads, enemy_height


# --- PROCESSING
def calculateDistance1(height_above, speed):
    """
    calculate horizontal distance for scenario 1
    :param height_above: float
    :param speed: float
    :return: float
    """
    time = math.sqrt(2 * height_above / 9.81)  # calculate time in air
    distance = speed * time
    return distance


def calculateDistance2(speed, angle):
    """
    calculate horizontal distance for scenario 2
    :param speed: float
    :param angle: float
    :return: float
    """
    # break given speed into x & y components
    horizontal_speed = speed * math.cos(angle)
    vertical_speed = speed * math.sin(angle)

    time = 2 * (vertical_speed/9.81)  # calculate time in air w/ Vy
    distance = horizontal_speed * time  # calculate distance w/ Vx
    return distance


def calculateDistance3(speed, angle, height):
    """
    calculate horizontal distance for scenario 3
    :param speed: float
    :param angle: float
    :param height: float
    :return: float
    """
    # break given speed into x & y components
    horizontal_speed = speed * math.cos(angle)
    initial_y_speed = speed * math.sin(angle)

    # to get time as part of scenario 2 component of scenario 3
    time1 = -2 * initial_y_speed / -9.81

    # to get time as part of scenario 1 component of scenario 3
    final_y_speed = -1 * math.sqrt(initial_y_speed**2 + 2 * -9.81 * -height)
    time2 = (final_y_speed + initial_y_speed) / -9.81
    total_time = time1 + time2

    distance = total_time * horizontal_speed  # calculate distance w/ total air time
    return distance


def calculateDistance4(speed, angle, enemy_height):
    """
    calculate horizontal distance for scenario 4
    :param speed: float
    :param angle: float
    :param enemy_height: float
    :return: float
    """
    # break given speed into x & y components
    initial_x_speed = speed * math.cos(angle)
    initial_y_speed = speed * math.sin(angle)

    # calculate time (using y values first)
    final_y_speed1 = -1 * math.sqrt(initial_y_speed**2 + 2 * -9.81 * enemy_height)  # farther distance Vfy
    final_y_speed2 = -1 * final_y_speed1  # closer distance Vfy
    time1 = (final_y_speed1 - initial_y_speed)/-9.81  # farther distance total time
    time2 = (final_y_speed2 - initial_y_speed)/-9.81  # closer distance total time

    distance1 = initial_x_speed * time1  # farther distance cannonball may travel
    distance2 = initial_x_speed * time2  # closer distance cannonball may travel
    return distance1, distance2


# --- OUTPUT
def displayDistance(distance, distance2):
    """
    display horizontal distance calculated
    :param distance: float
    :param distance2: float or int
    :return: None
    """
    print(f"The total distance the cannonball travelled is: {distance:.2f}m.")
    if distance2 != 0:
        print(f"The total distance the cannonball travelled is either: {distance:.2f}m or {distance2:.2f}m.")


def calcAgain():
    """
    determine whether user wants to make another calculation
    :return: None
    """
    again = input("Want to make another calculation? (Y/n): ")
    if again == "y" or again == "Y" or again == "" or again == "yes":
        pass
    else:
        exit()


# ----- MAIN PROGRAM CODE ----- #
if __name__ == "__main__":
    while True:
        # INPUTS
        SCENARIO = menu()

        # PROCESSING
        if SCENARIO == 1:
            SPEED, HEIGHT = scenario1()
            DISTANCE, DISTANCE2 = calculateDistance1(HEIGHT, SPEED), 0
        elif SCENARIO == 2:
            SPEED, ANGLE_RADS = scenario2()
            DISTANCE, DISTANCE2 = calculateDistance2(SPEED, ANGLE_RADS), 0
        elif SCENARIO == 3:
            SPEED, ANGLE_RADS, HEIGHT = scenario3()
            DISTANCE, DISTANCE2 = calculateDistance3(SPEED, ANGLE_RADS, HEIGHT), 0
        else:
            SPEED, ANGLE_RADS, ENEMY_HEIGHT = scenario4()
            DISTANCE, DISTANCE2 = calculateDistance4(SPEED, ANGLE_RADS, ENEMY_HEIGHT)

        # OUTPUTS
        displayDistance(DISTANCE, DISTANCE2)
        calcAgain()
