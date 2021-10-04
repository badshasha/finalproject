
// chart page
var ctx = document.getElementById('myChart').getContext('2d');
var ctx2 = document.getElementById('myChart2').getContext('2d');
console.log(ctx2);
// chart create
var my_chart = createChart(ctx,'pie',data=[12, 19],label=['red','blue'])
var my_chart2  = createChart(ctx2,'bar',data=[12,19],label=['red','blue'])


var prev_response = 0;
var preses_button = 0;

//function for controlling graph
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


// function addData(chart, label, data) {
//     chart.data.labels.push(label);
//     chart.data.datasets.forEach((dataset) => {
//         dataset.data.push(data);
//     });
//     chart.update();
// }

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


// button controllers
//subject selecter
var s_btn = document.getElementById("subject");
s_btn.addEventListener('click',function (event){
    ajaxsender(event,1,'json',"selected subject and unselected subject -pie",)
})

// selected subjects
var s2_btn = document.getElementById("subject2");
s2_btn.addEventListener('click',function (event){
    ajaxsender(event,2,'json_subject',"selected subject and subtopic -pie");
})

// bar button controller

var chartChange = document.getElementById("bar");
chartChange.addEventListener('click',function (event){

    if (preses_button == 1){
       chartDestroyAndCreate(ctx,prev_response,'bar',"selected subject and unselected subject - bar")
    }
    else if (preses_button == 2){
        // console.log("button working")
        chartDestroyAndCreate(ctx,prev_response,'bar',"selected subject and subtopic -bar ")
    }
})



