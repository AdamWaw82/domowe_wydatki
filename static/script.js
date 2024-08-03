$( document ).ready(function() {
$('#viewExpenseModal').on('show.bs.modal', function (event) {
        var button = $(event.relatedTarget);
        var date = button.data('date');
        var category = button.data('category');
        var description = button.data('description');
        var amount = button.data('amount');

        var modal = $(this);
        modal.find('#viewDate').text(date);
        modal.find('#viewCategory').text(category);
        modal.find('#viewDescription').text(description);
        modal.find('#viewAmount').text(amount);
    });

    $('#editExpenseModal').on('show.bs.modal', function (event) {
        var button = $(event.relatedTarget);
        var date = button.data('date');
        var category = button.data('category');
        var description = button.data('description');
        var amount = button.data('amount');
        var index = button.data('index');

        var modal = $(this);
        modal.find('#editDate').val(date);
        modal.find('#editCategory').val(category);
        modal.find('#editDescription').val(description);
        modal.find('#editAmount').val(amount);
        modal.find('[name=index]').val(index);
    });


    $('#deleteExpenseModal').on('show.bs.modal', function (event) {

        var button = $(event.relatedTarget);
        var date = button.data('date');
        var category = button.data('category');
        var description = button.data('description');
        var amount = button.data('amount');
        var index = button.data('index');


        var modal = $(this);
        modal.find('#deleteDate').text(date);
        modal.find('#deleteCategory').text(category);
        modal.find('#deleteDescription').text(description);
        modal.find('#deleteAmount').text(amount);
        modal.find('[name=index]').val(index);

    });
});