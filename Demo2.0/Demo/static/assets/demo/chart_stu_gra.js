// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

// Pie Chart Example
var ctx = document.getElementById("chart_stu_gra");
var ttt = document.getElementById("stu_gra");
var obj = ttt.innerText.split("[")[1];
obj=obj.split("]")[0];
obj=obj.split(", ")
console.log(obj);
var myPieChart = new Chart(ctx, {
  type: 'pie',
  data: {
    labels: ["小学", "初中", "高中"],
    datasets: [{
      data: obj,
      backgroundColor: ['#007bff', '#dc3545', '#ffc107'],
    }],
  },
});
