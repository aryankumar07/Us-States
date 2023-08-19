import turtle
import pandas as pd

pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
screen = turtle.Screen()
screen.title("Game")
image = "/Users/aryankumar/Desktop/python/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
state_data = pd.read_csv("/Users/aryankumar/Desktop/python/50_states.csv")
states = state_data["state"]


play = True

while play:
    answer_state = screen.textinput(title="Guess the state",prompt="enter the state name")

    found = False

    for ans in states:
        if ans == answer_state:
            row = state_data[state_data["state"]==ans]
            xpos = row.iloc[0]['x']
            ypos = row.iloc[0]['y']
            pen.goto(xpos,ypos)
            pen.write(ans,align="center",font=("Arial",12,"normal"))




screen.exitonclick()