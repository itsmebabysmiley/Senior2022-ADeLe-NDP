document.getElementById('upload_file').addEventListener('click', uploadFile);
function uploadFile(){
    document.getElementById('html-input-file-btn').click();
}
document.getElementById('take_photo').addEventListener('click', takePhoto);
function takePhoto(){
    document.getElementById('html-take-photo-btn').click();
}
async function loadFile(event) {
    document.getElementById('html-submit-btn').click();
    

}
