    // Add product to cart and set cart_items_counter

$(document).ready(function(){
    const form = $('#size_choise');
    form.on('submit', function(e){
    e.preventDefault();
    const product_size = $('#size').val();
    const product_color = $('#color').val();
    const submit_button = $('#submit_button')
    const product_id = submit_button.data("product_id")
    const product_title = submit_button.data("product_title")
    const product_price = submit_button.data("product_price")
    const csrf_token = $('#size_choise [name="csrfmiddlewaretoken"]').val()
    const popup = $('.my-popup')



        let data = {}
        data.product_id = product_id
        data.product_size = product_size
        data.product_color = product_color
        data.product_price = product_price
        data["csrfmiddlewaretoken"] = csrf_token
        const url = form.attr("action")

        $.ajax({
            url: url,
            type: 'POST',
            data: data,
            cache: true,
            success: function(data){
            console.log('OK')
                console.log('p-counter: ', data.products_counter)
                $('.basket_counter').text(data.products_counter)
                popup.addClass('show-popup')

                // set url for popup 'go-to-cart' (default 'en')
                let current_url = window.location.href
                let popup_url = $('.my-popup-url')
                if (current_url.indexOf('/ru/') > 1){
                    let cart_url = '/ru/order/cart/'
                    popup_url.attr('href', cart_url);
                } else if (current_url.indexOf('/uk/') > 1){
                    let cart_url = '/uk/order/cart/'
                    popup_url.attr('href', cart_url);
                }
            },
            error: function(){
            console.log('error')
            },

        })
    })
   

    function calculateBasketPrice(){
        let calculated_order_price = 0
        let delivery_price = 80
        $('.product_total_price').each(function(){
            calculated_order_price += parseInt($(this).text())
        })
        if (calculated_order_price > 999) {
            delivery_price = 0
        }
        $(".calculated_products_price").text(calculated_order_price)
        $('.delivery_price').text(delivery_price)
        $('.hidden_delivery_price').val(delivery_price)
        $('.calculated_order_price').text(calculated_order_price + delivery_price)
        $('.hidden_total').val(calculated_order_price + delivery_price)

    }

// Change quantity and update value in database

    
    if ($('.product_quantity')){
        calculateBasketPrice()
        

        $('.minus').on('click', function(){
            let quantity = $(this).parent().find('.product_quantity')
            console.log(quantity)
            if (quantity.val() > 1){
                quantity.val(quantity.val() - 1)
                let current_quantity = parseInt(quantity.val())
                let price_per_item = parseInt($(this).parent().find('.price_for_item').text())
                let current_total_price = price_per_item*current_quantity
                $(this).parent().find('.product_total_price').text(current_total_price)
                calculateBasketPrice()

                let data = {}
                const csrf_token = $('#order_form [name="csrfmiddlewaretoken"]').val()
                data["csrfmiddlewaretoken"] = csrf_token
                let item_id = parseInt($(this).parent().find('.item_id').text())
                data['item_id'] = item_id
                data['quantity'] = current_quantity

                    $.ajax({
                    url: '/order/change_quantity/',
                    type: 'POST',
                    data : data,
                    cache: true,
                    success: function(data){
                        console.log('quantity changed!')},
                })
            }
        })


        $('.plus').on('click', function(){
            let quantity = $(this).parent().find('.product_quantity')
            quantity.val(parseInt(quantity.val()) + 1)
            let current_quantity = parseInt(quantity.val())
            let price_per_item = parseInt($(this).parent().find('.price_for_item').text())
            let current_total_price = price_per_item*current_quantity
            $(this).parent().find('.product_total_price').text(current_total_price)
            calculateBasketPrice()

            let data = {}
            const csrf_token = $('#order_form [name="csrfmiddlewaretoken"]').val()
            data["csrfmiddlewaretoken"] = csrf_token
            let item_id = parseInt($(this).parent().find('.item_id').text())
            data['item_id'] = item_id
            data['quantity'] = current_quantity

                $.ajax({
                url: '/order/change_quantity/',
                type: 'POST',
                data : data,
                cache: true,
                success: function(data){
                    console.log('quantity changed!')},
            })
                
        })
    }
        
    


// Remove product from the cart and update cart_items_counter

     $(document).on('click', '.remove_product_button', function(e){
        e.preventDefault()
        let par = $(this).parent()
        let item_id = parseInt($(this).parent().find('.item_id').text())
        console.log('qwe', par)
        console.log('iID', item_id)
        const delPopup = $('.del-popup')
        delPopup.addClass('show-popup')
        $('input[name="del-parent"]').val(item_id)
     })

     $(document).on('click', '.del-popup-ok', function(e){
        let item_id = $('input[name="del-parent"]')[0].value
        let items = $('.item_id')
        $.each(items, function(e, el){
            console.log(parseInt(el.innerText))
            if (parseInt(el.innerText) == item_id){
                el.closest('.cart_item').remove()
            }
        })

        const delPopup = $('.del-popup')
        delPopup.removeClass('show-popup')
        calculateBasketPrice()

        let data = {}
        const csrf_token = $('#order_form [name="csrfmiddlewaretoken"]').val()
        data["csrfmiddlewaretoken"] = csrf_token
        data['item_id'] = item_id

        $.ajax({
            url: '/order/remove_item_from_cart/',
            type: 'POST',
            data : data,
            cache: true,
            success: function(data){
            console.log('item_removed')
            console.log('data-cart', data)
            console.log('data-cart.prod-counter = ', data.products_counter)
            $('.basket_counter').text(data.products_counter)
            console.log($('.basket_counter').text())
            if (parseInt($('.basket_counter').text()) < 1){
                location.reload()
            }

            }
        })
     })

    // closing popups

    //  my-popup

    $(document).on('click', '.my-popup-close', function(e){
        const popup = $('.my-popup')
        popup.removeClass('show-popup')
    })

    $(window).click(function (e) {
    const popup = $('.my-popup-container')
    if (e.target == popup[0]) {
      $('.my-popup').removeClass("show-popup");

    }
  });

    // del-popup

    $(document).on('click', '.del-popup-no', function(e){
        const delPopup = $('.del-popup')
        delPopup.removeClass('show-popup')
    })

    $(window).click(function (e) {
    const delPopup = $('.del-popup-container')
    if (e.target == delPopup[0]) {
      $('.del-popup').removeClass("show-popup");

    }
  });

})