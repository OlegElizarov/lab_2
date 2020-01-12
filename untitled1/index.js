$(document).ready(function ()
{
    var $from = $('.from');
    var $to = $('.to');
    var $func = $('.func');
    var $button = $('.button');
    var $graph = $('.graph');
    const $delta = $('.delta');

    $($button).click(function () {
        var points=[];
            if (parseFloat($from.val(), 10) > parseFloat($to.val(), 10)) {
            }
            else {
                for (var i = parseFloat($from.val(), 10); i <= parseFloat($to.val(), 10);
                     i=i+parseFloat($delta.val(), 10)) {
                    const fun = $func.val()+'(' + i + ')' ;
                    const y = eval(fun);
                    points.push([i,y]);
                    console.log(i,y,points);
                }


                let options = {
                    legend: {
                        show: true,
                        position: "ne"
                    },
                    width: 10,
                    height: 10
                };

                let data = [
                    {
                        data: points,
                        label: $func.val().toString(),
                        color: "lightgreen",
                    }
                ];
                var plot = $.plot($("#graph"),[] , options);
                plot.setData(data);
                plot.setupGrid(); //only necessary if your new data will change the axes or grid
                plot.draw();
            }

        }
    );


});