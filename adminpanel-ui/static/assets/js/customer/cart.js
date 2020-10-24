$( document ).ready(function() {
    var api_manager = new ApiManager();
    var util = new Util();

function PlaceOrder(price){
    var data ={}
    data["price"]=price

    
    api_manager.sendRequest('/place-order/',"post" , data, function(resp){
        console.log(resp)
        if(resp.type === "+OK") {
            
            console.log(data)
            
       
        } else {
            console.log("Response err");
        }
    });
} 

$(".place-order").on("click",function(e) {
    e.preventDefault();
    var price = $(this).data("price");
    console.log(price)
    return PlaceOrder(price);
});
});
