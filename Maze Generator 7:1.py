import random
import math
import svgwrite
import sys
from svgwrite import cm, mm   

def create_maze(height,width):
    length = 0
    file = open("Maze.txt","w+")
    for x in range(width):
        for y in range(height):
            if x == 0 and y == 0:
                file.write(str(x+1)+','+str(y+1)+' Visited\n')
            else:
                file.write(str(x+1)+','+str(y+1)+'\n')
    con = open("Maze Connections.txt","w+")
    for x in range(width):
        for y in range(height):
            con.write(str(x+1)+'                 '+str(y+1)+'\n\n\n\n\n')
    file.close()
    x_coord = 1
    y_coord = 1
    done = 'no'
    count = 0
    while count < 1000:
        count = count + 1
        dirc = "not_done"
        file = open("Maze.txt",'r')
        con = open("Maze Connections.txt",'r')
        file_lines = file.readlines()
        con_lines = con.readlines()
        file.close()
        con.close()
        ymax = y_coord == height
        ymin = y_coord == 1
        xmax = x_coord == width
        xmin = x_coord == 1
        if y_coord != 1:
            ymin = False
        if x_coord != width:
            xmax = False
        if x_coord != 1:
            xmin = False
        current_x = x_coord
        current_y = y_coord
        it = 0
        con_count = 0               

        

        #print(con_lines[ (x + 1) * 10 + (y + 1)])
        while dirc != "done" and it < 100:
            it3 = 1
            it = it + 1
            print('it')
            print(it)
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
                print(x_coord)
                print(y_coord)
                print(len(file_lines))
                print(line_in_file + 1)
                upvisit = ("Visited" in file_lines[line_in_file + 1])
            if y_coord != 1:
                downvisit = ("Visited" in file_lines[line_in_file - 1])
            if x_coord != 1:
                leftvisit = ("Visited" in file_lines[line_in_file - width])
            if not xmax:
                rightvisit = ("Visited" in file_lines[line_in_file + width])
            direction = random.randint(1,4)
            '''if upvisit and rightvisit and downvisit and leftvisit:
                print(upvisit)
                print(rightvisit)
                print(downvisit)
                print(leftvisit)
                sys.exit()'''
            print("Visiteds:")
            print(direction)
            print(leftvisit)
            print(rightvisit)
            print(downvisit)
            print(upvisit)
            if direction == 1 and not ymax and not upvisit:
                dirc = "done"
                #print('upvisit')
                print(file_lines[line_in_file])
                print(file_lines[line_in_file + 1])
                print(upvisit)
                y_coord = y_coord + 1
            if direction == 2 and not xmax and not rightvisit:
                dirc = "done"
                #print('rightvisit')
                print(file_lines[line_in_file])
                print(file_lines[line_in_file + width])
                print(rightvisit)
                x_coord = x_coord + 1
            if direction == 3 and not ymin and not downvisit:
                dirc = "done"
                #print('downvisit')
                print(file_lines[line_in_file])
                print(file_lines[line_in_file - 1])
                print(downvisit)
                y_coord = y_coord - 1
            if direction == 4 and not xmin and not leftvisit:
                dirc = "done"
                #print('leftvisit')
                print(file_lines[line_in_file])
                print(file_lines[line_in_file - width])
                print(leftvisit)
                x_coord = x_coord - 1
            if dirc == "done":
                length = length + 1
            
            elif leftvisit and rightvisit and upvisit and downvisit:
                dirdone = False
                print("All Visited")
                print(it3)
                count = 100000
                it = 1000

                if it3 < 20:
                    it3 = it3 + 1
                    print("Backtrack testing")
                    print(x_coord)
                    print(y_coord)
                    x1 = (con_lines[(height * (x_coord - 1) + (y_coord - 1))][:5])
                    y1 = (con_lines[(height * (x_coord - 1) + (y_coord - 1))][-6:])
                    print(con_lines[(height * (x_coord - 1) + (y_coord - 1))][:5])
                    print(x1)
                    print(y1)

                if it3 == 22:
                    it3 = it3 + 100
                    con_count = 0
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
                                        down = True
                                    if y1 < y2:
                                        up = True
                                    if x1 > x2:
                                        right = True
                                    if x1 < x2:
                                        left = True
                        con_count = con_count + 1
                '''it2 = 0
                while dirdone == False and it2 < 5:
                    direction = random.randint(1,4)
                    print(up)
                    print(right)
                    print(down)
                    print(left)
                    if direction == 1 and up == True:
                        #up
                        print("Up")
                        print(up)
                        print(direction)
                        dirdone = True
                        y_coord = y_coord + 1
                    if direction == 2 and right == True:
                        #right
                        print("Right")
                        print(right)
                        print(direction)
                        dirdone = True
                        x_coord = x_coord + 1
                    if direction == 3 and down == True:
                        #down
                        print("Down")
                        print(down)
                        print(direction)
                        dirdone = True
                        y_coord = y_coord - 1
                    if direction == 4 and left == True:
                        #left
                        print("Left")
                        print(left)
                        print(direction)
                        dirdone = True
                        x_coord = x_coord - 1
                    print("Backtracking:") 
                    print(direction)
                    print(dirdone)
                    it2 = it2 + 1'''

                '''if direction == 4:
                    x_coord = x_coord - 1
                if direction == 3:    
                    y_coord = y_coord - 1
                if direction == 2:    
                    x_coord = x_coord + 1
                if direction == 1:    
                    y_coord = y_coord + 1'''

        if not leftvisit or not rightvisit or not upvisit or not downvisit:    
            count = count + 1
            line_number = height * (x_coord - 1) + (y_coord - 1)
            file = open("Maze.txt",'w')
            for line in file_lines:
                if file_lines.index(line) != line_number:
                    file.write(line)
                elif file_lines.index(line) == line_number:
                    file.write(str(x_coord) + ',' + str(y_coord) + ' Visited\n')
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
            print("Diagnostic")
            print(x_coord)
            print(current_x)
            print(y_coord)
            print(current_y)
            for conline in con_lines:
                if con_count == conline_pos_a + cycle_count_a:
                    if conline == '\n':
                        con.write(str(x_coord) + "                       " + str(y_coord) + "\n")
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
    dwg = svgwrite.Drawing('Maze.svg', profile='tiny', size=(int(width)*mm,int(height)*mm))
    con = open("Maze Connections.txt",'r')
    con_lines = con.readlines()
    con_count = 0
    con_count = con_count + 1 
    con_count = 0               
    path_width = 0.2
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
                        dwg.add(dwg.line(((x1+path_width)*mm,(y1-path_width)*mm),((x2+path_width)*mm,(y2+path_width)*mm),stroke_width=0.01*mm,stroke=svgwrite.rgb(10, 10, 16, '%')))
                        dwg.add(dwg.line(((x1-path_width)*mm,(y1-path_width)*mm),((x2-path_width)*mm,(y2+path_width)*mm),stroke_width=0.01*mm,stroke=svgwrite.rgb(10, 10, 16, '%')))
                        down = True
                    if y1 < y2:
                        dwg.add(dwg.line(((x1+path_width)*mm,(y1+path_width)*mm),((x2+path_width)*mm,(y2-path_width)*mm),stroke_width=0.01*mm,stroke=svgwrite.rgb(10, 10, 16, '%')))
                        dwg.add(dwg.line(((x1-path_width)*mm,(y1+path_width)*mm),((x2-path_width)*mm,(y2-path_width)*mm),stroke_width=0.01*mm,stroke=svgwrite.rgb(10, 10, 16, '%')))
                        up = True
                    if x1 > x2:
                        dwg.add(dwg.line(((x1-path_width)*mm,(y1+path_width)*mm),((x2+path_width)*mm,(y2+path_width)*mm),stroke_width=0.01*mm,stroke=svgwrite.rgb(10, 10, 16, '%')))
                        dwg.add(dwg.line(((x1-path_width)*mm,(y1-path_width)*mm),((x2+path_width)*mm,(y2-path_width)*mm),stroke_width=0.01*mm,stroke=svgwrite.rgb(10, 10, 16, '%')))
                        right = True
                    if x1 < x2:
                        dwg.add(dwg.line(((x1+path_width)*mm,(y1+path_width)*mm),((x2-path_width)*mm,(y2+path_width)*mm),stroke_width=0.01*mm,stroke=svgwrite.rgb(10, 10, 16, '%')))
                        dwg.add(dwg.line(((x1+path_width)*mm,(y1-path_width)*mm),((x2-path_width)*mm,(y2-path_width)*mm),stroke_width=0.01*mm,stroke=svgwrite.rgb(10, 10, 16, '%')))
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
    print(length)
        #print(file_lines)
        #print(file_lines)
    #print(con_lines)
'''length = 0
for x in range(20):
    if length < 20:
        create_maze(10,10)'''
create_maze(10,10)