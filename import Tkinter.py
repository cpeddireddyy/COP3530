from tkinter import *
from PIL import Image, ImageTk

#must install pillow and tkinter

nextNode = "---"
distLeft = "---"
useMinTree = False
def startNav():
    #shortest path s-t
    #redisplay path
    startpoint = (int)(start_entry.get()) #gets origin 
    endpoint = (int)(end_entry.get()) #gets destination
    nextNode = startpoint
    distLeft = endpoint - startpoint
    dist_label["text"] = distLeft
    nextstopNode_label["text"] = nextNode
    #calculate shortest path and makes queue to read directions for

def toggleMinTree():
    global useMinTree
    useMinTree = not (useMinTree)
    if (useMinTree):
        Min_button["text"] = "True"
    else:
        Min_button["text"] = "False"

    

def step1():
    print("step 1")
def step10():
    print("step 10")
def step100():
    print("step 100")
def step1000():
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
nextstopNode_label = Label(gui, text=nextNode, bg="#e33939", font=("Courier", 26), width= 12)
nextstopNode_label.place(x=940, y=20)
dist_label = Label(gui, text=distLeft, bg="#e33939", font=("Courier", 26), width= 12)
dist_label.place(x=940, y=500)
bulldoze_label = Label(gui, text="Any road that makes a cycle in the roadnetwork\nis \'unnecessary\' as that means there are two routes\nto get to the same destination. Click to\ntoggle map if all unnecessary roads are\nbulldozed then restart navigation. (Min. spanning tree)", bg="#e33939", font=("Courier", 10), width= 55, height= 5)
bulldoze_label.place(x=630, y=560)
Min_button = Button(gui, command = toggleMinTree, text ="False" ,font=("Courier", 22), bg="#61aaed", width = 6, height = 2)
Min_button.place(x=1085, y=560)




#parsing data
f = open("road-usroads-test.mtx", "r")      #using test file 
#storing tree (adjacency list bc sparse)
#class 
adjList = {}
listNode = []

def newNode (node):
    if node not in listNode:
        listNode.append(node)

def newEdge (toNode, fromNode, weight):
    tempEdge = []
    if toNode in listNode and fromNode in listNode:
        if toNode not in adjList:
            tempEdge.append(fromNode, weight)
            adjList[toNode] = tempEdge
        elif toNode in adjList:
            tempEdge.extend(adjList[toNode])
            tempEdge.append([fromNode, weight])
            adjList[toNode] = tempEdge

with f:
    for junk in range (15):
        next(f)
    for line in f:
        #adding all nodes
        for word in line.split():
            newNode(int(word))


    #adding edges with weight
    tempData = iter(f.read().split())
    while True:
        try:
            toNode = next(tempData)
            fromNode = next(tempData)
            #weight is based on distance
            weight = abs(int(toNode)-int(fromNode))
            newEdge (toNode, fromNode, weight)
        except StopIteration:
            break

#shortest path defined above

#min span tree to make secondary tree for "bulldoze" mode
print(len(adjList))



#run at end of 'main'
gui.mainloop()



