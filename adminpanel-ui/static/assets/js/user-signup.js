$( document ).ready(function() {
    var api_manager= new ApiManager()
    var util = new Util();

    $("#user-signup-form").submit(function(e){
        util.hideErrors();
        
        e.preventDefault();
        data=util.getFormData(this,true);
        data['user']['user_type']=4

        api_manager.sendRequest('/api/customer/',"post" , data, function(resp){
            
            if(resp.type === "+OK") {
                
                util.showMsg(".success-msg", resp.message);
                
            } else {

                util.showMsg(".error-msg", resp.message);
            }
        });
    });



    
    $("#restaurant-signup").submit(function(e){
        e.preventDefault();
        data=util.getFormData(this,true);
        data['user']['user_type']=2

        api_manager.sendRequest('/api/restaurant/',"post" , data, function(resp){
            if(resp.type === "+OK") {
                    console.log(data)
                
            } else {
                console.log("Response err");
            }
        });
    });

    
});