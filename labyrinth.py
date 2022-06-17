import random
from tkinter import Y

def title():
    print("\
 | |           | |                 (_)       | |  | |    \n\
 | |      __ _ | |__   _   _  _ __  _  _ __  | |_ | |__  \n\
 | |     / _` || '_ \ | | | || '__|| || '_ \ | __|| '_ \ \n\
 | |____| (_| || |_) || |_| || |   | || | | || |_ | | | |\n\
 |______|\__,_||_.__/  \__, ||_|   |_||_| |_| \__||_| |_|\n\
                        __/ |                            \n\
                       |___/                             \n")

def options():
    print("         <--       ^       -->\n          1        2       3")
    pick = str(input("Which Way?: "))
    return pick

def left_right():
    current = True
    while current == True:
        print("\
|||||||[___][____][____][____][__|||||||\n\
|||||||_][____][____][____][____]|||||||\n\
|||||||[___][____][____][____][__|||||||\n\
|||||||_][____][____][____][____]|||||||\n\
|||||||[___][____][____][____][__|||||||\n\
|||||||_][____][____][____][____]|||||||\n\
|||||||[___][____][____][____][__|||||||\n\
|||||||_][____][____][____][____]|||||||\n\
|||||||                          |||||||\n\
|||||||                          |||||||\n\
|||||||                          |||||||\n\
|||||||                          |||||||\n\
|||||||                          |||||||\n\
||||||/                          \||||||\n\
|||||/                            \|||||\n\
||||/                              \||||\n\
|||/                                \|||\n\
||/                                  \||\n\
|/                                    \|\n\
/                                      \ ")
        pick = options()
        if pick == '1':
            current = False
            skip()
            return '1'
        elif pick == '3':
            current = False
            skip()
            return '3'
        else:
            skip()
            print(pick+" Is An Invalid Direction")

def dead_end():
    print("\
|||||||[___][____][____][____][__|||||||\n\
|||||||_][____][____][____][____]|||||||\n\
|||||||[___][____][____][____][__|||||||\n\
|||||||_][____][____][____][____]|||||||\n\
|||||||[___][____][____][____][__|||||||\n\
|||||||_][____][____][____][____]|||||||\n\
|||||||[___][____][____][____][__|||||||\n\
|||||||_][____][____][____][____]|||||||\n\
|||||||[___][____][____][____][__|||||||\n\
|||||||_][____][____][____][____]|||||||\n\
|||||||[___][____][____][____][__|||||||\n\
|||||||_][____][____][____][____]|||||||\n\
|||||||[___][____][____][____][__|||||||\n\
||||||/                          \||||||\n\
|||||/                            \|||||\n\
||||/                              \||||\n\
|||/                                \|||\n\
||/                                  \||\n\
|/                                    \|\n\
/                                      \ ")
    pick = options()
    skip()
    print(pick+" Is An Invalid Direction")
    skip()

def straight_right():
    current = True
    while current == True:
        print("\
|||||||||||||||||\   /|||||[_][__|||||||\n\
||||||||||||||||||   ||||||[____]|||||||\n\
|||||||||||||||||/   \|||||[_][__|||||||\n\
||||||||||||||||/     \||||[____]|||||||\n\
|||||||||||||||/       \|||[_][__|||||||\n\
||||||||||||||/         \||[____]|||||||\n\
|||||||||||||/           \|[_][__|||||||\n\
||||||||||||/             \[____]|||||||\n\
|||||||||||/                     |||||||\n\
||||||||||/                      |||||||\n\
|||||||||/                       |||||||\n\
||||||||/                        |||||||\n\
|||||||/                         |||||||\n\
||||||/                          \||||||\n\
|||||/                            \|||||\n\
||||/                              \||||\n\
|||/                                \|||\n\
||/                                  \||\n\
|/                                    \|\n\
/                                      \ ")
        pick = options()
        if pick == '2':
            current = False
            skip()
            return '2'
        elif pick == '3':
            current = False
            skip()
            return '3'
        else:
            skip()
            print(pick+" Is An Invalid Direction")

def straight_left():
    current = True
    while current == True:
        print("\
|||||||__][_]|||||\   /|||||||||||||||||\n\
|||||||[____]||||||   ||||||||||||||||||\n\
|||||||__][_]|||||/   \|||||||||||||||||\n\
|||||||[____]||||/     \||||||||||||||||\n\
|||||||__][_]|||/       \|||||||||||||||\n\
|||||||[____]||/         \||||||||||||||\n\
|||||||__][_]|/           \|||||||||||||\n\
|||||||[____]/             \||||||||||||\n\
|||||||                     \|||||||||||\n\
|||||||                      \||||||||||\n\
|||||||                       \|||||||||\n\
|||||||                        \||||||||\n\
|||||||                         \|||||||\n\
||||||/                          \||||||\n\
|||||/                            \|||||\n\
||||/                              \||||\n\
|||/                                \|||\n\
||/                                  \||\n\
|/                                    \|\n\
/                                      \ ")
        pick = options()
        if pick == '1':
            current = False
            skip()
            return '1'
        elif pick == '2':
            current = False
            skip()
            return '2'
        else:
            skip()
            print(pick+" Is An Invalid Direction")

def straight_left_right():
    current = True
    while current == True:
        print("\
|||||||__][_]|||||\   /|||||[_][__|||||||\n\
|||||||[____]||||||   ||||||[____]|||||||\n\
|||||||__][_]|||||/   \|||||[_][__|||||||\n\
|||||||[____]||||/     \||||[____]|||||||\n\
|||||||__][_]|||/       \|||[_][__|||||||\n\
|||||||[____]||/         \||[____]|||||||\n\
|||||||__][_]|/           \|[_][__|||||||\n\
|||||||[____]/             \[____]|||||||\n\
|||||||                           |||||||\n\
|||||||                           |||||||\n\
|||||||                           |||||||\n\
|||||||                           |||||||\n\
|||||||                           |||||||\n\
||||||/                           \||||||\n\
|||||/                             \|||||\n\
||||/                               \||||\n\
|||/                                 \|||\n\
||/                                   \||\n\
|/                                     \|\n\
/                                       \ ")
        pick = options()
        if pick == '1':
            current = False
            skip()
            return '1'
        elif pick == '2':
            current = False
            skip()
            return '2'
        elif pick == '3':
            current = False
            skip()
            return '3'
        else:
            skip()
            print(pick+" Is An Invalid Direction")

def straight():
    current = True
    while current == True:
        print("\
|||||||||||||||||\    /|||||||||||||||||\n\
||||||||||||||||||    ||||||||||||||||||\n\
|||||||||||||||||/    \|||||||||||||||||\n\
||||||||||||||||/      \||||||||||||||||\n\
|||||||||||||||/        \|||||||||||||||\n\
||||||||||||||/          \||||||||||||||\n\
|||||||||||||/            \|||||||||||||\n\
||||||||||||/              \||||||||||||\n\
|||||||||||/                \|||||||||||\n\
||||||||||/                  \||||||||||\n\
|||||||||/                    \|||||||||\n\
||||||||/                      \||||||||\n\
|||||||/                        \|||||||\n\
||||||/                          \||||||\n\
|||||/                            \|||||\n\
||||/                              \||||\n\
|||/                                \|||\n\
||/                                  \||\n\
|/                                    \|\n\
/                                      \ ")
        pick = options()
        if pick == '2':
            current = False
            skip()
        else:
            skip()
            print(pick+" Is An Invalid Direction")

def left():
    current = True
    while current == True:
        print("\
|||||||[___][____][____][__|||||||||||||\n\
|||||||_][____][____][____]|||||||||||||\n\
|||||||[___][____][____][__|||||||||||||\n\
|||||||_][____][____][____]|||||||||||||\n\
|||||||[___][____][____][__|||||||||||||\n\
|||||||_][____][____][____]|||||||||||||\n\
|||||||[___][____][____][__|||||||||||||\n\
|||||||_][____][____][____]|||||||||||||\n\
|||||||                     \|||||||||||\n\
|||||||                      \||||||||||\n\
|||||||                       \|||||||||\n\
|||||||                        \||||||||\n\
|||||||                         \|||||||\n\
||||||/                          \||||||\n\
|||||/                            \|||||\n\
||||/                              \||||\n\
|||/                                \|||\n\
||/                                  \||\n\
|/                                    \|\n\
/                                      \ ")
        pick = options()
        if pick == '1':
            current = False
            skip()
        else:
            skip()
            print(pick+" Is An Invalid Direction")

def right():
    current = True
    while current == True:
        print("\
|||||||||||||____][____][____][__|||||||\n\
|||||||||||||_][____][____][____]|||||||\n\
|||||||||||||____][____][____][__|||||||\n\
|||||||||||||_][____][____][____]|||||||\n\
|||||||||||||____][____][____][__|||||||\n\
|||||||||||||_][____][____][____]|||||||\n\
|||||||||||||____][____][____][__|||||||\n\
|||||||||||||__][____][____][____]||||||\n\
|||||||||||/                     |||||||\n\
||||||||||/                      |||||||\n\
|||||||||/                       |||||||\n\
||||||||/                        |||||||\n\
|||||||/                         |||||||\n\
||||||/                          \||||||\n\
|||||/                            \|||||\n\
||||/                              \||||\n\
|||/                                \|||\n\
||/                                  \||\n\
|/                                    \|\n\
/                                      \ ")
        pick = options()
        if pick == '3':
            current = False
            skip()
        else:
            skip()
            print(pick+" Is An Invalid Direction")

def sphinx():
    current = True
    while current == True:
        print("\
            Beware The Sphinx\n\
|||||||||||||||||\     /|||||||||||||||||\n\
||||||||||||||||||     ||||||||||||||||||\n\
|||||||||||||||||/     \|||||||||||||||||\n\
||||||||||||||||/       \||||||||||||||||\n\
|||||||||||||||/         \|||||||||||||||\n\
||||||||||||||/    ___    \||||||||||||||\n\
|||||||||||||/   /-\V/-\   \|||||||||||||\n\
||||||||||||/   /|<> <>|\   \||||||||||||\n\
|||||||||||/   /--\_-_/--\   \|||||||||||\n\
||||||||||/   /---/ V \---\   \||||||||||\n\
|||||||||/   |\---|\ /|---/|   \|||||||||\n\
||||||||/    | \-/  O  \-/ |    \||||||||\n\
|||||||/     | |         | |     \|||||||\n\
||||||/     /   \ -___- /   \     \||||||\n\
|||||/   ___Y Y Y_______Y Y Y___   \|||||\n\
||||/   /_______________________\   \||||\n\
|||/   /_________________________\   \|||\n\
||/   /___________________________\   \||\n\
|/                                     \|\n\
/                                       \ ")
        riddle1 = "what is your favorite color?"
        riddle2 = "what?"
        riddle3 = "what?"
        current = False
    

def skip():
    print("\n\n")

def labyrinth5x5():
    inmaze = True
    while inmaze == True:
        straight()
        left()
        right()
        straight()
        right()
        current = left_right()
        if current == '1':
            left()
            straight()
            left()
            right()
            left()
            current = left_right()
            if current == '3':
                right()
                straight()
                current = straight_right()
                if current == '2':
                    inmaze = False
                elif current == '3':
                    dead_end()
                    input("Press Enter To Begin Again")
                    skip()
                    print(' '*10+"Back At The Begining")
            elif current == '1':
                right()
                right()
                left()
                current = left_right()
                if current == '1':
                    straight()
                    dead_end()
                    input("Press Enter To Begin Again")
                    skip()
                    print(' '*10+"Back At The Begining")
                elif current == '3':
                    right()
                    dead_end()
                    input("Press Enter To Begin Again")
                    skip()
                    print(' '*10+"Back At The Begining")
        elif current == '3':
            dead_end()
            input("Press Enter To Begin Again")
            skip()
            print(' '*10+"Back At The Begining")

def labyrinthrandom():
    inmaze = True
    while inmaze == True:
        what = random.randint(1,85)
        if what >= 1 and what <= 10:
            left_right()
        elif what >= 11 and what <= 15:
            dead_end()
            input("Press Enter To Begin Again")
            skip()
            print(' '*10+"Back At The Begining")
        elif what >= 21 and what <= 30:
            straight_right()
        elif what >= 31 and what <= 40:
            straight_left()
        elif what >= 41 and what <= 50:
            straight_left_right()
        elif what >= 51 and what <= 60:
            straight()
        elif what >= 61 and what <= 70:
            left()
        elif what >= 71 and what <= 80:
            right()
        elif what >= 81:
            inmaze = False


def main():
    menu = True
    while menu == True:
        skip()
        print("WELCOME TO\n")
        title()
        ready = input("Will You Enter? (Y/N): ")
        if ready.capitalize() == "N":
            skip()
            skip()
            print("Your Fear Protects You.")
            skip()
            skip()
            quit()
        elif ready.capitalize() == "Y":
            skip()
            print(' '*15+"Then Enter")
            menu = False
        else:
            skip()
            skip()
            print("That Wasnt A Valid Answer")
    labyrinth5x5()
    skip()
    print("Congragulations You Solved The Maze!")
    skip()

main()