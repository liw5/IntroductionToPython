"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Wenxing Li.
"""
########################################################################
# DONE: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################
import rosegraphics as rg

window = rg.TurtleWindow()
Crazy_Turtle_1 = rg.SimpleTurtle('turtle')
Crazy_Turtle_1.pen = rg.Pen('red', 4)
Crazy_Turtle_1.speed = 20

Crazy_Turtle_2 = rg.SimpleTurtle('turtle')
Crazy_Turtle_2.pen = rg.Pen('blue', 2)
Crazy_Turtle_2.speed = 20

for k in range(12):
    Crazy_Turtle_1.draw_circle((12 - k) * 10)
    Crazy_Turtle_1.pen_up()
    Crazy_Turtle_1.right(30)
    Crazy_Turtle_1.pen_down()

    Crazy_Turtle_2.backward((12 - k) * 10)
    Crazy_Turtle_2.draw_square((12 - k) * 20)
    Crazy_Turtle_2.pen_up()
    Crazy_Turtle_2.forward((12 - k) * 10)
    Crazy_Turtle_2.right(30)
    Crazy_Turtle_2.pen_down()

window.close_on_mouse_click()
