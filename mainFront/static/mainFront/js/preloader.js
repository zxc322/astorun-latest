window.onload = function(){

    setTimeout(function(){
        let preloader = document.getElementById('page-preloader')
        if  (!preloader.classList.contains('preloader-done')){
            preloader.classList.add('preloader-done')
        }
    }, 300)

}
