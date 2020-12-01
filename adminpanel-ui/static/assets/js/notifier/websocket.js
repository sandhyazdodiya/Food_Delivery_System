$(document).ready(function(){
    var socket = new WebSocket("ws:/"+ window.location.host +"/notifications/");

    socket.onopen = function(e) {
      console.log("[open] Connection established");
      console.log("Sending to server");
      socket.send("My name is John");
    };
    
    socket.onmessage = function(event) {
        console.log(event)
        console.log(`[message] Data received from server: ${event.data}`);
        $(".order-notification").html(event.data)
    };
    
    socket.onclose = function(event) {
      if (event.wasClean) {
        console.log(`[close] Connection closed cleanly, code=${event.code} reason=${event.reason}`);
      } else {
        // e.g. server process killed or network down
        // event.code is usually 1006 in this case
        console.log('[close] Connection died');
      }
    };
    
    socket.onerror = function(error) {
      console.log(`[error] ${error.message}`);
    };
  });