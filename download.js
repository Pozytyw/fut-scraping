() => {
    var link = document.createElement('a');
    link.download = file_name;
    link.href = document.getElementById('output').toDataURL()
    link.click();
}