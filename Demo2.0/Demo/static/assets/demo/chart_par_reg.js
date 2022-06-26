// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

// Bar Chart Example
var ctx = document.getElementById("chart_par_reg");
//var ttt = [100,100,100,100,100,100];
//var ttt = [1,2,3,4,5,6];
var ttt = document.getElementById("par_reg");
var obj = ttt.innerText.split("[")[1];
obj=obj.split("]")[0];
obj=obj.split(", ")
console.log(obj);
var myLineChart = new Chart(ctx, {
  type: 'bar',
  data: {
    labels: ["南开区", "和平区", "河西区", "津南区"],
    datasets: [{
      label: "Revenue",
      backgroundColor: "rgba(2,117,216,1)",
      borderColor: "rgba(2,117,216,1)",
      data: obj,
    }],
  },
  options: {
    scales: {
      xAxes: [{
        time: {
          unit: 'month'
        },
        gridLines: {
          display: false
        },
        ticks: {
          maxTicksLimit: 6
        }
      }],
      yAxes: [{
        ticks: {
          min: 0,
          max: 5,
          maxTicksLimit: 10
        },
        gridLines: {
          display: true
        }
      }],
    },
    legend: {
      display: false
    }
  }
});
