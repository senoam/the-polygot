

var express = require('express');
app = express();
var port = 3000;
app.listen(port, function () {
    console.log(`server running on http://localhost:${port}`);
});

app.get('/', function (req, res) {
    var spawn = require('child_process').spawn;
    var process = spawn('python', ['./app.py']);
    res.sendFile(__dirname + '/page.html');
    process.stdout.on('data', function (data) {
        return !res.headersSent && res.send(data.toString());
    });
});


function start(){
    const http = require('http');

    const hostname='127.0.0.1'
    const port = 8050;
    console.log("I'm inside");
    const server = http.createServer((req, res) => {
        res.statusCode = 200
        res.setHeader('Content-Type', 'text/plain');
    });

    server.listen(port, hostname, () => {
        console.log(`Server is running at http://${hostname}:${port}/`)
    });

}

