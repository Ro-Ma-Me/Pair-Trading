$(function () {

        $('#container').highcharts('StockChart', {

            rangeSelector: {
                selected: 4
            },
            xAxis: {
            type: 'datetime'
          },

            yAxis: {
                labels: {
                    formatter: function () {
                        return (this.value > 0 ? ' + ' : '') + this.value + '%';
                    }
                },
                plotLines: [{
                    value: 0,
                    width: 2,
                    color: 'silver'
                }]
            },

            plotOptions: {
                series: {
                    compare: 'percent'
                }
            },

            tooltip: {
                pointFormat: '<span style="color:{series.color}">{series.name}</span>: <b>{point.y}</b> ({point.change}%)<br/>',
                valueDecimals: 2
            },

            series: [{
          name: jsonKO.dataset.name,
          data: jsonKO.dataset.data

      }, {
        name: jsonPEP.dataset.name,
        data: jsonPEP.dataset.data

      }, {
        name: jsonBA.dataset.name,
        data: jsonBA.dataset.data

      }]
        });

});
