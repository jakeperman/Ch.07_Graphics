'''
FLAG PROJECT
---------------
Make your flag 260 pixels tall
Use the scaling image on the website to determine other dimensions
The hexadecimal colors for the official flag are red:#BF0A30 and blue:#002868
Title the window, "The Stars and Stripes"
I used a draw_text command and used 20 pt. asterisks for the stars.
We will have a competition to see who can make this flag in the least lines of code.
The record is 16! You will have to use some loops to achieve this.
'''
import arcade


# function to draw a star
def star(x, y):
    draw = ((x-6, y+2), (x-1, y+1), (x, y+6), (x+2, y+1), (x+6, y+2), (x+2, y-1.5), (x+5, y-6), (x, y-3), (x-5, y-6),
            (x-2, y-1.5))
    arcade.draw_polygon_filled(draw, arcade.color.WHITE)


# addressable database of flag proportions
def num(x):
    index = ord(x)-97
    print(index)
    values = [260, 494, 140, 198, 14, 14, 16.4, 16.4, 16, None, None, 20]
    px = values[index]
    print(px)
    return px


# open window to draw flag
arcade.open_window(num('b'), num('a'), "Flag")
arcade.set_background_color(arcade.color.WHITE)
# start of render
arcade.start_render()
# draw the stripes
for i in range(0, 300, 40):
    arcade.draw_rectangle_filled(num('b')/2, 10+i, num('b'), num('l'), (191, 10, 48))
# draw the flag outline
arcade.draw_rectangle_outline(247, 130, num('b'), num('a'), arcade.color.BLACK, 5)
# draw the blue section of flag (xpos, ypos, d, c)
arcade.draw_rectangle_filled(99, 190, num('d'), num('c'), (0, 40, 104))


# drawing of the stars
times = 0
# loops for each y-level stars should be drawn at
for level in range(1, 10):
    # sets current y position
    ypos = (num('a') - (num('f')*times))-num('e')
    times += 1
    # changes star position and count based on whether an odd or even row
    if level%2 == 0:
        count = 5
        xdis = num('h')*2
    else:
        count = 6
        xdis = num('g')
    # draws stars across flag at current y level
    for stars in range(0, count):
        # xpos = num('g'), num('d') - num('g'), num('h') * 2
        # offsets the x position each time the loop runs
        xpos = (num('g')*stars) * 2 + xdis
        star(xpos, ypos)
# end of render
arcade.finish_render()
arcade.run()
