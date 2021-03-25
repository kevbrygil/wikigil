var form_store = $('#form_store');

var first_page_and_reload_table = function(){
    $('#table_store').DataTable().page(0);
    $('#table_store').DataTable().ajax.reload();
};

$('#btn_new_store').click(function() {
    var data_store = {
        data:{
            attributes:{
                name: form_store.find('[name="name"]').val(),
                address: form_store.find('[name="address"]').val(),
                latitude: form_store.find('[name="latitude"]').val(),
                longitude: form_store.find('[name="longitude"]').val()
            }
        }, 
        type: 'store'
    };

    if (data_store.data.attributes.name.length > 0 && data_store.data.attributes.address.length > 0) {
        post_ajax_generic('/api/stores.json', data_store).then(function(data) {
          toastr.success('Se agregó una tienda.');
          $('#modal_store').modal('hide');
          form_store[0].reset();
          first_page_and_reload_table();
        }).catch(function(e) {
          toastr.error('Ocurrio un error, asegurese de introducir correctamente los datos.');
        });
    } else {
      toastr.info('El campo nombre y dirección son obligatorios.');
    }
});

var handleTable = function() {
    $('#table_store').dataTable({
        'ajax': {
            'url': '/api/stores.json',
            'type': 'GET',
            'dataSrc': '',
        },
        'columns': [
            {data: 'id', title:'#'},
            {data: 'attributes.name', title:'Nombre'},
            {data: 'attributes.address', title:'Dirección'},
            {
                data: 'attributes.latitude', title:'Coordenadas', 
                render: function(data, status,row){
                    return '(' + row.attributes.latitude + ',' + row.attributes.longitude + ')';
                }
            },
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
    });
};

$(document).ready(function() {
    handleTable();
    $('[data-toggle="tooltip"]').tooltip();
});

/*get_and_set_data_for_select2({
    url: URL_ROOT + '/servicio/paises',
    obj: $('#country'),
    id: 'id',
    text: 'nombre',
    placeholder: 'Pais',
    multiple: false,
    dropdownParent: $('#modal_user')
}).then(function (data) { });

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