'''
PYCASSO PROJECT
---------------
Your job is to make a cool picture.
You must use multiple colors.
You must have a coherent picture. No abstract art with random shapes.
You must use multiple types of graphic functions (e.g. circles, rectangles, lines, etc.)
Somewhere you must include a WHILE or FOR loop to create a repeating pattern.
Do not just redraw the same thing in the same location 10 times. 
You can contain multiple drawing commands in a loop, so you can draw multiple train cars for example.
Please use comments and blank lines to make it easy to follow your program. 
If you have 5 lines that draw a robot, group them together with blank lines above and below. 
Then add a comment at the top telling the reader what you are drawing.
IN THE WINDOW TITLE PLEASE PUT YOUR NAME.
When you are finished Pull Request your file to your instructor.
'''
import arcade

y = 800
x = 600
xc = x/2
yc = y/2
arcade.open_window(x, y, "")
arcade.set_background_color(arcade.color.STAR_COMMAND_BLUE)

arcade.start_render()

arcade.draw_ellipse_filled(xc, yc, 400, 500, arcade.color.ALMOND)
# hair
sizex = 600
sizey = 900
yhair = (yc - ((sizey-500)/2))
for i in range(0, 30):
    sizex -= 10
    sizey -= 6
    yhair += 3
    arcade.draw_arc_outline(xc, yhair, sizex, sizey, arcade.color.BLOND, 0, 180, 6)
    arcade.draw_arc_outline(xc, yhair - 2, sizex-2, sizey-1, arcade.color.ANTIQUE_BRASS, 0, 180, 6)
    arcade.draw_arc_outline(xc, yhair, sizex, sizey, arcade.color.BLOND, 0, 180, 6)
    arcade.draw_arc_outline(xc, yhair - 1, sizex - 1, sizey + 1, arcade.color.ANTIQUE_BRASS, 0, 180, 6)
    arcade.draw_arc_outline(xc, yhair-3, sizex-3, sizey+1.5, arcade.color.BLOND, 0, 180, 6)





# Draw the eyes
for i in range(-80, 160, 160):
    arcade.draw_ellipse_filled(xc+i, yc+100, 60, 35, arcade.color.WHITE)
    arcade.draw_ellipse_filled(xc+i, yc+100, 40, 25, arcade.color.BLUE)
    arcade.draw_ellipse_filled(xc+i, yc+100, 15, 15, arcade.color.BLACK)

# eyebrows
# arcade.draw_polygon_filled(xc-80, yc+125, )
for i in range(-80, 160, 160):
    arcade.draw_rectangle_outline(xc-i, yc+130, 55, 5, arcade.color.BLACK, 1, -(1.05*(i+(i+1))))
    arcade.draw_rectangle_filled(xc-i, yc+130, 55, 5, arcade.color.BURLYWOOD, 1.05*(i+(i+1)))


# draw the nose
arcade.draw_arc_outline(xc-50, yc, 50, 100, arcade.color.BLACK, -10, 60, 10, -30)
arcade.draw_arc_outline(xc+50, yc+25, 50, 100, arcade.color.BLACK, 170, 240, 10, 10)
arcade.draw_circle_filled(xc+20, yc-15, 5, arcade.color.BLACK)
arcade.draw_circle_filled(xc-10, yc-15, 5, arcade.color.BLACK)
arcade.draw_arc_outline(xc+25, yc-15, 40, 40, arcade.color.BLACK, 80, 195, 8)
arcade.draw_arc_outline(xc-15, yc-15, 40, 40, arcade.color.BLACK, 0, 115, 8)

# draw the mouth
# arcade.draw_arc_outline(xc, yc-60, 250, 200, arcade.color.BRICK_RED, -150, -30, 33)
arcade.draw_arc_outline(xc, yc-125, 150, 1, arcade.color.BLACK, 0, 260, 20)
arcade.draw_arc_outline(xc, yc-125, 150, 20, arcade.color.BRICK_RED, 0, 360, 25)



arcade.finish_render()
arcade.run()



