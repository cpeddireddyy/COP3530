from tkinter import *
from PIL import Image, ImageTk
import heapq
#must install  pillow, and tkinter

#data to track path and graph to use
currentPath = list()
currentVertexIndex = 0
distLeft = list()
lastVertexIndex = 0
useMinGraph = False

#calls dijkstras then updates currentPath for accessing data
def startNav():
    global minAdjList, adjList, currentPath, lastVertexIndex, currentVertexIndex
    try:
        startpoint = (int)(start_entry.get()) #gets origin
        endpoint = (int)(end_entry.get())  # gets destination
        if startpoint < 0 or endpoint < 0:
            print("Enter Positive Number")
            dist_label["text"] = "---"
            nextstopNode_label["text"] = "---"
            return
        if startpoint > 129163 or endpoint > 129163:
            print("Out of Range")
            dist_label["text"] = "---"
            nextstopNode_label["text"] = "---"
            return
    except:
        print("Bad input")
        dist_label["text"] = "---"
        nextstopNode_label["text"] = "---"
        return
    if startpoint == endpoint:
        dist_label["text"] = "0 miles"
        nextstopNode_label["text"] = "Arrived"
        return
    if(useMinGraph):
        dijkstra(minAdjList, startpoint, endpoint)
    else:
        dijkstra(adjList, startpoint, endpoint)
    currentVertexIndex = 0
    lastVertexIndex = len(currentPath)-1
    if(currentPath[0] == -1):
        dist_label["text"] = "No path"
        nextstopNode_label["text"] = "No path"
    else:
        dist_label["text"] = str(distLeft[currentVertexIndex]) + " mile(s)"
        nextstopNode_label["text"] = currentPath[currentVertexIndex+1]
        print("Node: " + str(currentPath[currentVertexIndex]))
        print("Node: " + str(currentPath[currentVertexIndex+1]))

#used as binary toggle as to use mingraph or regular graph
def toggleMinGraph():
    global useMinGraph, currentPath
    dist_label["text"] = "---"
    nextstopNode_label["text"] = "---"
    currentPath = []
    useMinGraph = not (useMinGraph)
    if (useMinGraph):
        Min_button["text"] = "True"
    else:
        Min_button["text"] = "False"

#when each step function is called, move currentVertexIndex up that many and updated display
def step1():
    global currentPath, currentVertexIndex, lastVertexIndex
    currentVertexIndex = min(currentVertexIndex+1, lastVertexIndex)
    if(currentVertexIndex == lastVertexIndex):
        dist_label["text"] = "0 miles"
        nextstopNode_label["text"] = "Arrived"
    else:
        dist_label["text"] = str(distLeft[currentVertexIndex]) + " mile(s)"
        nextstopNode_label["text"] = str(currentPath[currentVertexIndex+1])
        print("Node: " + str(currentPath[currentVertexIndex+1]))

def step10():
    global currentPath, currentVertexIndex, lastVertexIndex
    currentVertexIndex = min(currentVertexIndex+10, lastVertexIndex)
    if(currentVertexIndex == lastVertexIndex):
        dist_label["text"] = "0 miles"
        nextstopNode_label["text"] = "Arrived"
    else:
        dist_label["text"] = str(distLeft[currentVertexIndex+1]) + " mile(s)"
        nextstopNode_label["text"] = str(currentPath[currentVertexIndex])
        print("Node: " + str(currentPath[currentVertexIndex+1]))

def step100():
    global currentPath, currentVertexIndex, lastVertexIndex  
    currentVertexIndex = min(currentVertexIndex+100, lastVertexIndex)
    if(currentVertexIndex == lastVertexIndex):
        dist_label["text"] = "0 miles"
        nextstopNode_label["text"] = "Arrived"
    else:
        dist_label["text"] = str(distLeft[currentVertexIndex+1]) + " mile(s)"
        nextstopNode_label["text"] = str(currentPath[currentVertexIndex])
        print("Node: " + str(currentPath[currentVertexIndex+1]))

def step1000():
    global currentPath, currentVertexIndex, lastVertexIndex
    currentVertexIndex = min(currentVertexIndex+1000, lastVertexIndex)
    if(currentVertexIndex == lastVertexIndex):
        dist_label["text"] = "0 miles"
        nextstopNode_label["text"] = "Arrived"
    else:
        dist_label["text"] = str(distLeft[currentVertexIndex+1]) + " mile(s)"
        nextstopNode_label["text"] = str(currentPath[currentVertexIndex])
        print("Node: " + str(currentPath[currentVertexIndex+1]))

#makes gui
gui = Tk(className = "iMaps - COP3530 Graph Project---Evan & Chaitra")
gui.geometry("1280x720")
# each label, button, and text entry box left side screen
descript_label = Label(gui, text = "Welcome to iMaps, created by Evan & Chaitra!\nThis navigation app uses a road network of\nthe United States and gives the fastest route\nfrom any two points. Enter a location\n(number 1-129163) to start and end navigation\nthen click \"Start Navigation\". Step through\neach direction using the buttons below.", bg="#e33939", font=("Courier", 16), width = 46, height = 9)
descript_label.place(x=20, y=20)

start_label = Label(gui, text="Origin", bg="#e33939", font=("Courier", 22), width= 16)
start_label.place(x=20, y=240)
end_label = Label(gui, text="Destination", bg="#e33939", font=("Courier", 22), width= 16)
end_label.place(x=340, y=240)

start_entry = Entry(gui, font=("Courier", 26), width= 13)
start_entry.place(x=20, y = 285)
end_entry = Entry(gui, font=("Courier", 26), width= 13)
end_entry.place(x=340, y = 285)

startNav_button = Button(gui, command = startNav, text = "Start Navigation",font=("Courier", 26), bg="#61aaed", width = 28, height = 2)
startNav_button.place(x=20, y=340)
my_label = Label(gui, text = "Step through navigation\n (step size)", bg="#e33939", font=("Courier", 26), width = 28, height = 2)
my_label.place(x=20, y=460)

step1_button = Button(gui, command = step1, text = "  1 step  ",font=("Courier", 20), bg="#61aaed", width = 7, height = 2)
step1_button.place(x=20, y=560)
step10_button = Button(gui, command = step10, text = " 10 step ",font=("Courier", 20), bg="#61aaed", width = 8, height = 2)
step10_button.place(x=150, y=560)
step100_button = Button(gui, command = step100, text = " 100 step ",font=("Courier", 20), bg="#61aaed", width = 9, height = 2)
step100_button.place(x=295, y=560)
step1000_button = Button(gui, command = step1000, text = "1000 step",font=("Courier", 20), bg="#61aaed", width = 9, height = 2)
step1000_button.place(x=455, y=560)

#US map image
basewidth = 650
img = Image.open('map.jpg')
wpercent = (basewidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((basewidth,hsize), Image.ANTIALIAS)
img.save('mapnew.jpg')

canvas = Canvas(gui, width = 800, height= 450)
canvas.place(x=630, y=80)
mapPNG = ImageTk.PhotoImage(file="mapnew.jpg")
canvas.create_image(300, 200, image=mapPNG, anchor="center")

#labels and buttons right side of screen
nextstop_label = Label(gui, text="Next stop: ", bg="#e33939", font=("Courier", 26), width= 16)
nextstop_label.place(x=630, y=20)
distleft_label = Label(gui, text="Distance Left:", bg="#e33939", font=("Courier", 26), width= 16)
distleft_label.place(x=630, y=500)
nextstopNode_label = Label(gui, text="---", bg="#e33939", font=("Courier", 26), width= 12)
nextstopNode_label.place(x=940, y=20)
dist_label = Label(gui, text="---", bg="#e33939", font=("Courier", 26), width= 12)
dist_label.place(x=940, y=500)
bulldoze_label = Label(gui, text="Any road that makes a cycle in the roadnetwork\nis \'unnecessary\' as that means there are two routes\nto get to the same destination. Click to\ntoggle map if all unnecessary roads are\nbulldozed then restart navigation. (Min. spanning tree)", bg="#e33939", font=("Courier", 10), width= 55, height= 5)
bulldoze_label.place(x=630, y=560)
Min_button = Button(gui, command = toggleMinGraph, text ="False" ,font=("Courier", 22), bg="#61aaed", width = 6, height = 2)
Min_button.place(x=1085, y=560)




#parsing data
file = open("road-usroads.mtx", "r")      #using test file
#storing tree (adjacency list bc sparse)
adjList = dict()
edgeList = []
with file:
    for junk in range(15):
        next(file)
    for line in file:           #creates adjacencylist and edgelist for kruskals
        nums = line.split()
        toNode = int(nums[0])
        fromNode = int(nums[1])
        weight = abs(fromNode - toNode)
        #makes edgeList for kruskals
        tempEdgeList = [fromNode, toNode, weight]
        edgeList.append(tempEdgeList)
        #makes adjList for s-t path
        tempList1 = [toNode, weight]
        tempList2 = [fromNode, weight]
        if fromNode not in adjList:
            adjList[fromNode] = []
        if toNode not in adjList:
            adjList[toNode] = []
        adjList[fromNode].append(tempList1)
        adjList[toNode].append(tempList2)
 #making min span tree----------credit to geeksforgeeks.org for explaining union by rank and path compression as a low time complexity for finding and unioning sets
sorted(edgeList, key=lambda edge: edge[2])
minAdjList = dict() #result min spanning graph
setRoots = []    #holds 'parent' of each vertex, when vertex's parent is itself, it is the set's root
heights = []  #holds "height" of each tree
for i in range(len(adjList)+1):
    heights.append(1)
    setRoots.append(i)

def find(vertex):   #determines the set that vertex belongs to
    global setRoots, heights
    if(setRoots[vertex] == vertex):
        return vertex
    setRoots[vertex] = find(setRoots[vertex])
    heights[vertex] = 2
    return setRoots[vertex]

def union(src, dest):   #combines sets by making root of one the root of both
    global setRoots, heights
    srcRoot = find(src)
    destRoot = find(dest)
    if(heights[srcRoot] > heights[destRoot]):
        setRoots[destRoot] = srcRoot
    elif(heights[srcRoot] < heights[destRoot]):
        setRoots[srcRoot] = destRoot
    else:
        setRoots[srcRoot] = destRoot
        heights[destRoot] +=1

index = 0
edgeCount = 0
while(edgeCount < len(adjList)-1 and index < len(edgeList)):  #go through each edge smallest to biggest adding to minAdjList if not making cycle until V-1 are added
    src, dest, weight = edgeList[index]
    index += 1
    if(find(src) != find(dest)): #cycle isnt made so add to minAdjList
        union(src, dest)
        edgeCount += 1
        tempList = [dest, weight]
        tempList2 = [src, weight]
        if src not in minAdjList:
            minAdjList[src] = []
        if dest not in minAdjList:
            minAdjList[dest] = []
        minAdjList[src].append(tempList)
        minAdjList[dest].append(tempList2)
Components = []
for setss in setRoots:
    if find(setss) not in Components:
        Components.append(find(setss))
print("Number of seperate components in road network: " + str(len(Components)))


def dijkstra (adjList, startpoint, endpoint):
    global currentPath, distLeft
    dist = [999999999999] * len(adjList) #hardcoded Infinity value need to change
    dist[startpoint] = 0 #list starts from 1 not 0
    path = {startpoint : 0}
    pred = [-1] * len(adjList)
    pred[startpoint] = startpoint
    reached = False
    while path and not reached:
        currNode = min(path, key = lambda k: path[k])
        del path[currNode]
        for node in adjList[currNode]:
            adjacent = node[0]
            adjLength = node[1]
            #relaxation
            if dist[adjacent] > dist[currNode] + adjLength:
                dist[adjacent] = adjLength + dist[currNode]
                path[adjacent] = dist[adjacent]
                pred[adjacent] = currNode
            if adjacent == endpoint:
                reached = True
                break
    #list of vert from end to start
    currentPath = []
    distLeft = []
    #figure out path

    pathingIndex = endpoint
    currentPath.append(pathingIndex)
    if pred[pathingIndex] != -1:    #only make path if there is a path start to end
        while pathingIndex != startpoint:
            distLeft.append(dist[pathingIndex])
            currentPath.append(pred[pathingIndex])
            pathingIndex = pred[pathingIndex]
        distLeft.append(0)
    else:
        currentPath = [-1]  #case where there is no path, checks for this value in each stepthrough
        distLeft = [999999999999]

#loop for interface to run
gui.mainloop()
