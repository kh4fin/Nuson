const apiUrl = "http://127.0.0.1:8000/api/nuson/";

fetch(apiUrl)
  .then((response) => response.json())
  .then((data) => {
    data = data.slice(-8);

    const labels = data.map((item) => formatTime(item.waktu));
    const nilai1 = data.map((item) => item.nilai1);
    const nilai2 = data.map((item) => item.nilai2);
    const nilai3 = data.map((item) => item.nilai3);
    const nilai4 = data.map((item) => item.nilai4);
    const nilai5 = data.map((item) => item.nilai5);

    function formatTime(dateTime) {
      const date = new Date(dateTime);
      const options = {
        year: "numeric",
        month: "2-digit",
        day: "2-digit",
        hour: "2-digit",
        minute: "2-digit",
      };
      return date.toLocaleString("id-ID", options);
    }

    var ctx = document.getElementById("myChart").getContext("2d");
    var myChart = new Chart(ctx, {
      type: "line",
      data: {
        labels: labels,
        datasets: [
          {
            label: "Nilai 1",
            data: nilai1,
            backgroundColor: "rgba(75, 192, 192, 0.2)",
            borderColor: "rgba(75, 192, 192, 1)",
            borderWidth: 1,
          },
          {
            label: "Nilai 2",
            data: nilai2,
            backgroundColor: "rgba(255, 99, 132, 0.2)",
            borderColor: "rgba(255, 99, 132, 1)",
            borderWidth: 1,
          },
          {
            label: "Nilai 3",
            data: nilai3,
            backgroundColor: "rgba(255, 206, 86, 0.2)",
            borderColor: "rgba(255, 206, 86, 1)",
            borderWidth: 1,
          },
          {
            label: "Nilai 4",
            data: nilai4,
            backgroundColor: "rgba(54, 162, 235, 0.2)",
            borderColor: "rgba(54, 162, 235, 1)",
            borderWidth: 1,
          },
          {
            label: "Nilai 5",
            data: nilai5,
            backgroundColor: "rgba(153, 102, 255, 0.2)",
            borderColor: "rgba(153, 102, 255, 1)",
            borderWidth: 1,
          },
        ],
      },
      options: {
        scales: {
          y: {
            beginAtZero: true,
          },
        },
      },
    });
  });

function setChartWidth() {
  const canvas = document.getElementById("myChart");
  const contentDiv = document.querySelector(".content");
  const chartWidth = contentDiv.clientWidth;
  canvas.style.width = chartWidth + "px";
}

window.addEventListener("load", setChartWidth);
window.addEventListener("resize", setChartWidth);
