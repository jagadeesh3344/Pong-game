import turtle

# Function to ask for winning score
def get_winning_score():
    while True:
        try:
            score = int(input("Enter the winning score: "))
            if score > 0:
                return score
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

# setup game objects =================
# ball
ball = turtle.Turtle()
ball.speed(0)  # drawing speed (fastest)
ball.shape("square")
ball.color("white")
ball.shapesize(stretch_len=1, stretch_wid=1)
ball.penup()
ball.goto(x=0, y=0)  # start position
ball_dx, ball_dy = 1, 1
ball_speed = .5

# setup window ======================
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.goto(x=0, y=260)
score_display.write("Player1: 0 Player2: 0", align="center",
                    font=("Courier", 24, "normal"))
score_display.hideturtle()  # hide the object as we only want to see the text
p1_score, p2_score = 0, 0

# Get the winning score from the user
winning_score = get_winning_score()

# Main game loop
while True:
    ball.setx(ball.xcor() + ball_dx * ball_speed)
    ball.sety(ball.ycor() + ball_dy * ball_speed)

    # Score handling
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball_dx *= -1
        score_display.clear()
        p1_score += 1
        score_display.write(f"Player1: {p1_score} Player2: {p2_score}", align="center",
                            font=("Courier", 24, "normal"))
        if p1_score == winning_score:
           #complet it 
           pass

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball_dx *= -1
        score_display.clear()
        p2_score += 1
        score_display.write(f"Player1: {p1_score} Player2: {p2_score}", align="center",
                            font=("Courier", 24, "normal"))
        if p2_score == winning_score:
           #complete it
           pass

    # Ball boundary checking for y-axis
    if ball.ycor() > 290:
        ball.sety(290)
        ball_dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball_dy *= -1
