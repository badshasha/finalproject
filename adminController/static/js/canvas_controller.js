var ctx = document.getElementById('myChart').getContext('2d');
var ctx2 = document.getElementById('myChart2').getContext('2d');

var my_chart = createChart(ctx,'pie',data=[12, 19],label=['red','blue'])
var my_chart2  = createChart(ctx2,'bar',data=[12,19],label=['red','blue'])

var prev_response = 0;
var preses_button = 0;


function createChart(canvas,graph,data,label,title){

    var myChart = new Chart(canvas, {
            type:  graph,
            data: {
                labels: label,
                datasets: [{
                    label: '# of Votes',
                    data: data,
                    backgroundColor: [
                        // 'rgba(255, 99, 132, 0.2)',
                        'rgba(0,0,0,.2)',
                        'rgba(37,169,112,.4)',
                        // 'rgba(54, 162, 235, 0.2)',
                        // 'rgba(255, 206, 86, 0.2)',
                        // 'rgba(75, 192, 192, 0.2)',
                        // 'rgba(153, 102, 255, 0.2)',
                        // 'rgba(255, 159, 64, 0.2)'
                    ],
                    borderColor: [
                         'rgba(0,0,0,.2,1)',
                         'rgb(44, 137, 84)',
                        // 'rgba(54, 162, 235, 1)',
                        // 'rgba(255, 206, 86, 1)',
                        // 'rgba(75, 192, 192, 1)',
                        // 'rgba(153, 102, 255, 1)',
                        // 'rgba(255, 159, 64, 1)'
                    ],
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                },

                plugins: {
                    title: {
                    display: true,
                    text: title
                     }
                }
            }
        });

    return myChart;

}
function ajaxsender(event,button_number,path,title){
        preses_button = button_number;
        event.preventDefault();
        my_chart.destroy();
        my_chart2.destroy();
        $.ajax({
            type:'GET',
            url : path,
            success : function (response){
                console.log(response);
                prev_response = response;
                my_chart = createChart(ctx,'pie',data=response.data,label= response.label,title )
                my_chart2  = createChart(ctx2,'bar',data=response.data,label= response.label,title )
            },
            error :function (response) {
                console.log("error")
            }
    })

}

function chartDestroyAndCreate(ctx,response,chart,title){
      my_chart.destroy();
      my_chart = createChart(ctx,chart,data=response.data,label=response.label,title);
}


// btn selection
var subject_btn = document.getElementById('subject')
subject_btn.addEventListener('click',function (event){
    ajaxsender(event,1,'subject_json/',"subjects and  subject subtopic -pie",)

})

var staff_priv = document.getElementById('userinfo');
staff_priv.addEventListener('click',function (event){
     ajaxsender(event,2,'staffpriv_json/',"admin and normal user chart-pie",)
})