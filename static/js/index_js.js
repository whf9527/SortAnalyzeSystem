test_for_cal_test_data = [9,7,8,3,4,5,2,3,1];
test_for_sort_result = [[[1,2,3,4,5,7,8,9], 10, 20],
    [[1,2,3,4,5,7,8,9], 9, 22],
    [[1,2,3,4,5,7,8,9], 8, 20],
    [[1,2,3,4,5,7,8,9], 13, 34],
    [[1,2,3,4,5,7,8,9], 12, 56],
    [[1,2,3,4,5,7,8,9], 11, 17]];
//y=a1*x^2+a2*x+a3
//[[a1, a2, a3], RMSE, [0,1,2,...,n], [c1, c2, c3,..., cn], [1, 1, ... ,n, n], [ac01, ..., ac91, ..., ac0n, ..., ac9n]]
//比较次数拟合多项式系数，均方根误差，序列长度，将序列长度带入多项式得到的比较次数，数据集生成单个序列的长度，数据集中该序列长度实际的比较次数
//比较次数拟合多项式系数，均方根误差，序列长度，将序列长度带入多项式得到的比较次数，数据集生成单个序列的长度，数据集中该序列长度实际的比较次数
test_for_analyze_compare_data = [
    [[1.98,0.23,0.11], 1.34, [0,1,2,3,4,5,6,7,8], [0,0,1,3,5,8,12,20,44], [1,1,2,2,3,3], [2,2,4,4,5,6]],
    [[1.78,0.43,0.51], 2.33, [0,1,2,3,4,5,6,7,8], [0,0,1,2,4,7,10,18,30], [1,1,2,2,3,3], [3,5,4,2,4,8]],
    [[1.08,0.53,0.13], 4.55, [0,1,2,3,4,5,6,7,8], [0,0,1,3,5,9,22,31,43], [1,1,2,2,3,3], [3,5,4,2,4,8]],
    [[1.98,0.23,0.11], 0.89, [0,1,2,3,4,5,6,7,8], [0,0,1,3,9,13,23,43,61], [1,1,2,2,3,3], [3,5,4,2,4,8]],
    [[1.98,0.23,0.11], 7.89, [0,1,2,3,4,5,6,7,8], [0,0,1,2,4,9,15,17,29], [1,1,2,2,3,3], [3,5,4,2,4,8]],
    [[1.98,0.23,0.11], 3.22, [0,1,2,3,4,5,6,7,8], [0,0,1,4,9,12,25,33,56],[1,1,2,2,3,3], [3,5,4,2,4,8]]];
test_for_analyze_exchange_data = [
    [[1.98,0.23,0.11], 1.34, [0,1,2,3,4,5,6,7,8], [0,0,1,4,15,18,22,33,45], [1,1,2,2,3,3], [3,5,4,2,4,8]],
    [[1.78,0.43,0.51], 2.33, [0,1,2,3,4,5,6,7,8], [0,0,1,5,14,17,20,28,38], [1,1,2,2,3,3], [3,5,4,2,4,8]],
    [[1.08,0.53,0.13], 4.55, [0,1,2,3,4,5,6,7,8], [0,0,1,4,15,19,32,41,65], [1,1,2,2,3,3], [3,5,4,2,4,8]],
    [[1.98,0.23,0.11], 0.69, [0,1,2,3,4,5,6,7,8], [0,0,1,3,19,23,33,49,71], [1,1,2,2,3,3], [3,5,4,2,4,8]],
    [[1.98,0.23,0.11], 7.89, [0,1,2,3,4,5,6,7,8], [0,0,1,3,14,19,25,37,59], [1,1,2,2,3,3], [3,5,4,2,4,8]],
    [[1.98,0.23,0.11], 3.22, [0,1,2,3,4,5,6,7,8], [0,0,1,2,8,13,20,31,46], [1,1,2,2,3,3], [3,5,4,2,4,8]]];
test_for_analyze_result = [test_for_analyze_compare_data, test_for_analyze_exchange_data];

sort_names = ['选择排序', '冒泡排序', '快速排序', '堆排序', '归并排序', '插入排序',"希尔排序","基数排序","二分插入排序","鸡尾酒排序"];
curpage = 0;
cal_cap_n = 0;  //算法测试模块，用户指定的输入规模
analyze_max_n = 0; //算法分析模块，用户输入的最大规模n
range_method = ""; //算法测试模块的用户指定的分析数据的排列方式，可能取值“正序”，“逆序”，“倒序”
analyze_data_method = ''; //算法分析模块的用户指定的分析数据的排列方式，可能取值“正序”，“逆序”，“倒序”
cal_test_data = []; //算法测试模块，将用户输入的指定规模n和数据排列方式发给后台后，得到的待排序数据
sort_result = []; //算法测试模块，将待排序数据发给后台后，得到的各个算法的排序结果，
// 格式为：[[[排好序的列表]， 比较次数，交换次数], [...], [...], [...], [...], [...]]
//注意顺序为 选择排序,冒泡排序,快速排序,堆排序,归并排序,插入排序
analyze_result_compare = []; //算法分析模块，将最大规模发给后台得到的比较次数分析结果，
// 其中包括多项式拟合的系数a1，a2，a3，均方根误差，用了哪些规模进行拟合，该规模下的比较次数是多少，
//格式可参照上面我写的测试数据
//注意算法的顺序为：选择排序,冒泡排序,快速排序,堆排序,归并排序,插入排序
analyze_result_excahnge = []; //算法分析模块，将最大规模发给后台得到的交换次数分析结果，
// 其中包括多项式拟合的系数a1，a2，a3，均方根误差，用了哪些规模进行拟合，该规模下的交换次数是多少，
// 格式可参照上面我写的测试数据
//注意算法的顺序为：选择排序,冒泡排序,快速排序,堆排序,归并排序,插入排序
all_line_chart_compare = '';
all_line_chart_exchange = '';
choose_chart = '';
bubble_chart = '';
quick_chart = '';
heap_chart = '';
merge_chart = '';
insert_chart = '';

shell_chart = '';
radix_chart = '';
binaryInsert_chart = '';
coaktail_chart = '';

baseline_n2 = [];
baseline_nlog = [];
result_seq = [];  //获取后台传回的单个生成序列
result_sort = []; //获取后台传回的排序后序列和比较次数以及移动次数
analyze_test_change = []; //获取后台传回的比较次数、移动次数拟合获得的系数和均方差，以及拟合多项式计算结果
progressBar = "<div class='progress-bar  bg-success progress-bar-striped progress-bar-animated' style='width:10%;border-radius: 2px;'></div>";

$(function () {
    initPanel();
    $(".btn-cal").click(function () {
        pagetoggle();
    });
    $(".btn-analyze").click(function () {
        pagetoggle();
    });
    $(".btn-generate-data").click(function () {
        cal_cap_n = $("#cal-cap-n").val();
        range_method = $("#cal-data-permtt-method").val();
        $(".btn-start-sort").hide();
        $('.genearte-data-progress').append(progressBar);
        progress = 10;
        var i=setInterval(function(){
            progress+=2;
            $('.progress-bar').css('width',progress+'%');
            if(progress==94){
                i=window.clearInterval(i);
            }
        },500);
        $.ajax({
            url: "/result_seq_test",   //对应flask中的路由
            type: "GET", //请求方法，算法分析不涉及保密和安全，使用get请求测试比较方便
            data: {
                cal_cap_n:cal_cap_n,
                range_method:range_method
            }, //传送的数据
            success: function (data) {  //成功得到返回数据后回调的函数 data与app.py中的result_seq_json一致
                result_seq = data
                window.clearInterval(i);
                $('.progress-bar').css('width', '100%');
                setTimeout(function () {
                    $('.progress-bar').remove();
                    show_cal_test_data(cal_cap_n, range_method)
                    $(".btn-start-sort").show();
                },1000);
            }
        })
    });
    $(".btn-start-sort").click(function () {
        cal_test_data = result_seq;
        $('.sort-progress').append(progressBar);
        progress = 10;
        var i=setInterval(function(){
            progress+=2;
            $('.progress-bar').css('width',progress+'%');
            if(progress==94){
                i=window.clearInterval(i);
            }
        },500);
        $.ajax({
            url: "/sort_result_test",   //对应flask中的路由
            type: "GET", //请求方法
            data: {
                cal_test_data:cal_test_data
            }, //传送的数据
            success: function (data) {  //成功得到返回数据后回调的函数 data与app.py中的test_sort_result一致
                result_sort = data;
                window.clearInterval(i);
                $('.progress-bar').css('width', '100%');
                setTimeout(function () {
                    $('.progress-bar').remove();
                    show_sort_result(cal_test_data);
                    $(".btn-start-sort").hide();
                },1000);
            }
        })

    });
    $(".btn-start-analyze").click(function () {
        analyze_max_n = $("#analyze-max-n").val();
        analyze_data_method = $("#analyze-data-permtt-method").val();
        console.log('method'+analyze_data_method)
        $('.start-analyze-progress').append(progressBar);
        progress = 10;
        var i=setInterval(function(){
            progress+=2;
            $('.progress-bar').css('width',progress+'%');
            if(progress==94){
                i=window.clearInterval(i);
            }
        },500);
        $.ajax({
            url: "/result_seq_analyze",   //对应flask中的路由
            type: "GET", //请求方法
            data: {
                analyze_max_n:analyze_max_n,
                analyze_data_method:analyze_data_method
            }, //传送的数据
            success: function (data) {  //成功得到返回数据后回调的函数 data与app.py中的test_time_two_total_json一致
                window.clearInterval(i);
                $('.progress-bar').css('width', '100%');
                setTimeout(function () {
                    $('.progress-bar').remove();
                    analyze_test_change = data
                    show_analyze_result()
                },1000);
            }
        })

    })
});

function show_cal_test_data(cal_cap_n, range_method) {

    cal_test_data = get_cal_test_data(cal_cap_n, range_method);

    $(".show-test-data").html(cal_test_data.toString());
}
//从后台读取规模为n，排列方式为range_method的测试数据
function get_cal_test_data(cal_cap_n, range_method) {
    console.log("n: "+cal_cap_n+" ; method: "+range_method);
    //将string类型的json转化为数组类型的
    test_for_cal_test_data = JSON.parse(result_seq);
    return test_for_cal_test_data;
}

function show_sort_result(cal_test_data) {
    sort_result = get_sort_results(cal_test_data);
    len = cal_test_data.length
    $("#sort-times").bootstrapTable("removeAll");
    for(i=0; i<len; i++){
        $(".sort-result").eq(i).html(sort_result[i][0].toString());
        $("#sort-times").bootstrapTable('insertRow',{index:i,row:[sort_names[i],
                sort_result[i][1],sort_result[i][2]]});
    }
}
//从后台获取cal_test_data的排序结果
//注意顺序：选择排序,冒泡排序,快速排序,堆排序,归并排序,插入排序
function get_sort_results(cal_test_data) {
    test_for_sort_result = JSON.parse(result_sort);
    return test_for_sort_result;
}

function show_analyze_result(max_n, data_method) {
    analyze_result = get_analyze_result(max_n, data_method);
    test_for_baseline_n2 = [];
    test_for_baseline_nlogn = [];

    //whf add
    analyze_result_compare = analyze_result[0];
    analyze_result_excahnge = analyze_result[1];

    compareNum_len = analyze_result[0].length
    exchangeNum_len = analyze_result[1].length

    for (i = 0; i <= analyze_result_compare[5][3].length; i++){
        test_for_baseline_n2.push(i*i);
        test_for_baseline_nlogn.push((i*Math.log2(i)).toFixed(2))
    }

    baseline_n2 = get_base_line(analyze_result_compare[0][2])[0];
    baseline_nlog = get_base_line(analyze_result_compare[0][2])[1];
    $("#compare-analyze").bootstrapTable("removeAll");
    $("#exchange-analyze").bootstrapTable("removeAll");
    for(i=0; i<compareNum_len; i++){
        $("#compare-analyze").bootstrapTable("insertRow", {index:i, row:[sort_names[i],
                get_polynomial(analyze_result_compare[i][0][0], analyze_result_compare[i][0][1], analyze_result_compare[i][0][2]),
                analyze_result_compare[i][1]]});
        $("#exchange-analyze").bootstrapTable("insertRow", {index:i, row:[sort_names[i],
                get_polynomial(analyze_result_excahnge[i][0][0], analyze_result_excahnge[i][0][1], analyze_result_excahnge[i][0][2]),
                analyze_result_excahnge[i][1]]})
    }

    //whf add
    option = create_option(['选择排序', '冒泡排序', '快速排序', '堆排序', '归并排序', '插入排序',"希尔排序","基数排序","二分插入排序","鸡尾酒排序", 'n^2', 'nlogn'],
        analyze_result_compare[0][2], [
            analyze_result_compare[0][3],
            analyze_result_compare[1][3],
            analyze_result_compare[2][3],
            analyze_result_compare[3][3],
            analyze_result_compare[4][3],
            analyze_result_compare[5][3],
            analyze_result_compare[6][3],
            analyze_result_compare[7][3],
            analyze_result_compare[8][3],
            analyze_result_compare[9][3],
            baseline_n2, baseline_nlog
        ], '输入的运算规模 n ', '算法的比较次数');
    all_line_chart_compare.clear();
    all_line_chart_compare.setOption(option);
    x_data = analyze_result_excahnge[0][2];
    legend = ['比较次数', '交换次数', 'n^2', 'nlogn'];

    //whf add
    option = create_option(['选择排序', '冒泡排序', '快速排序', '堆排序', '归并排序', '插入排序', "希尔排序","基数排序","二分插入排序","鸡尾酒排序", 'n^2', 'nlogn'],
        x_data, [
            analyze_result_excahnge[0][3],
            analyze_result_excahnge[1][3],
            analyze_result_excahnge[2][3],
            analyze_result_excahnge[3][3],
            analyze_result_excahnge[4][3],
            analyze_result_excahnge[5][3],
            analyze_result_excahnge[6][3],
            analyze_result_excahnge[7][3],
            analyze_result_excahnge[8][3],
            analyze_result_excahnge[9][3],
            baseline_n2, baseline_nlog
        ], '输入的运算规模 n ', '算法的交换次数');
    all_line_chart_exchange.clear();
    all_line_chart_exchange.setOption(option);

    option = create_option(legend, x_data, [analyze_result_compare[0][5], analyze_result_excahnge[0][5],
        baseline_n2, baseline_nlog
    ], '选择排序的输入规模 n', '基本运算次数');
    choose_chart.clear();
    choose_chart.setOption(option);

    option = create_option(legend, x_data, [analyze_result_compare[1][5], analyze_result_excahnge[1][5],
        baseline_n2, baseline_nlog
    ], '冒泡排序的输入规模 n', '基本运算次数');
    bubble_chart.clear();
    bubble_chart.setOption(option);

    option = create_option(legend, x_data, [analyze_result_compare[2][5], analyze_result_excahnge[2][5],
        baseline_n2, baseline_nlog
    ], '快速排序的输入规模 n', '基本运算次数');
    quick_chart.clear();
    quick_chart.setOption(option);

    option = create_option(legend, x_data, [analyze_result_compare[3][5], analyze_result_excahnge[3][5],
        baseline_n2, baseline_nlog
    ], '堆排序的输入规模 n', '基本运算次数');
    heap_chart.clear();
    heap_chart.setOption(option);

    option = create_option(legend, x_data, [analyze_result_compare[4][5], analyze_result_excahnge[4][5],
        baseline_n2, baseline_nlog
    ], '归并排序的输入规模 n', '基本运算次数');
    merge_chart.clear();
    merge_chart.setOption(option);

    option = create_option(legend, x_data, [analyze_result_compare[5][5], analyze_result_excahnge[5][5],
        baseline_n2, baseline_nlog
    ], '插入排序的输入规模 n', '基本运算次数');
    insert_chart.clear();
    insert_chart.setOption(option)

    //whf add

    option = create_option(legend, x_data, [analyze_result_compare[6][5], analyze_result_excahnge[6][5],
        baseline_n2, baseline_nlog
    ], '希尔排序的输入规模 n', '基本运算次数');
    shell_chart.clear();
    shell_chart.setOption(option);

    option = create_option(legend, x_data, [analyze_result_compare[7][5], analyze_result_excahnge[7][5],
        baseline_n2, baseline_nlog
    ], '基数排序的输入规模 n', '基本运算次数');
        radix_chart.clear();
    radix_chart.setOption(option);

    option = create_option(legend, x_data, [analyze_result_compare[8][5], analyze_result_excahnge[8][5],
        baseline_n2, baseline_nlog
    ], '二分插入排序的输入规模 n', '基本运算次数');
    binaryInsert_chart.clear();
    binaryInsert_chart.setOption(option);

    option = create_option(legend, x_data, [analyze_result_compare[9][5], analyze_result_excahnge[9][5],
        baseline_n2, baseline_nlog
    ], '鸡尾酒排序的输入规模 n', '基本运算次数');
    coaktail_chart.clear();
    coaktail_chart.setOption(option);

}
//从后台读取最大规模为max_n，排列方式为data_method的数据分析结果
//注意顺序：选择排序,冒泡排序,快速排序,堆排序,归并排序,插入排序
function get_analyze_result(max_n, data_method) {
    test_for_analyze_result = JSON.parse(analyze_test_change)
    return test_for_analyze_result
}
function get_polynomial (a1, a2, a3) {
    if(a2 < 0)
        return a1+"*a<sup>2</sup>"+a2+"*a+"+a3;
    else if(a3 < 0)
        return a1+"*a<sup>2</sup>+"+a2+"*a"+a3;
    else if(a2 < 0 && a3 <0)
        return a1+"*a<sup>2</sup>"+a2+"*a"+a3;
    else
        return a1+"*a<sup>2</sup>+"+a2+"*a+"+a3;
}
function create_option(legend, x_data, y_data_list, x_label, y_label) {
    data_series = [];
    for(i=0; i<legend.length; i++){
        data_series[i] = {
            name: legend[i],
            type:'line',
            stack:'',
            data:y_data_list[i],
            symbolSize: 0
        }
    }
    data_series[legend.length-2]['lineStyle']={
        width:'2',
        type: 'dashed'
    };
    data_series[legend.length-1]['lineStyle']={
        width:'2',
        type: 'dashed'
    };
    return {
        tooltip: {
            trigger: 'axis'
        },
        legend: {
            data: legend
        },
        grid: {
            left: 20,
            right: '4%',
            bottom: 30,
            containLabel: true
        },
        toolbox: {
            feature: {
                saveAsImage: {title: 'save'},
                dataView: {title: 'data'}
            },
            right: 0,
            top: 18
        },
        xAxis: {
            type: 'category',
            boundaryGap: false,
            data: x_data,
            name: x_label,
            position: 'bottom',
            nameLocation: 'middle',
            nameGap: 30
        },
        yAxis: {
            type: 'value',
            name: y_label,
            position: 'left',
            nameLocation: 'middle',
            nameGap: 35,
            nameRotate: 90
        },
        series:data_series
    }
}
function get_base_line(x_series) {
    return [test_for_baseline_n2, test_for_baseline_nlogn];
}

function initPanel() {
    if (curpage==0){
        $(".btn-cal").css({
            color: "#666"
        });
        $(".btn-analyze").css({
            color: "#ccc"
        });
        $(".analyze").hide();
    }
    $(".btn-start-sort").hide();
    all_line_chart_compare = echarts.init(document.getElementById("all-sort-compare-times"));
    all_line_chart_exchange = echarts.init(document.getElementById("all-sort-excahnge-times"))
    choose_chart = echarts.init(document.getElementById("line-chart-choose"));
    bubble_chart = echarts.init(document.getElementById("line-chart-bubble"));
    quick_chart = echarts.init(document.getElementById("line-chart-quick"));
    heap_chart = echarts.init(document.getElementById("line-chart-heap"));
    merge_chart = echarts.init(document.getElementById("line-chart-merge"));
    insert_chart = echarts.init(document.getElementById('line-chart-insert'));


    shell_chart = echarts.init(document.getElementById("line-chart-shell"));
    radix_chart = echarts.init(document.getElementById("line-chart-radix"));
    binaryInsert_chart = echarts.init(document.getElementById("line-chart-binaryInsert"));
    coaktail_chart = echarts.init(document.getElementById('line-chart-coaktail'));
}

function pagetoggle() {
    if (curpage==0){
        curpage=1;
        $(".analyze").show();
        $(".cal").hide();
        $(".btn-cal").css({
            color: "#ccc"
        });
        $(".btn-analyze").css({
            color: "#666"
        });
        return;
    }
    if (curpage==1){
        curpage=0;
        $(".cal").show();
        $(".analyze").hide();
        $(".btn-cal").css({
            color: "#666"
        });
        $(".btn-analyze").css({
            color: "#ccc"
        });
    }
}