var myChart;
var months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december'];

document.getElementById('chart-tab').addEventListener('click', function() {
    var incomeData = [];
    var expensesData = [];

    document.getElementById('download').addEventListener('click', function() {
        var canvas = document.getElementById('myChart');
        var image = canvas.toDataURL('image/png');
        
        var link = document.createElement('a');
        link.href = image;
        link.download = 'chart.png';
        link.click();
    });
    
    months.forEach(function(month) {
        var income = document.getElementById(month + '-income').value;
        var expenses = document.getElementById(month + '-expenses').value;
    
        incomeData.push(income);
        expensesData.push(expenses);
    });
    
    if (myChart) {
        myChart.destroy();
    }   

    var ctx = document.getElementById('myChart').getContext('2d');
    myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
            datasets: [{
                label: 'Income',
                data: incomeData, // Set income data here
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 1
            }, {
                label: 'Expenses',
                data: expensesData, // Set expenses data here
                backgroundColor: 'rgba(255, 99, 132, 0.2)',
                borderColor: 'rgba(255, 99, 132, 1)',
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
});

// This file is intentionally left blank