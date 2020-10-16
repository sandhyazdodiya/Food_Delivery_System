$( document ).ready(function() {
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');


function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});
});

class ApiManager {
    constructor () {}
    sendRequest(url, method, data, success_callback, error_callback, content_type) {
        if (content_type == undefined || content_type == "application/json") {
            content_type = "application/json";
            data = JSON.stringify(data);
        }
        if (error_callback == undefined) {
            error_callback = this.handleError
        }
        
        return $.ajax({
            url: url,
            data: data,
            method: method,
            processData: false,
            contentType: content_type
        }).done(success_callback).fail(error_callback);
    }
    handleError(error){
        var resp_json = error.responseJSON;
        if (resp_json == undefined) {
            console.log(error_msgs.unknown);
            $(".error-msg").text(error_msgs.unknown).show(100);
            return
        }
        var resp = resp_json.errors;
        if (error.status == 401) {
            window.location.href = "/login/"
            return false
        } else if (error.status == 400) {
            $.each(resp, function(k, err_msg){
                $(".err-"+ k).text(err_msg).show(100);
            });
            if (resp.detail != undefined) {
                $(".error-msg").text(resp.detail).show(100);
            }
            return false
        } else if (error.status == 403 || error.status == 500) {
            $(".error-msg").text(resp.detail).show(100);
        } else {
            $(".error-msg").text(error_msgs.unknown).show(100);
        }
    }
    handleError2(error, selector){
        var resp_json = error.responseJSON;
        if (resp_json == undefined) {
            $(selector).text(error_msgs.unknown).show(100);
            return
        }
        var resp = resp_json.errors;
        if (error.status == 401) {
            window.location.href = "/login/"
            return false
        } else if (error.status == 400) {
            $.each(resp, function(k, err_msg){
                $(".err-"+ k).text(err_msg).show(100);
            });
            if (resp.detail != undefined) {
                $(selector).text(resp.detail).show(100);
            }
            return false
        } else if (error.status == 403 || error.status == 500) {
            $(selector).text(resp.detail).show(100);
        } else {
            $(selector).text(error_msgs.unknown).show(100);
        }
    }
    checkAuthError(error, selector=".error-msg"){
        if (error.status == 401) {
            window.location.href = "/login/"
        } else if (error.status == 403) {
            $(selector).text(resp.detail).show(100);
        }
    }
}

class Util {
    constructor () {}
    hideErrors(selector) {
        $(".error-msg,.field-error-msg,.success-msg,.custom-alert").hide();
        if (selector != undefined) {
            $(selector).hide();
        }
    }
    hideLater(selector, time=2000) {
        setTimeout(function(){
            $(selector).text("").hide(100);
        }, time);
    }
    redirectLater(url, time) {
        setTimeout(function(){
            window.location.href = url;
        }, time);
    }
    showMsg(selector, msg, time=100, hide_time) {
        $(selector).text(msg).show(time);
        if (hide_time != undefined) {
            this.hideLater(selector, hide_time);
        }
        $(selector).focus();
    }
    validatePhone(selector){
        var input_phone = document.querySelector(selector);
        var iti = window.intlTelInputGlobals.getInstance(input_phone);
        if (!iti.isValidNumber()) {
            return false;
        }
        return iti.getNumber();
    }
    getFormData(selector, deep=false){
    /*
    Return dictionary of form data
    if deep is true it return the 2 level dictionary.  Helpful when backend used inline serializer
    serializer name and field name split using "-"
    */
        var data = {};
        $.each($(selector).serializeArray(), function(k, input){
            if (deep && input.name.includes("-")) {
                var name = input.name.split("-")[0];
                var sub_name = input.name.split("-")[1];
                if (!data[name]) {
                    data[name] = {};
                }
                data[name][sub_name] = input.value;
            } else {
                data[input.name] = input.value;
            }
            
        });
        return data;
    }
}

var error_msgs={
    unknown:"Please Refresh Page and try again."
}