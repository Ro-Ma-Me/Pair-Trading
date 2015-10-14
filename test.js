var jsonValue = json
var jsonValue2 = json2
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
          name: jsonValue.dataset.name,
          data: jsonValue.dataset.data

      }, {
        name: jsonValue2.dataset.name,
        data: jsonValue2.dataset.data

      }]
        });

});
