//Establish connection
var socket = io.connect('http://localhost:8080');

var btn = document.getElementById('ping');
var box = document.getElementById('box');



btn.addEventListener('click',function(){
  socket.emit('message',"hello");
});



socket.on('message', function(data){
  box.innerHTML = 'Pong!';
});
