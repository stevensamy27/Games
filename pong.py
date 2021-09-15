import turtle

wn = turtle.screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, heigt=600)
wn.tracer(0)


#Main Game Loop
while True:
    wn.update()