#Sign your name:________________

'''
Recreate, exactly the Test Picture from the website. The arcade colors used in this picture in no particular order are:
BLACK, ALMOND, PHLOX, BLUSH, RED, BLUE, WISTERIA, AMBER, BRICK_RED and YELLOW.
The picture is 500px wide and 400px tall. Look up ARC in the documentation to do the PAC-MAN.
'''
import arcade

arcade.open_window(500,400, "Jedi test")

for i in range(1,20):
    x = 20
    arcade.draw_line(x,0,x,400, arcade.color.BLACK, 2)
    x += 20
for i in range(1, 501, 20):
    arcade.draw_line(i, 0, i, 500, arcade.color.BLACK, 2)

