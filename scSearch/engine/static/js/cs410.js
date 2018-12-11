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
});