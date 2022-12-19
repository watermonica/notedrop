import turtle
import random
#import numpy as np

node_array = []*20

class Node:
    def __init__(self):
        self.graph()
        self.start_node()
        self.end_node()
        self.map()

    def graph(self):
        self.root = turtle.Screen()
        self.root.title = "nodes"
        self.root.setup(width=600,height=600)
        self.root.bgcolor('black')
        self.root.tracer(0)

    def start_node(self):
        self.node = turtle.Turtle()
        self.node.shape('circle')
        self.node.color('green')
        self.node.penup()
        self.node.goto(-250,250)
        node_coords = (self.node.xcor(), self.node.ycor())
        node_array.append(node_coords)

    def node(self):
        #create the node
        self.node = turtle.Turtle()
        self.node.shape('circle')
        self.node.color('white')
        self.node.penup()
        self.node.goto(random.randint(-225,225),random.randint(-225,225))

        node_coords = (self.node.xcor(), self.node.ycor())
        node_array.append(node_coords)
    
    def end_node(self):
        self.node = turtle.Turtle()
        self.node.shape('circle')
        self.node.color('red')
        self.node.penup()
        self.node.goto(250,-250)
        node_coords = (self.node.xcor(), self.node.ycor())
        node_array.append(node_coords)

    def line(self):
        self.line = turtle.Turtle()
        self.line.hideturtle()
        self.line.color('blue')
        self.line.penup()

    def map(self):
        _nodecount = 0
        line = Node.line(self)
        node_array.pop(1)
        
        while _nodecount < 4:
            Node.node(self)
            self.line.goto(node_array[_nodecount])
            self.line.pendown()
            self.root.update()
            _nodecount += 1
            

        Node.end_node(self)
        self.line.goto(node_array[-1])
        self.root.update()

        self.root.mainloop()
        for i in node_array:
            print(i)

 
def main():
    Node()

if __name__ == '__main__':
    main()