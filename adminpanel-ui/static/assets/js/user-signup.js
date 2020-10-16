$( document ).ready(function() {
    var api_manager= new ApiManager()
    var util = new Util();
    // $( "#target" ).click(function() {
    //     alert( "Handler for .click() called." );
    //   });
    $("#user-signup-form").submit(function(e){
        
        e.preventDefault();
        data=util.getFormData(this,true);
        console.log(data)
        data['user']['user_type']=4

        api_manager.sendRequest('/api/customer/',"post" , data, function(resp){
            if(resp.type === "+OK") {
                if(method === "post"){
                    console.log(data)
                }
            } else {
                console.log("Response err");
            }
        });
    });



    
    $("#restaurant-signup").submit(function(e){
        e.preventDefault();
        data=util.getFormData(this,true);
        data['user']['user_type']=2

        api_manager.sendRequest('/api/restaurant/',"post" , data, function(resp){
            if(resp.type === "+OK") {
                if(method === "post"){
                    console.log(data)
                }
            } else {
                console.log("Response err");
            }
        });
    });

    
});