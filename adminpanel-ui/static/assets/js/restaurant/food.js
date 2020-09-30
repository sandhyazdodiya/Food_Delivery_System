$( document ).ready(function() {
    var api_manager = new ApiManager();
    var util = new Util();
    $("#food-create-form").submit(function(e){
        e.preventDefault();
        var data = util.getFormData(this);
        
        api_manager.sendRequest("/fooditem/api/","post" , data, function(resp){
            if(resp.type === "+OK") {
                if(method === "post"){
                    console.log(data)
                }
            } else {
                console.log("Response err");
            }
        });
       
    });
    $("#food-edit-form").submit(function(e){
        e.preventDefault();
        var data = util.getFormData(this);
        
        api_manager.sendRequest(`/fooditem/api/`+data.id+`/`,"patch" , data, function(resp){
            if(resp.type === "+OK") {
                if(method === "patch"){
                    console.log(data)
                }
            } else {
                console.log("Response err");
            }
        });
    });
function addtocart(id){
    data = {"id": id}
    api_manager.sendRequest(`/add_to_cart/`,"post" , data, function(resp){
        console.log(resp)
        if(resp.type === "+OK") {
            
            console.log(data)
       
        } else {
            console.log("Response err");
        }
    });
} 

$(".add-to-cart").on("click",function(e) {
    e.preventDefault();
    food_id = $(this).attr("data-id")
    console.log(food_id)
    return addtocart(food_id);
});
});
