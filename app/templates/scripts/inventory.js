var form_inventory = $('#form_inventory');

var first_page_and_reload_table = function(){
    $('#table_inventory').DataTable().page(0);
    $('#table_inventory').DataTable().ajax.reload();
};

$('#btn_new_inventory').click(function() {
    var data_inventory = {
        data:{
            attributes:{
                name: form_inventory.find('[name="name"]').val(),
                stock: form_inventory.find('[name="stock"]').val(),
                shelfcount: form_inventory.find('[name="shelfcount"]').val(),
                storeid: form_inventory.find('[name="storeid"]').val(),
                productid: form_inventory.find('[name="productid"]').val(),
                shelfid: form_inventory.find('[name="shelfid"]').val(),
            }
        }, 
        type: 'inventory'
    };

    if (data_inventory.data.attributes.name.length > 0 && !isNaN(data_inventory.data.attributes.stock) && 
        data_inventory.data.attributes.storeid && data_inventory.data.attributes.productid) {
        post_ajax_generic('/api/inventoryitems.json', data_inventory).then(function(data) {
          toastr.success('Se agregó un nuevo inventario.');
          $('#modal_inventory').modal('hide');
          form_inventory[0].reset();
          first_page_and_reload_table();
        }).catch(function(e) {
          toastr.error('Ocurrio un error, asegurese de introducir correctamente los datos.');
        });
    } else {
      toastr.info('Asegurese de introducir bien los datos.');
    }
});

var handleTable = function() {
    $('#table_inventory').dataTable({
        'ajax': {
            'url': '/api/inventoryitems.json',
            'type': 'GET',
            'dataSrc': '',
        },
        'columns': [
            {data: 'id', title:'#'},
            {data: 'attributes.name', title:'Nombre'},
            {data: 'attributes.stock', title:'Existencia'},
            {data: 'attributes.shelfcount', title:'Capacidad'},
            {data: 'attributes.product.data.attributes.name', title:'Producto'},
            {data: 'attributes.store.data.attributes.name', title:'Tienda'},
            {data: 'attributes.shelf.data.attributes.name', title:'Almacen'},
            {   
                title:'Acciones', 
                render: function(data, status,row){
                    var html_action =
                    '<div class="row">'+
                    '        <a class="btn col-md-3 text-info" id="update_'+row.id+'" href="" data-toggle="tooltip_table" title="Modificar">'+
                    '            <i class="fas fa-edit" aria-hidden="true" ></i>'+
                    '        </a>'+
                    '        <a class="btn col-md-3 text-danger" id="delete_'+row.id+'" href="" data-toggle="tooltip_table" title="Eliminar">'+
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
            delete_ajax_generic('/api/inventoryitems/' + this.id.split('_')[1] + '.json').then(function(data_ajax) {
                toastr.success('Se Eliminó el almacen correctamente.');
                first_page_and_reload_table();
              }).catch(function(e) {
                toastr.error('Ocurrio un error al querer eliminar el almacen.');
              });
        });
    });
};

$(document).ready(function() {
    handleTable();
    $('[data-toggle="tooltip"]').tooltip();
});

get_and_set_data_for_select2({
    url: '/api/stores.json',
    obj: $('#storeid'),
    id: 'id',
    text: 'name',
    placeholder: 'Tienda',
    multiple: false,
    dropdownParent: $('#modal_inventory')
}).then(function (data) { });

get_and_set_data_for_select2({
    url: '/api/products.json',
    obj: $('#productid'),
    id: 'id',
    text: 'name',
    placeholder: 'Producto',
    multiple: false,
    dropdownParent: $('#modal_inventory')
}).then(function (data) { });

get_and_set_data_for_select2({
    url: '/api/shelfs.json',
    obj: $('#shelfid'),
    id: 'id',
    text: 'name',
    placeholder: 'Almacen',
    multiple: false,
    dropdownParent: $('#modal_inventory')
}).then(function (data) { });