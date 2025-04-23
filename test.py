import math
import random
app.background = 'black'
baseverts = [[-50, 50, -50], [50, 50, -50], [50, 50, 50], [-50, 50, 50], [-50, -50, -50], [50, -50, -50], [50, -50, 50], [-50, -50, 50]]
faces = [[1, 2, 3, 4], [1, 2, 6, 5], [1, 4, 8, 5], [3, 4, 8, 7], [5, 6, 7, 8], [2, 3, 7, 6]]
faceverts = []
newverts = []
adjustedverts = []
rotation = [0, 0, 1]
cubegroup = [Rect(200, 200, 200, 200)]

focal = 200
def cubeinit():
    global baseverts
    global faces
    global faceverts
    global adjustedverts
    global rotation
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
    for i in faces:
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
    for i in faces:
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
    for i in adjustedverts:
        c += 1
        x = Polygon(fill = None, border = 'white', borderWidth = 5)
        x.pointList = adjustedverts[c]
        cubegroup.append(x)
    adjustedverts = []
    x = -1
    for i in faces:
        x += 1
        adjustedverts.append([[baseverts[faces[x][0] - 1][0], baseverts[faces[x][0] - 1][1], baseverts[faces[x][0] - 1][2]], [baseverts[faces[x][1] - 1][0], baseverts[faces[x][1] - 1][1], baseverts[faces[x][1] - 1][2]], [baseverts[faces[x][2] - 1][0], baseverts[faces[x][2] - 1][1], baseverts[faces[x][2] - 1][2]], [baseverts[faces[x][3] - 1][0], baseverts[faces[x][3] - 1][1], baseverts[faces[x][3] - 1][2]]])
# rotate around x axis
def rotatex(amountdeg):
    cube()
    global baseverts
    global faces
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
            xx = newverts[x][c][0]
            zz = newverts[x][c][1]
            yy = newverts[x][c][2]
            newverts[x][c][1] = ((yy * math.cos(deg)) - (zz * math.sin(deg)))
            newverts[x][c][2] = ((yy * math.sin(deg)) + (zz * math.cos(deg)))
            
    cube()
# rotate around y axis
def rotatey(amountdeg):
    cube()
    global baseverts
    global faces
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
            xx = newverts[x][c][0]
            zz = newverts[x][c][1]
            yy = newverts[x][c][2]
            newverts[x][c][0] = (((xx * math.cos(deg)) + (zz * math.sin(deg))))
            newverts[x][c][1] = (((-1 * xx) * math.sin(deg)) + (zz * math.cos(deg)))
            
    cube()
# rotate around z axis
def rotatez(amountdeg):
    cube()
    global baseverts
    global faces
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
            xx = newverts[x][c][0]
            zz = newverts[x][c][1]
            yy = newverts[x][c][2]
            newverts[x][c][0] = ((xx * math.cos(deg)) - (yy * math.sin(deg)))
            newverts[x][c][2] = ((xx * math.sin(deg)) + (yy * math.cos(deg)))
    cube()
def move(amount, xx, yy, zz):
    x = -1
    for i in newverts:
        c = -1
        x += 1
        for f in newverts[x]:
            c += 1
            newverts[x][c][0] += amount * xx
            newverts[x][c][1] += amount * zz
            newverts[x][c][2] += (-1 * amount) * yy
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
            rotatez(5)
        if i == 'down':
            rotatez(-5)

app.stepsPerSecond = 30;
# def onStep():
#     rotatez(1)
#     rotatey(1)
#     choice = [-1, 0, 1]
#     move(5, rounded(random.choice(choice)), rounded(random.choice(choice)),rounded(random.choice(choice)))
cubeinit()
cube()
