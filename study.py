
#print("maitei mundore")
# Cuenta del 1 al 5 (solo estoy probando el pq no consigo ver las lineas en github)
#for i in range(1, 6):
    #print(f"Número: {i}")

#tryin again de subir algodon    

#python practice 08/04/2026
#current_time_str = input ("What is the current time (in hours 0 - 23)?")
#wait_time_str = input ("How many hours do you want to wait")
#current_time_int = int (current_time_str) 
#wait_time_int = int(wait_time_int)  wait_time_int does not have a value so it cannot be used on the right hand side.
#final_time_int = current_time_int + wait_time_int
#print(final_time_int)   

#present_time = input("Enter the present timein hours:")
#set_time = input("Set the hours for alarm:")
#present_time = int(present_time) 
#set_time = int (set_time)
#alarm_time = present_time + set_time
#print(alarm_time)

#16/04/2026
#the mantra 
#Get something working and keep it working
#its a exercise to create a little house
import turtle
import math
wn = turtle.Screen()
bob = turtle.Turtle()
bob.right(90)
bob.forward(50)
bob.left(90)
bob.forward(50)
bob.left(90)
bob.forward(50)
bob.left(90)
bob.forward(50)
bob.right(135)
dist = math.sqrt(50*50/2)
bob.forward(dist)
bob.right(90)
bob.forward(dist)   

#another form just to create a square
import turtle
wn = turtle.Screen()
june = turtle.Turtle()

for _ in range (4):
    june.color ("green","yellow")
    june.forward("50")
    june. right(90)

#waqi' etz'nab waq'lajuj

# a code to draw a regular pentagon

import turtle
wn = turtle.Screen()
bernie = turtle.Turtle()
bernie.forward(80)
bernie.left(72)
bernie.forward(80)
bernie.left(72)
bernie.forward(80)
bernie.left(72)
bernie.forward(80)
bernie.left(72)
bernie.forward(80)

#create a circular geometric mandala, ussing the .speed method
import turtle
t = turtle.Turtle()
t.speed(0) 


for _ in range(18):
    t.forward(100)
    t.right(190)

turtle.done()