$(document).ready(function(){
    $('.btn-menu').click(function(){
        $('.mobile-header, .btn-menu__item--top, .btn-menu__item--mid, .btn-menu__item--bot').toggleClass('is-active')
        $('body').toggleClass('lock')
        $('.mobile-icons').addClass('blink')
        $('.circle1').removeClass('circle1-move')
        $('.circle2').removeClass('circle2-move')
        $('.circle3').removeClass('circle3-move')
        document.querySelectorAll('.show-icon').forEach(item =>{
            item.classList.remove('show-icon')
            item.classList.add('hidden-icon')
        })
    })

    window.addEventListener("orientationchange", function() {
        let currentScreen = window.screen.availWidth
        if (currentScreen > 820){
            $('.mobile-header, .btn-menu__item--top, .btn-menu__item--mid, .btn-menu__item--bot').removeClass('is-active')
            $('body').removeClass('lock')
            $('.mobile-icons').addClass('blink')
            $('.circle1').removeClass('circle1-move')
            $('.circle2').removeClass('circle2-move')
            $('.circle3').removeClass('circle3-move')
            document.querySelectorAll('.show-icon').forEach(item =>{
                item.classList.remove('show-icon')
                item.classList.add('hidden-icon')
            })
        }
    }, false);



})