$(function() {
    $('#add-term').click(function() {
        var $gene = $('#gene-input');
        var $weight = $('#weight-input');
        if ($gene.val().length < 1) return;
        $.get('/engine/gene_card/' + $gene.val().toUpperCase() + '/' + $weight.val(), function(data){
            $(data).appendTo($('#cards-holder'));
            $gene.val('').focus();
            $weight.val('1');
        });
    });

    $('.delete-gene-card').click(function() {
        $(this).parents('.gene-card').remove();
    });

    $('#search-btn').click(function() {
        var queryJSON = {};
        $('.gene-card').each(function() {
            console.log($(this));
            queryJSON[$(this).data('gene')] = parseInt($(this).data('weight'));
        });
        var queryString = JSON.stringify(queryJSON);
        $('#results-area').empty().append($('<p>').text('Getting search results...'));
        $.get('/engine/search/' + queryString + '/', function(data) {
            $('#results-area').empty().append($(data));
        });
    });
});