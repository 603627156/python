///*编辑个人信息模态窗 */
//点击更新按钮，获取id，从逻辑端查出对应的数据，弹出模态窗渲染数据
$(".update").click(function(){
//    $('#updateModal').modal('hide')
    var id=$(this).attr("data-id")
    $.getJSON("/update/",{'id':id},function(data){
            console.log(data);
            $("#upid").val(id);
            $("#name").val(data["user_name"]);
            $("#name_cn").val(data["user_user"]);
            $("#mobile").val(data["user_phone"]);
            $("#email").val(data["user_mail"]);
            $('#updateModal').modal('show');
        })
})

// 更新数据
$("#updatebtn").click(function(){
$.post("/update/",$("#updateForm").serialize(),function(data) {
    //data=JSON.parse(data)
    if(data['code'] == 0){
        alert("modfiy success")
        location.reload()
    }else{
        alert("update error")
    }
    })
    //return false;
})

//**********************************************/*删除用户代码*/********************************************
    $(".del").click(function(){
	if(confirm("是否确认删除？")){
		var id = $(this).attr('data-id')
        var url = "/delete?id="+id
        //alert(url)
		$.getJSON(url,function(data){
			if (data['code'] == 0 ){
                alert("删除成功")
                location.reload()
			}else{
                alert(data["errmsg"])
			}
    	})
    }  // end confirm
})
