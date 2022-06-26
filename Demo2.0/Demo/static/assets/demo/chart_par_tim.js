// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

// Pie Chart Example
var ctx = document.getElementById("chart_par_tim");
var ttt = document.getElementById("par_tim");
var obj = ttt.innerText.split("[")[1];
obj=obj.split("]")[0];
obj=obj.split(", ")
console.log(obj);
var myPieChart = new Chart(ctx, {
  type: 'pie',
  data: {
    labels: ["上午", "中午", "晚上"],
    datasets: [{
      data: obj,
      backgroundColor: ['#dc3545', '#ffc107', '#28a745'],
    }],
  },
});
