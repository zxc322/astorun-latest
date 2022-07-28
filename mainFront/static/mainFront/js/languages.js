let current_href = window.location.href

if (current_href.indexOf('/uk/') > 1){
    console.log(current_href)
    $('.lang-button').each(function(i, el){
        el.classList.remove('chosen-lang')
    })
    $('.ukrainian').addClass('chosen-lang')
} else if ((current_href.indexOf('/ru/') > 1)){
    $('.lang-button').each(function(i, el){
        el.classList.remove('chosen-lang')
    })
    $('.russian').addClass('chosen-lang')
} else {
    $('.lang-button').each(function(i, el){
        el.classList.remove('chosen-lang')
    })
    $('.english').addClass('chosen-lang')
}



// Code for cart svg scale

if (document.getElementById('basket_counter_header')){

    document.getElementById('basket_counter_header').addEventListener('mouseenter', e =>
        document.getElementById('cart-hart').classList.add('scale')

    )

    document.getElementById('basket_counter_header').addEventListener('mouseleave', e =>
        document.getElementById('cart-hart').classList.remove('scale')
    )
}

// hide col-buy lang-choise



if (current_href.indexOf('/buy_collection') > 1){
        $('.mobile-lang').addClass('hidden')
    }


// chosen header link

if (current_href.indexOf('/shop/') > 1){
        $('.shop-link').each(function(i, el){
            el.classList.add('chosen-header-link')
        })
    }

if (current_href.indexOf('/collection/') > 1){
        $('.collection-link').each(function(i, el){
            el.classList.add('chosen-header-link')
        })
    }

if (current_href.indexOf('/news/') > 1){
        $('.news-link').each(function(i, el){
            el.classList.add('chosen-header-link')
        })
    }

if (current_href.indexOf('/contacts/') > 1){
        $('.contacts-link').each(function(i, el){
            el.classList.add('chosen-header-link')
        })
    }