import sys
from tkinter import *
from PIL import Image, ImageTk
import heapq

#must install  pillow, and tkinter


currentPath = []
currentVertex = 0
distLeft = 0
lastVertex = 0
useMinGraph = False

#calls dijkstras then updates currentPath for accessing data
def startNav():
    global minAdjList, adjList, currentPath
    try:
        startpoint = (int)(start_entry.get()) #gets origin
        endpoint = (int)(end_entry.get()) #gets destination
    except:
        print("Bad input")
        dist_label["text"] = "---"
        nextstopNode_label["text"] = "---"
        return
    if(useMinGraph):
        currentPath = dijkstra(minAdjList, startpoint)
    else:
        curentPath = dijkstra(minAdjList, startpoint)
    currentVertex = 0
    lastVertex = len(curentPath)-1
    dist_label["text"] = str(distLeft)
    nextstopNode_label["text"] = currentPath[1]

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

#when each step function is called, move currentVertex up that many and updated display
def step1():
    global currentPath, currentVertex, lastVertex
    currentVertex = max(currentVertex+1, lastVertex)
    if(currentVertex == lastVertex):
        dist_label["text"] = "0 miles"
        nextstopNode_label["text"] = "Destination Reached"
    else:
        dist_label["text"] = distLeft
        nextstopNode_label["text"] = currentPath[currentVertex]
    print("step 1")
def step10():
    global currentPath, currentVertex, lastVertex
    currentVertex = max(currentVertex+10, lastVertex)
    if(currentVertex == lastVertex):
        dist_label["text"] = "0 miles"
        nextstopNode_label["text"] = "Destination Reached"
    else:
        dist_label["text"] = distLeft
        nextstopNode_label["text"] = currentPath[currentVertex]
    print("step 10")
def step100():
    global currentPath, currentVertex, lastVertex
    currentVertex = max(currentVertex+100, lastVertex)
    if(currentVertex == lastVertex):
        dist_label["text"] = "0 miles"
        nextstopNode_label["text"] = "Destination Reached"
    else:
        dist_label["text"] = distLeft
        nextstopNode_label["text"] = currentPath[currentVertex]
    print("step 100")
def step1000():
    global currentPath, currentVertex, lastVertex
    currentVertex = max(currentVertex+1000, lastVertex)
    if(currentVertex == lastVertex):
        dist_label["text"] = "0 miles"
        nextstopNode_label["text"] = "Destination Reached"
    else:
        dist_label["text"] = distLeft
        nextstopNode_label["text"] = currentPath[currentVertex]
    print("step 1000")

#makes window
gui = Tk(className = "iMaps - COP3530 Graph Project---Evan & Chaitra")
gui.geometry("1280x720")
# each label, button, and text entry box left side screen
descript_label = Label(gui, text = "Welcome to iMaps created by Evan & Chaitra!\nThis navigation app uses a road network of\nthe United States and gives the fastest route\nfrom any two points. Enter a location\n(number 1-129163) to start and end navigation\nthen click \"Start Navigation\". Step through\neach direction using the buttons below.", bg="#e33939", font=("Courier", 16), width = 46, height = 9)
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
#class
adjList = dict()
edgeList = []
with file:
    for junk in range(15):
        next(file)
    for line in file:
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
print(len(adjList))
 #making min span tree
sorted(edgeList, key=lambda edge: edge[2])
#credit to geeksforgeeks.org for explaining union by rank and path compression as a low time complexity for finding and unioning sets
minAdjList = dict() #result graph
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
        if src not in minAdjList:
            minAdjList[src] = []
        if dest not in minAdjList:
            minAdjList[dest] = []
        minAdjList[src].append(tempList)

def dijkstra (adjList, startpoint):

    dist = [999999999999] * len(adjList) #hardcoded Infinity value need to change
    dist[startpoint - 1] = 0 #list starts from 1 not 0
    path = {startpoint : 0}
    dijMatrix = dict()
    while path:
        currNode = min(path, key = lambda k: path[k])
        del path[currNode]
        for node in adjList[currNode]:
            adjacent = node[0]
            adjLength = node[1]
            #relaxation
            if dist[adjacent - 1] > dist[currNode - 1] + adjLength:
                dist[adjacent - 1] = dist[currNode - 1] + adjLength
                path[adjacent] = dist[adjacent - 1]
    dist = currentPath #updates currentpath w/ verts

#shortest path defined above

#min span tree to make secondary tree for "bulldoze" mode
print(len(adjList))
print(len(minAdjList))



#run at end of 'main'
gui.mainloop()
