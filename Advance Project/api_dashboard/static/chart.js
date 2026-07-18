function renderChart(temp, btc) {
    const ctx = document.getElementById('chart');
    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['Weather °C', 'Bitcoin USD'],
            datasets: [{
                label: 'API Data',
                data: [temp, parseFloat(btc.replace(",", ""))],
                backgroundColor: ['#36a2eb','#ff6384']
            }]
        }
    });
}
