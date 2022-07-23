


$('.top-slider-chek').on('change', function(e){
    $('.top-slider-chek').each(function(){
        if (e.target != this){
            this.checked = false
        }
    })
    pricer()
    setItemsIds()


})

$('.mid-slider-chek').on('change', function(e){
    $('.mid-slider-chek').each(function(){
        if (e.target != this){
            this.checked = false
        }
    })
    pricer()
    setItemsIds()
})

$('.bot-slider-chek').on('change', function(e){
    $('.bot-slider-chek').each(function(){
        if (e.target != this){
            this.checked = false
        }
    })
    pricer()
    setItemsIds()
})


let pricer = function(){
    let i = 0
    total = 0
    $('.js').each(function(e, el){
        if (el.checked == true){
            i += 1
            total += parseInt(el.name)


        }
    })
    if (i==2){
        $('.discount-section').removeClass('hide-discount')
        $('.discount-section').addClass('show-discount')
        window.scrollTo(0, document.body.scrollHeight);
        $('.discount-percent').text(' 10%')
        $('.chosen-items').text(i)
        $('.discount-price').text(parseInt(total*0.9))
        $('.hidden-price').val(parseInt(total*0.9))
        $('.hidden-percent').val('10%')

    } else if(i==3){
        $('.discount-percent').text(' 20%')
        $('.chosen-items').text(i)
        $('.discount-price').text(parseInt(total*0.8))
        $('.hidden-price').val(parseInt(total*0.8))
        $('.hidden-percent').val('20%')
    } else{
        if ($('.discount-section').hasClass('show-discount')){
            $('.discount-section').removeClass('show-discount')
            $('.discount-section').addClass('hide-discount')
        }

    }
}


let setItemsIds = function(){
    let ids = []
    $('.js').each(function(e, el){

        if (el.checked == true){
            ids.push(el.id)

            $('.hidden-ids').val(ids)
        }
    })
}


//$('form').eq(0).on('submit', function() {
//     return $('input[name^=field]:checked:enabled').length == 1;
//});