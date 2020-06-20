$( document ).ready(function() {
    $("#user-signup").submit(function(e){
        e.preventDefault();
        
    
        var data={};
	    $.each($(this).serializeArray(), function(k, input){
		data[input.name] = input.value;
        });
        data['user_type']=1
        var data = JSON.stringify(data);
        console.log(data);
        
        var req = $.ajax({
            url:'/users/api/',
            type: "POST",
            data: data,
            processData: false,
            contentType:"application/json"
        });
        
        req.done(function(req) {
            if (req.type === "+OK"){
               console.log(data)
            }
            else{
                console.log("Response err");
            }
            $("body").css("cursor", 'default');
        });
    
        req.fail(function(a) {
            var msg = "Something went wrong. Please reload the page and try again.";
            console.log(msg)
        });

    });
});

$( document ).ready(function() {
    $("#restaurant-signup").submit(function(e){
        e.preventDefault();
        
    
        var data={};
	    $.each($(this).serializeArray(), function(k, input){
		data[input.name] = input.value;
        });
        data['user_type']=2
        var data = JSON.stringify(data);
        console.log(data);
        
        var req = $.ajax({
            url:'/restaurant/api/',
            type: "POST",
            data: data,
            processData: false,
            contentType:"application/json"
        });
        
        req.done(function(req) {
            if (req.type === "+OK"){
               console.log(data)
            }
            else{
                console.log("Response err");
            }
            $("body").css("cursor", 'default');
        });
    
        req.fail(function(a) {
            var msg = "Something went wrong. Please reload the page and try again.";
            console.log(msg)
        });

    });
});