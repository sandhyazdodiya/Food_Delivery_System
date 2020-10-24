$( document ).ready(function() {
    var api_manager = new ApiManager();
    var util = new Util();
    $("#user-login").submit(function(e){

        e.preventDefault();
        var data = util.getFormData(this);
        console.log(data)
        api_manager.sendRequest('/login/api/',"post",data, function(resp){
            if(resp.type === "+OK") {
                window.location.href = "/login/";
                    console.log(data)
                }
        });
    });
});