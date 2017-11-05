var notice, warning, error;
notice = "提示";
warning = "警告";
error = "错误";
var Toast = {
    success: function (msg, title, fn) {
        if (!title)
            title = notice;
        if (fn) {
            toastr.options.onclick = fn;
        }
        if (typeof(title) == "function") {
            fn = title;
            title = notice;
            toastr.options.onclick = fn;
        }
        toastr["success"](msg, title);
    },
    info: function (msg, title, fn) {
        if (!title)
            title = notice;
        if (fn) {
            toastr.options.onclick = fn;
        }
        if (typeof(title) == "function") {
            fn = title;
            title = notice;
            toastr.options.onclick = fn;
        }
        toastr["info"](msg, title);
    },
    warning: function (msg, title, fn) {
        if (!title)
            title = warning;
        if (fn) {
            toastr.options.onclick = fn;
        }
        if (typeof(title) == "function") {
            fn = title;
            title = warning;
            toastr.options.onclick = fn;
        }
        toastr["warning"](msg, title);
    },
    error: function (msg, title, fn) {
        if (!title)
            title = error;
        if (fn) {
            toastr.options.onclick = fn;
        }
        if (typeof(title) == "function") {
            fn = title;
            title = error;
            toastr.options.onclick = fn;
        }
        toastr["error"](msg, title);
    },
    tips:function (result) {
        if(result.code == 0){
            Toast.success(result.msg);
        } else {
            Toast.error(result.msg);
        }
    },
    init: function () {
        $("head").prepend("<link rel=\"stylesheet\" href=\"/static/toastr.min.css\">");
        toastr.options = {
            closeButton: true,
            debug: false,
            positionClass: "toast-bottom-right",
            onclick: null,
            showDuration: 300,
            hideDuration: 1000,
            timeOut: 5000,
            extendedTimeOut: 1000,
            showEasing: 'swing',
            hideEasing: 'linear',
            showMethod: 'fadeIn',
            hideMethod: 'fadeOut'
        };
    }
};
$(document).ready(function () {
    Toast.init();
});
