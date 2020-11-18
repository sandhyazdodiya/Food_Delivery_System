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




});
