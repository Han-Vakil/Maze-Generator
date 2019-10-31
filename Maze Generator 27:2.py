import random
import math
import svgwrite
import sys
from svgwrite import cm, mm   

def create_maze(height,width):
    path_width = 0.2
    dwg = svgwrite.Drawing('Maze.svg', profile='tiny', size=(int(width)*mm,int(height)*mm))
    length = 0
    Maze = []
    for x in range(width):
        Maze.append([])
        for y in range(height):
            #Maze[x].append(['('+str(y+1)+','+str(x+1)+')'])
            Maze[x].append([])
    #print(Maze)
    file = open("Maze.txt","w+")
    '''for x in range(width):
        for y in range(height):
            if x == 0 and y == 0:
                file.write(str(x+1)+','+str(y+1)+' Visited\n')
            else:
                file.write(str(x+1)+','+str(y+1)+'\n')'''
    con = open("Maze Connections.txt","w+")
    for x in range(width):
        for y in range(height):
            con.write(str(x+1)+'                 '+str(y+1)+'\n\n\n\n\n')
    Connections = []
    for x in range(width):
        Connections.append([])
        for y in range(height):
            Maze[x].append([])
            for n in range(4):
                Maze[x][y].append([])
    for abc in Connections:
        for defg in abc:
            print(defg)
    file.close()
    itcount = 0
    x_coord = 1
    y_coord = 1
    Maze[y_coord - 1][x_coord - 1] = 'Visited'
    done = 'no'
    all_connect = False
    count = 0
    while all_connect == False:
        count = count + 1
        dirc = "not_done"
        #file = open("Maze.txt",'r')
        con = open("Maze Connections.txt",'r')
        #file_lines = file.readlines()
        con_lines = con.readlines()
        file.close()
        con.close()
        ymax = y_coord == height
        ymin = y_coord == 1
        xmax = x_coord == width
        xmin = x_coord == 1
        
        current_x = x_coord
        current_y = y_coord
        it = 0
        con_count = 0               

        

        #print(con_lines[ (x + 1) * 10 + (y + 1)])
        while dirc != "done" and it < 20:
            xmax = x_coord == width
            ymax = y_coord == height
            xmin = x_coord == 1
            ymin = y_coord == 1

            it3 = 1
            it = it + 1
            #print('it')
            #print(it)
            if ymax:
                upvisit = True
            if xmax:
                rightvisit = True
            if x_coord == 1:
                leftvisit = True
            if y_coord == 1:
                downvisit = True
            line_in_file = (x_coord - 1) * height + (y_coord - 1)
            if not ymax:
                '''print(x_coord)
                print(y_coord)
                print(len(file_lines))
                print(line_in_file + 1)'''
                upvisit = Maze[y_coord - 0][x_coord - 1] == 'Visited'
            if y_coord != 1:
                downvisit = Maze[y_coord - 2][x_coord - 1] == 'Visited'
            if x_coord != 1:
                #leftvisit = ("Visited" in file_lines[line_in_file - width])
                leftvisit = Maze[y_coord - 1][x_coord - 2] == 'Visited'
            if not xmax:
                '''print(x_coord)
                print(width)
                print(y_coord)
                print(line_in_file + width)'''
                #rightvisit = ("Visited" in file_lines[line_in_file + width])
                rightvisit = Maze[y_coord - 1][x_coord - 0] == 'Visited'
                
            direction = random.randint(1,4)
            '''if upvisit and rightvisit and downvisit and leftvisit:
                print(upvisit)
                print(rightvisit)
                print(downvisit)
                print(leftvisit)
                sys.exit()'''
            '''print("Visiteds:")
            print(direction)
            print(leftvisit)
            print(rightvisit)
            print(downvisit)
            print(upvisit)'''
            if direction == 1 and not ymax and not upvisit:
                dirc = "done"
                #print('upvisit')
                '''print(file_lines[line_in_file])
                print(file_lines[line_in_file + 1])
                print(upvisit)'''
                current_x = x_coord
                current_y = y_coord
                y_coord = y_coord + 1
                dwg.add(dwg.line(((current_x+path_width)*mm,(current_y+path_width)*mm),((x_coord+path_width)*mm,(y_coord-path_width)*mm),stroke_width=0.01*mm,stroke=svgwrite.rgb(10, 10, 16, '%')))
                dwg.add(dwg.line(((current_x-path_width)*mm,(current_y+path_width)*mm),((x_coord-path_width)*mm,(y_coord-path_width)*mm),stroke_width=0.01*mm,stroke=svgwrite.rgb(10, 10, 16, '%')))
                #dwg.add(dwg.line(((current_x)*mm,(current_y)*mm),((x_coord)*mm,(y_coord)*mm),stroke_width=0.03*mm,stroke=svgwrite.rgb(10, 10, 16, '%')))                
            if direction == 2 and not xmax and not rightvisit:
                dirc = "done"
                #print('rightvisit')
                '''print(file_lines[line_in_file])
                print(file_lines[line_in_file + width])
                print(rightvisit)'''
                current_y = y_coord
                current_x = x_coord
                x_coord = x_coord + 1
                dwg.add(dwg.line(((current_x+path_width)*mm,(current_y+path_width)*mm),((x_coord-path_width)*mm,(y_coord+path_width)*mm),stroke_width=0.01*mm,stroke=svgwrite.rgb(10, 10, 16, '%')))
                dwg.add(dwg.line(((current_x+path_width)*mm,(current_y-path_width)*mm),((x_coord-path_width)*mm,(y_coord-path_width)*mm),stroke_width=0.01*mm,stroke=svgwrite.rgb(10, 10, 16, '%')))
                #dwg.add(dwg.line(((current_x)*mm,(current_y)*mm),((x_coord)*mm,(y_coord)*mm),stroke_width=0.03*mm,stroke=svgwrite.rgb(10, 10, 16, '%')))
            if direction == 3 and not ymin and not downvisit:
                dirc = "done"
                #print('downvisit')
                '''print(file_lines[line_in_file])
                print(file_lines[line_in_file - 1])
                print(downvisit)'''
                current_x = x_coord
                current_y = y_coord
                y_coord = y_coord - 1
                dwg.add(dwg.line(((current_x+path_width)*mm,(current_y-path_width)*mm),((x_coord+path_width)*mm,(y_coord+path_width)*mm),stroke_width=0.01*mm,stroke=svgwrite.rgb(10, 10, 16, '%')))
                dwg.add(dwg.line(((current_x-path_width)*mm,(current_y-path_width)*mm),((x_coord-path_width)*mm,(y_coord+path_width)*mm),stroke_width=0.01*mm,stroke=svgwrite.rgb(10, 10, 16, '%')))
                #dwg.add(dwg.line(((current_x)*mm,(current_y)*mm),((x_coord)*mm,(y_coord)*mm),stroke_width=0.03*mm,stroke=svgwrite.rgb(10, 10, 16, '%')))                
            if direction == 4 and not xmin and not leftvisit:
                dirc = "done"
                #print('leftvisit')
                '''print(file_lines[line_in_file])
                print(file_lines[line_in_file - width])
                print(leftvisit)'''
                current_y = y_coord
                current_x = x_coord
                x_coord = x_coord - 1
                dwg.add(dwg.line(((current_x-path_width)*mm,(current_y+path_width)*mm),((x_coord+path_width)*mm,(y_coord+path_width)*mm),stroke_width=0.01*mm,stroke=svgwrite.rgb(10, 10, 16, '%')))
                dwg.add(dwg.line(((current_x-path_width)*mm,(current_y-path_width)*mm),((x_coord+path_width)*mm,(y_coord-path_width)*mm),stroke_width=0.01*mm,stroke=svgwrite.rgb(10, 10, 16, '%')))
                #dwg.add(dwg.line(((current_x)*mm,(current_y)*mm),((x_coord)*mm,(y_coord)*mm),stroke_width=0.03*mm,stroke=svgwrite.rgb(10, 10, 16, '%')))                
            if dirc == "done":
                length = length + 1
            
            elif leftvisit and rightvisit and upvisit and downvisit:
                dirdone = False
                '''print("All Visited")
                print(it3)'''
                #count = 100000
                #it = 1000

                if it3 < 2000:
                    it4 = 0
                    it3 = it3 + 1
                    up = False
                    down = False
                    right = False
                    left = False
                    '''print("Backtrack testing")
                    print(x_coord)
                    print(y_coord)
                    print(con_lines[5 * (height * (x_coord - 1) + (y_coord - 1))])
                    print(con_lines[5 * (height * (x_coord - 1) + (y_coord - 1))][:5])
                    print(con_lines[5 * (height * (x_coord - 1) + (y_coord - 1))][-6:])'''
                    #Note: Switching n1 and n2 here doesn't help
                    if (con_lines[5 * (height * (x_coord - 1) + (y_coord - 1))]) != '\n':
                        x1 = int(con_lines[5 * (height * (x_coord - 1) + (y_coord - 1))][:5])
                        y1 = int(con_lines[5 * (height * (x_coord - 1) + (y_coord - 1))][-6:])
                        '''print(x_coord)
                        print(y_coord)
                        print(x1)
                        print('\n')'''
                    for n in range(4):
                        if (con_lines[5 * (height * (x_coord - 1) + (y_coord - 1)) + n + 1]) != '\n':
                            #print(con_lines[(height * (x_coord - 1) + (y_coord - 1)) + n][-6:])
                            x2 = int(con_lines[5 * (height * (x_coord - 1) + (y_coord - 1)) + n + 1][:5])
                            y2 = int(con_lines[5 * (height * (x_coord - 1) + (y_coord - 1)) + n + 1][-6:])
                            if y1 > y2:
                                up = True
                            if y1 < y2:
                                down = True
                            if x1 > x2:
                                left = True
                            if x1 < x2:
                                right = True
                    it4 = 0
                    while it4 < 5:
                        #Note: Switching current_n and n_coord does not help
                        #Note: Making n_coord = n_coord + 1 instead of -1 doesn't help (and vice versa)
                        direction = random.randint(1,4)
                        if direction == 1 and up:
                            current_x = x_coord
                            current_y = y_coord
                            y_coord = y_coord - 1
                            itcount = itcount + 1
                            #dwg.add(dwg.line(((current_x)*mm,(current_y)*mm),((x_coord)*mm,(y_coord)*mm),stroke_width=0.03*mm,stroke=svgwrite.rgb(10, 10, 16, '%')))

                            #dwg.add(dwg.circle(center=((x_coord)*mm,(y_coord-10)*mm), r=0.15*mm, stroke='red',fill='red', stroke_width=0.05*mm))
                            it4 = 5
                        elif direction == 2 and right and it4 == 0:
                            current_x = x_coord
                            current_y = y_coord
                            x_coord = x_coord + 1
                            itcount = itcount + 1
                            #dwg.add(dwg.line(((current_x)*mm,(current_y)*mm),((x_coord)*mm,(y_coord)*mm),stroke_width=0.03*mm,stroke=svgwrite.rgb(10, 10, 16, '%')))

                            #dwg.add(dwg.circle(center=((x_coord)*mm,(y_coord)*mm), r=0.15*mm, stroke='red',fill='black', stroke_width=0.05*mm))
                            it4 = 5
                        elif direction == 3 and down and it4 == 0:
                            current_y = y_coord
                            current_x = x_coord
                            y_coord = y_coord + 1
                            itcount = itcount + 1
                            #dwg.add(dwg.line(((current_x)*mm,(current_y)*mm),((x_coord)*mm,(y_coord)*mm),stroke_width=0.03*mm,stroke=svgwrite.rgb(10, 10, 16, '%')))

                            #dwg.add(dwg.circle(center=((x_coord)*mm,(y_coord)*mm), r=0.15*mm, stroke='red',fill='yellow', stroke_width=0.05*mm))
                            it4 = 5
                        elif direction == 4 and left and it4 == 0:
                            current_x = x_coord
                            current_y = y_coord
                            x_coord = x_coord - 1
                            itcount = itcount + 1
                            #dwg.add(dwg.line(((current_x)*mm,(current_y)*mm),((x_coord)*mm,(y_coord)*mm),stroke_width=0.03*mm,stroke=svgwrite.rgb(10, 10, 16, '%')))

                            #dwg.add(dwg.circle(center=((x_coord)*mm,(y_coord)*mm), r=0.15*mm, stroke='red',fill='green', stroke_width=0.05*mm))
                            it4 = 5
                        if it4 == 5:
                            pass
                        
                '''print("COO")
                print(x_coord)
                print(y_coord)'''
                


                '''if direction == 4:
                    x_coord = x_coord - 1
                if direction == 3:    
                    y_coord = y_coord - 1
                if direction == 2:    
                    x_coord = x_coord + 1
                if direction == 1:    
                    y_coord = y_coord + 1'''
        #Note: Makingt the next line have 'or it4 == 5' (to include backtracking) does NOT work 
        if not leftvisit or not rightvisit or not upvisit or not downvisit:    
            count = count + 1
            line_number = height * (x_coord - 1) + (y_coord - 1)
            file = open("Maze.txt",'w')
            '''for line in file_lines:
                if file_lines.index(line) != line_number:
                    file.write(line)
                elif file_lines.index(line) == line_number:
                    file.write(str(x_coord) + ',' + str(y_coord) + ' Visited\n')'''
            #print(y_coord)
            #print(Maze(y_coord))
            Maze[y_coord - 1][x_coord - 1] = 'Visited'
            #print(Maze[y_coord - 1][x_coord - 1])
            con = open("Maze Connections.txt","w")
            edit = False
            conline_pos_a = 5 * (height * (current_x - 1) + (current_y - 1))
            conline_pos_b = 5 * (height * (x_coord - 1) + (y_coord - 1))
            #print(x_coord)
            #print(y_coord)
            #print(conline_pos_b)
            con_count = 0
            cycle_count_a = 1
            cycle_count_b = 1
            '''print("Diagnostic")
            print(x_coord)
            print(current_x)
            print(y_coord)
            print(current_y)'''
            for conline in con_lines:
                if con_count == conline_pos_a + cycle_count_a:
                    if conline == '\n':
                        con.write(str(x_coord) + "                       " + str(y_coord) + "\n")
                        #Note: When y_coord above is replaced with current_y it creates a similar issue to the main bug
                        cycle_count_a = 1
                    elif conline != '\n':
                        con.write(conline)
                        cycle_count_a = cycle_count_a + 1
                elif con_count == conline_pos_b + cycle_count_b:
                    if conline == '\n':
                        con.write(str(current_x) + "                       " + str(current_y) + "\n")
                        cycle_count_b = 1
                    elif conline != '\n':
                        con.write(conline)
                        cycle_count_b = cycle_count_b + 1
                    #con.write("test (" + str(current_x) +"," + str(current_y) + ")\n")
                else:
                    con.write(conline)
                con_count = con_count + 1
        con = open("Maze Connections.txt",'r')
        con_lines = con.readlines()
        con_count = 0
        con_count = con_count + 1 
        con_count = 0
        check_count = 0
        all_connect = True
        for cell in con_lines:
            if check_count % 5 == 0:
                if con_lines[check_count + 1] == '\n':
                    all_connect = False
            check_count = check_count + 1
    con = open("Maze Connections.txt",'r')
    con_lines = con.readlines()
    con_count = 0
    con_count = con_count + 1 
    con_count = 0
    check_count = 0
    all_connect = True
    for item in Maze: 
        for subitem in item:
            if subitem == []:
                all_connect = False

    for cell in con_lines:
        if con_count % 5 == 0:
            up = False
            down = False
            right = False
            left = False
            conn_test = False
            for conn in range(4):
                if con_lines[con_count + conn + 1] != '\n':
                    conn_test = True
                    #print(("First Cell Contents:"))
                    #print(con_lines[con_count + conn + 1])
                    x1 = int(con_lines[con_count + conn + 1][:5])
                    y1 = int(con_lines[con_count + conn + 1][-6:])
                    x2 = int(cell[:5])
                    y2 = int(cell[-6:])
                    if y1 > y2:
                        #dwg.add(dwg.line(((x1+path_width)*mm,(y1-path_width)*mm),((x2+path_width)*mm,(y2+path_width)*mm),stroke_width=0.01*mm,stroke=svgwrite.rgb(10, 10, 16, '%')))
                        #dwg.add(dwg.line(((x1-path_width)*mm,(y1-path_width)*mm),((x2-path_width)*mm,(y2+path_width)*mm),stroke_width=0.01*mm,stroke=svgwrite.rgb(10, 10, 16, '%')))
                        down = True
                    if y1 < y2:
                        #dwg.add(dwg.line(((x1+path_width)*mm,(y1+path_width)*mm),((x2+path_width)*mm,(y2-path_width)*mm),stroke_width=0.01*mm,stroke=svgwrite.rgb(10, 10, 16, '%')))
                        #dwg.add(dwg.line(((x1-path_width)*mm,(y1+path_width)*mm),((x2-path_width)*mm,(y2-path_width)*mm),stroke_width=0.01*mm,stroke=svgwrite.rgb(10, 10, 16, '%')))
                        up = True
                    if x1 > x2:
                        #dwg.add(dwg.line(((x1-path_width)*mm,(y1+path_width)*mm),((x2+path_width)*mm,(y2+path_width)*mm),stroke_width=0.01*mm,stroke=svgwrite.rgb(10, 10, 16, '%')))
                        #dwg.add(dwg.line(((x1-path_width)*mm,(y1-path_width)*mm),((x2+path_width)*mm,(y2-path_width)*mm),stroke_width=0.01*mm,stroke=svgwrite.rgb(10, 10, 16, '%')))
                        right = True
                    if x1 < x2:
                        #dwg.add(dwg.line(((x1+path_width)*mm,(y1+path_width)*mm),((x2-path_width)*mm,(y2+path_width)*mm),stroke_width=0.01*mm,stroke=svgwrite.rgb(10, 10, 16, '%')))
                        #dwg.add(dwg.line(((x1+path_width)*mm,(y1-path_width)*mm),((x2-path_width)*mm,(y2-path_width)*mm),stroke_width=0.01*mm,stroke=svgwrite.rgb(10, 10, 16, '%')))
                        left = True
            if conn_test == True:    
                if not down:
                    dwg.add(dwg.line(((x2+path_width)*mm,(y2+path_width)*mm),((x2-path_width)*mm,(y2+path_width)*mm),stroke_width=0.01*mm,stroke=svgwrite.rgb(10, 10, 16, '%')))
                if not up:
                    dwg.add(dwg.line(((x2+path_width)*mm,(y2-path_width)*mm),((x2-path_width)*mm,(y2-path_width)*mm),stroke_width=0.01*mm,stroke=svgwrite.rgb(10, 10, 16, '%')))
                if not right:
                    dwg.add(dwg.line(((x2+path_width)*mm,(y2+path_width)*mm),((x2+path_width)*mm,(y2-path_width)*mm),stroke_width=0.01*mm,stroke=svgwrite.rgb(10, 10, 16, '%')))
                if not left:
                    dwg.add(dwg.line(((x2-path_width)*mm,(y2+path_width)*mm),((x2-path_width)*mm,(y2-path_width)*mm),stroke_width=0.01*mm,stroke=svgwrite.rgb(10, 10, 16, '%')))

        con_count = con_count + 1
    dwg.save()
    print(Maze)
    print(all_connect)
    #print("itcount")
    #print(itcount)
    #print(length)
        #print(file_lines)
        #print(file_lines)
    #print(con_lines)
'''length = 0
for x in range(20):
    if length < 20:
        create_maze(10,10)'''
create_maze(10,10)