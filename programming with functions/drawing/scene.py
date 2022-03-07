
from turtle import width
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py library
    # which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.

    draw_grid(canvas, scene_width, scene_height, 50)
    draw_sky(canvas,scene_width,scene_height)
    draw_sun(canvas, 500, 200)  

    draw_ground(canvas, 600, 300)

    draw_clouds(canvas, 200, 100)

    draw_pine_tree(canvas, 750, 150, 290)
    draw_pine_tree(canvas, 700, 150, 240)
    draw_pine_tree(canvas, 650, 150, 250)
    draw_pine_tree(canvas, 400, 150, 260)
    draw_pine_tree(canvas, 550, 150, 270)
    draw_pine_tree(canvas, 500, 150, 230)
    draw_pine_tree(canvas, 450, 150, 280)
    draw_pine_tree(canvas, 600, 150, 300)
    
    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.

def draw_pine_tree(canvas, center_x, bottom, height):
    trunk_width = height / 10
    trunk_height = height / 5
    left_trunk = center_x - trunk_width / 2
    bottom_trunk = bottom
    right_trunk = center_x + trunk_width / 2
    trunk_top = bottom + trunk_height
    draw_rectangle(canvas, left_trunk, bottom_trunk, right_trunk, trunk_top, fill = "tan4")
    skirt_width = height / 2
    skirt_left = center_x - skirt_width / 2
    skirt_bottom = trunk_top
    skirt_center = center_x
    skirt_top = bottom + height
    skirt_right = center_x + skirt_width / 2
    draw_polygon(canvas, skirt_left, skirt_bottom, skirt_center, skirt_top, skirt_right, skirt_bottom, fill = "green3")

def draw_grid(canvas, width, height, interval):
    label_y = 15
    for x in range(interval, width, interval):
        draw_line(canvas, x, 0, x, height)
        draw_text(canvas, x, label_y, f"{x}")
    label_x = 15
    for y in range(interval, height, interval):
        draw_line(canvas, 0, y, width, y)
        draw_text(canvas, label_x, y, f"{y}")
def draw_sky(canvas, width, height):
    draw_line(canvas, 0, 0, 300, 750, width = 1650, fill="cyan1")
    #draw_line(canvas, 0, 5, 100, 50, width=10, fill="blue")
def draw_sun(canvas,width,height):
    draw_oval(canvas, 200, 500, 50, 300, fill="yellow")
def draw_ground(canvas,width,height):
    for i in range(500):
        draw_line(canvas, 0, 150, 0, 0, width = 1650, fill="tan2")
def draw_clouds(canvas,width, height):
    draw_oval(canvas, 710, 350, 220, 550, fill="lavender")



# Call the main function so that
# this program will start executing.
main()

