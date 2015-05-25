document.getElementById("nav01").innerHTML =
    "<ul id='menu'>" +
    "<li><a href='index.html'>Home</a></li>" +
    "<li><a href='login.html'>Login</a></li>" +
    "<li><a href='game.html'>Game</a></li>" +
    "</ul>";

function drawBoard() {
    var board = document.createElement("CANVAS");
    var ctx = board.getContext("2d");
    var board_image = document.getElementById('poker_table')
    ctx.drawImage(board_image);
}