var btn = document.getElementsByClassName("bb");
console.log(btn);

for(var i = 0; i < btn.length; i++){
    btn[i].addEventListener("click",function (event){
        event.preventDefault();
        console.log(event.srcElement.id)
        $.ajax({
            type:'GET',
            url : 'sub/'+event.srcElement.id+'',
            success:function (response){

                var value = JSON.parse(response.subtopic);


                var add = document.getElementById("add_hear");
                add.innerHTML = '';
                var htmlRender = "";
                let full_paper_link_id ;
                for (var i = 0; i<value.length;i++){

                    htmlRender += "<a class='link'  href='sub/subexam/" + value[i].pk +"'/>"+value[i].fields["name"]+"</a>";
                    full_paper_link_id = value[i].fields["subject"];

                }
                htmlRender += "<br><a class='link' href='fullpage/1' style='background-color: #2DA64B;margin-top:1rem; '>fullpaper</a>"
                add.insertAdjacentHTML('beforeend',htmlRender);


            }

        })

    })
}

// document.addEventListener("click",function (event){
//     console.log('working bro');
// })

// function getId(btn){
//     alert(btn.id);
// }