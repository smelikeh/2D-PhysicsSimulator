# 2D Physics Simulator

**An interactive educational application built using Python, Tkinter and Turtle to help students visualise and understand fundamental physics concepts.**

**Developer:** Melikeh Khan  
**Project:** HSC Software Design and Development Major Project (2024)  
**Language:** Python  
**Technologies:** Tkinter, Turtle, Python Math Library

---

## About the Project

The **2D Physics Simulator** is a Python-based desktop application developed as part of my Year 12 HSC Software Design and Development major project.

The application was designed to make learning physics more interactive and accessible by allowing students and teachers to explore physics concepts through visual simulations.

Rather than relying solely on theoretical explanations and mathematical formulas, users can enter their own parameters and observe how different variables influence the movement and behaviour of objects.

The project combines **graphical user interface development, mathematical calculations, user input validation, file handling and object-oriented programming**.

## Features

### Interactive Physics Simulations

The application includes several simulations demonstrating fundamental physics concepts.

**1. Projectile Motion**
- Simulates the trajectory of a projectile in a 2D environment.
- Allows users to customise initial velocity, launch angle and gravity.
- Uses mathematical calculations to determine the projectile's position over time.
- Visually demonstrates how different parameters affect the projectile's trajectory.

**2. Newton's First Law of Motion**
- Demonstrates the basic principles of motion.
- Uses Turtle graphics to visualise an object's movement.
- Provides an interactive demonstration to support theoretical learning.

**3. Hooke's Law and Simple Harmonic Motion**
- Demonstrates spring displacement and oscillatory motion.
- Allows users to enter spring constant, displacement and weight.
- Uses mathematical formulas to calculate and visualise spring behaviour.
- Helps users understand the relationship between applied force and displacement.

**4. Interactive Particle Simulation**
- Demonstrates the movement of particles within a 2D environment.
- Particles change direction when they reach the boundaries of the simulation.
- Users can interact with the simulation to generate additional particles.
- Uses Python classes to manage multiple particle objects.

### User Authentication
- User registration and login functionality.
- Account details are stored locally using file handling.
- User credentials are read from and written to `users.txt`.
- Demonstrates fundamental file I/O operations.

*Note: The authentication system was developed for educational purposes and is not intended for production use.*

### Graphical User Interface
- Desktop interface developed using Tkinter.
- Interactive simulations rendered using Turtle graphics.
- Navigation between different physics concepts.
- Input fields, buttons and error messages.
- Consistent layouts and interface elements.

### Input Validation
- Validates numerical inputs before running simulations.
- Converts user input into floating-point values for calculations.
- Displays error messages when invalid values are entered.
- Helps prevent unexpected errors caused by incorrect inputs.

### User Support
- User manual and installation documentation.
- Additional explanations of physics concepts.
- External links to educational resources.
- Feedback and questions forms.

---

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Tkinter | Graphical user interface |
| Turtle | 2D graphics and animations |
| Math Library | Physics calculations |
| File I/O | User registration and authentication |
| Object-Oriented Programming | Managing particle objects |
| PyCharm | Development environment |

---

## Getting Started

### Prerequisites

To run the application, you will need:

- Python 3 installed on your computer.
- A Python installation that supports Tkinter.
- A desktop environment capable of displaying GUI windows.

--

## How It Works

The application combines mathematical formulas with graphical animations to simulate physical behaviour.

For example, the projectile motion simulation calculates an object's horizontal and vertical position using:

**Horizontal displacement:**

`x = v × cos(θ) × t`

**Vertical displacement:**

`y = v × sin(θ) × t - ½gt²`

Where:

- `v` = Initial velocity
- `θ` = Launch angle
- `t` = Time
- `g` = Gravitational acceleration

The calculated coordinates are used to update the position of a Turtle graphics object, producing a visual representation of projectile motion.

The simulation continues updating the object's position until it reaches the defined ground boundary.

Other simulations follow a similar approach, combining user inputs, mathematical calculations and graphical movement.

---

## Development Process

This project was developed through several stages:

**Planning and Research**

Identified the need for an interactive educational physics tool and researched existing 2D physics simulations.

**GUI Development**

Created the main application interface using Tkinter, including navigation, buttons and input fields.

**Physics Implementation**

Implemented mathematical formulas and integrated Turtle graphics to demonstrate projectile motion, Newton's First Law and Hooke's Law.

**User Interaction**

Added customisable simulation parameters, input validation and user authentication.

**Testing and Evaluation**

Tested application functionality, gathered client feedback and improved the interface and simulations.

---

## Testing

The application was tested to ensure that its core features functioned as intended.

Testing included:

- User registration and login.
- Reading and writing account information.
- Navigation between application windows.
- Validation of numerical inputs.
- Running simulations using user-defined parameters.
- Checking the functionality of buttons and interactive elements.

Client feedback indicated that the application met its primary educational objectives, with opportunities for further improvement to the user interface and the addition of more physics concepts.

---

## Challenges and Learning Outcomes

Developing this project helped strengthen my understanding of Python programming and software development.

Some of the main challenges included:

- Integrating Turtle graphics into a Tkinter interface.
- Translating mathematical physics formulas into Python code.
- Updating object positions to produce animated simulations.
- Handling incorrect user inputs.
- Implementing file-based user authentication.
- Managing multiple particle objects using classes.
- Designing an interface that is accessible to students and teachers.

Through this project, I gained practical experience in:

- Python programming
- GUI development
- Object-oriented programming
- Mathematical modelling
- File handling
- Debugging and testing
- Software documentation
- User-centred design

---

## Future Improvements

Potential improvements include:

- Modernising the graphical user interface.
- Adding additional physics concepts and simulations.
- Allowing users to save and reload previous simulations.
- Introducing graphical representations of simulation data.
- Improving animation performance and visual accuracy.
- Enhancing user authentication and credential security.
- Refactoring the code into a more modular structure.

---

## Project Background

This application was created as my **2024 HSC Software Design and Development Major Project**.

The goal was to develop a functional software solution that demonstrated programming skills while addressing a real educational need.

The project involved planning, research, implementation, testing, user documentation and evaluation against client requirements.

It represents an early milestone in my software development journey and my interest in programming and building interactive applications.

---

## Author

**Melikeh Khan**

Bachelor of Information Technology  
University of Technology Sydney (UTS)

Interested in software development, networking, cybersecurity and building practical technology solutions.
