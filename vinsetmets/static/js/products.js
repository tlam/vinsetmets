function drawInventory() {
  $.get('/products/' + $('#product-id').val() + '.json', function(response) {
    var data = new google.visualization.DataTable();
    data.addColumn('date', 'Date');
    data.addColumn('number', 'Inventory');
    data.addColumn('number', 'Price');

    var history = [];
    for (let entry of response.history) {
      history.push([new Date(entry.added_on), entry.inventory, parseFloat(entry.price)]);
    }
    data.addRows(history);

    var options = {
      title: 'Inventory across time',
      height: 450,
      hAxis: {
        format: 'EEE, MMM d'
      }
    };
    var chart = new google.visualization.LineChart(document.getElementById('chart-output'));
    chart.draw(data, options);
  });
}

$(document).ready(function() {
  // Set a callback to run when the Google Visualization API is loaded.
  google.charts.setOnLoadCallback(drawInventory);
});
