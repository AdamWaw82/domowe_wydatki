$( document ).ready(function() {

$.get( "/api/v1/wydatki/", function( data ) {
 data = JSON.parse(data)
 listBody = $("#listBody")
 html = ""
    for (i in data) {
        html += "<tr><td>"+data[i].date+"</td><td>"+data[i].kategoria+"</td><td>"+data[i].opis+"</td><td>"+data[i].kwota+"</td><td>" +
                "<button class='btn btn-info btn-sm' data-toggle='modal' data-target='#viewExpenseModal'    data-index='"+i+"'>Podgląd</button>"+
                "<button class='btn btn-primary btn-sm' data-toggle='modal' data-target='#editExpenseModal' data-index='"+i+"'>Edytuj</button>"+
                "<button class='btn btn-danger btn-sm'  data-toggle='modal' data-target='#deleteExpenseModal' data-index='"+i+"' >Usuń</button>"+
            "</td></tr>"

    }
listBody.html(html)
});


$("#deleteExpenseForm").on("submit", function(event){
    event.preventDefault();
    var button = $("#deleteSubmit");
    var index = button.data('index');
    var modal = $(this);

    $.ajax({
       url: '/api/v1/wydatki/' + index,
       type: 'DELETE',
       success: function(response) {
            if (response.result)
                window.location.reload();
       }
    });
})

$("#editExpenseForm").on("submit", function(event){
    event.preventDefault();
    var button = $("#editSubmit");
    var index = button.data('index');
    var modal = $(this);

    var data_serialize = $(this).serializeArray()
    var data = {}
    for (i in data_serialize){
        data[data_serialize[i]["name"]] = data_serialize[i]["value"]
    }

    $.ajax({
       url: '/api/v1/wydatki/' + index,
       type: 'PUT',
       contentType: "application/json",
       data: JSON.stringify(data),
       success: function(response) {
            if (response.result)
                window.location.reload();
       }
    });
})


$('#viewExpenseModal').on('show.bs.modal', function (event) {
    var button = $(event.relatedTarget);
    var index = button.data('index');
    var modal = $(this);
    $.get( "/api/v1/wydatki/"+index, function( data ) {
        wydatek = JSON.parse(data)
        modal.find('#viewDate').text(wydatek.date);
        modal.find('#viewCategory').text(wydatek.kategoria);
        modal.find('#viewDescription').text(wydatek.opis);
        modal.find('#viewAmount').text(wydatek.kwota);

    })
});

$('#editExpenseModal').on('show.bs.modal', function (event) {
    var button = $(event.relatedTarget);
    var index = button.data('index');
    var modal = $(this);
    $.get( "/api/v1/wydatki/"+index, function( data ) {
        wydatek = JSON.parse(data)
        modal.find('#editDate').val(wydatek.date);
        modal.find('#editCategory').val(wydatek.kategoria);
        modal.find('#editDescription').val(wydatek.opis);
        modal.find('#editAmount').val(wydatek.kwota);
        modal.find('#editSubmit').attr('data-index', index);
    })
});


$('#deleteExpenseModal').on('show.bs.modal', function (event) {

    var button = $(event.relatedTarget);
    var index = button.data('index');
    var modal = $(this);

    $.get( "/api/v1/wydatki/"+index, function( data ) {
        wydatek = JSON.parse(data)
        modal.find('#deleteDate').text(wydatek.date);
        modal.find('#deleteCategory').text(wydatek.kategoria);
        modal.find('#deleteDescription').text(wydatek.opis);
        modal.find('#deleteAmount').text(wydatek.kwota);
        modal.find('#deleteSubmit').attr('data-index', index);

    })

});
});