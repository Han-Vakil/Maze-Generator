import random
import math
import svgwrite
import sys
from svgwrite import cm, mm   

def create_maze(width,height):
    path_width = 0.2
    dwg = svgwrite.Drawing('Maze.svg', profile='tiny', size=(int(width)*mm,int(height)*mm))
    length = 0
    Maze = []
    for y in range(height):
        Maze.append([])
        for x in range(width):
            Maze[y].append([])
            Maze[y].append([])
    Connections = []
    for y in range(height):
        Connections.append([])
        for x in range(width):
            Connections[y].append([])
            for n in range(6):
                Connections[y][x].append([])
                Connections[y][x][0] = [x + 1,y + 1]
    for x in Maze:
        print(x)
    for x in Connections:
        print(x)
    itcount = 0
    x_coord = width
    y_coord = height//2 + 1
    Connections[y_coord - 1][x_coord - 1][5] = 'Done'
    Maze[y_coord - 1][x_coord - 1] = 'Visited'
    done = 'no'
    all_connect = False
    count = 0
    while all_connect == False:
        dirc = "not_done"
        ymax = y_coord == height
        ymin = y_coord == 1
        xmax = x_coord == width
        xmin = x_coord == 1
        
        current_x = x_coord
        current_y = y_coord
        it = 0
        con_count = 0
        while dirc != "done" and it < 20:
            xmax = x_coord == width
            ymax = y_coord == height
            xmin = x_coord == 1
            ymin = y_coord == 1

            it3 = 1
            it = it + 1
            if ymax:
                upvisit = True
            if xmax:
                rightvisit = True
            if x_coord == 1:
                leftvisit = True
            if y_coord == 1:
                downvisit = True
            if not ymax:
                upvisit = Maze[y_coord][x_coord - 1] == 'Visited'
            if y_coord != 1:
                downvisit = Maze[y_coord - 2][x_coord - 1] == 'Visited'
            if x_coord != 1:
                leftvisit = Maze[y_coord - 1][x_coord - 2] == 'Visited'
            if not xmax:
                #print(Maze[y_coord - 1])
                #print(y_coord)
                rightvisit = Maze[y_coord - 1][x_coord] == 'Visited'
                
            direction = random.randint(1,4)
            if direction == 1 and not ymax and not upvisit:
                dirc = "done"
                current_x = x_coord
                current_y = y_coord
                y_coord = y_coord + 1
            if direction == 2 and not xmax and not rightvisit:
                dirc = "done"
                current_y = y_coord
                current_x = x_coord
                x_coord = x_coord + 1
            if direction == 3 and not ymin and not downvisit:
                dirc = "done"
                current_x = x_coord
                current_y = y_coord
                y_coord = y_coord - 1
            if direction == 4 and not xmin and not leftvisit:
                dirc = "done"
                current_y = y_coord
                current_x = x_coord
                x_coord = x_coord - 1  
            if dirc == "done":
                length = length + 1
            
            elif leftvisit and rightvisit and upvisit and downvisit:
                dirdone = False
                if it3 < 2000:
                    it4 = 0
                    it3 = it3 + 1
                    right = Connections[y_coord - 1][x_coord - 1][2] == 'East'
                    left = Connections[y_coord - 1][x_coord - 1][4] == 'West'
                    up = Connections[y_coord - 1][x_coord - 1][1] == 'North'
                    down = Connections[y_coord - 1][x_coord - 1][3] == 'South'
                    it4 = 0
                    while it4 < 5:
                        direction = random.randint(1,4)
                        if direction == 1 and up:
                            current_x = x_coord
                            current_y = y_coord
                            y_coord = y_coord - 1
                            itcount = itcount + 1
                            it4 = 5
                        elif direction == 2 and right and it4 == 0:
                            current_x = x_coord
                            current_y = y_coord
                            x_coord = x_coord + 1
                            itcount = itcount + 1
                            it4 = 5
                        elif direction == 3 and down and it4 == 0:
                            current_y = y_coord
                            current_x = x_coord
                            y_coord = y_coord + 1
                            itcount = itcount + 1
                            it4 = 5
                        elif direction == 4 and left and it4 == 0:
                            current_x = x_coord
                            current_y = y_coord
                            x_coord = x_coord - 1
                            itcount = itcount + 1
                            it4 = 5

        if not leftvisit or not rightvisit or not upvisit or not downvisit:    
            count = count + 1
            line_number = height * (x_coord - 1) + (y_coord - 1)
            file = open("Maze.txt",'w')
            Maze[y_coord - 1][x_coord - 1] = 'Visited'

            if current_x == (x_coord - 1):
                Connections[current_y - 1][current_x - 1][2] = 'East'
                Connections[y_coord - 1][x_coord - 1][4] = 'West'
            if current_x - 1 == x_coord:
                Connections[current_y - 1][current_x - 1][4] = 'West'
                Connections[y_coord - 1][x_coord - 1][2] = 'East'
            if current_y - 1 == y_coord:
                Connections[current_y - 1][current_x - 1][1] = 'North'
                Connections[y_coord - 1][x_coord - 1][3] = 'South'
            if current_y + 1 == y_coord:
                Connections[current_y - 1][current_x - 1][3] = 'South'
                Connections[y_coord - 1][x_coord - 1][1] = 'North'
            Connections[y_coord - 1][x_coord - 1][5] = 'Done'
        all_connect = True

        for x in Connections: 
            for y in x:
                if y[5] != 'Done':
                    all_connect = False
        #print(all_connect)

    for abc in Connections:
        for y in abc:
            South = True
            North = True
            East = True
            West = True
            if y[3] != 'South':
                South = False
                dwg.add(dwg.line(((y[0][0]+path_width)*mm,(y[0][1]+path_width)*mm),((y[0][0]-path_width)*mm,(y[0][1]+path_width)*mm),stroke_width=0.01*mm,stroke=svgwrite.rgb(10, 10, 16, '%')))  
            if y[1] != 'North':
                North = False
                dwg.add(dwg.line(((y[0][0]+path_width)*mm,(y[0][1]-path_width)*mm),((y[0][0]-path_width)*mm,(y[0][1]-path_width)*mm),stroke_width=0.01*mm,stroke=svgwrite.rgb(10, 10, 16, '%')))
            if y[4] != 'West':
                West = False
                dwg.add(dwg.line(((y[0][0]-path_width)*mm,(y[0][1]+path_width)*mm),((y[0][0]-path_width)*mm,(y[0][1]-path_width)*mm),stroke_width=0.01*mm,stroke=svgwrite.rgb(10, 10, 16, '%')))
            if y[2] != 'East':
                East = False
                dwg.add(dwg.line(((y[0][0]+path_width)*mm,(y[0][1]+path_width)*mm),((y[0][0]+path_width)*mm,(y[0][1]-path_width)*mm),stroke_width=0.01*mm,stroke=svgwrite.rgb(10, 10, 16, '%')))
            if North:
                dwg.add(dwg.line(((y[0][0]+path_width)*mm,(y[0][1]-path_width)*mm),((y[0][0]+path_width)*mm,(y[0][1]-1+path_width)*mm),stroke_width=0.01*mm,stroke=svgwrite.rgb(10, 10, 16, '%')))
                dwg.add(dwg.line(((y[0][0]-path_width)*mm,(y[0][1]-path_width)*mm),((y[0][0]-path_width)*mm,(y[0][1]-1+path_width)*mm),stroke_width=0.01*mm,stroke=svgwrite.rgb(10, 10, 16, '%')))
            if East:
                dwg.add(dwg.line(((y[0][0]+path_width)*mm,(y[0][1]+path_width)*mm),((y[0][0]+1-path_width)*mm,(y[0][1]+path_width)*mm),stroke_width=0.01*mm,stroke=svgwrite.rgb(10, 10, 16, '%')))
                dwg.add(dwg.line(((y[0][0]+path_width)*mm,(y[0][1]-path_width)*mm),((y[0][0]+1-path_width)*mm,(y[0][1]-path_width)*mm),stroke_width=0.01*mm,stroke=svgwrite.rgb(10, 10, 16, '%')))
    dwg.save()
    

create_maze(21,7)