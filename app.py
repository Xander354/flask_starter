import flask
from game import Game

#games
vsl = {
  "name": "VirtuaSlayer",
  "description": "VirtuaSlayer is a first person shooter game made in a custom 2D game engine that takes place in the glitchy world of the users computer as they fight viruses from too many downloads.",
  "video": "https://drive.google.com/file/d/0B4_dbFq47deYYnl1alNNV2NlMzQ/preview",
  "snippets": [
    [ "Recursive Sector Render Deque", "\/*Que Sectors in order to be rendered. Starts by checking if a sector has a portal to another sector in view, \n  and then recursivley checks sectors in view \n  Parameters:\n    que: deque to use to store sectors in rendering order, start: the sector to start looking in\n    sectNum: The number of the starting sector, LastSect: The last sector checked (used in recursion)\n    Qued: pointer to number of sectors qued. *\/\nvoid QueSectors(std::deque<Sector> *que, Sector start, int SectNum, int LastSect, int *Qued)\n{\n  \/\/Go through each vertex in the sector\n\tfor (int i = 0; i < start.numverticies; ++i)\n\t{\n\t\tif (start.portal[i])\n      \/\/If the located portal does not lead back to the previous sector\n\t\t\tif (!(start.portalSects[i].x == LastSect || start.portalSects[i].y == LastSect))\n\t\t\t{\n        \/\/If the portal is visible\n\t\t\t\tif ((InFov(start.vertices[i]) || InFov(start.vertices[i + 1])\n\t\t\t\t\t|| FovBetweenPoints(start.vertices[i], start.vertices[i + 1]))\n\t\t\t\t\t&& !(NoIntersectWithWallinSector(start.vertices[i], SectNum)\n\t\t\t\t\t\t&& NoIntersectWithWallinSector(start.vertices[i + 1], SectNum)))\n\t\t\t\t{\n          \/\/Check where the portal leads and update the deque\n\t\t\t\t\tint sec1 = (int)start.portalSects[i].x, sec2 = (int)start.portalSects[i].y, nextSect;\n\t\t\t\t\tif (SectNum == sec1)\n\t\t\t\t\t{\n\t\t\t\t\t\tque->push_back(sectors[sec2]);\n\t\t\t\t\t\tnextSect = sec2;\n\t\t\t\t\t}\n\t\t\t\t\telse\n\t\t\t\t\t{\n\t\t\t\t\t\tque->push_back(sectors[sec1]);\n\t\t\t\t\t\tnextSect = sec1;\n\t\t\t\t\t}\n\t\t\t\t\t++*Qued;\n          \/\/If the next sector leads somewhere\n\t\t\t\t\tif (sectors[nextSect].numportals > 1)\n\t\t\t\t\t\tQueSectors(que, sectors[nextSect], nextSect, SectNum, Qued);\n\t\t\t\t}\n\t\t\t}\n\t}\n}", "This code was used to recursivley add each sector (room) to the rendering que in the correct order. The actual map data is a list of 2D points made in a top down perspective. After being translated to 3D planes, this function orders them from the perspective of the player" ],
    [ "MapData", "vsverts.png", "This is a visual representation of how the map data is stored in the level files" ],
    [ "Variadic Template Component Function", "\/\/Attatch any component type\ntemplate <typename T>\ninline void AttatchComponent(T* component)\n{\n\tcomponents.AttatchComponent(component);\n}\n\nGameObject::GameObject(const char* name, const int numOfComponents, Component components, ...)\n{\n\tva_list comps;\n\tva_start(comps, components);\n\n\t\/\/va_start creats the list following the initial parameter, so this one\n\t\/\/needs to be added first\n\tAttatchComponent(new Component(components));\n\n\tfor (int i = 1; i < numOfComponents; ++i)\n\t{\n\t\tComponent comp = va_arg(comps, Component);\n\t\tAttatchComponent(new Component(comp));\n\t}\n\n\tva_end(comps);\n}", "This function allowed for dynamically adding components to an object by accepting any component of any type, and as many as needed by using a variadic templated function" ]
  ],
  "img": "menu.png"
}

#web projects
maze = {
  "name": "Maze Creator and Solver",
  "description": "This project was made to practice perform Depth-First vs Bredth-First searching. When the page loads, it creates a maze and begins searching for the best way out.",
  "video": "/static/web/maze.html",
  "snippets": [["View Source", "var canvas = document.getElementById(\"mycanvas\");\n  var ctx = canvas.getContext(\"2d\");\n  \/\/ used to store 2-Dimensional array of points\n  var pts = [];\n  \/\/ used to store all the paths\n  var paths = [];\n  \/\/ array which acts as a stack for the DFS algorithm\n  var ptStack = [];\n  \/\/ array which acts as a stack for the BFS algorithm\n  var solveQueue = [];\n  \/\/ variable to set the size of the grid\n  var gridSize = 60;\n\n  var start = null;\n  var goal = null;\n\n  initialize();\n  \/\/ an interval is used to visualize the BFS algorithm's thinking\n  var solve = setInterval(bfsSolve, 50);\n\n  \/\/Constructor for a point object\n  function Point(x, y) {\n    \/\/ x and y coordinates for drawing the point on the canvas\n    this.drawX = (x + 1) * 10;\n    this.drawY = (y + 1) * 10;\n    \/**\n     * variable to indicate if a point has been visited\n     * this is necessary to ensure that the maze does not\n     * contain any loops, and that every point is traversed\n     *\/\n    this.dfsVisited = false;\n    this.bfsVisited = false;\n    this.neighbors = [];\n    this.paths = [];\n    \/\/ stores the parent in relation to the BFS traversal\n    this.parent = null;\n\n    \/\/draw the point, used to animate the maze drawing\n    this.draw = function () {\n      ctx.beginPath();\n      ctx.fillStyle = \"#ff80ff\";\n      ctx.fillRect(this.drawX - 4, this.drawY - 4, 8, 8);\n      ctx.closePath();\n    };\n\n    \/**\n     * Function to get a random unvisited neighbor\n     * returns false if there are no neighbors\n     *\/\n    this.getUnvisited = function () {\n      \/\/ clear any visited neighbors from the array\n      for (var i = this.neighbors.length - 1; i >= 0; i--) {\n        if (this.neighbors[i].dfsVisited) {\n          this.neighbors.splice(i, 1);\n        }\n      }\n      \/\/ select a random unvisited neighbor if there are any\n      if (this.neighbors.length > 0) {\n        var idx = Math.floor(Math.random() * this.neighbors.length);\n        return this.neighbors[idx];\n      } else {\n        return false;\n      }\n    };\n\n  }\n\n  \/\/constructor for a path object, Takes two points as parameters\n  function Path(p1, p2, color) {\n    this.p1 = p1;\n    this.p2 = p2;\n    \/\/ determines if the path is horizontal or vertical\n    this.vertical = p1.drawX == p2.drawX;\n    this.color = color;\n    this.draw = function () {\n      ctx.strokeStyle = this.color;\n      ctx.lineWidth = 4;\n      ctx.beginPath();\n      if (this.vertical) {\n        \/\/ this code makes the corners look nice :)\n        ctx.moveTo(p1.drawX, Math.min(p1.drawY, p2.drawY) - 2);\n        ctx.lineTo(p2.drawX, Math.max(p1.drawY, p2.drawY) + 2);\n      } else {\n        ctx.moveTo(p1.drawX, p1.drawY);\n        ctx.lineTo(p2.drawX, p2.drawY);\n      }\n      ctx.stroke();\n      ctx.closePath();\n    }\n  }\n\n  \/\/ create all points, the maze, and initialize the queue for the BFS traversal\n  function initialize() {\n    \/\/create the points\n    for (var i = 0; i < gridSize; i++) {\n      var row = [];\n      for (var j = 0; j < gridSize; j++) {\n        row.push(new Point(i, j));\n        if (i > 0) {\n          \/**\n           * If there is a point above the current point\n           * this adds that point to the current point's\n           * neighbors list and adds the current point to\n           * the vertical neighbor's neighbors list.\n           *\/\n          pts[i - 1][j].neighbors.push(row[j]);\n          row[j].neighbors.push(pts[i - 1][j]);\n        }\n        if (j > 0) {\n          \/**\n           * If there is a point to the right of the \n           * current point this adds that point to the \n           * current point's neighbors list and adds \n           * the current point to the vertical neighbor's \n           * neighbors list.\n           *\/\n          row[j - 1].neighbors.push(row[j]);\n          row[j].neighbors.push(row[j - 1]);\n        }\n      }\n      pts.push(row);\n    }\n    \/\/pick a random point to start the stack and mark it as visited\n    start = pickRandomPoint();\n    ptStack.push(start);\n    ptStack[0].dfsVisited = true;\n    createMaze();\n    drawMaze();\n    \/\/ pick random points for the start and end of the maze\n    start = pickRandomPoint();\n    start.bfsVisited = true;\n    solveQueue.push(start);\n    goal = pickRandomPoint();\n  }\n\n  \/\/ Function to pick a random point in the maze\n  function pickRandomPoint() {\n    var x = Math.floor(Math.random() * gridSize);\n    var y = Math.floor(Math.random() * gridSize);\n    return pts[x][y];\n  }\n\n  function drawMaze() {\n    ctx.clearRect(0, 0, canvas.width, canvas.height);\n    for (var i = 0; i < paths.length; i++) {\n      paths[i].draw();\n    }\n\n  }\n\n  function createMaze() {\n    while (true) {\n      var nb = ptStack[0].getUnvisited();\n      while (nb == false) {\n        \/\/ 'pop' the first item off the stack\n        ptStack.splice(0, 1);\n        if (ptStack.length == 0) {\n          return;\n        }\n        nb = ptStack[0].getUnvisited();\n      }\n      nb.dfsVisited = true;\n      paths.push(new Path(ptStack[0], nb, \"white\"));\n      ptStack[0].paths.push(nb);\n      nb.paths.push(ptStack[0]);\n      \/\/ 'push' an item onto the stack\n      ptStack.splice(0, 0, nb);\n    }\n\n  }\n\n  function bfsSolve() {\n    drawMaze();\n    goal.draw();\n    start.draw();\n    var pt = solveQueue.pop();\n    if (pt == goal) {\n      clearInterval(solve);\n      drawSolution();\n      return;\n    }\n    pt.bfsVisited = true;\n    for (var i = 0; i < pt.paths.length; i++) {\n      if (!pt.paths[i].bfsVisited) {\n        pt.paths[i].parent = pt;\n        solveQueue.splice(0, 0, pt.paths[i]);\n        paths.push(new Path(pt, pt.paths[i], \"blue\"));\n      }\n    }\n  }\n\n  function drawSolution() {\n    while (paths[paths.length - 1].color === \"blue\") {\n      paths.pop();\n    }\n    var pt = goal;\n    while (pt.parent != null) {\n      paths.push(new Path(pt, pt.parent, \"red\"));\n      pt = pt.parent;\n    }\n    drawMaze();\n    goal.draw();\n    start.draw();\n  }\n", "This Javascript file creates and searches the maze on an HTML5 Canvas"]],
  "img": "maze.png"
}

games = {
  "VirtuaSlayer": vsl,
  "Maze Creator and Solver": maze,
  }

displayInfo = [Game(vsl['name'], vsl['description'], vsl['img'])]

webInfo = [Game(maze['name'], maze['description'], maze['img'])]

app = flask.Flask(__name__)

@app.route('/')
def index():
    return flask.render_template('index.html', games = displayInfo, sites = webInfo)


@app.route('/games')
def game():
  return flask.render_template('games.html', projects = displayInfo, games = displayInfo, sites = webInfo)

@app.route('/sites')
def site():
  return flask.render_template('games.html', projects = webInfo, games = displayInfo, sites = webInfo)

@app.route('/games/<name>')
def gamepage(name):
  gm = games[name]
  return flask.render_template('game.html', games = displayInfo, sites = webInfo, name = gm['name'], desc = gm['description'], vid = gm['video'], snippets = gm['snippets'])

if __name__ == '__main__':
    app.run()