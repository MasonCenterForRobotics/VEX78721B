# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       AnirudhBoreddy                                               #
# 	Created:      1/11/2026, 1:28:47 PM                                        #
# 	Description:  IQ2 project                                                  #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *
def main():
    # Brain should be defined by default
    brain=Brain()
    drivetrain=DriveTrain()

    brain.screen.print("Hello IQ2")
    drivetrain.drive_for(FORWARD, 350, MM)
    drivetrain.turn_for(RIGHT, 45, DEGREES)
    lift_motor.spin_for(REVERSE, 360, DEGREES)
    drivetrain.drive_for(FORWARD, 110, MM)
    lift_motor.spin_for(FORWARD, 450, DEGREES)
    claw_motor.spin_for(FORWARD, 360, DEGREES)
    drivetrain.drive_for(REVERSE, 50, MM)
    lift_motor.spin_for(FORWARD, 360, DEGREES)
    claw_motor.spin_for(REVERSE, 360, DEGREES)
    drivetrain.drive_for(FORWARD, 50, MM)
    lift_motor.spin_for(REVERSE, 450, DEGREES)
    drivetrain.drive_for(FORWARD, 300, MM)
    lift_motor.spin_for(FORWARD, 300, DEGREES)
    claw_motor.spin_for(FORWARD, 360, DEGREES)
    drivetrain.drive_for(REVERSE, 50, MM)
    lift_motor.spin_for(FORWARD, 400, DEGREES)
    drivetrain.drive_for(FORWARD, 50, MM)
    claw_motor.spin_for(REVERSE, 360, DEGREES)
    lift_motor.spin_for(REVERSE, 1000, DEGREES)
    drivetrain.drive_for(FORWARD, 350, MM)
    drivetrain.turn_for(LEFT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 260, MM)
    claw_motor.spin_for(REVERSE, 360, DEGREES)
    lift_motor.spin_for(REVERSE, 110, DEGREES)
    lift_motor.spin_for(FORWARD, 500, DEGREES)
    claw_motor.spin_for(FORWARD, 360, DEGREES)
    drivetrain.drive_for(REVERSE, 250, MM)
    drivetrain.turn_for(LEFT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 400, MM)
    drivetrain.turn_for(RIGHT, 90, DEGREES)


   
