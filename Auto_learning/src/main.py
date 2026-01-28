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

# Brain should be defined by default
brain=Brain()
lm=Motor(Ports.PORT7, 1.0, True)
rm=Motor(Ports.PORT12, 1.0, False)
drivetrain=DriveTrain(lm,rm)

claw_motor = Motor(Ports.PORT4)
lift_motor = Motor(Ports.PORT11)    

brain.screen.print("Hello IQ2")

def main():
    drivetrain.drive_for(FORWARD, 350, MM, wait=False)
    drivetrain.turn_for(RIGHT, 45, DEGREES, wait=Fale)
    lift_motor.spin_for(REVERSE, 360, DEGREES)
    drivetrain.drive_for(FORWARD, 110, MM)
    print("Milestone 1")
    lift_motor.spin_for(FORWARD, 450, DEGREES, wait=False)
    claw_motor.spin_for(FORWARD, 360, DEGREES, wait=False)
    drivetrain.drive_for(REVERSE, 50, MM, wait=False)
    lift_motor.spin_for(FORWARD, 360, DEGREES, wait=False)
    claw_motor.spin_for(REVERSE, 360, DEGREES, wait=False)
    drivetrain.drive_for(FORWARD, 50, MM, wait=False)
    lift_motor.spin_for(REVERSE, 450, DEGREES, wait=False)
    drivetrain.drive_for(FORWARD, 300, MM, wait=False)
    lift_motor.spin_for(FORWARD, 300, DEGREES, wait=False)
    claw_motor.spin_for(FORWARD, 360, DEGREES, wait=False)
    drivetrain.drive_for(REVERSE, 50, MM, wait=False)
    lift_motor.spin_for(FORWARD, 400, DEGREES, wait=False)
    drivetrain.drive_for(FORWARD, 50, MM, wait=False)
    claw_motor.spin_for(REVERSE, 360, DEGREES, wait=False)
    lift_motor.spin_for(REVERSE, 1000, DEGREES, wait=False)
    drivetrain.drive_for(FORWARD, 350, MM, wait=False)
    drivetrain.turn_for(LEFT, 90, DEGREES, wait=False)
    drivetrain.drive_for(FORWARD, 260, MM, wait=False)
    claw_motor.spin_for(REVERSE, 360, DEGREES, wait=False)
    lift_motor.spin_for(REVERSE, 110, DEGREES, wait=False)
    lift_motor.spin_for(FORWARD, 500, DEGREES, wait=False)
    print("Milestone 2")
    claw_motor.spin_for(FORWARD, 360, DEGREES, wait=False)
    drivetrain.drive_for(REVERSE, 250, MM, wait=False)
    drivetrain.turn_for(LEFT, 90, DEGREES, wait=False)
    drivetrain.drive_for(FORWARD, 400, MM, wait=False)
    drivetrain.turn_for(RIGHT, 90, DEGREES, wait=False)
    brain.screen.new_line()
    brain.screen.print("DONE")

auton_thread = Thrd(main)
