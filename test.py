# uses quads btw (i think thats what they are), pretty sure theres no limit/minimum faces/verts
# also I dont remember what half the variables do im pretty sure I could get rid of faceverts though
# also your faces need to be in order but im pretty sure that's standard
# origin is set to 0, 0, 0 so figure it out if you want to change that
import math
import random

# obj file (remove all empty newlines)
icosahedron_data = """v 0.000000 -0.525731 0.850651
v 0.850651 0.000000 0.525731
v 0.850651 0.000000 -0.525731
v -0.850651 0.000000 -0.525731
v -0.850651 0.000000 0.525731
v -0.525731 0.850651 0.000000
v 0.525731 0.850651 0.000000
v 0.525731 -0.850651 0.000000
v -0.525731 -0.850651 0.000000
v 0.000000 -0.525731 -0.850651
v 0.000000 0.525731 -0.850651
v 0.000000 0.525731 0.850651
vn 0.934172 0.356822 0.000000
vn 0.934172 -0.356822 0.000000
vn -0.934172 0.356822 0.000000
vn -0.934172 -0.356822 0.000000
vn 0.000000 0.934172 0.356822
vn 0.000000 0.934172 -0.356822
vn 0.356822 0.000000 -0.934172
vn -0.356822 0.000000 -0.934172
vn 0.000000 -0.934172 -0.356822
vn 0.000000 -0.934172 0.356822
vn 0.356822 0.000000 0.934172
vn -0.356822 0.000000 0.934172
vn 0.577350 0.577350 -0.577350
vn 0.577350 0.577350 0.577350
vn -0.577350 0.577350 -0.577350
vn -0.577350 0.577350 0.577350
vn 0.577350 -0.577350 -0.577350
vn 0.577350 -0.577350 0.577350
vn -0.577350 -0.577350 -0.577350
vn -0.577350 -0.577350 0.577350
f 2//1 3//1 7//1
f 2//2 8//2 3//2
f 4//3 5//3 6//3
f 5//4 4//4 9//4
f 7//5 6//5 12//5
f 6//6 7//6 11//6
f 10//7 11//7 3//7
f 11//8 10//8 4//8
f 8//9 9//9 10//9
f 9//10 8//10 1//10
f 12//11 1//11 2//11
f 1//12 12//12 5//12
f 7//13 3//13 11//13
f 2//14 7//14 12//14
f 4//15 6//15 11//15
f 6//16 5//16 12//16
f 3//17 8//17 10//17
f 8//18 2//18 1//18
f 4//19 10//19 9//19
f 5//20 9//20 1//20"""

# object file conversion
icosplit = icosahedron_data.splitlines()
icoverts = []
icofaces = []
# get vertices
for i in icosplit:
    if i[0] == 'v' and i[1] != 'n':
        icoverts.append([float([i[2:].split(' ')][0][0]), float([i[2:].split(' ')][0][2]), float([i[2:].split(' ')][0][1])])
    if i[0] == 'f':
        x = 0
        g = 0
        for y in [i[2:].split(' ')]:
            icofaces.append([int(y[0].split('//')[0]), int(y[2].split('//')[0]), int(y[1].split('//')[0])])
print(icofaces)

app.background = 'black'
faceverts = []
newverts = []
adjustedverts = []
offset = [[0, 0], [0, 0], [0, 0]]
cubegroup = [Rect(200, 200, 200, 200)]
baseverts = icoverts
baseverts = [[x * 100 for x in v] for v in baseverts]
tri = icofaces

# Convert triangular faces into quads
faces = []
for i in tri:
    faces.append([i[0], i[1], i[2], i[2]])

focal = 200
def cubeinit():
    global baseverts
    global faces
    global faceverts
    global adjustedverts
    global offset
    global cubegroup
    global focal
    global newverts
    for i in app.group:
        app.group.remove(i)
    faceverts = []
    adjustedverts = []
    # set 0, 0 to center and adjust vert list into only x and y
    x = -1
    for i in baseverts:
        x += 1
    x = -1
    # change adjusted verts to each face
    while x < 5:
        x += 1
        adjustedverts.append([[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]])
        newverts.append([[baseverts[faces[x][0] - 1][0], baseverts[faces[x][0] - 1][1], baseverts[faces[x][0] - 1][2]], [baseverts[faces[x][1] - 1][0], baseverts[faces[x][1] - 1][1], baseverts[faces[x][1] - 1][2]], [baseverts[faces[x][2] - 1][0], baseverts[faces[x][2] - 1][1], baseverts[faces[x][2] - 1][2]], [baseverts[faces[x][3] - 1][0], baseverts[faces[x][3] - 1][1], baseverts[faces[x][3] - 1][2]]])
        faceverts.append([[baseverts[faces[x][0] - 1][0], baseverts[faces[x][0] - 1][1], baseverts[faces[x][0] - 1][2]], [baseverts[faces[x][1] - 1][0], baseverts[faces[x][1] - 1][1], baseverts[faces[x][1] - 1][2]], [baseverts[faces[x][2] - 1][0], baseverts[faces[x][2] - 1][1], baseverts[faces[x][2] - 1][2]], [baseverts[faces[x][3] - 1][0], baseverts[faces[x][3] - 1][1], baseverts[faces[x][3] - 1][2]]])
    x = -1
    # adjust vertices to match perspective
    for i in faceverts:
        c = -1
        x += 1
        for f in faceverts[x]:
            c += 1
            adjustedverts[x][c] = [(focal * (faceverts[x][c][0]/(faceverts[x][c][1] + focal))) + 200, (focal * (faceverts[x][c][2]/(faceverts[x][c][1] + focal))) + 200]
        # print(adjustedverts[x])
        # print(" ")
    c = -1
    # create final shape
    for i in adjustedverts:
        c += 1
        x = Polygon()
        x.pointList = adjustedverts[c]
        cubegroup.append(x)
def cube():
    global baseverts
    global faces
    global faceverts
    global newverts
    global adjustedverts
    global cubegroup
    global focal
    for i in app.group:
        app.group.remove(i)
    adjustedverts = []
    x = -1
    for i in baseverts:
        x += 1
    x = -1
    # change adjusted verts to each face
    while x < 5:
        x += 1
        adjustedverts.append([[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]])
        faceverts = (newverts)
    x = -1
    # adjust vertices to match perspective
    for i in faceverts:
        c = -1
        x += 1
        for f in faceverts[x]:
            c += 1
            adjustedverts[x][c] = [(focal * (faceverts[x][c][0]/(faceverts[x][c][1] + focal))) + 200, (focal * (faceverts[x][c][2]/(faceverts[x][c][1] + focal))) + 200]
        # print(adjustedverts[x])
        # print(" ")
    c = -1
    # create final shape
    # it is possible to make a face a certain color by adding a 5th value (the color as a string) to the face. Be warned, I have not implemented correct layers, so the faces overlap
    for i in adjustedverts:
        c += 1
        x = Polygon(fill = None, borderWidth = 1)
        if len(faces[c]) == 4:
            x.border = 'white'
        else:
            x.border = faces[c][4]
        x.pointList = adjustedverts[c]
        cubegroup.append(x)
    adjustedverts = []
    x = -1
    while x < 5:
        x += 1
        adjustedverts.append([[baseverts[faces[x][0] - 1][0], baseverts[faces[x][0] - 1][1], baseverts[faces[x][0] - 1][2]], [baseverts[faces[x][1] - 1][0], baseverts[faces[x][1] - 1][1], baseverts[faces[x][1] - 1][2]], [baseverts[faces[x][2] - 1][0], baseverts[faces[x][2] - 1][1], baseverts[faces[x][2] - 1][2]], [baseverts[faces[x][3] - 1][0], baseverts[faces[x][3] - 1][1], baseverts[faces[x][3] - 1][2]]])
# rotate around x axis
def rotatex(amountdeg):
    cube()
    global baseverts
    global faces
    global faceverts
    global offset
    global newverts
    global adjustedverts
    global cubegroup
    global focal
    deg = amountdeg * (math.pi/180)
    x = -1
    for i in newverts:
        c = -1
        x += 1
        for f in i:
            c += 1
            newverts[x][c][0] -= offset[0][0]
            newverts[x][c][1] -= offset[1][0]
            newverts[x][c][2] -= offset[2][0]
            xx = newverts[x][c][0]
            zz = newverts[x][c][1]
            yy = newverts[x][c][2]
            newverts[x][c][1] = ((yy * math.sin(deg)) + (zz * math.cos(deg)))
            newverts[x][c][2] = ((yy * math.cos(deg)) - (zz * math.sin(deg)))
            newverts[x][c][0] += offset[0][0]
            newverts[x][c][1] += offset[1][0]
            newverts[x][c][2] += offset[2][0]
    cube()
# rotate around y axis
def rotatey(amountdeg):
    cube()
    global baseverts
    global faces
    global faceverts
    global newverts
    global offset
    global adjustedverts
    global cubegroup
    global focal
    deg = amountdeg * (math.pi/180)
    x = -1
    for i in newverts:
        c = -1
        x += 1
        for f in i:
            c += 1
            newverts[x][c][0] -= offset[0][0]
            newverts[x][c][1] -= offset[1][0]
            newverts[x][c][2] -= offset[2][0]
            xx = newverts[x][c][0]
            zz = newverts[x][c][1]
            yy = newverts[x][c][2]
            newverts[x][c][0] = (((xx * math.cos(deg)) + (zz * math.sin(deg))))
            newverts[x][c][1] = (((-1 * xx) * math.sin(deg)) + (zz * math.cos(deg)))
            newverts[x][c][0] += offset[0][0]
            newverts[x][c][1] += offset[1][0]
            newverts[x][c][2] += offset[2][0]
    cube()
# rotate around z axis
def rotatez(amountdeg):
    cube()
    global baseverts
    global faces
    global offset
    global faceverts
    global newverts
    global adjustedverts
    global cubegroup
    global focal
    deg = amountdeg * (math.pi/180)
    x = -1
    for i in newverts:
        c = -1
        x += 1
        for f in i:
            c += 1
            newverts[x][c][0] -= offset[0][0]
            newverts[x][c][1] -= offset[1][0]
            newverts[x][c][2] -= offset[2][0]
            xx = newverts[x][c][0]
            zz = newverts[x][c][1]
            yy = newverts[x][c][2]
            newverts[x][c][0] = ((xx * math.cos(deg)) - (yy * math.sin(deg)))
            newverts[x][c][2] = ((xx * math.sin(deg)) + (yy * math.cos(deg)))
            newverts[x][c][0] += offset[0][0]
            newverts[x][c][1] += offset[1][0]
            newverts[x][c][2] += offset[2][0]
    cube()
def move(amount, xx, yy, zz):
    global offset
    global newverts
    x = -1
    offset[0][0] += amount * xx
    offset[1][0] += amount * zz
    offset[2][0] -= amount * yy
    for i in newverts:
        c = -1
        x += 1
        for f in i:
            c += 1
            newverts[x][c][0] += amount * xx
            newverts[x][c][1] += amount * zz
            newverts[x][c][2] -= amount * yy
    cube()
def onKeyHold(keys):
    for i in keys:
        if i == 'a':
            move(-5, 1, 0, 0)
        if i == 'd':
            move(5, 1, 0, 0)
        if i == 'w':
            move(5, 0, 0, 1)
        if i == 's':
            move(-5, 0, 0, 1)
        if i == 'space':
            move(5, 0, 1, 0)
        if i == 'c':
            move(-5, 0, 1, 0)
        if i == 'right':
            rotatey(-5)
        if i == 'left':
            rotatey(5)
        if i == 'up':
            rotatex(-5)
        if i == 'down':
            rotatex(5)
app.stepsPerSecond = 30;

# def onStep():
#     rotatez(1)
#     rotatey(1)
#     choice = [-1, 0, 1]
#     move(5, rounded(random.choice(choice)), rounded(random.choice(choice)),rounded(random.choice(choice)))

cubeinit()
# cube

cube()
