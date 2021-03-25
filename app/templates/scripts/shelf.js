var form_shelf = $('#form_shelf');

var first_page_and_reload_table = function(){
    $('#table_shelf').DataTable().page(0);
    $('#table_shelf').DataTable().ajax.reload();
};

$('#btn_new_shelf').click(function() {
    var data_shelf = {
        data:{
            attributes:{
                name: form_shelf.find('[name="name"]').val(),
                capacity: form_shelf.find('[name="capacity"]').val(),
                latitude: form_shelf.find('[name="latitude"]').val(),
                longitude: form_shelf.find('[name="longitude"]').val(),
                storeid: form_shelf.find('[name="storeid"]').val()
            }
        }, 
        type: 'shelf'
    };

    if (data_shelf.data.attributes.name.length > 0 && data_shelf.data.attributes.capacity.length > 0 && 
        data_shelf.data.attributes.storeid) {
        post_ajax_generic('/api/shelfs.json', data_shelf).then(function(data) {
          toastr.success('Se agregó una tienda.');
          $('#modal_shelf').modal('hide');
          form_shelf[0].reset();
          first_page_and_reload_table();
        }).catch(function(e) {
          toastr.error('Ocurrio un error, asegurese de introducir correctamente los datos.');
        });
    } else {
      toastr.info('El campo nombre, capacidad y tienda son obligatorios.');
    }
});

var handleTable = function() {
    $('#table_shelf').dataTable({
        'ajax': {
            'url': '/api/shelfs.json',
            'type': 'GET',
            'dataSrc': '',
        },
        'columns': [
            {data: 'id', title:'#'},
            {data: 'attributes.name', title:'Nombre'},
            {data: 'attributes.capacity', title:'Capacidad'},
            {
                data: 'attributes.latitude', title:'Coordenadas', 
                render: function(data, status,row){
                    return '(' + row.attributes.latitude + ',' + row.attributes.longitude + ')';
                }
            },
            {data: 'attributes.store.data.attributes.name', title:'Tienda'},
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
            delete_ajax_generic('/api/shelfs/' + this.id.split('_')[1] + '.json').then(function(data_ajax) {
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
    placeholder: 'Almacen',
    multiple: false,
    dropdownParent: $('#modal_shelf')
}).then(function (data) { });

/*
$('#country').on('change', function (e) {
    if ($(this).val()) {
        get_and_set_data_for_select2({
            url: URL_ROOT + '/servicio/estados',
            obj: $('#state'),
            id: 'id',
            text: 'nombre',
            placeholder: 'Estado',
            multiple: false,
            dropdownParent: $('#modal_user')
        }).then(function () {
            $('#city').empty();
        });
    } 
});

$('#state').on('change', function (e) {
    if ($(this).val()) {
        get_and_set_data_for_select2({
            url: URL_ROOT + '/servicio/ciudades',
            obj: $('#city'),
            id: 'id',
            text: 'nombre',
            placeholder: 'Ciudad',
            multiple: false,
            dropdownParent: $('#modal_user')
        }).then(function () {
        });
    } 
});*/