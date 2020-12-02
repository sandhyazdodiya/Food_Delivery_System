$(document).ready(function(){
  
    var socket = new WebSocket("ws:/"+ window.location.host +"/notifications/");

    socket.onopen = function(e) {
      console.log("[open] Connection established");
    };
    
    socket.onmessage = function(event) {
        console.log(event)
        var json_data = JSON.parse(event.data);
        
        if(json_data.event_type="new_order") {
          new_order_received(json_data);
        }

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



  function new_order_received(data){
    $(".order-notification").html(data.message);
    var order_url='/restaurant-order-detail/'+data.order_id
    var tr_html=" <tr>"+
                "<td><a href='"+order_url+"'>#"+ data.order_id +"</a></td>"+
                "<td>{Date}}</td>"+
                "<td>{Customer name}</td>"+
                "<td>{Location}</td>"+
                "<td>${{order.price}}</td>"+
                "<td>{{order.status}}</td>"+
                "</tr>";
    $("#order-list-table").find("tbody").prepend(tr_html);
  }



});

