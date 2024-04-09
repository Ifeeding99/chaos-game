import pygame
import numpy as np
import math
import time
import sys
import turtle

pygame.init()
red = (230,50,50)
green = (0, 255, 0)
blue = (0, 0, 128)
brown = (127,64,0)
yellow = (255,255,0)
white = (255, 255, 255)
black = (0,0,0)
violet = (127,0,255)
info = pygame.display.Info()
w = info.current_w
h = info.current_h
screen = pygame.display.set_mode((w,h),pygame.NOFRAME)
pygame.display.set_caption("Chaos Game")

class Y_N_box:
    def __init__(self, y):
        self.y = y #'y' if it's yes 'n' if it's no
        if self.y == 'y':
            self.color = green
        else:
            self.color = red
    def change_color(self):
        if self.color == yellow and self.y == 'y':
            self.color = green
        elif self.color == yellow and self.y == 'n':
            self.color = red
        else:
            self.color = yellow
    def draw(self,x,y,s):
        self.text_rect = pygame.draw.rect(screen, self.color, (x,y,s,s))


        

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def coordinate_converter(x,y):
    b = x + int(info.current_w/2), int(info.current_h/2) - y
    return b


def music_menu():
    s = 20
    choice = False
    choice2 = False
    font = pygame.font.Font('freesansbold.ttf', 16)
    phrase = "Do you want music in the background?"
    text = font.render(phrase, True, white, black)
    rect = text.get_rect()
    rect.center = (int(w/2),int(h/8))
    y = Y_N_box('y')
    n = Y_N_box('n')
    phrase2 = "Are you sure?"
    text2 = font.render(phrase2, True, white, black)
    rect2 = text2.get_rect()
    rect2.center = (int(w/2),int(h/8))
    y2 = Y_N_box('y')
    n2 = Y_N_box('n')
    running = True
    while running:
        screen.fill(black)
        screen.blit(text,rect)
        y.draw(int(w/2 - 3* s),int(h/8 + 20),s)
        n.draw(int(w/2 + 3* s),int(h/8 + 20),s)
        mpos = pygame.mouse.get_pos()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
                break

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    pygame.quit()
                    sys.exit()
                    break

            elif event.type == pygame.MOUSEBUTTONDOWN and y.text_rect.collidepoint(mpos) and n.color != yellow:
                y.change_color()
                y.draw(int(w / 2 - 3 * s), int(h / 8 + 20), s)
                pygame.display.update()
                time.sleep(1)
                choice = not(choice)
                running2 = True

            elif event.type == pygame.MOUSEBUTTONDOWN and n.text_rect.collidepoint(mpos) and y.color != yellow:
                n.change_color()
                n.draw(int(w / 2 + 3 * s), int(h / 8 + 20), s)
                pygame.display.update()
                time.sleep(1)
                choice = not(choice)
                running2 = True

        if choice == True and running2 == True:
            while running2:
                screen.fill(black)
                screen.blit(text2, rect2)
                y2.draw(int(w / 2 - 3 * s), int(h / 8 + 20), s)
                n2.draw(int(w / 2 + 3 * s), int(h / 8 + 20), s)
                mpos = pygame.mouse.get_pos()
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        pygame.quit()
                        sys.exit()
                        break

                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            running = False
                            pygame.quit()
                            sys.exit()
                            break
                    elif event.type == pygame.MOUSEBUTTONDOWN and n2.text_rect.collidepoint(mpos) and y2.color != yellow:
                        n2.change_color()
                        n2.draw(int(w / 2 + 3 * s), int(h / 8 + 20), s)
                        pygame.display.update()
                        time.sleep(1)
                        running2 = False
                        choice = False
                        y.color = green
                        n.color = red
                        n2.color = red
                        break
                    elif event.type == pygame.MOUSEBUTTONDOWN and y2.text_rect.collidepoint(mpos) and n2.color != yellow:
                        y2.change_color()
                        y2.draw(int(w / 2 - 3 * s), int(h / 8 + 20), s)
                        pygame.display.update()
                        time.sleep(1)
                        running2 = False
                        running = False
                        if y.color == yellow:
                            music = True
                        else:
                            music = False

    if music:
        #The_Final_Game-2
        #Für Elise
        #Beethoven-Moonlight-Sonata-_FULL_
        #Edward-Elgar-Enigma-Variations
        song_input = int(turtle.textinput('Choose the song:',
                                          "Choose the song from the ones below(insert the correspondent number):"
                                          "\n1-Für Elise"
                                          "\n 2-Moonlight Sonata"
                                          "\n 3-Enigma variations"
                                          "\n 4-The final game"))
        turtle.bye()
        # Per resuscitare turtle, dato che turtle.bye() killa la finestra
        turtle.Turtle._screen = None  # force recreation of singleton Screen object
        turtle.TurtleScreen._RUNNING = True  # only set upon TurtleScreen() definition
        assert(song_input == 1 or song_input == 2 or song_input == 3 or song_input == 4), "Invalid answer!!!"
        if song_input == 1:
            song = 'Für Elise.ogg'
        elif song_input == 2:
            song = 'Beethoven-Moonlight-Sonata-_FULL_.ogg'
        elif song_input == 3:
            song = 'Edward-Elgar-Enigma-Variations.ogg'
        elif song_input == 4:
            song = 'The_Final_Game-2.ogg'
        pygame.mixer.music.load(song)
        pygame.mixer.music.play(-1)


def multi_point_menu():
    choice = False
    s = 20
    font = pygame.font.Font('freesansbold.ttf', 16)
    phrase1 = 'Do you want 3 points?(if no you\'ll insert the correct number of points)'
    text1 = font.render(phrase1, True, white, black)
    rect1 = text1.get_rect()
    rect1.center = (int(w/2),int(h/8))
    y1 = Y_N_box('y')
    n1 = Y_N_box('n')
    running = True
    while running:
        screen.fill(black)
        screen.blit(text1,rect1)
        y1.draw(int(w/2 - 3* s),int(h/8 + 20),s)
        n1.draw(int(w/2 + 3* s),int(h/8 + 20),s)
        mpos = pygame.mouse.get_pos()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
                break

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    pygame.quit()
                    sys.exit()
                    break

            elif event.type == pygame.MOUSEBUTTONDOWN and y1.text_rect.collidepoint(mpos) and n1.color != yellow:

                y1.change_color()
                y1.draw(int(w / 2 - 3 * s), int(h / 8 + 20), s)
                pygame.display.update()
                time.sleep(1)
                choice = not(choice)
                running2 = True

            elif event.type == pygame.MOUSEBUTTONDOWN and n1.text_rect.collidepoint(mpos) and y1.color != yellow:
                n1.change_color()
                n1.draw(int(w / 2 + 3 * s), int(h / 8 + 20), s)
                pygame.display.update()
                time.sleep(1)
                choice = not(choice)
                running2 = True

            if choice == True and running2 == True:
                phrase2 = "Are you sure?"
                text2 = font.render(phrase2, True, white, black)
                rect2 = text2.get_rect()
                rect2.center = (int(w/2),int(h/8))
                y2 = Y_N_box('y')
                n2 = Y_N_box('n')
                while running2:
                    screen.fill(black)
                    screen.blit(text2, rect2)
                    y2.draw(int(w / 2 - 3 * s), int(h / 8 + 20), s)
                    n2.draw(int(w / 2 + 3 * s), int(h / 8 + 20), s)
                    mpos = pygame.mouse.get_pos()
                    pygame.display.update()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            running = False
                            pygame.quit()
                            sys.exit()
                            break

                        elif event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_ESCAPE:
                                running = False
                                pygame.quit()
                                sys.exit()
                                break

                        elif event.type == pygame.MOUSEBUTTONDOWN and y2.text_rect.collidepoint(
                                mpos) and n2.color != yellow:

                            y2.change_color()
                            y2.draw(int(w / 2 - 3 * s), int(h / 8 + 20), s)
                            pygame.display.update()
                            time.sleep(1)
                            choice = not (choice)
                            running = False
                            running2 = False
                            if y1.color == yellow:
                                n_points = 3
                            else:
                                n_points = int(turtle.textinput('Number of points', 'Insert the number of points you want'))
                                turtle.bye()
                                # Per resuscitare turtle, dato che turtle.bye() killa la finestra
                                turtle.Turtle._screen = None  # force recreation of singleton Screen object
                                turtle.TurtleScreen._RUNNING = True  # only set upon TurtleScreen() definition

                        elif event.type == pygame.MOUSEBUTTONDOWN and n2.text_rect.collidepoint(
                                mpos) and y2.color != yellow:
                            n2.change_color()
                            n2.draw(int(w / 2 + 3 * s), int(h / 8 + 20), s)
                            pygame.display.update()
                            time.sleep(1)
                            choice = not (choice)
                            running2 = False
                            y1.color = green
                            n1.color = red
                            n2.color = red

    return n_points





def main_menu():
    global s #side of yes/no rects
    choice1 = False
    choice2 = False
    choice3 = False


    equilateral_triangle = True
    random_starting_point = True
    half_travel_distance = True

    s = 20 
    font = pygame.font.Font('freesansbold.ttf', 16)
    phrase1 = "Equilateral triangle?(y/n)"
    text1 = font.render(phrase1, True, white, black)
    rect1 = text1.get_rect()
    rect1.center = (int(w/2),int(h/8))
    
    y1 = Y_N_box('y')
    n1 = Y_N_box('n')
    
    phrase2 = "Random starting point? (y/n)"
    text2 = font.render(phrase2, True, white, black)
    rect2 = text2.get_rect()
    rect2.center = (int(w/2),int(h/4))
    
    y2 = Y_N_box('y')
    n2 = Y_N_box('n')
    
    phrase3 = "Go to midpoint of the segment?(travel half distance)"
    text3 = font.render(phrase3, True, white, black)
    rect3 = text3.get_rect()
    rect3.center = (int(w/2),int(3*h/8))
    
    y3 = Y_N_box('y')
    n3 = Y_N_box('n')

    phrase4 = "Do you confirm these settings?"
    text4 = font.render(phrase4, True, white, black)
    rect4 = text4.get_rect()
    rect4.center = (int(w/2),int(h/8))
    
    y4 = Y_N_box('y')
    n4 = Y_N_box('n')
    running = True
    while running:
        screen.fill(black)
        screen.blit(text1,rect1)
        screen.blit(text2,rect2)
        screen.blit(text3,rect3)
        font = pygame.font.Font('freesansbold.ttf', 16)
        y1.draw(int(w/2 - 3* s),int(h/8 + 20),s)
        n1.draw(int(w/2 + 3* s),int(h/8 + 20),s)
        y2.draw(int(w/2 - 3* s),int(h/4 + 20),s)
        n2.draw(int(w/2 + 3* s),int(h/4 + 20),s)
        y3.draw(int(w/2 - 3* s),int(3*h/8 + 20),s)
        n3.draw(int(w/2 + 3* s),int(3*h/8 + 20),s)      
        mpos = pygame.mouse.get_pos()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
                break

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    pygame.quit()
                    sys.exit()
                    break
            
            elif event.type == pygame.MOUSEBUTTONDOWN and y1.text_rect.collidepoint(mpos) and n1.color != yellow:
                y1.change_color()
                y1.draw(int(w/2 - 3* s),int(h/8 + 20),s)
                pygame.display.update()
                choice1 = not(choice1)

            elif event.type == pygame.MOUSEBUTTONDOWN and n1.text_rect.collidepoint(mpos) and y1.color != yellow:
                n1.change_color()
                n1.draw(int(w/2 + 3* s),int(h/8 + 20),s)
                pygame.display.update()
                choice1 = not(choice1)
                
            elif event.type == pygame.MOUSEBUTTONDOWN and y2.text_rect.collidepoint(mpos) and n2.color != yellow:
                y2.change_color()
                y2.draw(int(w/2 - 3* s),int(h/4 + 20),s)
                pygame.display.update()
                choice2 = not(choice2)
                
            elif event.type == pygame.MOUSEBUTTONDOWN and n2.text_rect.collidepoint(mpos) and y2.color != yellow:
                n2.change_color()
                n2.draw(int(w/2 + 3* s),int(h/4 + 20),s)
                pygame.display.update()
                choice2 = not(choice2)

            elif event.type == pygame.MOUSEBUTTONDOWN and y3.text_rect.collidepoint(mpos) and n3.color != yellow:
                y3.change_color()
                y3.draw(int(w/2 - 3* s),int(3*h/8 + 20),s)
                pygame.display.update()
                choice3 = not(choice3)

            elif event.type == pygame.MOUSEBUTTONDOWN and n3.text_rect.collidepoint(mpos) and y3.color != yellow:
                n3.change_color()
                n3.draw(int(w/2 + 3* s),int(3*h/8 + 20),s)
                pygame.display.update()
                choice3 = not(choice3)

                
        if choice1 == True and choice2 == True and choice3 == True:
            time.sleep(1)
            confirm_menu = True
            screen.fill(black)
            y4.color = green
            n4.color = red
            
            while confirm_menu:
                screen.blit(text4,rect4)
                y4.draw(int(w/2 - 3* s),int(h/8 + 20),s)
                n4.draw(int(w/2 + 3* s),int(h/8 + 20),s)
                mpos = pygame.mouse.get_pos()
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        confirm_menu = False
                        running = False
                        pygame.quit()
                        sys.exit()
                        break

                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            confirm_menu = False
                            running = False
                            pygame.quit()
                            sys.exit()
                            break
                    elif event.type == pygame.MOUSEBUTTONDOWN and y4.text_rect.collidepoint(mpos) and n4.color != yellow:
                        y4.color = yellow
                        y4.draw(int(w/2 - 3* s),int(h/8 + 20),s)
                        pygame.display.update()
                        time.sleep(1)
                        confirm_menu = False
                        running = False           

                        if n1.color == yellow:
                            equilateral_triangle = False
                        elif y1.color == yellow:
                            equilateral_triangle = True
                            
                        if n2.color == yellow:
                            random_starting_point = False
                        elif y2.color == yellow:
                            random_starting_point = True

                        if n3.color == yellow:
                            half_travel_distance = False
                        elif y3.color == yellow:
                            half_travel_distance = True

                    elif event.type == pygame.MOUSEBUTTONDOWN and n4.text_rect.collidepoint(mpos) and y4.color != yellow:
                        n4.color = yellow
                        n4.draw(int(w/2 + 3* s),int(h/8 + 20),s)
                        pygame.display.update()
                        time.sleep(1)
                        confirm_menu = False
                        choice1 = False
                        choice2 = False
                        choice3 = False
                        y1.color = green
                        n1.color = red
                        y2.color = green
                        n2.color = red
                        y3.color = green
                        n3.color = red


    return equilateral_triangle, random_starting_point, half_travel_distance




def menu_2(eq_t, r_p, h_d): #equilateral triangle, random point, half distance
    manually = False
    global A,B,C, START_POINT
    A = Point(0,0)
    B = Point(0,0)
    C = Point(0,0)
    START_POINT = Point(0,0)
    font = pygame.font.Font('freesansbold.ttf',16)
    choice1, choice2, choice3 = True, True, True
    if eq_t:
        A = Point(400,(-int(h/2))+10)
        B = Point(-400, (-int(h/2))+10)
        C = Point(0, 800*(math.sqrt(3)/2) + (-(int(h/2)))+10)
    if not(eq_t):
        choice1 = False
        phrase1 = "Do you want to choose the vertices with the mouse? (if not you'll be asked later if you want to enter them manually or not)"
        text1 = font.render(phrase1, True, white, black)
        rect1 = text1.get_rect()
        rect1.center = (int(w/2),int(h/8))
        
        y1 = Y_N_box('y')
        n1 = Y_N_box('n')

    if r_p:
        START_POINT.x = np.random.randint(-(int(w/2)),int(w/2)+1)
        START_POINT.y = np.random.randint(-(int(h/2)),int(h/2)+1)

    if not(r_p):
        choice2 = False
        phrase2 = "Do you want to choose the starting point with your mouse?"
        text2 = font.render(phrase2, True, white, black)
        rect2 = text2.get_rect()
        rect2.center = (int(w/2),int(h/4))
        y2 = Y_N_box('y')
        n2 = Y_N_box('n')


    if not(h_d):
        choice3 = False
        

    if h_d:
        d = 0.5

    phrase4 = "Do you confirm these settings?"
    text4 = font.render(phrase4, True, white, black)
    rect4 = text4.get_rect()
    rect4.center = (int(w/2),int(h/8))
    
    y4 = Y_N_box('y')
    n4 = Y_N_box('n')
    
    running = True
    while running:
        if not(eq_t):
            screen.blit(text1, rect1)
            y1.draw(int(w/2 - 3* s),int(h/8 + 20),s)
            n1.draw(int(w/2 + 3* s),int(h/8 + 20),s)
        if not(r_p):
            screen.blit(text2, rect2)
            y2.draw(int(w/2 - 3* s),int(h/4 + 20),s)
            n2.draw(int(w/2 + 3* s),int(h/4 + 20),s)

        if not(h_d) and not(choice3):
            d = float(turtle.textinput("distance","Enter what fraction of the distance between points you want to travel (es: 0.5, 0.75, etc...)"))
            turtle.bye()
            # Per resuscitare turtle, dato che turtle.bye() killa la finestra
            turtle.Turtle._screen = None  # force recreation of singleton Screen object
            turtle.TurtleScreen._RUNNING = True  # only set upon TurtleScreen() definition
            choice3 = True
        mpos = pygame.mouse.get_pos()
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit
                break

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    pygame.quit()
                    sys.exit()
                    break

            elif not(eq_t) and event.type == pygame.MOUSEBUTTONDOWN and y1.text_rect.collidepoint(mpos) and n1.color != yellow:
                y1.change_color()
                y1.draw(int(w/2 - 3* s),int(h/8 + 20),s)
                pygame.display.update()
                choice1 = not(choice1)
                
            elif not(eq_t) and event.type == pygame.MOUSEBUTTONDOWN and n1.text_rect.collidepoint(mpos) and y1.color != yellow:
                n1.change_color()
                n1.draw(int(w/2 + 3* s),int(h/8 + 20),s)
                pygame.display.update()
                choice1 = not(choice1)

            elif not(r_p) and event.type == pygame.MOUSEBUTTONDOWN and y2.text_rect.collidepoint(mpos) and n2.color != yellow:
                y2.change_color()
                y2.draw(int(w/2 - 3* s),int(h/4 + 20),s)
                pygame.display.update()
                choice2 = not(choice2)
                
            elif not(r_p) and event.type == pygame.MOUSEBUTTONDOWN and n2.text_rect.collidepoint(mpos) and y2.color != yellow:
                n2.change_color()
                n2.draw(int(w/2 + 3* s),int(h/4 + 20),s)
                pygame.display.update()
                choice2 = not(choice2)

        if choice1 == True and choice2 == True and choice3 == True:    #start of the confirm menu
            time.sleep(1)
            confirm_menu = True
            screen.fill(black)
            y4.color = green
            n4.color = red
            if not(eq_t) and n1.color == yellow:
                phrase5 = "Do you want to enter the coordinates of the vertices of the triangle manually? (if you choose no they will be randomly chosen)"
                text5 = font.render(phrase5, True, white, black)
                rect5 = text5.get_rect()
                rect5.center = (int(w/2),int(h/8))
                y5 = Y_N_box('y')
                n5 = Y_N_box('n')
                option2 = True
                while option2:
                    mpos = pygame.mouse.get_pos()
                    screen.blit(text5, rect5)
                    y5.draw(int(w/2 - 3* s),int(h/8 + 20),s)
                    n5.draw(int(w/2 + 3* s),int(h/8 + 20),s)
                    pygame.display.update()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            running = False
                            pygame.quit()
                            sys.exit
                            break

                        elif event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_ESCAPE:
                                running = False
                                pygame.quit()
                                sys.exit()
                                break
                        elif event.type == pygame.MOUSEBUTTONDOWN and y5.text_rect.collidepoint(mpos) and n5.color != yellow:
                            y5.color = yellow
                            y5.draw(int(w/2 - 3* s),int(h/8 + 20),s)
                            pygame.display.update()
                            manually = True #it is used to flag that the user will enter the vertices manually
                            option2 = False
                            break
                        elif event.type == pygame.MOUSEBUTTONDOWN and n5.text_rect.collidepoint(mpos) and y5.color != yellow:
                            n5.color = yellow
                            n5.draw(int(w/2 + 3* s),int(h/8 + 20),s)
                            pygame.display.update()
                            manually = False #it is used to flag that the user will enter the vertices manually
                            option2 = False
                            break
                if manually and y5.color == yellow:
                    L_P = []  # list of points
                    for i in range(3):
                        Px = float(turtle.textinput("vertices coordinates",
                                                    f"Enter the x-coordinate of the point number {i + 1} of the triangle"))
                        assert (-(w/2) <= Px <= (w/2)), "X coordinate out of the screen!!!"
                        Py = float(turtle.textinput("vertices coordinates",
                                                    f"Enter the y-coordinate of the point number {i + 1} of the triagle"))
                        assert (-(h/2) <= Py <= (h/2)), "Y coordinate out of the screen!!!"
                        L_P.append(Px)
                        L_P.append(Py)
                    turtle.bye()
                        # Per resuscitare turtle, dato che turtle.bye() killa la finestra
                    turtle.Turtle._screen = None  # force recreation of singleton Screen object
                    turtle.TurtleScreen._RUNNING = True  # only set upon TurtleScreen() definition
                    A.x = L_P[0]
                    A.y = L_P[1]
                    B.x = L_P[2]
                    B.y = L_P[3]
                    C.x = L_P[4]
                    C.y = L_P[5]

            time.sleep(1)
            screen.fill(black)
            if not (r_p) and y2.color == green and n2.color == yellow:
                x_cor = int(turtle.textinput("X Coordinate of the starting point","Enter the x-coordinate of the starting point (1,1366)"))
                assert (-(w/2) <= x_cor <= (w/2)), "X coordinate out of the screen!!!"
                y_cor = int(turtle.textinput("Y Coordinate of the starting point","Enter the y-coordinate of the starting point (1,768)"))
                assert (-(h/2) <= y_cor <= (h/2)), "Y coordinate out of the screen!!!"
                turtle.bye()
                START_POINT.x = x_cor
                START_POINT.y = y_cor
                # Per resuscitare turtle, dato che turtle.bye() killa la finestra
                turtle.Turtle._screen = None  # force recreation of singleton Screen object
                turtle.TurtleScreen._RUNNING = True  # only set upon TurtleScreen() definition
            time.sleep(1)
            screen.fill(black)

            time.sleep(1)
            screen.fill(black)
            while confirm_menu:
                screen.blit(text4,rect4)
                y4.draw(int(w/2 - 3* s),int(h/8 + 20),s)
                n4.draw(int(w/2 + 3* s),int(h/8 + 20),s)
                mpos = pygame.mouse.get_pos()
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        confirm_menu = False
                        running = False
                        pygame.quit()
                        sys.exit()
                        break

                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            confirm_menu = False
                            running = False
                            pygame.quit()
                            sys.exit()
                            break
                    elif event.type == pygame.MOUSEBUTTONDOWN and y4.text_rect.collidepoint(mpos) and n4.color != yellow:
                        y4.color = yellow
                        y4.draw(int(w/2 - 3* s),int(h/8 + 20),s)
                        pygame.display.update()
                        time.sleep(1)
                        confirm_menu = False
                        running = False

                                    
                        if not(eq_t) and y1.color == yellow:
                            Q1 = 1 #points selected with mouse
                        if not(eq_t) and y1.color == green:
                            Q1 = 2 #points selected at random
                        if eq_t:
                            Q1 = 0 #equilateral triangle; A,B,C have already been defined

                        if not(r_p) and y2.color == yellow:
                            Q2 = 1 #point selected with mouse
                        if not(r_p) and y2.color == green:
                            Q2 = 0
                        if r_p:
                            Q2 = 0 #default case
                        Q3 = d
       


                    elif event.type == pygame.MOUSEBUTTONDOWN and n4.text_rect.collidepoint(mpos) and y4.color != yellow:
                        n4.color = yellow
                        n4.draw(int(w/2 + 3* s),int(h/8 + 20),s)
                        pygame.display.update()
                        time.sleep(1)
                        confirm_menu = False
                        choice1 = False
                        choice2 = False
                        choice3 = False
                        if not(eq_t):
                            y1.color = green
                            n1.color = red
                        if not(r_p):
                            y2.color = green
                            n2.color = red
                        d = 0.5

    return Q1, Q2, Q3               
def choose_with_mouse(s1,s2):
    screen.fill(black)
    font = pygame.font.Font('freesansbold.ttf',16)
    if s1 == 2:
        A.x = np.random.randint(-int(w/2),int(w/2)+1)
        A.y = np.random.randint(-int(h / 2), int(h / 2) + 1)

        B.x = np.random.randint(-int(w/2),int(w/2)+1)
        B.y = np.random.randint(-int(h / 2), int(h / 2) + 1)

        C.x = np.random.randint(-int(w/2),int(w/2)+1)
        C.y = np.random.randint(-int(h / 2), int(h / 2) + 1)
    if s1 == 1:
        running = True
        n_points_taken = 0
        phrase1 = "Click on the point you want to choose. You have 3 left"
        phrase2 = "Click on the point you want to choose. You have 2 left"
        phrase3 = "Click on the point you want to choose. You have 1 left"
        phrase4 = "Click on the point you want to choose. You have 0 left"
        text1 = font.render(phrase1, True, white, black)
        while running:
            screen.fill(black)
            rect1 = text1.get_rect()
            rect1.center = (int(w / 2), int(h / 8))
            screen.blit(text1,rect1)
            mpos = pygame.mouse.get_pos()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                        pygame.quit()
                        sys.exit()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if n_points_taken == 0:
                        A.x = mpos[0] - int(w/2)
                        A.y = int(h/2) - mpos[1]
                        n_points_taken += 1
                        text1 = font.render(phrase2, True, white, black)


                    elif n_points_taken == 1:
                        B.x = mpos[0] - int(w/2)
                        B.y = int(h/2) - mpos[1]
                        n_points_taken += 1
                        screen.fill(black)
                        text1 = font.render(phrase3, True, white, black)
                        screen.blit(text1,rect1)
                        pygame.display.update()


                    elif n_points_taken == 2:
                        C.x = mpos[0] - int(w/2)
                        C.y = int(h/2) - mpos[1]
                        n_points_taken += 1
                        screen.fill(black)
                        text1 = font.render(phrase4, True, white, black)
                        screen.blit(text1,rect1)
                        pygame.display.update()

                elif n_points_taken == 3:
                    screen.fill(black)
                    phrase1 = "You have chosen every single point"
                    text1 = font.render(phrase1, True, white, black)
                    screen.blit(text1,rect1)
                    pygame.display.update()
                    time.sleep(2)
                    running = False
                    break


    if s2 == 1:
        running = True
        phrase1 = "Click where you want to pick the starting point"
        while running:
            screen.fill(black)
            text1 = font.render(phrase1, True, white, black)
            rect1 = text1.get_rect()
            rect1.center = (int(w / 2), int(h / 8))
            screen.blit(text1, rect1)
            mpos = pygame.mouse.get_pos()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                        pygame.quit()
                        sys.exit()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    START_POINT.x = mpos[0] - int(w/2)
                    START_POINT.y = int(h/2) - mpos[1]
                    screen.fill(black)
                    phrase1 = "You have chosen the starting point"
                    text1 = font.render(phrase1, True, white, black)
                    screen.blit(text1,rect1)
                    pygame.display.update()
                    time.sleep(2)
                    running = False
                    break




def draw_triangle(steps):
    first_x = START_POINT.x
    first_y = START_POINT.y
    TRAVELLING_POINT = Point(first_x,first_y)
    M = D * 2
    pygame.draw.circle(screen, red, coordinate_converter(A.x,A.y), 2)
    pygame.draw.circle(screen, red, coordinate_converter(B.x,B.y), 2)
    pygame.draw.circle(screen, red, coordinate_converter(C.x,C.y), 2)
    pygame.draw.circle(screen, violet, coordinate_converter(first_x,first_y), 2)
    for i in range(steps):
        n = np.random.randint(1,4)
        if n == 1:
            TRAVELLING_POINT.x = int((TRAVELLING_POINT.x+A.x)*D)
            TRAVELLING_POINT.y = int((TRAVELLING_POINT.y+A.y)*D)
            screen.set_at(coordinate_converter(TRAVELLING_POINT.x, TRAVELLING_POINT.y), white)
        if n == 2:
            TRAVELLING_POINT.x = int((TRAVELLING_POINT.x+B.x)*D)
            TRAVELLING_POINT.y = int((TRAVELLING_POINT.y+B.y)*D)
            screen.set_at(coordinate_converter(TRAVELLING_POINT.x, TRAVELLING_POINT.y), white)
        if n == 3:
            TRAVELLING_POINT.x = int((TRAVELLING_POINT.x+C.x)*D)
            TRAVELLING_POINT.y = int((TRAVELLING_POINT.y+C.y)*D)
            screen.set_at(coordinate_converter(TRAVELLING_POINT.x, TRAVELLING_POINT.y), white)
        pygame.display.update()



def sierpinsky_triangle():
    ongoing = True
    while ongoing:
        screen.fill(black)
        pygame.display.update()
        Q = turtle.textinput("simulation","Do you want to make another simulation with these settings? (y/n)")
        turtle.bye()
        turtle.Turtle._screen = None  # force recreation of singleton Screen object
        turtle.TurtleScreen._RUNNING = True  # only set upon TurtleScreen() definition
        assert (Q == 'y' or Q == 'n'), "Invalid answer!!!"
        if Q == 'y':
            screen.fill(black)
            question = turtle.textinput("How many triangles","Do you want one simulation or many? (1 for one, + for many)")
            assert (question == '1' or question == '+'), "Invalid answer!!!"
            turtle.bye()
            # Per resuscitare turtle, dato che turtle.bye() killa la finestra
            turtle.Turtle._screen = None  # force recreation of singleton Screen object
            turtle.TurtleScreen._RUNNING = True  # only set upon TurtleScreen() definition
            if question == '1':
                steps = int(turtle.textinput("Number of steps", "How many steps do you want?"))
                turtle.bye()
                turtle.Turtle._screen = None  # force recreation of singleton Screen object
                turtle.TurtleScreen._RUNNING = True  # only set upon TurtleScreen() definition
                running = True
                draw_triangle(steps)
                while running:
                    pygame.display.update()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            running = False
                        elif event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_ESCAPE:
                                running = False
                        elif event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_SPACE:
                                running = False
                                break

            else:
                steps = int(turtle.textinput("Number of steps", "How many steps do you want?"))
                turtle.bye()
                turtle.Turtle._screen = None  # force recreation of singleton Screen object
                turtle.TurtleScreen._RUNNING = True  # only set upon TurtleScreen() definition
                running = True

                while running:
                    screen.fill(black)
                    draw_triangle(steps)
                    pygame.display.update()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            running = False
                            ongoing = False
                        elif event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_ESCAPE:
                                running = False
                                ongoing = False
                        elif event.type == pygame.KEYDOWN:
                            if event.key != pygame.K_ESCAPE:
                                running = False
        elif Q == 'n':
            ongoing = False


def take_points(N):
    points = []
    running2 = False
    s = 20
    font = pygame.font.Font('freesansbold.ttf', 16)
    phrase1 = 'Do you want the points to be selected at random?'
    text1 = font.render(phrase1, True, white, black)
    rect1 = text1.get_rect()
    rect1.center = (int(w/2),int(h/8))
    y1 = Y_N_box('y')
    n1 = Y_N_box('n')
    phrase2 = 'Do you want to select the points with your mouse?(Otherwise you\'ll enter the coordinates manually)'
    text2 = font.render(phrase2, True, white, black)
    rect2 = text2.get_rect()
    rect2.center = (int(w/2),int(h/8))
    y2 = Y_N_box('y')
    n2 = Y_N_box('n')
    running = True
    while running:
        screen.fill(black)
        screen.blit(text1,rect1)
        y1.draw(int(w/2 - 3* s),int(h/8 + 20),s)
        n1.draw(int(w/2 + 3* s),int(h/8 + 20),s)
        mpos = pygame.mouse.get_pos()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
                break

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    pygame.quit()
                    sys.exit()
                    break

            elif event.type == pygame.MOUSEBUTTONDOWN and y1.text_rect.collidepoint(mpos) and n1.color != yellow:

                y1.change_color()
                y1.draw(int(w / 2 - 3 * s), int(h / 8 + 20), s)
                pygame.display.update()
                running = False
                mouse_click = False
                time.sleep(1)
                for i in range(N):
                    points.append(Point(np.random.randint(-(int(w/2)),int(w/2)+1),np.random.randint(-(int(h/2)),int(h/2)+1)))


            elif event.type == pygame.MOUSEBUTTONDOWN and n1.text_rect.collidepoint(mpos) and y1.color != yellow:
                n1.change_color()
                n1.draw(int(w / 2 + 3 * s), int(h / 8 + 20), s)
                pygame.display.update()
                time.sleep(1)
                #running2 = True
                running3 = True
                phrase_reg = "Do you want a regular polygon?"
                text_reg = font.render(phrase_reg, True, white, black)
                rect_reg = text_reg.get_rect()
                rect_reg.center = (int(w / 2), int(h / 8))
                y_reg = Y_N_box('y')
                n_reg = Y_N_box('n')
                while running3:
                    screen.fill(black)
                    screen.blit(text_reg, rect_reg)
                    y_reg.draw(int(w / 2 - 3 * s), int(h / 8 + 20), s)
                    n_reg.draw(int(w / 2 + 3 * s), int(h / 8 + 20), s)
                    mpos = pygame.mouse.get_pos()
                    pygame.display.update()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            running = False
                            pygame.quit()
                            sys.exit()
                            break

                        elif event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_ESCAPE:
                                running = False
                                pygame.quit()
                                sys.exit()
                                break

                        elif event.type == pygame.MOUSEBUTTONDOWN and y_reg.text_rect.collidepoint(mpos) and n_reg.color != yellow:
                            y_reg.change_color()
                            y_reg.draw(int(w / 2 - 3 * s), int(h / 8 + 20), s)
                            pygame.display.update()
                            time.sleep(1)
                            if int(h/2) >= int(w/2):
                                r = int(w/2) -10
                            else:
                                r = int(h/2) - 10
                            for n in range (N):
                                x_cor = r* math.cos(2*math.pi*(n/N))
                                y_cor = r* math.sin(2*math.pi*(n/N))
                                points.append(Point(x_cor,y_cor))
                            running3 = False
                            running2 = False
                            running = False
                            mouse_click = False

                        elif event.type == pygame.MOUSEBUTTONDOWN and n_reg.text_rect.collidepoint(mpos) and y_reg.color != yellow:
                            n_reg.change_color()
                            n_reg.draw(int(w / 2 + 3 * s), int(h / 8 + 20), s)
                            pygame.display.update()
                            time.sleep(1)
                            running3 = False
                            running2 = True
                            break

        if running2:
            while running2:
                screen.fill(black)
                screen.blit(text2, rect2)
                y2.draw(int(w / 2 - 3 * s), int(h / 8 + 20), s)
                n2.draw(int(w / 2 + 3 * s), int(h / 8 + 20), s)
                mpos = pygame.mouse.get_pos()
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running2 = False
                        pygame.quit()
                        sys.exit()
                        break

                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            running2 = False
                            pygame.quit()
                            sys.exit()
                            break

                    elif event.type == pygame.MOUSEBUTTONDOWN and y2.text_rect.collidepoint(
                            mpos) and n2.color != yellow:

                        y2.change_color()
                        y2.draw(int(w / 2 - 3 * s), int(h / 8 + 20), s)
                        pygame.display.update()
                        time.sleep(1)
                        mouse_click = True
                        running2 = False
                        running = False


                    elif event.type == pygame.MOUSEBUTTONDOWN and n2.text_rect.collidepoint(
                            mpos) and y2.color != yellow:
                        n2.change_color()
                        n2.draw(int(w / 2 + 3 * s), int(h / 8 + 20), s)
                        pygame.display.update()
                        time.sleep(1)
                        mouse_click = False
                        for i in range(N):
                            phrasex = f'Enter the x-coordinate of the point number {i+1}'
                            phrasey = f'Enter the y-coordinate of the point number {i + 1}'

                            x_cor = int(turtle.textinput('X Coordinate', phrasex))
                            y_cor = int(turtle.textinput('Y Coordinate', phrasey))
                            turtle.bye()
                            # Per resuscitare turtle, dato che turtle.bye() killa la finestra
                            turtle.Turtle._screen = None  # force recreation of singleton Screen object
                            turtle.TurtleScreen._RUNNING = True  # only set upon TurtleScreen() definition
                            points.append(Point(x_cor,y_cor))
                        running2 = False
                        running = False

    return points, mouse_click

def start_point_menu():
    global M_START_POINT #multiple points starting point
    M_START_POINT = Point(0,0)
    s = 20
    font = pygame.font.Font('freesansbold.ttf', 16)
    phrase1 = 'Do you want the starting point to be randomly chosen?'
    phrase2 = 'Do you want to click with the mouse to choose the starting point?(if not you\'ll enter it manually)'
    text1 = font.render(phrase1, True, white, black)
    rect1 = text1.get_rect()
    rect1.center = (int(w/2),int(h/8))
    text2 = font.render(phrase2, True, white, black)
    rect2 = text2.get_rect()
    rect2.center = (int(w/2),int(h/8))
    y1 = Y_N_box('y')
    n1 = Y_N_box('n')
    y2 = Y_N_box('y')
    n2 = Y_N_box('n')
    running = True
    while running:
        screen.fill(black)
        screen.blit(text1,rect1)
        y1.draw(int(w/2 - 3* s),int(h/8 + 20),s)
        n1.draw(int(w/2 + 3* s),int(h/8 + 20),s)
        mpos = pygame.mouse.get_pos()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
                break

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    pygame.quit()
                    sys.exit()
                    break

            elif event.type == pygame.MOUSEBUTTONDOWN and y1.text_rect.collidepoint(mpos) and n1.color != yellow:

                y1.change_color()
                y1.draw(int(w / 2 - 3 * s), int(h / 8 + 20), s)
                pygame.display.update()
                running = False
                M_START_POINT.x = np.random.randint(-int(w / 2), int(w / 2)+1)
                M_START_POINT.y = np.random.randint(-int(h / 2), int(h / 2) + 1)
                time.sleep(1)


            elif event.type == pygame.MOUSEBUTTONDOWN and n1.text_rect.collidepoint(mpos) and y1.color != yellow:
                n1.change_color()
                n1.draw(int(w / 2 + 3 * s), int(h / 8 + 20), s)
                pygame.display.update()
                time.sleep(1)
                running2 = True
                while running2:
                    screen.fill(black)
                    screen.blit(text2, rect2)
                    y2.draw(int(w / 2 - 3 * s), int(h / 8 + 20), s)
                    n2.draw(int(w / 2 + 3 * s), int(h / 8 + 20), s)
                    mpos = pygame.mouse.get_pos()
                    pygame.display.update()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            running = False
                            pygame.quit()
                            sys.exit()
                            break

                        elif event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_ESCAPE:
                                running = False
                                pygame.quit()
                                sys.exit()
                                break

                        elif event.type == pygame.MOUSEBUTTONDOWN and y2.text_rect.collidepoint(
                                mpos) and n2.color != yellow:

                            y2.change_color()
                            y2.draw(int(w / 2 - 3 * s), int(h / 8 + 20), s)
                            pygame.display.update()
                            running2 = False
                            running = False
                            time.sleep(1)
                            running3 = True
                            phrase3 = "Pick the starting point"
                            text3 = font.render(phrase3, True, white, black)
                            rect3 = text3.get_rect()
                            rect3.center = (int(w/2),int(h/8))
                            while running3:
                                screen.fill(black)
                                screen.blit(text3, rect3)
                                mpos = pygame.mouse.get_pos()
                                pygame.display.update()
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        running = False
                                        pygame.quit()
                                        sys.exit()
                                        break

                                    elif event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_ESCAPE:
                                            running = False
                                            pygame.quit()
                                            sys.exit()
                                            break

                                    elif event.type == pygame.MOUSEBUTTONDOWN:
                                        M_START_POINT.x = mpos[0] - int(w/2)
                                        M_START_POINT.y = int(h/2) - mpos[1]
                                        running3 = False
                                        break


                        elif event.type == pygame.MOUSEBUTTONDOWN and n2.text_rect.collidepoint(
                                mpos) and y2.color != yellow:

                            n2.change_color()
                            n2.draw(int(w / 2 - 3 * s), int(h / 8 + 20), s)
                            pygame.display.update()
                            running2 = False
                            running = False
                            time.sleep(1)
                            x_cor = int(turtle.textinput("Starting point X", "Enter the X-coordinate of the starting point"))
                            y_cor = int(
                                turtle.textinput("Starting point Y", "Enter the Y-coordinate of the starting point"))
                            turtle.bye()
                            # Per resuscitare turtle, dato che turtle.bye() killa la finestra
                            turtle.Turtle._screen = None  # force recreation of singleton Screen object
                            turtle.TurtleScreen._RUNNING = True  # only set upon TurtleScreen() definition
                            M_START_POINT.x = x_cor
                            M_START_POINT.y = y_cor


def draw_points(p, m, N):

    s = 20
    font = pygame.font.Font('freesansbold.ttf', 16)

    if p == [] and m == True:
        n_p = 0  # number of point chosen
        running = True
        while running:
            screen.fill(black)
            mpos = pygame.mouse.get_pos()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()
                    break

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                        pygame.quit()
                        sys.exit()
                        break

            while n_p < N:
                screen.fill(black)
                mpos = pygame.mouse.get_pos()
                phrase = f'Choose the points, you have {N-n_p} left'
                text = font.render(phrase, True, white, black)
                rect = text.get_rect()
                rect.center = (int(w/2),int(h/8))
                screen.blit(text,rect)
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        pygame.quit()
                        sys.exit()
                        break

                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            running = False
                            pygame.quit()
                            sys.exit()
                            break
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        x_cor = mpos[0] - int(w/2)
                        y_cor = int(h/2) - mpos[1]
                        p.append(Point(x_cor, y_cor))
                        n_p += 1

            if n_p == N:
                running = False
                break

    screen.fill(black)
    for el in p:
        pygame.draw.circle(screen, red, coordinate_converter(el.x,el.y), 2)
    pygame.draw.circle(screen, violet, coordinate_converter(M_START_POINT.x, M_START_POINT.y), 2)
    global multiplier
    multiplier = float(turtle.textinput("Multiplier", "Enter at what fraction of the distance you want to go to"))
    turtle.bye()
    # Per resuscitare turtle, dato che turtle.bye() killa la finestra
    turtle.Turtle._screen = None  # force recreation of singleton Screen object
    turtle.TurtleScreen._RUNNING = True  # only set upon TurtleScreen() definition
    steps = int(turtle.textinput("steps", "Enter the number of steps"))
    turtle.bye()
    # Per resuscitare turtle, dato che turtle.bye() killa la finestra
    turtle.Turtle._screen = None  # force recreation of singleton Screen object
    turtle.TurtleScreen._RUNNING = True  # only set upon TurtleScreen() definition
    def M_sierpinsky(p, steps):
        TRAVELLING_POINT = Point(M_START_POINT.x, M_START_POINT.y)
        n_points = len(p)
        for i in range(steps):
            n = np.random.randint(0, n_points)
            TRAVELLING_POINT.x += (p[n].x-TRAVELLING_POINT.x) * multiplier
            TRAVELLING_POINT.y += (p[n].y-TRAVELLING_POINT.y) * multiplier
            screen.set_at(coordinate_converter(int(TRAVELLING_POINT.x), int(TRAVELLING_POINT.y)), white)
            pygame.display.update()
        if i == (steps-1):
            print('Done')
    running = True
    M_sierpinsky(p, steps)
    while running:
        mpos = pygame.mouse.get_pos()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
                break

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    pygame.quit()
                    sys.exit()
                    break



music_menu()
n_points = multi_point_menu()

if n_points == 3:
    eq_t,r_sp,h_d = main_menu() #equilateral triangle, random starting point, half distance
    screen.fill(black)
    m_c_t, sp_c, D = menu_2(eq_t,r_sp,h_d) #cliccl for triangle verteces, click for starting point , distance
    choose_with_mouse(m_c_t, sp_c)

    sierpinsky_triangle()

else:
    P, m_c = take_points(n_points) #Points and Mouse Click
    screen.fill(black)
    start_point_menu()
    draw_points(P,m_c, n_points)


pygame.quit()
