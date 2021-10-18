import turtle 
win = turtle.Screen()
win.bgcolor("black")
win.setup(700,700)
win.title("Fidget Spinner")
turtle.color("Yellow")
turtle.write("FIDGET SPINNER" , align= "right" , font=("Arial" , 20 , "bold") )
turtle.color("green")
turtle.write("USE SPACE BUTTON TO SPEED UP " , align= "left" , font=("Arial" , 15 , "bold") )



obj1 = turtle.Turtle()
obj1.speed(8)
obj1.color("white")
obj1.width(3)
obj1.hideturtle()
obj1.goto(0.00 , -200.00)
speed= {"turn" :0}
length = 100
rad = 120
def spinner():
    obj1.clear()
    angle = speed["turn"]/10
    obj1.right(angle)
    obj1.forward(length)
    obj1.dot(rad , "red")
    obj1.dot(20,"yellow")
    obj1.back(length)
    obj1.right(120)



    
    obj1.forward(length)
    obj1.dot(rad , "green")
    obj1.dot(20,"yellow")
    obj1.back(length)
    obj1.right(120)


    
    obj1.forward(length)
    obj1.dot(rad , "blue")
    obj1.dot(20,"yellow")
    obj1.back(length)
    obj1.right(120)
    




def speedingup():
    speed["turn"] += 40 
def  roatate():
    if speed["turn"] !=0 :
        speed["turn"] -= 1
    spinner()
    win.ontimer(roatate,20)
def main():
    win.tracer(False)
    win.onkey(speedingup,'space')
    win.listen()
    roatate()
    
    
    turtle.done()

if _name=="main_":
    main()
