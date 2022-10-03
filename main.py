"""
title: Cannonball Distance Calculator
author: Joanna Hao
date-created: 2022-09-23
"""
# math library trig functions in radians (need to convert to degrees)
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
    time = math.sqrt(2 * height_above / 9.81)
    distance = speed * time
    return distance


def calculateDistance2(speed, angle):
    horizontal_speed = speed * math.cos(angle)
    vertical_speed = speed * math.sin(angle)
    time = 2 * (vertical_speed/9.81)
    distance = horizontal_speed * time
    return distance


def calculateDistance3(speed, angle, height):
    horizontal_speed = speed * math.cos(angle)
    initial_y_speed = speed * math.sin(angle)

    # to get time as part of scenario 2 component of scenario 3
    time1 = -2 * initial_y_speed / -9.81

    # to get time as part of scenario 1 component of scenario 3
    final_y_speed = -1 * math.sqrt(initial_y_speed**2 + 2 * -9.81 * -height)
    time2 = (final_y_speed + initial_y_speed) / -9.81
    total_time = time1 + time2

    distance = total_time * horizontal_speed
    return distance


def calculateDistance4(speed, angle, enemy_height):
    # FAR DISTANCE
    initial_x_speed = speed * math.cos(angle)
    initial_y_speed = speed * math.sin(angle)

    # calculate time (using y values first)
    final_y_speed1 = -1 * math.sqrt(initial_y_speed**2 + 2 * -9.81 * enemy_height)
    final_y_speed2 = -1 * final_y_speed1
    time1 = (final_y_speed1 - initial_y_speed)/-9.81
    time2 = (final_y_speed2 - initial_y_speed)/-9.81

    distance1 = initial_x_speed * time1
    distance2 = initial_x_speed * time2
    return distance1, distance2


# --- OUTPUT
def displayDistance(distance, distance2):
    print(f"The total distance the cannonball travelled is: {distance:.2f}m.")
    if distance2 != 0:
        print(f"The total distance the cannonball travelled is either: {distance:.2f}m or {distance2:.2f}m.")

def calcAgain():
    again = input("Want to make another calculation? (Y/n): ")
    if again == "y" or again == "Y" or again == "" or again == "yes":
        return True
    else:
        exit()

# ----- MAIN PROGRAM CODE ----- #
if __name__ == "__main__":
    while True:
        # INPUTS
        scenario = menu()

        # PROCESSING
        if scenario == 1:
            speed, height = scenario1()
            distance, distance2 = calculateDistance1(height, speed), 0
        elif scenario == 2:
            speed, angle_rads = scenario2()
            distance, distance2 = calculateDistance2(speed, angle_rads), 0
        elif scenario == 3:
            speed, angle_rads, height = scenario3()
            distance, distance2 = calculateDistance3(speed, angle_rads, height), 0
        else:
            speed, angle_rads, enemy_height = scenario4()
            distance, distance2 = calculateDistance4(speed, angle_rads, enemy_height)

        # OUTPUTS
        displayDistance(distance, distance2)
        calcAgain()
