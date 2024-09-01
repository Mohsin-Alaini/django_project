function print_error_forms(forms, prefix1=null, is_formset=false) {
    $.each(forms, function(i1, form) {
        console.log(form)
        let error_form = JSON.parse(form.errors);
        $.each(error_form, function(i, value) {
            let div = '<span class="text-danger" >';
            $.each(value, function(j, message) {
                div += `${message.message} <br>`;
            });
            var id_field = "#id_"
            if (prefix1 != null){
                id_field += prefix1 +"-"
            }
            if (is_formset == true){
                id_field += form.row + "-"
            }
            id_field += i
            div += "</span>"
            if(i == "__all__"){

                $(id_field).parent().parent().find("td:eq('0')").append(div);
            }else{

                $(id_field).parent().append(div);
            }

        });
    });

}
