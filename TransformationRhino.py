import rhinoscriptsyntax as rs
import ghpythonlib.treehelpers as th


#Define grid points values
pointList = []
gridAmountX = 5
gridAmountY = 5
gridSizeX = 10
gridSizeY = 10

#Define empty Square list and parameters
rectangleList = []
amountSquares = 5
initialSquareSize = 1
squaresOffset = 2

#Generate square of grid

#iterate trough X axis
for x in range(gridAmountX):
    #iterate trough Y axis
    for y in range(gridAmountY):
        tempRectangleList = []
        #iterate for rectangle from each point
        for size in range(initialSquareSize,amountSquares*squaresOffset+initialSquareSize, squaresOffset):
            #Starting Point
            point = rs.CreatePoint(x*gridSizeX, y*gridSizeY, 0)
            #Just to viz
            pointList.append(point)
            #Correct the origin point for each rectangle (It's not domained, it starts from the 0,0)
            translation = rs.XformTranslation([-size/2, -size/2, 0])
            correctedPoint = rs.TransformObject(point, translation, True)
            currentPlane = rs.CreatePlane(correctedPoint, (1,0,0), (0,1,0))
            #Create all te rectangles from each point
            tempRectangleList.append(rs.AddRectangle(currentPlane, size, size))
        #Appends each sets of rectangle to the tree
        rectangleList.append(tempRectangleList)

#Converts the list of list to a GH Tree
offsetRectangle = th.list_to_tree(rectangleList)