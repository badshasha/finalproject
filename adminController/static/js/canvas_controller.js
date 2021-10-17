var ctx = document.getElementById('myChart').getContext('2d');
var ctx2 = document.getElementById('myChart2').getContext('2d');

var my_chart = createChart(ctx,'pie',data=[12, 19],label=['red','blue'])
var my_chart2  = createChart(ctx2,'bar',data=[12,19],label=['red','blue'])

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