function fill_forms(data, prefix1 = null, is_formset = false,is_mean=false) {
    var data1 = JSON.parse(data)
    if (is_formset == true) {

        $(`#id_${prefix1}-INITIAL_FORMS`).val(data1.length);
        $(`#${prefix1}_table`).find(".delete-row").click();
    }

    $.each(data1, function (counter, data2) {
        var id_field = "#id_"
        if (prefix1 != null) {

            id_field += prefix1 + "-"
        }
        if (is_formset == true) {
            id_field += counter + "-";
            
            $(`#${prefix1}_table`).find(".add-row").click();
        }
        try {
            if (is_mean){
                $(`[name=id]`).val(data2.pk)

            }
            $(id_field + `id`).val(data2.pk)
        } catch (e) {

        }
        $.each(data2.fields, function (field_name, field_value) {

            if ($(`select[id=${id_field.split("#")[1]}${field_name}]`).length > 0 && $(`${id_field}${field_name}`).data("autocomplete-light-url") != undefined) {
                $(`${id_field}${field_name}`).find("option").remove()
                $(`${id_field}${field_name}`).append(`<option selected value=${field_value}>${field_value}<option/>`)
            } else {
                $(`${id_field}${field_name}`).val(field_value)

            }
        });
    });

}
