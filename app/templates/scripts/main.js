
var get_and_set_data_for_select2 = function(params) {
  return new Promise(function(resolve, reject) {
    params.obj.empty();
    get_ajax_generic(params.url).then(function(result) {
      result.map(function(result_item) {
        var item = result_item.attributes;
        item.id = result_item.id;
        params.obj.append('<option value="' + item[params.id] + (params.valsecound? ('___' + (item[params.valsecound]?item[params.valsecound]:params.valsecound) + ''):'') + '"' +
        '>' + (params.function_name ? params.function_name(item) : item[params.text]) + '</option>');
      });
      var params_select2 = {
        language: 'es',
        width: params.width ? params.width : '100%',
        placeholder: params.placeholder,
        multiple: params.multiple ? params.multiple : false,
        allowClear: params.allowClear ? params.allowClear : false
      };
      if (params.dropdownParent) {
        params_select2.dropdownParent = params.dropdownParent;
      }
      params.obj.select2(params_select2);

      if (typeof params.isChangeNull != 'undefined') {
        if (params.isChangeNull) {
          params.obj.val(params.changeNull).trigger('change');
        }
      } else {
        params.obj.val(null).trigger('change');
      }
      resolve(true);
    });
  });
};


var get_ajax_generic = function(url) {
  return new Promise(function(resolve, reject) {
    $.ajax({
      url: url,
      success: function(data) {
        resolve(data);
      },
      error: function(e) {
        reject(e);
      }
    });
  });
};

var post_ajax_generic = function(url, data) {
  return new Promise(function(resolve, reject) {
    $.ajax({
      url: url,
      data: JSON.stringify(data),
      datatype: 'json',
      type: 'POST',
      contentType: "application/json",
      headers: {
        'Content-Type': 'application/json'
      },
      success: function(data) {
        resolve(data);
      },
      error: function(e) {
        console.info(e);
        reject(e);
      }
    });
  });
};


var delete_ajax_generic = function(url) {
  return new Promise(function(resolve, reject) {
    $.ajax({
      url: url,
      type: 'DELETE',
      headers: {
        'Content-Type': 'application/json'
      },
      success: function(data) {
        resolve(data);
      },
      error: function(e) {
        reject(e);
      }
    });
  });
};