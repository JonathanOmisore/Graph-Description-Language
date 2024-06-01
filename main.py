from GraphDLInterpreter import GraphDLInterpreter
interpreter = GraphDLInterpreter()
commands = [
    "create graph myGraph",
    "add vertex A to myGraph",
    "add vertex B to myGraph",
    "add vertex C to myGraph",
    "add edge A to B in myGraph",
    "add edge B to C in myGraph",
    "neighbors of A in myGraph",
    "is connected A to C in myGraph",
    "is empty myGraph",
    "degree of B in myGraph",
    "all vertices in myGraph"
]

for command in commands:
    interpreter.execute(command)
