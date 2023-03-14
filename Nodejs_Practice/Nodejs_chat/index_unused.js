
const express = require('express'),
      app = express(),
      util = require('util'),
      bodyParser = require('body-parser'),
      http = require('http').Server(app),
      io = require('socket.io')(http, {cors: {origin: "*"}}),
      cors = require('cors');

app.use(express.static('public'));
// app.use(cors({
//   origin: true,
//   credential: true
// }));

// app.set('views', __dirname + "/./views");
// app.set('view engine', 'ejs');
// app.engine('html', require('ejs').renderFile);

// app.use( (req, res, next) => {
//   res.header("Access-Control-Allow-Origin", "*");
//   res.header("Access-Control-Allow-Credentials", "true");
//   res.header("Access-Control-Allow-Headers", "X-Requested-With");
//   res.header("Access-Control-Allow-Headers", "Content-Type, Authorization");
//   res.header("Access-Control-Allow-Methods", "PUT, GET, POST, DELETE, OPTIONS");

//   if (req.method === 'OPTIONS') {
//       res.status(200).end();

//   } else {
//       next();
//   }
// });

const server = app.listen(7000, function(){
  console.log("Express's started on port 7000");
});

io.listen(server, {
  log: false,
  origins: '*:*',
  pingInterval: 3000,
  pingTimeout: 5000
});

io.on('connection', (socket, opt) => {
  socket.emit('message', {msg: 'Welcome ' + socket.id});

  util.log("connection>>", socket.id, socket.handshake.query)

  socket.on('join', function(roomId, fn) {
    socket.join(roomId, function() {
      util.log("Join", roomId, Object.keys(socket.rooms));
      if (fn)
        fn();
    });
  });

  socket.on('leave', function(roomId, fn) {
    util.log("leave>>", roomId, socket.id)
    socket.leave(roomId, function() {
      if (fn)
        fn();
    });
  });

  socket.on('rooms', function(fn) {
    if (fn)
      fn(Object.keys(socket.rooms));
  });

  // data: {room: 'roomid', msg: 'msg 내용..'}
  socket.on('message', (data, fn) => {
    util.log("message>>", data)

    socket.broadcast.to(data.room).emit('message', {room: data.room, msg: data.msg});

    if (fn)
      fn(data.msg);
  });

  socket.on('message-for-one', (socketid, msg, fn) => {
    // socket.broadcast.to(socketid).emit('message', {msg: msg});
    socket.to(socketid).emit('message', {msg: msg});
  });

  socket.on('disconnecting', function(data) {
    util.log("disconnecting>>", socket.id, Object.keys(socket.rooms))
  });

  socket.on('disconnect', function(data) {
    util.log("disconnect>>", socket.id, Object.keys(socket.rooms))
  });

});
