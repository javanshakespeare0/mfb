import colorsys
import math
import turtle


screen = turtle.Screen()
screen.bgcolor("#08051c")
screen.title("Rainbow Flower Wave")
screen.setup(width=900, height=800)
screen.tracer(0)

petal_count = 12
arc_steps = 12
wave_delay = 3
layer = 0
layer_frame = 0
timer_delay = 3
frames_per_tick = 9
frames_per_layer = (petal_count - 1) * wave_delay + arc_steps * 2 + 1
pens = []

for petal in range(petal_count):
    pen = turtle.Turtle()
    pen.speed(0)
    pen.pensize(2)
    pen.hideturtle()
    pens.append(pen)

writing_pen = turtle.Turtle()
writing_pen.hideturtle()
writing_pen.penup()
writing_pen.pensize(1)
message = "Love yo Tasha"
text_radius = 470
text_center_y = -195
character_spacing = 24
text_index = 0
text_pass = 0
text_passes = 8


def draw_message():
    global text_index, text_pass

    index = text_index
    character = message[index]
    offset = (index - (len(message) - 1) / 2) * character_spacing
    angle = math.pi / 2 - offset / text_radius
    x = text_radius * math.cos(angle)
    y = text_center_y + text_radius * math.sin(angle)
    brightness = 0.2 + 0.8 * text_pass / (text_passes - 1)

    writing_pen.goto(x, y)
    writing_pen.pencolor(
        colorsys.hsv_to_rgb(index / len(message), 0.55, brightness)
    )
    writing_pen.write(character, align="center", font=("Arial", 18, "normal"))

    text_index += 1
    if text_index == len(message):
        text_index = 0
        text_pass += 1

    screen.update()
    if text_pass < text_passes:
        screen.ontimer(draw_message, 45)


def animate():
    global layer, layer_frame, timer_delay

    for _ in range(frames_per_tick):
        if layer == 70:
            for pen in pens:
                pen.clear()
            layer = 0
            layer_frame = 0

        radius = 80 + 40 * math.sin(layer / 15)

        for petal, pen in enumerate(pens):
            start_frame = petal * wave_delay
            progress = layer_frame - start_frame

            if progress == 0:
                hue = (petal / petal_count + layer / 35) % 1
                pen.pencolor(colorsys.hsv_to_rgb(hue, 0.82, 1.0))
                pen.penup()
                pen.home()
                pen.setheading(petal * 30 + layer)
                pen.pendown()
            elif 1 <= progress <= arc_steps:
                pen.circle(radius, 10)
            elif progress == arc_steps + 1:
                pen.left(120)
                pen.circle(radius, 10)
            elif arc_steps + 1 < progress <= arc_steps * 2:
                pen.circle(radius, 10)

        layer_frame += 1

        if layer_frame == frames_per_layer:
            layer += 1
            layer_frame = 0

    screen.update()

    screen.ontimer(animate, timer_delay)
    timer_delay = 7 - timer_delay


draw_message()
animate()
screen.mainloop()
