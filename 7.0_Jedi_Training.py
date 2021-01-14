#Sign your name:________________

'''
Recreate, exactly the Test Picture from the website. The arcade colors used in this picture in no particular order are:
BLACK, ALMOND, PHLOX, BLUSH, RED, BLUE, WISTERIA, AMBER, BRICK_RED and YELLOW.
The picture is 500px wide and 400px tall. Look up ARC in the documentation to do the PAC-MAN.
'''
import arcade

# draw window with width 500 & height 400
arcade.open_window(500, 400, "Jedi test")
arcade.set_background_color(arcade.color.ALMOND)


arcade.start_render()
# draw vertical grid lines
for i in range(1, 501, 20):
    arcade.draw_line(i, 0, i, 400, arcade.color.BLACK, 2)
# draw horizontal grid lines
for i in range(1, 401, 20):
    arcade.draw_line(0, i, 500, i, arcade.color.BLACK, 2)
# draw rectangle at x=50, y=370, with width 60 & height 20
arcade.draw_rectangle_filled(50, 370, 60, 20, arcade.color.PHLOX)
# draw rectangle at x=200, y=260, with width 40 & height 20
arcade.draw_rectangle_filled(200, 260, 40, 20, arcade.color.BLUSH, -45)
# draw circle at (250, 200) with a radius of 40
arcade.draw_circle_filled(250, 200, 40, arcade.color.WISTERIA)
# Draw text at (20, 155) in 23pt size
arcade.draw_text("I love you. I know.", 20, 155, arcade.color.BRICK_RED, 23)
# draw blue line
arcade.draw_line(80, 20, 120, 60, arcade.color.BLUE, 1)
# draw the orange oval
arcade.draw_ellipse_filled(100,100, 120, 40, arcade.color.AMBER)
# draw the yellow pacman thing
arcade.draw_arc_filled(400,320, 120, 120, arcade.color.YELLOW, 30, 330)
# draw the small red square
arcade.draw_rectangle_filled(461,10, 6, 6, arcade.color.RED)
arcade.finish_render()


arcade.run()

