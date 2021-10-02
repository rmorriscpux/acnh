$(document).ready(function(){
    console.log(critterType);
    $("div.graphic-box").hover(function(){
        var tooltip = $(this).find("span.critter-tooltip");
        var image = $(this).find("img.critter");
        // Pull critter info from the database and place it in the associated tooltip span.
        tooltip.load("./critter_info/", {
            csrfmiddlewaretoken : $("input[name='csrfmiddlewaretoken']").val(), 
            name : image.attr('alt')
        });
        tooltip.show();
    }, function(){
        var tooltip = $(this).find("span.critter-tooltip");
        tooltip.html("");
        tooltip.hide();
    });
});