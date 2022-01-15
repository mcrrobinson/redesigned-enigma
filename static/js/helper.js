function return_selected_radio_button(buttons){
    for(var i=0; i<buttons.length; i++){
        if(buttons[i].checked){
            return buttons[i].value;
        }
    }
}