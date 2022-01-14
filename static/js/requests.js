function popupate_with_files() {
    var content_div = document.getElementById('content');
    if(content_div === 'undefined'){
        console.log("The content div is undefined, so we can't populate it with files.");
        return;
    }
    var xhr = new XMLHttpRequest();
    xhr.addEventListener('load', function(){
        json_response = JSON.parse(this.responseText);
        json_response.forEach(element => {
            var file_div = document.createElement('div');
            file_div.className = 'file';
            file_div.innerHTML = '<a href="' + element + '">' + element + '</a>';
            content_div.appendChild(file_div);
        });
    })
    xhr.open('GET', '/api/files', true);
    xhr.send();
}

function populate_with_content(file_name, buffer) {
    var xhr = new XMLHttpRequest();
    xhr.addEventListener('load', function(){
        var file_div = document.getElementById('content');
        file_div.innerHTML += JSON.parse(this.responseText);
    });
    xhr.open('GET', '/api/' + file_name + '/content/' + buffer, true);
    xhr.send();
}