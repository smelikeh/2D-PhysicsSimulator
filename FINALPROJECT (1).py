import tkinter as tk  # creating GUI
import turtle  # drawing / simulating the graphics
import math  # mathematical functions
import time  # adding delays to simulations
import webbrowser
import customtkinter
import os
from subprocess import call
from tkinter import messagebox  # error messages

dark = "#0d1b2a"
dark2 = "#1b263b"
med = "#415a77"
light = "#778da9"
vlight = "#e0e1dd"

def mainscreen1():
    global mainscreen
    root.withdraw()
    mainscreen = tk.Toplevel()
    mainscreen.title('Main Screen')
    mainscreen.geometry("800x500")
    mainscreen.configure(background=vlight)

    # Creating the main page title
    frametop = tk.Frame(mainscreen, width=800, height=50, bg=light)
    frametop.place(x=1, y=1)

    framemid = tk.Frame(mainscreen, width=800, height=300, bg=light)
    framemid.place(x=1, y=275)

    heading = tk.Label(mainscreen, text="Basic Physics Simulator", fg="Black", bg=light, font=("Times New Roman", 25, "bold"))
    heading.place(x=1, y=1)

    welcome = tk.Label(mainscreen, text="Welcome to 2D Physics Simulator", fg=dark, bg=vlight, font=("Times New Roman", 30, "bold"))
    welcome.place(x=120, y=70)

    where = tk.Label(mainscreen, text="Click one of the options below to run the physics simulation in real time, and\n"
                                "be able to interact with them using parameters and interactions!",
                     bg=vlight, fg=dark, font=("Times New Roman", 15))
    where.place(x=90, y=160)

    button1 = tk.Button(mainscreen, text="Newtons 1st Law", command=newtonsLaw, font=("Times New Roman", 15))
    button1.place(x=100, y=300)

    button2 = tk.Button(mainscreen, text="Projectile Motion", command=projectilemotion, font=("Times New Roman", 15))
    button2.place(x=300, y=300)

    button3 = tk.Button(mainscreen, text="Hooke's Law", command=HookesLaw, font=("Times New Roman", 15))
    button3.place(x=500, y=300)

    button4 = tk.Button(mainscreen, text="Particle Motion", command=particlemotion, font=("Times New Roman", 15))
    button4.place(x=310, y=350)

    howtousebutton = tk.Button(mainscreen, text="How to use", command=howtouse, font=("Times New Roman", 15))
    howtousebutton.place(x=5, y=460)

    qanda = tk.Button(mainscreen, text="Q and A", font=("Times New Roman", 15), command=lambda: open_link("https://docs.google.com/document/d/19P0im2PpjIQtK8A5Mk2B8bNlmiPJUn5J7x45znkld14/edit?usp=sharing"))
    qanda.place(x=716, y=460)

    concerns = tk.Button(mainscreen, text="Concerns/Questions", font=("Times New Roman", 15),
                         command=lambda: open_link("https://forms.gle/xMV19rvKeBCuSW9y8"))
    concerns.place(x=120, y=460)

    feedback = tk.Button(mainscreen, text="Feedback", font=("Times New Roman", 15),
                         command=lambda: open_link("https://forms.gle/AspFPCHZAR3d3i4Y8"))
    feedback.place(x=623, y=460)

    mainscreen.mainloop()

userfile = 'users.txt'

def Runcode():
    call(["python", "physics1.py"])

def writeusers(user, pw):
    f = open(userfile, 'a')
    f.write(f"{user},{pw}\n")
def readusers():
        if not os.path.exists(userfile):
            return
        f = open(userfile, 'r')
        lines = f.readlines()
        users = {}
        for line in lines:
            user, pw = line.strip().split(',')
            users[user] = pw
        return users
def ssignup():
    loginframe.pack_forget()
    loginframe.pack()
def slogin():
    signupframe.pack_forget()
    signupframe.pack()
def signup():
        user = signupuser.get()
        pw = signuppw.get()
        if user and pw:
            users = readusers()
            if user in users:
                signuperror.config(text="account already exists", fg="red")
            else:
                writeusers(user,pw)
                signupuser.set("")
                signuppw.set("")
                signuperror.config(text="")
        else:
            signuperror.config(text="please enter a username and password", fg="red")
def login():
        user = loginuser.get()
        pw = loginpw.get()
        if user and pw:
            users = readusers()
            if user in users and users[user] == pw:
                loginuser.set("")
                loginpw.set("")
                mainscreen1()
            else:
                loginerror.config(text="invalid user/password", fg="red")
        else:
            loginerror.config(text="please enter a username and passowrd", fg="red")

def open_link(url):
        webbrowser.open_new(url)



def applytforce():
    turtle_particle.setx(turtle_particle.xcor() + 200)

def back_to_main(window):
    window.destroy()

def newtonsLaw():
    global turtle_particle
    top = tk.Toplevel()
    top.geometry("800x650")
    top.title("Newton's Law")
    top.configure(background=light)

    nwheading = tk.Label(top, text="Basic Physics Simulator", fg="Black", bg=light,
                         font=("Times New Roman", 25, "bold"))
    nwheading.place(x=1, y=1)

    nwwelcome = tk.Label(top, text="Newton's Laws of Motion", fg=dark, bg=light,
                         font=("Times New Roman", 30))
    nwwelcome.pack(pady=(40, 0))

    nwwhere_text = "Newton's First Law: Inertia\nF = ma\n" \
                   "F = Force M = Mass A = Acceleration/Gravity\n" \
                   "When an object remains at rest, and an object in motion remains\n" \
                   "in motion at constant speed and in a straight line\n" \
                   "unless acted on by an unbalanced force."

    nwwhere = tk.Label(top, text=nwwhere_text, bg="white", fg=dark, font=("Times New Roman", 15))
    nwwhere.pack(pady=(50, 0))

    canvas_frame = tk.Frame(top, width=800, height=200, bg="#ddffff")
    canvas_frame.pack(pady=(50, 0))

    canvas = tk.Canvas(canvas_frame, width=800, height=200, bg=light)
    canvas.pack()

    turtle_screen = turtle.TurtleScreen(canvas)
    turtle_particle = turtle.RawTurtle(turtle_screen)
    turtle_particle.shape("circle")
    turtle_particle.color(dark)

    launch_platform = turtle.RawTurtle(turtle_screen)
    launch_platform.penup()
    launch_platform.goto(-300, -100)
    launch_platform.pendown()
    launch_platform.goto(-280, -100)
    launch_platform.hideturtle()

    applyforce = tk.Button(top, text="Apply Force", command=applytforce, font=("Times New Roman", 15))
    applyforce.pack(pady=20)


    nwback = tk.Button(top, text="Back", command=lambda: back_to_main(top), font=("Times New Roman", 15))
    nwback.pack(padx=70)

def projectilemotion():
    pm = tk.Toplevel()
    pm.geometry("800x800")
    pm.title("Projectile motion")
    pm.configure(background=light)

    label1 = tk.Label(pm, text="Projectile Motion", bg=light, font=("Times New Roman", 20, "bold"))
    label1.pack(pady=10)

    input_frame = tk.Frame(pm,bg=light)
    input_frame.pack(pady=10)

    velocity_label = tk.Label(input_frame, text="Initial Velocity: \n"
                              "1-250", bg=light, font=("Times New Roman", 13))
    velocity_label.grid(row=0, column=0, padx=5, pady=5, sticky='e')
    velocity_entry = tk.Entry(input_frame)
    velocity_entry.grid(row=0, column=1, padx=5, pady=5)

    angle_label = tk.Label(input_frame, text="Angle:", bg=light, font=("Times New Roman", 13))
    angle_label.grid(row=1, column=0, padx=5, pady=5, sticky='e')
    angle_entry = tk.Entry(input_frame)
    angle_entry.grid(row=1, column=1, padx=5, pady=5)

    gravity_label = tk.Label(input_frame, text="Gravity:", bg=light, font=("Times New Roman", 13))
    gravity_label.grid(row=2, column=0, padx=5, pady=5, sticky='e')
    gravity_entry = tk.Entry(input_frame)
    gravity_entry.grid(row=2, column=1, padx=5, pady=5)

    math_button = tk.Button(input_frame, text="Mathematical Explanation", font=("Times New Roman", 13), command=lambda: open_link("https://docs.google.com/document/d/1Y3DEiEN4fu-YJxkn477kMesEKq1F-7CCVMUi-JieZZw/edit?usp=sharing"))
    math_button.grid(row=6, column=1)

    def simulatepm(turtle_particle, velocity, angle, gravity, screen):
        # Set the initial position, also clear position when the module is run each time
        turtle_particle.clear()
        turtle_particle.penup()
        turtle_particle.goto(-300, -100)
        turtle_particle.pendown()
        turtle_particle.clear()

        # Calculate initial velocities in the x and y directions
        vx = velocity * math.cos(angle)
        vy = velocity * math.sin(angle)
        t = 0
        dt = 0.05  # Time step for the simulation

        while True:
            x = vx * t
            y = vy * t - 0.5 * gravity * 10 * t ** 2
            if y < -100:  # If the projectile hits the ground, break the loop
                break
            turtle_particle.goto(-300 + x, -100 + y)  # Move the turtle to the new position
            screen.update()
            time.sleep(dt)  # Delay for smooth animation
            t += dt

    canvas = tk.Canvas(pm, width=800, height=400, bg="#ddffff")
    canvas.pack()


    turtle_screen = turtle.TurtleScreen(canvas)
    turtle_particle = turtle.RawTurtle(turtle_screen)
    turtle_particle.shape("circle")
    turtle_particle.color(dark)

    launch_platform = turtle.RawTurtle(turtle_screen)
    launch_platform.penup()
    launch_platform.goto(-300, -100)
    launch_platform.pendown()
    launch_platform.goto(-280, -100)
    launch_platform.hideturtle()

    button_frame = tk.Frame(pm, bg=light)
    button_frame.pack(pady=10)

    def runpmturt():
        # Get input values from entries
        velocity_input = velocity_entry.get()
        angle_input = angle_entry.get()
        gravity_input = gravity_entry.get()

        # Check if the inputs are valid numbers
        if not (velocity_input.replace('.', '', 1).isdigit() and angle_input.replace('.', '', 1).isdigit() and gravity_input.replace(
                '.', '', 1).isdigit()):
            messagebox.showerror("Invalid Input", "Please enter valid numerical values for velocity, angle, and gravity.")
            return

        # Convert inputs to float
        velocity = float(velocity_input)
        angle = math.radians(float(angle_input))
        gravity = float(gravity_input)

        # Run the simulation with the validated inputs
        simulatepm(turtle_particle, velocity, angle, gravity, turtle_screen)

    start_button = tk.Button(button_frame, text="Start Simulation", command=runpmturt, font=("Times New Roman", 15))
    start_button.grid(row=0, column=0, padx=5, pady=5)

    back_button = tk.Button(button_frame, text="Back", command=lambda: back_to_main(pm), font=("Times New Roman", 15))
    back_button.grid(row=0, column=1, padx=5, pady=5)

def HookesLaw():
    hl = tk.Toplevel()
    hl.geometry("800x800")
    hl.title("Hooke's Law")
    hl.configure(background=light)

    label1 = tk.Label(hl, text="Hooke's Law Simulation", bg=light, font=("Times New Roman", 25, "bold"))
    label1.pack(pady=10)

    input_frame = tk.Frame(hl, bg=light)
    input_frame.pack(pady=10)

    k_label = tk.Label(input_frame, text="Velocity:", bg=light, font=("Times New Roman", 15))
    k_label.grid(row=0, column=0, padx=5, pady=5, sticky='e')
    k_entry = tk.Entry(input_frame)
    k_entry.grid(row=0, column=1, padx=5, pady=5)

    displacement_label = tk.Label(input_frame, text="Distance:", bg=light, font=("Times New Roman", 15))
    displacement_label.grid(row=1, column=0, padx=5, pady=5, sticky='e')
    displacement_entry = tk.Entry(input_frame)
    displacement_entry.grid(row=1, column=1, padx=5, pady=5)

    weight_label = tk.Label(input_frame, text="Weight:", bg=light, font=("Times New Roman", 15))
    weight_label.grid(row=2, column=0, padx=5, pady=5, sticky='e')
    weight_entry = tk.Entry(input_frame)
    weight_entry.grid(row=2, column=1, padx=5, pady=5)

    math_butt = tk.Button(input_frame, text="Mathematical Explanation", font=("Times New Roman", 13),
                            command=lambda: open_link(
                                "https://docs.google.com/document/d/1yBYyMdl_IW0DBc8EWGrsq3FaL2uo67trSI27Km2YFCc/edit?usp=drive_link"))
    math_butt.grid(row=6, column=1)

    canvas = tk.Canvas(hl, width=800, height=400, bg="#ddffff")
    canvas.pack()

    turtle_screen = turtle.TurtleScreen(canvas)
    spring_turtle = turtle.RawTurtle(turtle_screen)
    spring_turtle.shape("circle")
    spring_turtle.color(dark)

    equilibrium_point = -100

    button_frame = tk.Frame(hl, bg=light)
    button_frame.pack(pady=10)

    def run_shm_simulation():
        # Get input values from entries
        k_input = k_entry.get()
        weight_input = weight_entry.get()

        # Check if the inputs are valid numbers
        if not (k_input.replace('.', '', 1).isdigit() and weight_input.replace('.', '', 1).isdigit()):
            messagebox.showerror("Invalid Input", "Please enter valid  values")
            return

        # Convert inputs to float
        k = float(k_input)
        weight = float(weight_input)

        omega = math.sqrt(k / weight)

        # Simulate simple harmonic motion
        spring_turtle.clear()
        spring_turtle.penup()
        spring_turtle.goto(-300, equilibrium_point)
        spring_turtle.pendown()

        t = 0
        dt = 0.05
        amplitude = weight / k  # Initial displacement based on weight and spring constant

        while True:
            y = amplitude * math.cos(omega * t)
            spring_turtle.goto(-300, equilibrium_point + y * 100)
            turtle_screen.update()
            time.sleep(dt)  # Delay for smooth animation
            t += dt  # Increment the time

            if t > 10:  # Stop after 10 seconds
                break

    start_hooke_button = tk.Button(button_frame, text="Start Hooke's Law Simulation", command=run_shm_simulation, font=("Times New Roman", 15))
    start_hooke_button.grid(row=0, column=0, padx=5, pady=5)

    back_button = tk.Button(button_frame, text="Back", command=lambda: back_to_main(hl), font=("Times New Roman", 15))
    back_button.grid(row=0, column=2, padx=5, pady=5)

def particlemotion():
    billard = tk.Toplevel()
    billard.title("Billards")
    billard.geometry("800x400")
    billard.configure(background=light)

    label1 = tk.Label(billard, text="Particle Motion", bg=light, font=("Times New Roman", 20, "bold"))
    label1.pack(pady=10)

    input_frame = tk.Frame(billard)
    input_frame.pack(pady=10)

    particlem = "This simulation models the behavior of particles moving within a confined space.\n"\
                "Each particle moves with a certain velocity, and when it hits the boundary of the\n" \
                "simulation area, it bounces back, much like a ball hitting a wall. This demonstrates\n"\
                "basic principles of motion and elastic collisions. By observing how the particles move\n"\
                "and interact with the boundaries, you can get a visual understanding of how objects\n"\
                " behave when they are free to move and encounter obstacles in their path.\n"\

    yea = "Feel free to click on the screen to add more particles and observe how they interact\n" \
            "within the confined space. This simple model can help you understand fundamental\n" \
            "concepts of particle dynamics and boundary interactions."

    stuff = tk.Label(input_frame, text=particlem, font=("Times New Roman", 15))
    stuff.pack()

    morestuff = tk.Label(input_frame, text=yea, font=("Times New Roman", 15))
    morestuff.pack()

    butt = tk.Button(input_frame, text="Start simulation", command=Runcode, font=("Times New Roman", 15))
    butt.pack()

    backbutt = tk.Button(input_frame, text="Back", command=lambda: back_to_main(billard), font=("Times New Roman", 15))
    backbutt.pack()

def howtouse():
    howto = tk.Toplevel()
    howto.geometry("300x150")
    howto.title("How to use")

    httext= tk.Label(howto, text="All you have to do is input the variables of your choice,\n"
                                 " which they will then be calculated. Once the\n"
                                 "calculation is made,the simulation will start.\n"
                                "Some selections dont have simulations, instead\n"
                                "they will show the working out.\n"
                                 " For more help please refer to the link bellow.", font=("Times New Roman", 10))
    httext.pack()

    okbutton = tk.Button(howto, text="ok", command=howto.destroy, font=("Times New Roman", 10))
    okbutton.pack()


    link = tk.Button(howto, text="Link", command=lambda: open_link("https://docs.google.com/document/d/18_pK3XKNg1OuF8PbnSzZJ0axYJNWbao5MzNBOFmchRU/edit?usp=sharing"), font=("Times New Roman", 10))
    link.pack()




root = tk.Tk()
root.title("Login/Signup")
root.geometry("800x500")
root.configure(background=light)

loginuser = tk.StringVar()
loginpw = tk.StringVar()
signupuser = tk.StringVar()
signuppw = tk.StringVar()

frametop = tk.Frame(root, width=800, height=800, bg=light)
frametop.pack(fill=tk.X)

heading = tk.Label(frametop,text="Basic Physics Simulator",fg=dark,bg=light,font=("Times New Roman",25,"bold"))
heading.pack()

welcome = tk.Label(root,text="Welcome to 2D Physics Simulator",fg=dark,bg=light,font=("Times New Roman",30,"bold"))
welcome.pack(pady=20)

# Login Frame
loginframe = tk.Frame(root, width=400, height=200, bg=med)
loginframe.pack(side=tk.LEFT, padx=10, pady=10, expand=True)

logina = tk.Label(loginframe, text="Login", bg=med, font=("Times New Roman", 20, "bold"))
logina.pack(pady=20)

loginb = tk.Label(loginframe, text="Username:", bg=med, font=("Times New Roman", 15))
loginb.pack(pady=5)
enterb = tk.Entry(loginframe, textvariable=loginuser, font=("Times New Roman", 15))
enterb.pack(pady=5)

loginc = tk.Label(loginframe, text="Password:", bg=med, font=("Times New Roman", 15))
loginc.pack(pady=5)
enterc = tk.Entry(loginframe, textvariable=loginpw, show="*", font=("Times New Roman", 15))
enterc.pack(pady=5)

loginbutt = tk.Button(loginframe, text="Login", command=login, font=("Times New Roman", 15))
loginbutt.pack(pady=20)

loginerror = tk.Label(loginframe, text="", bg=med)
loginerror.pack()

# Signup Frame
signupframe = tk.Frame(root, width=400, height=200, bg=med)
signupframe.pack(side=tk.RIGHT, padx=10, pady=10, expand=True)

signupa = tk.Label(signupframe, text="Sign Up", bg=med, font=("Times New Roman", 20, "bold"))
signupa.pack(pady=20)

signupb = tk.Label(signupframe, text="Username:", bg=med, font=("Times New Roman", 15))
signupb.pack(pady=5)
signupc = tk.Entry(signupframe, textvariable=signupuser, font=("Times New Roman", 15))
signupc.pack(pady=5)

signupd = tk.Label(signupframe, text="Password:", bg=med, font=("Times New Roman", 15))
signupd.pack(pady=5)
signupe = tk.Entry(signupframe, textvariable=signuppw, show="*", font=("Times New Roman", 15))
signupe.pack(pady=5)

signupbut = tk.Button(signupframe, text="Sign Up", command=signup, font=("Times New Roman", 15))
signupbut.pack(pady=20)

signuperror = tk.Label(signupframe, text="", bg=med)
signuperror.pack()

howtousebutton = tk.Button(root, text="How to use", command=howtouse, font=("Times New Roman", 15))
howtousebutton.place(x=5, y=460)

qanda = tk.Button(root, text="Q and A", font=("Times New Roman", 15), command=lambda: open_link("https://docs.google.com/document/d/19P0im2PpjIQtK8A5Mk2B8bNlmiPJUn5J7x45znkld14/edit?usp=sharing"))
qanda.place(x=716, y=460)



root.mainloop()
