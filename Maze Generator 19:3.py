import random
import math
import svgwrite
import sys
from svgwrite import cm, mm
import PIL
from PIL import Image   

def create_maze(width,height,coefficient,path_width,mat_thickness,tool_depth,image):
    if image != 'none':
        im = Image
    g_count = 0
    g_list = []
    dwg = svgwrite.Drawing('Maze.svg', profile='tiny', size=(int(width)*(int(coefficient)+0.5)*mm,int(height)*(int(coefficient)+0.5)*mm))
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
            for n in range(7):
                Connections[y][x].append([])
            Connections[y][x][0] = [x + 1,y + 1]
    
    path_list = []
    '''for x in Maze:
        print(x)
    for x in Connections:
        print(x)'''
    itcount = 0
    #x_coord = width
    #y_coord = height//2 + 1
    x_start = 5
    y_start = 5
    x_coord = x_start
    y_coord = y_start
    Connections[y_coord - 1][x_coord - 1][5] = 'Done'
    Maze[y_coord - 1][x_coord - 1] = 'Visited'
    done = 'no'
    all_connect = False
    count = 0
    while all_connect == False:
        count = count + 1
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
                
            direction = random.randint(1,5)
            if direction == 1 and not ymax and not upvisit:
                dirc = "done"
                current_x = x_coord
                current_y = y_coord
                y_coord = y_coord + 1
                path_list.append([[current_x * coefficient,current_y * coefficient],[x_coord * coefficient,y_coord * coefficient],[g_count]])
                g_count = g_count + 1
                #g_list.append('G01 Y' + str(y_coord*coefficient))
            if direction == 2 and not xmax and not rightvisit:
                dirc = "done"
                current_y = y_coord
                current_x = x_coord
                x_coord = x_coord + 1
                path_list.append([[current_x * coefficient,current_y * coefficient],[x_coord * coefficient,y_coord * coefficient],[g_count]])
                g_count = g_count + 1
                #g_list.append('G01 X' + str(x_coord*coefficient))
            if direction == 3 and not ymin and not downvisit:
                dirc = "done"
                current_x = x_coord
                current_y = y_coord
                y_coord = y_coord - 1
                path_list.append([[current_x * coefficient,current_y * coefficient],[x_coord * coefficient,y_coord * coefficient],[g_count]])
                g_count = g_count + 1
                #g_list.append('G01 Y' + str(y_coord*coefficient))
            if direction == 4 and not xmin and not leftvisit:
                dirc = "done"
                current_y = y_coord
                current_x = x_coord
                x_coord = x_coord - 1  
                path_list.append([[current_x * coefficient,current_y * coefficient],[x_coord * coefficient,y_coord * coefficient],[g_count]])
                g_count = g_count + 1
                #g_list.append('G01 X' + str(x_coord*coefficient))
            if dirc == 'Done':
                if g_list[-1] == ['G01 Z5']:
                    pass

            
            elif leftvisit and rightvisit and upvisit and downvisit:
                #g_list.append('G01 Z5')
                dirdone = False
                if it3 < 2000:
                    it4 = 0
                    it3 = it3 + 1

                    right = Connections[y_coord - 1][x_coord - 1][2] == 'East'
                    left = Connections[y_coord - 1][x_coord - 1][4] == 'West'
                    up = Connections[y_coord - 1][x_coord - 1][1] == 'North'
                    down = Connections[y_coord - 1][x_coord - 1][3] == 'South'

                    xmax = x_coord == width
                    ymax = y_coord == height
                    xmin = x_coord == 1
                    ymin = y_coord == 1
                    if ymax:
                        upsecond = True
                    if xmax:
                        rightsecond = True
                    if x_coord == 1:
                        leftsecond = True
                    if y_coord == 1:
                        downsecond = True

                    if not ymin:
                        upsecond = Connections[y_coord - 2][x_coord - 1][6] == 'Seconded'
                    if not ymax:
                        downsecond = Connections[y_coord - 0][x_coord - 1][6] == 'Seconded'
                    if not xmin:
                        leftsecond = Connections[y_coord - 1][x_coord - 2][6] == 'Seconded'
                    if not xmax:
                        rightsecond = Connections[y_coord - 1][x_coord - 0][6] == 'Seconded'


                    it4 = 0
                    while it4 < 5:
                        direction = random.randint(1,4)
                        if direction == 1 and up and not upsecond:
                            current_x = x_coord
                            current_y = y_coord
                            Connections[y_coord - 1][x_coord - 1][6] = 'Seconded'
                            y_coord = y_coord - 1
                            itcount = itcount + 1
                            it4 = 5
                        elif direction == 2 and right and it4 == 0 and not rightsecond:
                            current_x = x_coord
                            current_y = y_coord
                            Connections[y_coord - 1][x_coord - 1][6] = 'Seconded'
                            x_coord = x_coord + 1
                            itcount = itcount + 1
                            it4 = 5
                        elif direction == 3 and down and it4 == 0 and not downsecond:
                            current_y = y_coord
                            current_x = x_coord
                            Connections[y_coord - 1][x_coord - 1][6] = 'Seconded'
                            y_coord = y_coord + 1
                            itcount = itcount + 1
                            it4 = 5
                        elif direction == 4 and left and it4 == 0 and not leftsecond:
                            current_x = x_coord
                            current_y = y_coord
                            Connections[y_coord - 1][x_coord - 1][6] = 'Seconded'
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
                        

    y = path_list[0][1]
    g_list.append('G90')
    g_list.append('G0 G53 Z0')
    g_list.append('')
    g_list.append('(Pocket1)')
    g_list.append('T1 M6 (flat end mill D=3.175)')
    g_list.append('S16000 M3')
    g_list.append('F600')
    g_list.append('G64')
    g_list.append('G54')
    g_list.append('G43 H1')
    g_list.append('')


    g_list.append('G0 Z15')
    g_list.append('G0 X' + str(coefficient * x_start) + ' Y' + str(coefficient * y_start))
    g_list.append('G1 Z-4')
    g_list.append('')
    
    for x in path_list:
        if x[2] != ['a']:
            #print('test')
            #print(x[0])
            #print(y)
            if x[0] == y or x[2] == [0]:
                #print('Same:')
                #print(y)
                #print(x[0])
                g_list.append('G1 X' + str(x[1][0]) + ' Y' + str(x[1][1]))
            elif x[0] != y:
                g_list.append('G0 Z15')
                g_list.append('G0 X' + str(x[0][0]) + ' Y' + str(x[0][1]))
                g_list.append('G1 Z-4')
                g_list.append('G1 X' + str(x[1][0]) + ' Y' + str(x[1][1]))
            y = x[1]

    passes = mat_thickness/tool_depth


    g_list.append('G1 Z15')
    g_list.append('M9')
    g_list.append('M5')
    g_list.append('G53 Z0.')
    g_list.append('M30')    





                
    g_file = open("GMazeTest.txt","w+")
    for x in g_list:
        g_file.write(x)
        g_file.write('\n')
        #print(x)
    #print(passes)   


        #print(g_list)
        #print(all_connect)
    for abc in Connections:
        for y in abc:
            South = True
            North = True
            East = True
            West = True
            if y[3] != 'South':
                South = False
                dwg.add(dwg.line(((y[0][0]+path_width)*int(coefficient)*mm,(y[0][1]+path_width)*int(coefficient)*mm),((y[0][0]-path_width)*int(coefficient)*mm,(y[0][1]+path_width)*int(coefficient)*mm),stroke_width=0.01*int(coefficient)*mm,stroke=svgwrite.rgb(10, 10, 16, '%')))  
            if y[1] != 'North':
                North = False
                dwg.add(dwg.line(((y[0][0]+path_width)*int(coefficient)*mm,(y[0][1]-path_width)*int(coefficient)*mm),((y[0][0]-path_width)*int(coefficient)*mm,(y[0][1]-path_width)*int(coefficient)*mm),stroke_width=0.01*int(coefficient)*mm,stroke=svgwrite.rgb(10, 10, 16, '%')))
            if y[4] != 'West':
                West = False
                dwg.add(dwg.line(((y[0][0]-path_width)*int(coefficient)*mm,(y[0][1]+path_width)*int(coefficient)*mm),((y[0][0]-path_width)*int(coefficient)*mm,(y[0][1]-path_width)*int(coefficient)*mm),stroke_width=0.01*int(coefficient)*mm,stroke=svgwrite.rgb(10, 10, 16, '%')))
            if y[2] != 'East':
                East = False
                dwg.add(dwg.line(((y[0][0]+path_width)*int(coefficient)*mm,(y[0][1]+path_width)*int(coefficient)*mm),((y[0][0]+path_width)*int(coefficient)*mm,(y[0][1]-path_width)*int(coefficient)*mm),stroke_width=0.01*int(coefficient)*mm,stroke=svgwrite.rgb(10, 10, 16, '%')))
            if North:
                dwg.add(dwg.line(((y[0][0]+path_width)*int(coefficient)*mm,(y[0][1]-path_width)*int(coefficient)*mm),((y[0][0]+path_width)*int(coefficient)*mm,(y[0][1]-1+path_width)*int(coefficient)*mm),stroke_width=0.01*int(coefficient)*mm,stroke=svgwrite.rgb(10, 10, 16, '%')))
                dwg.add(dwg.line(((y[0][0]-path_width)*int(coefficient)*mm,(y[0][1]-path_width)*int(coefficient)*mm),((y[0][0]-path_width)*int(coefficient)*mm,(y[0][1]-1+path_width)*int(coefficient)*mm),stroke_width=0.01*int(coefficient)*mm,stroke=svgwrite.rgb(10, 10, 16, '%')))
            if East:
                dwg.add(dwg.line(((y[0][0]+path_width)*int(coefficient)*mm,(y[0][1]+path_width)*int(coefficient)*mm),((y[0][0]+1-path_width)*int(coefficient)*mm,(y[0][1]+path_width)*int(coefficient)*mm),stroke_width=0.01*int(coefficient)*mm,stroke=svgwrite.rgb(10, 10, 16, '%')))
                dwg.add(dwg.line(((y[0][0]+path_width)*int(coefficient)*mm,(y[0][1]-path_width)*int(coefficient)*mm),((y[0][0]+1-path_width)*int(coefficient)*mm,(y[0][1]-path_width)*int(coefficient)*mm),stroke_width=0.01*int(coefficient)*mm,stroke=svgwrite.rgb(10, 10, 16, '%')))
        
    dwg.save()
    for y in Connections:
        for x in y:
            #print(x)
            pass
    for x in g_list:
        #print(x)
        pass
    

create_maze(20,20,1,0.25,22.5,4,'none')


