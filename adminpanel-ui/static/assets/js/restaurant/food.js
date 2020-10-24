$( document ).ready(function() {
    var api_manager = new ApiManager();
    var util = new Util();
    $("#food-create-form").submit(function(e){
        e.preventDefault();
        var data= new FormData(this);
        
        api_manager.sendRequest("/api/fooditem/","post" , data, function(resp){
            if(resp.type === "+OK") {
                    console.log(data)
                
            } else {
                console.log("Response err");
            }
        },undefined,false);
       
    });
    
    $("#food-edit-form").submit(function(e){
        e.preventDefault();
        var data= new FormData(this);
        var id= $("#food_id").val();
        
        api_manager.sendRequest(`/api/fooditem/`+id+`/`,"patch" , data, function(resp){
            if(resp.type === "+OK") {
                    console.log(data)
                
            } else {
                console.log("Response err");
            }
        },undefined,false);
    });

function addtocart(food_id,action){
    var data ={}
    data["food_id"]=food_id
    data["action"]=action
    
    api_manager.sendRequest('/add-to-cart/',"post" , data, function(resp){
        console.log(resp)
        if(resp.type === "+OK") {
            
            console.log(data)
            window.location.reload(); 
       
        } else {
            console.log("Response err");
        }
    });
} 

$(".add-to-cart").on("click",function(e) {
    e.preventDefault();
    food_id = $(this).attr("data-id")
    action=$(this).attr("data-action")
    console.log(food_id,action)
    return addtocart(food_id,action);
});
});
