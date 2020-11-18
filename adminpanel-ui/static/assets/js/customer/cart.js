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

function AddRemoveToCart(food_id,action,$this){

    var data ={}
    data["food_id"]=food_id
    data["action"]=action
    
    api_manager.sendRequest('/add-to-cart/',"post" , data, function(resp){
        console.log(resp)
        if(resp.type === "+OK") {
            GetCart(food_id,$this);
            console.log(data)
       
        } else {
            
            console.log("Response err");
        }
    });
} 

function GetCart(food_id,$this){
    
    api_manager.sendRequest('/get-cart/',"get" , food_id, function(resp){
        if(resp.type === "+OK") {
            var $cart =$($this).parent(".cart").hasClass("not-in-cart");
            console.log($cart);
            var $span =$($this).parents(".card-body").find(".item-count");
            $($span).text(resp.data);
            console.log($span)
            console.log(resp)
       
        } else {
            
            console.log("Response err");
        }
    },undefined,false);
}
    $(".place-order").on("click",function(e) {
        e.preventDefault();
        var price = $(this).data("price");
        console.log(price)
        return PlaceOrder(price);
    });

    $(".add-to-cart").on("click",function(e) {
        e.preventDefault();
        food_id = $(this).attr("data-id")
        action=$(this).attr("data-action")
        
        console.log(food_id,action)
        return AddRemoveToCart(food_id,action,this);
    });
});
