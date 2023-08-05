const http = require('http');
const fs = require('fs');
const port = 3000;

const server = http.createServer(function (req, res) {
  if (req.url === '/') {
    res.writeHead(200, { 'Content-Type': 'text/html' });
    fs.readFile('index.html', function (error, data) {
      if (error) {
        res.writeHead(404);
        res.write('Error file not found');
      } else {
        res.write(data);
      }
      res.end();
    });
  } else {
    res.writeHead(404);
    res.write('Not Found');
    res.end();
  }
});

server.listen(port, function (error) {
  if (error) {
    console.log('Something went wrong', error);
  } else {
    console.log('Server is listening on port ' + port);
  }
});
