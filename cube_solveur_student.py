import kociemba


# ---------------- Memory -----------------


cube_memory = {
    "U": "UP",    # Face Up is on the top initially 
    "D": "DOWN",  # Face Down is on the bottom initially 
    "F": "FRONT", # Face Front is forward initially 
    "B": "BACK",  # Face Back is backward initially 
    "L": "LEFT",  # Face Left is facing the left initially 
    "R": "RIGHT"  # Face Right is facing the right initially 
}

def rotation_L():
    """
    All the rotation functions are parts of the memory for the robot. 
    rotation_X modifies the dictionary 'cube_memory' by applying an X rotation.

    """
    global cube_memory
    
    # We save how the cube is currently oriented before modifying it 
    previous = cube_memory.copy()
    
    cube_memory["L"] = previous["D"] # The previous down is now at the left
    cube_memory["R"] = previous["U"] # The previous up is now at the right
    cube_memory["B"] = previous["F"] # The previous front is now at the back 
    cube_memory["F"] = previous["B"] # The previous back is now at the front
    cube_memory["U"] = previous["R"] # The previous right is now up
    cube_memory["D"] = previous["L"] # The previous left is now down
    return

def rotation_R():
    return

def rotation_U():
    return

def rotation_D():
    return

def rotation_F():
    return

def rotation_B():
    return

def rotation_Li():
    return

def rotation_Ri():
    return

def rotation_Ui():
    return

def rotation_Di():
    return

def rotation_Fi():
    return

def rotation_Bi():
    return

def rotation_L2():
    return

def rotation_R2():
    return

def rotation_U2():
    return

def rotation_D2():
    return

def rotation_F2():
    return

def rotation_B2():
    return

rotations = {
    "L": rotation_L,
    
    }


def memorisation(initial_solution = list):
    """
    This function's purpose is to change the solution to implement a memory for the robot 
    because of the fact that the robot will change the orientation of it, so the faces will 
    change during the resolution of the cube.
    """
    sol = []
    
    
    return sol




# --------------- Movement ----------------


details_movement = {
    "L":["#L",
        "#take from above",
        "movel(p[-0.335, -0.1, 0.15, 2.221, -2.221, 0], a=2, v=1)",
        "movel(p[-0.335, -0.1, 0.048, 2.221, -2.221, 0], a=1.2, v=0.75)",
        "twofg_grip(40, 30, 2)",
        "movel(p[-0.335, -0.1, 0.15, 2.221, -2.221, 0], a=1.2, v=0.75)",
        "#place the left side down",
        "movel(p[-0.351, -0.083, 0.15, 0, 2.221, -2.221], a=2, v=1)",
        "movel(p[-0.351, -0.083, 0.052, 0, 2.221, -2.221], a=1.2, v=0.75)",
        "twofg_grip(80, 30, 2)",
        "movel(p[-0.351, -0.083, 0.15, 0, 2.221, -2.221], a=1.2, v=0.75)",
        "#move the clamp up",
        "movel(p[-0.351, -0.1, 0.15,  0, 3.142, 0], a=2, v=1)",
        "movel(p[-0.351, -0.1, 0.048, 0, 3.142, 0], a=1.2, v=0.75)",
        "twofg_grip(40, 30, 2)",
        "#turn the leftside clockwise",
        "movel(p[-0.351, -0.1, 0.050, 2.221, 2.221, 0], a=1.2, v=0.5)",
        "twofg_grip(80, 30, 2)",
        "movel(p[-0.351, -0.1, 0.15, 2.221, 2.221, 0], a=1.2, v=0.75)"
        ],
    "R":[
        ],
    "F":[
        ],
    "B":[
        ],
    "U":[
        ],
    "D":[
        ],
    "L'":[
        ],
    "R'":[
        ],
    "F'":[
        ],
    "B'":[
        ],
    "U'":[
        ],
    "D'":[
        ],
    "L2":[
        ],
    "R2":[
        ],
    "F2":[
        ],
    "B2":[
        ],
    "U2":[
        ],
    "D2":[
        ],
    }

possible_movement = {
    # simple rotations (90° clockwise)
    "ROTATE_LEFT_FACE"  : "L",
    "ROTATE_RIGHT_FACE" : "R",
    
    # counter rotations (90° counterclockwise)
    "ROTATE_LEFT_FACE_OPPOSITE"  : "L'",
    "ROTATE_RIGHT_FACE_OPPOSITE" : "R'",
    
    # double rotations (180° clockwise)
    "ROTATE_LEFT_FACE_DOUBLE"  : "L2",
    "ROTATE_RIGHT_FACE_DOUBLE" : "R2",
    
    }



# ------------ Part to fill for the cube ------------


scrambled_cube = {
                'U': [], 
                'D': [],
                'F': [],
                'L': [], 
                'B': [], 
                'R': []
                }


# ---------- Function of resolution ---------------






def conversion(cube = dict):
    return



# ------------- Writing to the file -------------


"""
Don't forget to choose the right file where you want this code 
to write the programm for the cube.

For this you can either save this code in the file you want the programme to be 
or modify the first parameter of the 'open()' section bellow.
"""

with open("program_rubiks.script", "w") as fichier:
    fichier.write("def resoudre_cube():\n")
    


    fichier.write("end\n")
    fichier.write("resoudre_cube()\n")







