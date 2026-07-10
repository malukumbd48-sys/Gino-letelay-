 <!DOCTYPE html>
<html>
<head>
    <title>Game</title>
</head>

<body>

<script src="main.js"></script>

</body>
</html>
 <!DOCTYPE html>
<html>
<head>
    <title>Game Canvas</title>

    <style>
        canvas {
            border: 3px solid #111;
        }
    </style>
</head>

<body>

<script>

let gamePiece;

function startGame() {
    gameArea.start();
    gamePiece = new component(30, 30, "red", 10, 120);
}


let gameArea = {
    canvas: document.createElement("canvas"),

    start: function() {
        this.canvas.width = 480;
        this.canvas.height = 270;

        this.context = this.canvas.getContext("2d");

        document.body.insertBefore(
            this.canvas,
            document.body.childNodes[0]
        );

        this.interval = setInterval(updateGameArea, 20);
    },


    clear: function() {
        this.context.clearRect(
            0,
            0,
            this.canvas.width,
            this.canvas.height
        );
    }
};



function component(width, height, color, x, y) {

    this.width = width;
    this.height = height;
    this.color = color;

    this.speedX = 0;
    this.speedY = 0;

    this.x = x;
    this.y = y;


    this.update = function() {

        let ctx = gameArea.context;

        ctx.fillStyle = color;

        ctx.fillRect(
            this.x,
            this.y,
            this.width,
            this.height
        );
    }


    this.newPos = function() {

        this.x += this.speedX;
        this.y += this.speedY;

    }

}



function updateGameArea() {

    gameArea.clear();

    gamePiece.update();

    gamePiece.newPos();

}



function moveup() {
    gamePiece.speedY -= 1;
}


function movedown() {
    gamePiece.speedY += 1;
}


function moveleft() {
    gamePiece.speedX -= 1;
}


function moveright() {
    gamePiece.speedX += 1;
}



startGame();

</script>

</body>
</html>
<div class="controls">
    <button class="btn up" onclick="moveup()">▲</button>

    <div>
        <button class="btn" onclick="moveleft()">◀</button>
        <button class="btn" onclick="movedown()">▼</button>
        <button class="btn" onclick="moveright()">▶</button>
    </div>
</div>