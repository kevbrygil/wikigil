var form_product = $('#form_product');
var currency_default = 'MXN';

var first_page_and_reload_table = function(){
    $('#table_product').DataTable().page(0);
    $('#table_product').DataTable().ajax.reload();
};

$('#btn_new_product').click(function() {
    var data_product = {
        data:{
            attributes:{
                name: form_product.find('[name="name"]').val(),
                sku: form_product.find('[name="sku"]').val(),
                price: form_product.find('[name="price"]').val(),
                size: form_product.find('[name="size"]').val()
            }
        }, 
        type: 'product'
    };

    if (data_product.data.attributes.name.length > 0 && data_product.data.attributes.sku.length > 0 && 
        data_product.data.attributes.price.length > 0 && data_product.data.attributes.size.length > 0 && 
        !isNaN(data_product.data.attributes.price)) {
        post_ajax_generic('/api/products.json', data_product).then(function(data) {
          toastr.success('Se agregó una tienda.');
          $('#modal_product').modal('hide');
          form_product[0].reset();
          first_page_and_reload_table();
        }).catch(function(e) {
          toastr.error('Ocurrio un error, asegurese de introducir correctamente los datos');
        });
    } else {
      toastr.info('Todos los campos son obligatorios.');
      if(!isNaN(data_product.data.attributes.price)) toastr.info('El campo Precio debe ser un Número.');
    }
});

var handleTable = function() {
    $('#table_product').dataTable({
        'ajax': {
            'url': '/api/products.json',
            'type': 'GET',
            'dataSrc': '',
        },
        'columns': [
            {data: 'id', title:'#'},
            {data: 'attributes.name', title:'Nombre'},
            {data: 'attributes.sku', title:'SKU'},
            {
                data: 'attributes.price', title:'Precio', 
                render: function(data, status,row){
                    return '$' + data + ' ' + currency_default;
                }
            },
            {data: 'attributes.size', title:'Tamaño'},
            {   
                title:'Acciones', 
                render: function(data, status,row){
                    var html_action =
                    '<div class="row">'+
                    '        <a class="btn col-md-3 text-info" id="update_'+row.id+'" href="#" data-toggle="tooltip_table" title="Modificar">'+
                    '            <i class="fas fa-edit" aria-hidden="true" ></i>'+
                    '        </a>'+
                    '        <a class="btn col-md-3 text-danger" id="delete_'+row.id+'" href="#" data-toggle="tooltip_table" title="Eliminar">'+
                    '            <i class="fas fa-trash-alt" aria-hidden="true" ></i>'+
                    '        </a>'+
                    '</div>';
                    return html_action;
                }
            }
        ],
        'language': {
            url: 'https://cdn.datatables.net/plug-ins/1.10.24/i18n/Spanish.json'
        },
        'pageLength': 25,
        'lengthMenu': [10,25,50,75,100],
        'ordering': false,
    }).on( 'draw.dt', function () {
        $('[data-toggle="tooltip_table"]').tooltip();
        $('[id^="delete_"]').click(function(e){
            delete_ajax_generic('/api/products/' + this.id.split('_')[1] + '.json').then(function(data_ajax) {
                toastr.success('Se Eliminó el producto correctamente.');
                first_page_and_reload_table();
              }).catch(function(e) {
                toastr.error('Ocurrio un error al querer eliminar el producto.');
              });
        });
    });
};

$(document).ready(function() {
    handleTable();
    $('[data-toggle="tooltip"]').tooltip();
});