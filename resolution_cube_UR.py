import kociemba
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# ----------Traduction for following function -----------

traduction_kociemba = {
    "W": "U",  # the white face is on the top 
    "Y": "D",  # the yellow face is on the bottom    
    "B": "B",  # the blue face is on the back
    "G": "F",  # the green face is on the front
    "R": "R",  # the red face is on the right 
    "O": "L"   # the orange face is on the left
    }

traduction_movement = {
    "U": "UP",    # Up == Haut
    "D": "DOWN",  # Down == Bas
    "F": "FRONT", # Front == Avant
    "B": "BACK",  # Back == Arriere
    "L": "LEFT",  # Left == Gauche
    "R": "RIGHT"  # Right == Droite
    }

traduction_FR_EN_couleur = {
    "Blanc" : "W",   # White
    "Jaune" : "Y",   # Yellow
    "Vert" : "G",    # Green
    "Bleu" : "B",    # Blue
    "Rouge" : "R",   # Red
    "Orange" : "O",  # Orange
    }


# --------------- Movement ----------------


details_movement = {
    "R":["#R",
        "#take from above",
        "movel(p[-0.37, -0.1, 0.15, 2.221, 2.221, 0], a=2, v=1)",
        "movel(p[-0.37, -0.1, 0.048, 2.221, 2.221, 0], a=1.2, v=0.75)",
        "twofg_grip(40, 30, 2)",
        "movel(p[-0.37, -0.1, 0.15, 2.221, 2.221, 0], a=1.2, v=0.75)",
        "#place the right side down",
        "movel(p[-0.351, -0.083, 0.15, 0, 2.221, -2.221], a=2, v=1)",
        "movel(p[-0.351, -0.083, 0.052, 0, 2.221, -2.221], a=1.2, v=0.75)",
        "twofg_grip(80, 30, 2)",
        "movel(p[-0.351, -0.083, 0.15, 0, 2.221, -2.221], a=1.2, v=0.75)",
        "#move the clamp up",
        "movel(p[-0.351, -0.1, 0.15,  0, 3.142, 0], a=2, v=1)",
        "movel(p[-0.351, -0.1, 0.048, 0, 3.142, 0], a=1.2, v=0.75)",
        "twofg_grip(40, 30, 2)",
        "#turn the right side clockwise",
        "movel(p[-0.351, -0.1, 0.050, 2.221, 2.221, 0], a=1.2, v=0.5)",
        "twofg_grip(80, 30, 2)",
        "movel(p[-0.351, -0.1, 0.15, 2.221, 2.221, 0], a=1.2, v=0.75)"
        ],
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
    "F":["#F",
        "#take from above",
        "movel(p[-0.35, -0.085, 0.15, 3.142, 0, 0], a=2, v=1)",
        "movel(p[-0.35, -0.085, 0.048, 3.142, 0, 0], a=1.2, v=0.75)",
        "twofg_grip(40, 30, 2)",
        "movel(p[-0.35, -0.085, 0.15, 3.142, 0, 0], a=1.2, v=0.75)",
        "#place the front side down",
        "movel(p[-0.35, -0.085, 0.15, 0, 3.142, 0], a=2, v=1)",
        "movel(p[-0.351, -0.083, 0.15, 0, 2.221, -2.221], a=2, v=1)",
        "movel(p[-0.351, -0.083, 0.052, 0, 2.221, -2.221], a=1.2, v=0.75)",
        "twofg_grip(80, 30, 2)",
        "movel(p[-0.351, -0.083, 0.15, 0, 2.221, -2.221], a=1.2, v=0.75)",
        "#move the clamp up",
        "movel(p[-0.351, -0.1, 0.15,  0, 3.142, 0], a=2, v=1)",
        "movel(p[-0.351, -0.1, 0.048, 0, 3.142, 0], a=1.2, v=0.75)",
        "twofg_grip(40, 30, 2)",
        "#turn the front side clockwise",
        "movel(p[-0.351, -0.1, 0.050, 2.221, 2.221, 0], a=1.2, v=0.5)",
        "twofg_grip(80, 30, 2)",
        "movel(p[-0.351, -0.1, 0.15, 2.221, 2.221, 0], a=1.2, v=0.75)"
        ],
    "B":["#B",
        "#take from above",
        "movel(p[-0.35, -0.12, 0.15, 0, 3.142, 0], a=2, v=1)",
        "movel(p[-0.35, -0.12, 0.048, 0, 3.142, 0], a=1.2, v=0.75)",
        "twofg_grip(40, 30, 2)",
        "movel(p[-0.35, -0.12, 0.15, 0, 3.142, 0], a=1.2, v=0.75)",
        "#place the back side down",
        "movel(p[-0.351, -0.083, 0.15, 0, 2.221, -2.221], a=2, v=1)",
        "movel(p[-0.351, -0.083, 0.052, 0, 2.221, -2.221], a=1.2, v=0.75)",
        "twofg_grip(80, 30, 2)",
        "movel(p[-0.351, -0.083, 0.15, 0, 2.221, -2.221], a=1.2, v=0.75)",
        "#move the clamp up",
        "movel(p[-0.351, -0.1, 0.15,  0, 3.142, 0], a=2, v=1)",
        "movel(p[-0.351, -0.1, 0.048, 0, 3.142, 0], a=1.2, v=0.75)",
        "twofg_grip(40, 30, 2)",
        "#turn the back side clockwise",
        "movel(p[-0.351, -0.1, 0.050, 2.221, 2.221, 0], a=1.2, v=0.5)",
        "twofg_grip(80, 30, 2)",
        "movel(p[-0.351, -0.1, 0.15, 2.221, 2.221, 0], a=1.2, v=0.75)"
        ],
    "U":["#U",
        "#take from above first time",
        "movel(p[-0.35, -0.12, 0.15, 0, 3.142, 0], a=2, v=1)",
        "movel(p[-0.35, -0.12, 0.048, 0, 3.142, 0], a=1.2, v=0.75)",
        "twofg_grip(40, 30, 2)",
        "movel(p[-0.35, -0.12, 0.15, 0, 3.142, 0], a=1.2, v=0.75)",
        "#place the back side down first",
        "movel(p[-0.351, -0.083, 0.15, 0, 2.221, -2.221], a=2, v=1)",
        "movel(p[-0.351, -0.083, 0.052, 0, 2.221, -2.221], a=1.2, v=0.75)",
        "twofg_grip(80, 30, 2)",
        "movel(p[-0.351, -0.083, 0.15, 0, 2.221, -2.221], a=1.2, v=0.75)",
        "#take from above second time",
        "movel(p[-0.35, -0.12, 0.15, 0, 3.142, 0], a=2, v=1)",
        "movel(p[-0.35, -0.12, 0.048, 0, 3.142, 0], a=1.2, v=0.75)",
        "twofg_grip(40, 30, 2)",
        "movel(p[-0.35, -0.12, 0.15, 0, 3.142, 0], a=1.2, v=0.75)",
        "#place the up side down",
        "movel(p[-0.351, -0.083, 0.15, 0, 2.221, -2.221], a=2, v=1)",
        "movel(p[-0.351, -0.083, 0.052, 0, 2.221, -2.221], a=1.2, v=0.75)",
        "twofg_grip(80, 30, 2)",
        "movel(p[-0.351, -0.083, 0.15, 0, 2.221, -2.221], a=1.2, v=0.75)",
        "#move the clamp up",
        "movel(p[-0.351, -0.1, 0.15,  0, 3.142, 0], a=2, v=1)",
        "movel(p[-0.351, -0.1, 0.048, 0, 3.142, 0], a=1.2, v=0.75)",
        "twofg_grip(40, 30, 2)",
        "#turn the up side clockwise",
        "movel(p[-0.351, -0.1, 0.050, 2.221, 2.221, 0], a=1.2, v=0.5)",
        "twofg_grip(80, 30, 2)",
        "movel(p[-0.351, -0.1, 0.15, 2.221, 2.221, 0], a=1.2, v=0.75)"
        ],
    "D":["#D",
        "#move the clamp up",
        "movel(p[-0.351, -0.1, 0.15,  0, 3.142, 0], a=2, v=1)",
        "movel(p[-0.351, -0.1, 0.048, 0, 3.142, 0], a=1.2, v=0.75)",
        "twofg_grip(40, 30, 2)",
        "#turn the down side clockwise",
        "movel(p[-0.351, -0.1, 0.050, 2.221, 2.221, 0], a=1.2, v=0.5)",
        "twofg_grip(80, 30, 2)",
        "movel(p[-0.351, -0.1, 0.15, 2.221, 2.221, 0], a=1.2, v=0.75)"
        ],
    "R'":["#R'",
        "#take from above",
        "movel(p[-0.37, -0.1, 0.15, 2.221, 2.221, 0], a=2, v=1)",
        "movel(p[-0.37, -0.1, 0.048, 2.221, 2.221, 0], a=1.2, v=0.75)",
        "twofg_grip(40, 30, 2)",
        "movel(p[-0.37, -0.1, 0.15, 2.221, 2.221, 0], a=1.2, v=0.75)",
        "#place the right side down",
        "movel(p[-0.351, -0.083, 0.15, 0, 2.221, -2.221], a=2, v=1)",
        "movel(p[-0.351, -0.083, 0.052, 0, 2.221, -2.221], a=1.2, v=0.75)",
        "twofg_grip(80, 30, 2)",
        "movel(p[-0.351, -0.083, 0.15, 0, 2.221, -2.221], a=1.2, v=0.75)",
        "#move the clamp up",
        "movel(p[-0.351, -0.1, 0.15,  0, 3.142, 0], a=2, v=1)",
        "movel(p[-0.351, -0.1, 0.048, 0, 3.142, 0], a=1.2, v=0.75)",
        "twofg_grip(40, 30, 2)",
        "#turn the right side counterclockwise",
        "movel(p[-0.351, -0.1, 0.050, 2.221, -2.221, 0], a=1.2, v=0.5)",
        "twofg_grip(80, 30, 2)",
        "movel(p[-0.351, -0.1, 0.15, 2.221, -2.221, 0], a=1.2, v=0.75)"
        ],
    "L'":["#L'",
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
        "#turn the left side counterclockwise",
        "movel(p[-0.351, -0.1, 0.050, 2.221, -2.221, 0], a=1.2, v=0.5)",
        "twofg_grip(80, 30, 2)",
        "movel(p[-0.351, -0.1, 0.15, 2.221, -2.221, 0], a=1.2, v=0.75)"
        ],
    "F'":["#F'",
        "#take from above",
        "movel(p[-0.35, -0.085, 0.15, 3.142, 0, 0], a=2, v=1)",
        "movel(p[-0.35, -0.085, 0.048, 3.142, 0, 0], a=1.2, v=0.75)",
        "twofg_grip(40, 30, 2)",
        "movel(p[-0.35, -0.085, 0.15, 3.142, 0, 0], a=1.2, v=0.75)",
        "#place the front side down",
        "movel(p[-0.35, -0.085, 0.15, 0, 3.142, 0], a=2, v=1)",
        "movel(p[-0.351, -0.083, 0.15, 0, 2.221, -2.221], a=2, v=1)",
        "movel(p[-0.351, -0.083, 0.052, 0, 2.221, -2.221], a=1.2, v=0.75)",
        "twofg_grip(80, 30, 2)",
        "movel(p[-0.351, -0.083, 0.15, 0, 2.221, -2.221], a=1.2, v=0.75)",
        "#move the clamp up",
        "movel(p[-0.351, -0.1, 0.15,  0, 3.142, 0], a=2, v=1)",
        "movel(p[-0.351, -0.1, 0.048, 0, 3.142, 0], a=1.2, v=0.75)",
        "twofg_grip(40, 30, 2)",
        "#turn the front side counterclockwise",
        "movel(p[-0.351, -0.1, 0.050, 2.221, -2.221, 0], a=1.2, v=0.5)",
        "twofg_grip(80, 30, 2)",
        "movel(p[-0.351, -0.1, 0.15, 2.221, -2.221, 0], a=1.2, v=0.75)"
        ],
    "B'":["#B'",
        "#take from above",
        "movel(p[-0.35, -0.12, 0.15, 0, 3.142, 0], a=2, v=1)",
        "movel(p[-0.35, -0.12, 0.048, 0, 3.142, 0], a=1.2, v=0.75)",
        "twofg_grip(40, 30, 2)",
        "movel(p[-0.35, -0.12, 0.15, 0, 3.142, 0], a=1.2, v=0.75)",
        "#place the back side down",
        "movel(p[-0.351, -0.083, 0.15, 0, 2.221, -2.221], a=2, v=1)",
        "movel(p[-0.351, -0.083, 0.052, 0, 2.221, -2.221], a=1.2, v=0.75)",
        "twofg_grip(80, 30, 2)",
        "movel(p[-0.351, -0.083, 0.15, 0, 2.221, -2.221], a=1.2, v=0.75)",
        "#move the clamp up",
        "movel(p[-0.351, -0.1, 0.15,  0, 3.142, 0], a=2, v=1)",
        "movel(p[-0.351, -0.1, 0.048, 0, 3.142, 0], a=1.2, v=0.75)",
        "twofg_grip(40, 30, 2)",
        "#turn the back side counterclockwise",
        "movel(p[-0.351, -0.1, 0.050, 2.221, -2.221, 0], a=1.2, v=0.5)",
        "twofg_grip(80, 30, 2)",
        "movel(p[-0.351, -0.1, 0.15, 2.221, -2.221, 0], a=1.2, v=0.75)"
        ],
    "U'":["#U'",
        "#take from above first time",
        "movel(p[-0.35, -0.12, 0.15, 0, 3.142, 0], a=2, v=1)",
        "movel(p[-0.35, -0.12, 0.048, 0, 3.142, 0], a=1.2, v=0.75)",
        "twofg_grip(40, 30, 2)",
        "movel(p[-0.35, -0.12, 0.15, 0, 3.142, 0], a=1.2, v=0.75)",
        "#place the back side down first",
        "movel(p[-0.351, -0.083, 0.15, 0, 2.221, -2.221], a=2, v=1)",
        "movel(p[-0.351, -0.083, 0.052, 0, 2.221, -2.221], a=1.2, v=0.75)",
        "twofg_grip(80, 30, 2)",
        "movel(p[-0.351, -0.083, 0.15, 0, 2.221, -2.221], a=1.2, v=0.75)",
        "#take from above second time",
        "movel(p[-0.35, -0.12, 0.15, 0, 3.142, 0], a=2, v=1)",
        "movel(p[-0.35, -0.12, 0.048, 0, 3.142, 0], a=1.2, v=0.75)",
        "twofg_grip(40, 30, 2)",
        "movel(p[-0.35, -0.12, 0.15, 0, 3.142, 0], a=1.2, v=0.75)",
        "#place the up side down",
        "movel(p[-0.351, -0.083, 0.15, 0, 2.221, -2.221], a=2, v=1)",
        "movel(p[-0.351, -0.083, 0.052, 0, 2.221, -2.221], a=1.2, v=0.75)",
        "twofg_grip(80, 30, 2)",
        "movel(p[-0.351, -0.083, 0.15, 0, 2.221, -2.221], a=1.2, v=0.75)",
        "#move the clamp up",
        "movel(p[-0.351, -0.1, 0.15,  0, 3.142, 0], a=2, v=1)",
        "movel(p[-0.351, -0.1, 0.048, 0, 3.142, 0], a=1.2, v=0.75)",
        "twofg_grip(40, 30, 2)",
        "#turn the up side counterclockwise",
        "movel(p[-0.351, -0.1, 0.050, 2.221, -2.221, 0], a=1.2, v=0.5)",
        "twofg_grip(80, 30, 2)",
        "movel(p[-0.351, -0.1, 0.15, 2.221, -2.221, 0], a=1.2, v=0.75)"
        ],
    "D'":["#D'",
        "#move the clamp up",
        "movel(p[-0.351, -0.1, 0.15,  0, 3.142, 0], a=2, v=1)",
        "movel(p[-0.351, -0.1, 0.048, 0, 3.142, 0], a=1.2, v=0.75)",
        "twofg_grip(40, 30, 2)",
        "#turn the down side counterclockwise",
        "movel(p[-0.351, -0.1, 0.050, 2.221, -2.221, 0], a=1.2, v=0.5)",
        "twofg_grip(80, 30, 2)",
        "movel(p[-0.351, -0.1, 0.15, 2.221, -2.221, 0], a=1.2, v=0.75)"
        ],
    "R2":["#R2",
        "#take from above",
        "movel(p[-0.37, -0.1, 0.15, 2.221, 2.221, 0], a=2, v=1)",
        "movel(p[-0.37, -0.1, 0.048, 2.221, 2.221, 0], a=1.2, v=0.75)",
        "twofg_grip(40, 30, 2)",
        "movel(p[-0.37, -0.1, 0.15, 2.221, 2.221, 0], a=1.2, v=0.75)",
        "#place the right side down",
        "movel(p[-0.351, -0.083, 0.15, 0, 2.221, -2.221], a=2, v=1)",
        "movel(p[-0.351, -0.083, 0.052, 0, 2.221, -2.221], a=1.2, v=0.75)",
        "twofg_grip(80, 30, 2)",
        "movel(p[-0.351, -0.083, 0.15, 0, 2.221, -2.221], a=1.2, v=0.75)",
        "#move the clamp up",
        "movel(p[-0.351, -0.1, 0.15,  0, 3.142, 0], a=2, v=1)",
        "movel(p[-0.351, -0.1, 0.048, 0, 3.142, 0], a=1.2, v=0.75)",
        "twofg_grip(40, 30, 2)",
        "#turn the right side clockwise twice",
        "movel(p[-0.351, -0.1, 0.050, 3.142, 0, 0], a=1.2, v=0.5)",
        "twofg_grip(80, 30, 2)",
        "movel(p[-0.351, -0.1, 0.15, 3.142, 0, 0], a=1.2, v=0.75)"
        ],
    "L2":["#L2",
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
        "#turn the left side clockwise twice",
        "movel(p[-0.351, -0.1, 0.050, 3.142, 0, 0], a=1.2, v=0.5)",
        "twofg_grip(80, 30, 2)",
        "movel(p[-0.351, -0.1, 0.15, 3.142, 0, 0], a=1.2, v=0.75)"
        ],
    "F2":["#F2",
        "#take from above",
        "movel(p[-0.35, -0.085, 0.15, 3.142, 0, 0], a=2, v=1)",
        "movel(p[-0.35, -0.085, 0.048, 3.142, 0, 0], a=1.2, v=0.75)",
        "twofg_grip(40, 30, 2)",
        "movel(p[-0.35, -0.085, 0.15, 3.142, 0, 0], a=1.2, v=0.75)",
        "#place the front side down",
        "movel(p[-0.35, -0.085, 0.15, 0, 3.142, 0], a=2, v=1)",
        "movel(p[-0.351, -0.083, 0.15, 0, 2.221, -2.221], a=2, v=1)",
        "movel(p[-0.351, -0.083, 0.052, 0, 2.221, -2.221], a=1.2, v=0.75)",
        "twofg_grip(80, 30, 2)",
        "movel(p[-0.351, -0.083, 0.15, 0, 2.221, -2.221], a=1.2, v=0.75)",
        "#move the clamp up",
        "movel(p[-0.351, -0.1, 0.15,  0, 3.142, 0], a=2, v=1)",
        "movel(p[-0.351, -0.1, 0.048, 0, 3.142, 0], a=1.2, v=0.75)",
        "twofg_grip(40, 30, 2)",
        "#turn the front side clockwise twice",
        "movel(p[-0.351, -0.1, 0.050, 3.142, 0, 0], a=1.2, v=0.5)",
        "twofg_grip(80, 30, 2)",
        "movel(p[-0.351, -0.1, 0.15, 3.142, 0, 0], a=1.2, v=0.75)"
        ],
    "B2":["#B2",
        "#take from above",
        "movel(p[-0.35, -0.12, 0.15, 0, 3.142, 0], a=2, v=1)",
        "movel(p[-0.35, -0.12, 0.048, 0, 3.142, 0], a=1.2, v=0.75)",
        "twofg_grip(40, 30, 2)",
        "movel(p[-0.35, -0.12, 0.15, 0, 3.142, 0], a=1.2, v=0.75)",
        "#place the back side down",
        "movel(p[-0.351, -0.083, 0.15, 0, 2.221, -2.221], a=2, v=1)",
        "movel(p[-0.351, -0.083, 0.052, 0, 2.221, -2.221], a=1.2, v=0.75)",
        "twofg_grip(80, 30, 2)",
        "movel(p[-0.351, -0.083, 0.15, 0, 2.221, -2.221], a=1.2, v=0.75)",
        "#move the clamp up",
        "movel(p[-0.351, -0.1, 0.15,  0, 3.142, 0], a=2, v=1)",
        "movel(p[-0.351, -0.1, 0.048, 0, 3.142, 0], a=1.2, v=0.75)",
        "twofg_grip(40, 30, 2)",
        "#turn the back side clockwise twice",
        "movel(p[-0.351, -0.1, 0.050, 3.142, 0, 0], a=1.2, v=0.5)",
        "twofg_grip(80, 30, 2)",
        "movel(p[-0.351, -0.1, 0.15, 3.142, 0, 0], a=1.2, v=0.75)"
        ],
    "U2":["#U2",
        "#take from above first time",
        "movel(p[-0.35, -0.12, 0.15, 0, 3.142, 0], a=2, v=1)",
        "movel(p[-0.35, -0.12, 0.048, 0, 3.142, 0], a=1.2, v=0.75)",
        "twofg_grip(40, 30, 2)",
        "movel(p[-0.35, -0.12, 0.15, 0, 3.142, 0], a=1.2, v=0.75)",
        "#place the back side down first",
        "movel(p[-0.351, -0.083, 0.15, 0, 2.221, -2.221], a=2, v=1)",
        "movel(p[-0.351, -0.083, 0.052, 0, 2.221, -2.221], a=1.2, v=0.75)",
        "twofg_grip(80, 30, 2)",
        "movel(p[-0.351, -0.083, 0.15, 0, 2.221, -2.221], a=1.2, v=0.75)",
        "#take from above second time",
        "movel(p[-0.35, -0.12, 0.15, 0, 3.142, 0], a=2, v=1)",
        "movel(p[-0.35, -0.12, 0.048, 0, 3.142, 0], a=1.2, v=0.75)",
        "twofg_grip(40, 30, 2)",
        "movel(p[-0.35, -0.12, 0.15, 0, 3.142, 0], a=1.2, v=0.75)",
        "#place the up side down",
        "movel(p[-0.351, -0.083, 0.15, 0, 2.221, -2.221], a=2, v=1)",
        "movel(p[-0.351, -0.083, 0.052, 0, 2.221, -2.221], a=1.2, v=0.75)",
        "twofg_grip(80, 30, 2)",
        "movel(p[-0.351, -0.083, 0.15, 0, 2.221, -2.221], a=1.2, v=0.75)",
        "#move the clamp up",
        "movel(p[-0.351, -0.1, 0.15,  0, 3.142, 0], a=2, v=1)",
        "movel(p[-0.351, -0.1, 0.048, 0, 3.142, 0], a=1.2, v=0.75)",
        "twofg_grip(40, 30, 2)",
        "#turn the up side clockwise twice",
        "movel(p[-0.351, -0.1, 0.050, 3.142, 0, 0], a=1.2, v=0.5)",
        "twofg_grip(80, 30, 2)",
        "movel(p[-0.351, -0.1, 0.15, 3.142, 0, 0], a=1.2, v=0.75)"
        ],
    "D2":["#D2",
        "#move the clamp up",
        "movel(p[-0.351, -0.1, 0.15,  0, 3.142, 0], a=2, v=1)",
        "movel(p[-0.351, -0.1, 0.048, 0, 3.142, 0], a=1.2, v=0.75)",
        "twofg_grip(40, 30, 2)",
        "#turn the down side clockwise twice",
        "movel(p[-0.351, -0.1, 0.050, 3.142, 0, 0], a=1.2, v=0.5)",
        "twofg_grip(80, 30, 2)",
        "movel(p[-0.351, -0.1, 0.15, 3.142, 0, 0], a=1.2, v=0.75)"
        ],
    "RI" : ["#RI",
        "#move the clamp up",
        "movel(p[-0.351, -0.1, 0.15,  0, 3.142, 0], a=2, v=1)",
        "movel(p[-0.351, -0.1, 0.048, 0, 3.142, 0], a=1.2, v=0.75)",
        "twofg_grip(40, 30, 2)",
        "movel(p[-0.351, -0.1, 0.15,  0, 3.142, 0], a=2, v=1)",
        "#turn the down side clockwise",
        "movel(p[-0.351, -0.1, 0.15, 2.221, 2.221, 0], a=1.2, v=0.75)",
        "movel(p[-0.351, -0.1, 0.050, 2.221, 2.221, 0], a=1.2, v=0.5)",
        "twofg_grip(80, 30, 2)",
        "movel(p[-0.351, -0.1, 0.15, 2.221, 2.221, 0], a=1.2, v=0.75)"
        ],
    "LI" : ["#LI",
        "#move the clamp up",
        "movel(p[-0.351, -0.1, 0.15,  0, 3.142, 0], a=2, v=1)",
        "movel(p[-0.351, -0.1, 0.048, 0, 3.142, 0], a=1.2, v=0.75)",
        "twofg_grip(40, 30, 2)",
        "movel(p[-0.351, -0.1, 0.15,  0, 3.142, 0], a=2, v=1)",
        "#turn the cube counterclockwise",
        "movel(p[-0.351, -0.1, 0.15, 2.221, -2.221, 0], a=1.2, v=0.5)",
        "movel(p[-0.351, -0.1, 0.050, 2.221, -2.221, 0], a=1.2, v=0.5)",
        "twofg_grip(80, 30, 2)",
        "movel(p[-0.351, -0.1, 0.15, 2.221, -2.221, 0], a=1.2, v=0.75)"
        ],
    "BI" : ["#BI",
        "#move the clamp up",
        "movel(p[-0.351, -0.1, 0.15,  0, 3.142, 0], a=2, v=1)",
        "movel(p[-0.351, -0.1, 0.048, 0, 3.142, 0], a=1.2, v=0.75)",
        "twofg_grip(40, 30, 2)",
        "movel(p[-0.351, -0.1, 0.15,  0, 3.142, 0], a=2, v=1)",
        "#turn the cube clockwise twice",
        "movel(p[-0.351, -0.1, 0.15, 3.142, 0, 0], a=1.2, v=0.75)",
        "movel(p[-0.351, -0.1, 0.050, 3.142, 0, 0], a=1.2, v=0.5)",
        "twofg_grip(80, 30, 2)",
        "movel(p[-0.351, -0.1, 0.15, 3.142, 0, 0], a=1.2, v=0.75)"
        ],
    "END" : ["#END",
        "movel(p[-0.351, -0.1, 0.15,  0, 3.142, 0], a=2, v=1)",
        "movel(p[-0.351, -0.1, 0.048, 0, 3.142, 0], a=1.2, v=0.75)",
        "twofg_grip(40, 30, 2)",
        "movel(p[-0.351, -0.1, 0.15,  0, 3.142, 0], a=2, v=1)"
        ]
    }

possible_movement = {
    # simple rotations (90° clockwise)
    "ROTATE_RIGHT_FACE" : "R",
    "ROTATE_LEFT_FACE"  : "L",
    "ROTATE_UP_FACE"    : "U",
    "ROTATE_DOWN_FACE"  : "D",
    "ROTATE_FRONT_FACE" : "F",
    "ROTATE_BACK_FACE"  : "B",
    
    # counter rotations (90° counterclockwise)
    "ROTATE_RIGHT_FACE_OPPOSITE" : "R'",
    "ROTATE_LEFT_FACE_OPPOSITE"  : "L'",
    "ROTATE_UP_FACE_OPPOSITE"    : "U'",
    "ROTATE_DOWN_FACE_OPPOSITE"  : "D'",
    "ROTATE_FRONT_FACE_OPPOSITE" : "F'",
    "ROTATE_BACK_FACE_OPPOSITE"  : "B'",
    
    # double rotations (180° clockwise)
    "ROTATE_RIGHT_FACE_DOUBLE" : "R2",
    "ROTATE_LEFT_FACE_DOUBLE"  : "L2",
    "ROTATE_UP_FACE_DOUBLE"    : "U2",
    "ROTATE_DOWN_FACE_DOUBLE"  : "D2",
    "ROTATE_FRONT_FACE_DOUBLE" : "F2",
    "ROTATE_BACK_FACE_DOUBLE"  : "B2",
    
    # initiate movement (turn the green face front at the end)
    "INITIATE_RIGHT_FACE" : "RI",
    "INITIATE_LEFT_FACE"  : "LI",
    "INITIATE_BACK_FACE"  : "BI",
    
    "ENDING" : "END"
    }


# ---------------- Memory -----------------


cube_memory = {
    "U": "UP",    # Face Up is on the top initially 
    "D": "DOWN",  # Face Down is on the bottom initially 
    "F": "FRONT", # Face Front is forward initially 
    "B": "BACK",  # Face Back is bacward initially 
    "L": "LEFT",  # Face Left is facing the left initially 
    "R": "RIGHT"  # Face Right is facing the right initially 
}

def rotation_L():
    """
    All the rotation function are parts of the memory for the robot. 
    rotation_X modify the dictionary 'cube_memory' by applying an X rotation.

    """
    global cube_memory
    
    # We save how the cube is actually looking befor modifying it 
    previous = cube_memory.copy()
    
    cube_memory["L"] = previous["D"] # The previous down is now at the left
    cube_memory["R"] = previous["U"] # The previous up is now at the right
    cube_memory["B"] = previous["F"] # The previous front is now at the back 
    cube_memory["F"] = previous["B"] # The previous back is now at the front
    cube_memory["U"] = previous["R"] # The previous right is now up
    cube_memory["D"] = previous["L"] # The previous left is now down
    return

def rotation_R():
    """
    type 'help(rotation_L)' for more details
    """
    
    global cube_memory
    
    # We save how the cube is actually looking befor modifying it 
    previous = cube_memory.copy()
    
    cube_memory["L"] = previous["D"]
    cube_memory["R"] = previous["U"]
    cube_memory["D"] = previous["R"]
    cube_memory["U"] = previous["L"]
    cube_memory["B"] = previous["B"]
    cube_memory["F"] = previous["F"]
    return

def rotation_U():
    """
    type 'help(rotation_L)' for more details
    """
    
    global cube_memory
    
    # We save how the cube is actually looking befor modifying it 
    previous = cube_memory.copy()
    
    cube_memory["U"] = previous["D"]
    cube_memory["D"] = previous["U"]
    cube_memory["R"] = previous["F"]
    cube_memory["L"] = previous["B"]
    cube_memory["F"] = previous["R"]
    cube_memory["B"] = previous["L"]
    return

def rotation_D():
    """
    type 'help(rotation_L)' for more details
    """
    
    global cube_memory
    
    # We save how the cube is actually looking befor modifying it 
    previous = cube_memory.copy()
    
    cube_memory["L"] = previous["F"]
    cube_memory["R"] = previous["B"]
    cube_memory["F"] = previous["R"]
    cube_memory["B"] = previous["L"]
    cube_memory["U"] = previous["U"]
    cube_memory["D"] = previous["D"]
    return

def rotation_F():
    """
    type 'help(rotation_L)' for more details
    """
    
    global cube_memory
    
    # We save how the cube is actually looking befor modifying it 
    previous = cube_memory.copy()
    
    cube_memory["L"] = previous["D"]
    cube_memory["R"] = previous["U"]
    cube_memory["D"] = previous["F"]
    cube_memory["U"] = previous["B"]
    cube_memory["B"] = previous["R"]
    cube_memory["F"] = previous["L"]
    return

def rotation_B():
    """
    type 'help(rotation_L)' for more details
    """
    
    global cube_memory
    
    # We save how the cube is actually looking befor modifying it 
    previous = cube_memory.copy()
    
    cube_memory["L"] = previous["D"]
    cube_memory["R"] = previous["U"]
    cube_memory["U"] = previous["F"]
    cube_memory["D"] = previous["B"]
    cube_memory["F"] = previous["R"]
    cube_memory["B"] = previous["L"]
    return

def rotation_Li():
    """
    type 'help(rotation_L)' for more details
    """
    
    global cube_memory
    
    # We save how the cube is actually looking befor modifying it 
    previous = cube_memory.copy()
    
    cube_memory["R"] = previous["D"]
    cube_memory["L"] = previous["U"]
    cube_memory["U"] = previous["R"]
    cube_memory["D"] = previous["L"]
    cube_memory["F"] = previous["F"]
    cube_memory["B"] = previous["B"]
    return

def rotation_Ri():
    """
    type 'help(rotation_L)' for more details
    """
    
    global cube_memory
    
    # We save how the cube is actually looking befor modifying it 
    previous = cube_memory.copy()
    
    cube_memory["R"] = previous["D"]
    cube_memory["L"] = previous["U"]
    cube_memory["B"] = previous["F"]
    cube_memory["F"] = previous["B"]
    cube_memory["D"] = previous["R"]
    cube_memory["U"] = previous["L"]
    return

def rotation_Ui():
    """
    type 'help(rotation_L)' for more details
    """
    
    global cube_memory
    
    # We save how the cube is actually looking befor modifying it 
    previous = cube_memory.copy()
    
    cube_memory["U"] = previous["D"]
    cube_memory["D"] = previous["U"]
    cube_memory["L"] = previous["F"]
    cube_memory["R"] = previous["B"]
    cube_memory["B"] = previous["R"]
    cube_memory["F"] = previous["L"]
    return

def rotation_Di():
    """
    type 'help(rotation_L)' for more details
    """
    
    global cube_memory
    
    # We save how the cube is actually looking befor modifying it 
    previous = cube_memory.copy()
    
    cube_memory["R"] = previous["F"]
    cube_memory["L"] = previous["B"]
    cube_memory["B"] = previous["R"]
    cube_memory["F"] = previous["L"]
    cube_memory["U"] = previous["U"]
    cube_memory["D"] = previous["D"]
    return

def rotation_Fi():
    """
    type 'help(rotation_L)' for more details
    """
    
    global cube_memory
    
    # We save how the cube is actually looking befor modifying it 
    previous = cube_memory.copy()
    
    cube_memory["R"] = previous["D"]
    cube_memory["L"] = previous["U"]
    cube_memory["D"] = previous["F"]
    cube_memory["U"] = previous["B"]
    cube_memory["F"] = previous["R"]
    cube_memory["B"] = previous["L"]
    return

def rotation_Bi():
    """
    type 'help(rotation_L)' for more details
    """
    
    global cube_memory
    
    # We save how the cube is actually looking befor modifying it 
    previous = cube_memory.copy()
    
    cube_memory["R"] = previous["D"]
    cube_memory["L"] = previous["U"]
    cube_memory["U"] = previous["F"]
    cube_memory["D"] = previous["B"]
    cube_memory["B"] = previous["R"]
    cube_memory["F"] = previous["L"]
    return

def rotation_L2():
    """
    type 'help(rotation_L)' for more details
    """
    
    global cube_memory
    
    # We save how the cube is actually looking befor modifying it 
    previous = cube_memory.copy()
    
    cube_memory["B"] = previous["D"]
    cube_memory["F"] = previous["U"]
    cube_memory["R"] = previous["F"]
    cube_memory["L"] = previous["B"]
    cube_memory["U"] = previous["R"]
    cube_memory["D"] = previous["L"]
    return

def rotation_R2():
    """
    type 'help(rotation_L)' for more details
    """
    
    global cube_memory
    
    # We save how the cube is actually looking befor modifying it 
    previous = cube_memory.copy()
    
    cube_memory["B"] = previous["D"]
    cube_memory["F"] = previous["U"]
    cube_memory["L"] = previous["F"]
    cube_memory["R"] = previous["B"]
    cube_memory["D"] = previous["R"]
    cube_memory["U"] = previous["L"]
    return

def rotation_U2():
    """
    type 'help(rotation_L)' for more details
    """
    
    global cube_memory
    
    # We save how the cube is actually looking befor modifying it 
    previous = cube_memory.copy()
    
    cube_memory["U"] = previous["D"]
    cube_memory["D"] = previous["U"]
    cube_memory["L"] = previous["R"]
    cube_memory["R"] = previous["L"]
    cube_memory["F"] = previous["F"]
    cube_memory["B"] = previous["B"]
    return

def rotation_D2():
    """
    type 'help(rotation_L)' for more details
    """
    
    global cube_memory
    
    # We save how the cube is actually looking befor modifying it 
    previous = cube_memory.copy()
    
    cube_memory["B"] = previous["F"]
    cube_memory["F"] = previous["B"]
    cube_memory["L"] = previous["R"]
    cube_memory["R"] = previous["L"]
    cube_memory["U"] = previous["U"]
    cube_memory["D"] = previous["D"]
    return

def rotation_F2():
    """
    type 'help(rotation_L)' for more details
    """
    
    global cube_memory
    
    # We save how the cube is actually looking befor modifying it 
    previous = cube_memory.copy()
    
    cube_memory["B"] = previous["D"]
    cube_memory["F"] = previous["U"]
    cube_memory["D"] = previous["F"]
    cube_memory["U"] = previous["B"]
    cube_memory["L"] = previous["L"]
    cube_memory["R"] = previous["R"]
    return

def rotation_B2():
    """
    type 'help(rotation_L)' for more details
    """
    
    global cube_memory
    
    # We save how the cube is actually looking befor modifying it 
    previous = cube_memory.copy()
    
    cube_memory["B"] = previous["D"]
    cube_memory["F"] = previous["U"]
    cube_memory["U"] = previous["F"]
    cube_memory["D"] = previous["B"]
    cube_memory["L"] = previous["R"]
    cube_memory["R"] = previous["L"]
    return

def rotation_RD():
    """
    This rotation is use at the end to rotate the cube with the yellow side 
    down if it is initialy at the right.
    """
    
    global cube_memory
    
    # We save how the cube is actually looking befor modifying it 
    previous = cube_memory.copy()
    
    cube_memory["U"] = previous["D"]
    cube_memory["B"] = previous["U"]
    cube_memory["R"] = previous["F"]
    cube_memory["L"] = previous["B"]
    cube_memory["D"] = previous["R"]
    cube_memory["U"] = previous["L"]
    return

def rotation_LD():
    """
    This rotation is use at the end to rotate the cube with the yellow side 
    down if it is initialy at the left.
    """
    
    global cube_memory
    
    # We save how the cube is actually looking befor modifying it 
    previous = cube_memory.copy()
    
    cube_memory["F"] = previous["D"]
    cube_memory["B"] = previous["U"]
    cube_memory["L"] = previous["F"]
    cube_memory["R"] = previous["B"]
    cube_memory["U"] = previous["R"]
    cube_memory["D"] = previous["L"]
    return

def rotation_FD():
    """
    This rotation is use at the end to rotate the cube with the yellow side 
    down if it is initialy at the front.
    """
    
    global cube_memory
    
    # We save how the cube is actually looking befor modifying it 
    previous = cube_memory.copy()
    
    cube_memory["F"] = previous["D"]
    cube_memory["B"] = previous["U"]
    cube_memory["D"] = previous["F"]
    cube_memory["U"] = previous["B"]
    cube_memory["L"] = previous["R"]
    cube_memory["R"] = previous["L"]
    return

def rotation_BD():
    """
    This rotation is use at the end to rotate the cube with the yellow side 
    down if it is initialy at the back.
    """
    
    global cube_memory
    
    # We save how the cube is actually looking befor modifying it 
    previous = cube_memory.copy()
    
    cube_memory["F"] = previous["D"]
    cube_memory["B"] = previous["U"]
    cube_memory["U"] = previous["F"]
    cube_memory["D"] = previous["B"]
    cube_memory["R"] = previous["R"]
    cube_memory["L"] = previous["L"]
    return

def rotation_UD():
    """
    This rotation is use at the end to rotate the cube with the yellow side 
    down if it is initialy at the top.
    """
    
    global cube_memory
    
    # We save how the cube is actually looking befor modifying it 
    previous = cube_memory.copy()
    
    cube_memory["U"] = previous["D"]
    cube_memory["D"] = previous["U"]
    cube_memory["B"] = previous["F"]
    cube_memory["F"] = previous["B"]
    cube_memory["R"] = previous["R"]
    cube_memory["L"] = previous["L"]
    return

rotations = {
    "L": rotation_L,
    "U": rotation_U,
    "D": rotation_D,
    "F": rotation_F,
    "B": rotation_B,
    "R": rotation_R,
    "U'": rotation_Ui,
    "D'": rotation_Di,
    "F'": rotation_Fi,
    "B'": rotation_Bi,
    "L'": rotation_Li,
    "R'": rotation_Ri,
    "U2": rotation_U2,
    "D2": rotation_D2,
    "F2": rotation_F2,
    "B2": rotation_B2,
    "L2": rotation_L2,
    "R2": rotation_R2,
    "UD": rotation_UD,
    "FD": rotation_FD,
    "BD": rotation_BD,
    "LD": rotation_LD,
    "RD": rotation_RD 
}


def memorisation(initial_solution = list):
    """
    This function purpose is to change the solution to implement a memory for the robot 
    because of the fact that the robot will change the orientation of it, so the faces will 
    change during the resolution of the cube.
    """
    sol = []
    for asked_movement in initial_solution:
        # 1. Analyser le mouvement demandé
        logical_face = asked_movement[0]           
        is_opposite = "'" in asked_movement        
        is_double = "2" in asked_movement         
        
        # 2. Trouver la position physique
        dict_miror = {objects: keys for keys, objects in cube_memory.items()}        
        real_face = dict_miror[traduction_movement[logical_face]]
        
        variation = ""
        if is_double:
            variation = "2"
        elif is_opposite:
            variation = "'"
        
        fonction_to_call = rotations[real_face+variation]
        fonction_to_call()
        sol.append(real_face+variation)
        
    return sol


# ------Function of resolution ------------


def conversion(scrambled_pattern = dict):
    """
    This function is to convert a scrambled cub as dictionnary in a string by looking at 
    the faces in a certain order (U, R, F, D, L and B) so that the Kociemba function can understand it.
    It also translates the color to a position, W == U, Y == D, ...
    """
    cube = ""
    order = ['U', 'R', 'F', 'D', 'L', 'B']
    for i in range(6):
        face = order[i]
        for color in scrambled_pattern[face]:
            cube += traduction_kociemba[color]
    return cube


def correction(solution):
    """
    This function is used to "correct" the poposed solution the kociemba function is giving us. 
    Kociemba gives us a string and this function transforms it into a liste where each slot is a movement.
    """
    L = list(solution)
    liste = []
    n = len(L)
    i = 0
    while i < n:
        if i==n-1:
            liste.append(L[i])
            i+=1
        elif L[i+1].isdigit() : 
            liste.append(L[i]+"2")
            i+=3
        elif L[i+1] == "'":
            liste.append(L[i]+"'")
            i+=3
        elif L[i+1] == " ":
            liste.append(L[i])
            i+=2
    return liste 


# ------------ Part to fill ------------


scrambled_cube = {
                'U': ['G', 'B', 'O', 'W', 'W', 'O', 'O', 'B', 'W'], 
                'D': ['Y', 'G', 'R', 'B', 'Y', 'R', 'G', 'Y', 'B'], 
                'F': ['G', 'O', 'R', 'W', 'G', 'O', 'B', 'Y', 'G'], 
                'L': ['R', 'B', 'Y', 'O', 'O', 'R', 'W', 'Y', 'R'], 
                'B': ['B', 'R', 'Y', 'G', 'B', 'G', 'Y', 'R', 'O'], 
                'R': ['B', 'Y', 'W', 'W', 'R', 'W', 'W', 'G', 'O']
                }


# ------------ display of the cube ------------


def dessiner_patron_graphique(cube):
    # 1. On associe tes lettres aux couleurs de matplotlib
    # (J'utilise 'whitesmoke' au lieu de 'white' pour bien voir les bords sur fond blanc)
    dico_couleurs = {
        'R': 'red', 
        'G': 'green', 
        'B': 'blue', 
        'W': 'whitesmoke', 
        'Y': 'yellow', 
        'O': 'orange'
    }

    # 2. On prépare la zone de dessin
    fig, ax = plt.subplots(figsize=(10, 7))
    ax.set_aspect('equal') # Force les carrés à rester parfaitement carrés
    ax.axis('off')         # Cache les axes X et Y du graphique

    # 3. Fonction interne pour dessiner une face (3x3 carrés) à une coordonnée précise
    def dessiner_face(nom_face, start_x, start_y):
        face = cube[nom_face]
        for i in range(9):
            col = i % 3
            ligne = i // 3
            couleur_lettre = face[i]
            
            # Calcul de la position (on inverse la ligne pour dessiner de haut en bas)
            x = start_x + col
            y = start_y + (2 - ligne)
            
            # Création du petit carré
            carre = patches.Rectangle(
                (x, y), 1, 1, 
                facecolor=dico_couleurs.get(couleur_lettre, 'gray'), 
                edgecolor='black', 
                linewidth=2
            )
            ax.add_patch(carre)

    # 4. On place chaque face sur la grille (comme un patron en croix)
    dessiner_face('U', 3, 6)  # Haut (au milieu en haut)
    dessiner_face('L', 0, 3)  # Gauche
    dessiner_face('F', 3, 3)  # Avant (au centre)
    dessiner_face('R', 6, 3)  # Droite
    dessiner_face('B', 9, 3)  # Arrière (tout à droite)
    dessiner_face('D', 3, 0)  # Bas (au milieu en bas)

    # 5. On ajuste la taille globale et on affiche
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 9)
    plt.tight_layout()
    plt.show()

dessiner_patron_graphique(scrambled_cube)

# ----------- Resolution of the cube -------------


# This ligne serve the purpose of converting the scrambled_cube dictionnary in a way 
# that the kociemba function understand it 
my_cube = conversion(scrambled_cube)

# We solve the cube using the kociemba.solve function and correct it in a way the program understand it
calculated_solution = correction(kociemba.solve(my_cube))
#calculated_solution = ["L", "B", "U'"] # Test line

print(calculated_solution)

# We modify the solution to integrate the memory of the robot 
#robot_solution = memorisation(calculated_solution)
robot_solution = ["R"] # Test line

print(robot_solution)
    
# ------------- Writing to the file -------------


"""
Don't forget to choose the right file where you want this code 
to write the programm for the cube.

For this you can either save this code in the file you want the programme to be 
or modify the 'open()' section bellow.
"""

with open("programme_rubiks.script", "w") as fichier:
    fichier.write("def resoudre_cube():\n")
    
    for asked_movement in robot_solution:
        
        # 1. Analyse the asked movement 
        face = asked_movement[0]           
        is_opposite = "'" in asked_movement        
        is_double = "2" in asked_movement         
        
        physical_position = traduction_movement[face]
        
        # 2. Determine the right suffix
        suffix = ""
        if is_double:
            suffix = "_DOUBLE"
        elif is_opposite:
            suffix = "_OPPOSITE"
            
        # 3. Reconstruct the macro name
        macro_name = f"ROTATE_{physical_position}_FACE{suffix}"
        instructions = details_movement[possible_movement[macro_name]]
        
        # 4. writing in the file choose before
        fichier.write(f"    # --- Cube Movement : {asked_movement} ---\n")
        for ligne in instructions:
            fichier.write(f"    {ligne}\n")
    

    
    # The following lines are replacing the cube in the initial position
    
    invert_dict = {objects: keys for keys, objects in cube_memory.items()}
    position = invert_dict['DOWN']
    if position != 'D' :
        face = traduction_movement[position]
        macro_name = f"ROTATE_{face}_FACE"
        instructions = details_movement[possible_movement[macro_name]]
        
        fichier.write("    # --- Returning to initial position ---\n")
        for ligne in instructions:
            if ligne == "#move the clamp up" :
                break
            else : 
                fichier.write(f"    {ligne}\n")
                
        fonction_to_call = rotations[position+'D']
        fonction_to_call()
        
    invert_dict = {objects: keys for keys, objects in cube_memory.items()}
    position = invert_dict['FRONT']
    
    if position != 'F' :
        face = traduction_movement[position]
        macro_name = f"INITIATE_{face}_FACE"
        instructions = details_movement[possible_movement[macro_name]]
        
        for ligne in instructions:
            fichier.write(f"    {ligne}\n")
                
        fonction_to_call = rotations[position]
        fonction_to_call()
    
    # The next lignes are to give the cube to the operator and end the program
    
    instructions = details_movement[possible_movement["ENDING"]]
    for ligne in instructions:
        fichier.write(f"    {ligne}\n")
        
    fichier.write('    popup("You can now pick the cube up.", title="End of the program", blocking=True)\n')
    fichier.write('    twofg_grip(80, 30, 2)\n\n')    


    fichier.write("end\n")
    fichier.write("resoudre_cube()\n")

