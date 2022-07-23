function getCookie(name) {
    let cookieValue = 0
    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';')
        for (let i =0; i < cookies.length; i++) {
            let cookie = jQuery.trim(cookies[i])

            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1))
                break
            }
        }
    }

    return cookieValue
}


function csrfSafeMethod(method) {
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method))
}




function add_to_bookmarks() {
    $('.bookmark-box').each((index, el) => {
        $(el).click((e) => {
            e.preventDefault()
            const id = $(el).data('id')

            if( $(el).hasClass('added') ) {
                $(el).attr('class', 'bookmark-box')
                $.ajax({
                    url: '/bookmarks/remove/',
                    type: 'POST',
                    dataType: 'json',
                    data: {'csrfmiddlewaretoken': getCookie('csrftoken'), 'id': id},
                    success: (data) => {
                        console.log('successRemoved')

                    }
                })
            } else {
                $(el).attr('class', 'bookmark-box added')
                $.ajax({
                    url: '/bookmarks/add/',
                    type: 'POST',
                    dataType: 'json',
                    data: {'csrfmiddlewaretoken': getCookie('csrftoken'), 'id': id},
                    success: (data) => {
                        console.log('successAdded')

                    }
                })
            }
        })
    })
}








function get_bookmarks_favorites(){
    $.getJSON('/bookmarks/api/', (json) => {
        if (json !== null) {
            for( let i = 0; i < json.length; i++) {
                $('.bookmark-box').each((index, el) => {
                    const id = $(el).data('id')
                    if (json[i] == id) {
                        $(el).attr('class', 'bookmark-box added')

                    }
                })
            }
        }
    })
}


// Remove product from bookmarks

     $(document).on('click', '.remove_from_bookmark_button', function(e){
        e.preventDefault()
        let par = $(this).closest('.bookmark_item')
        par.remove()

        let data = {}
        const id = $(this).data('id')


        $.ajax({
            url: '/bookmarks/remove/',
            type: 'POST',
            dataType: 'json',
            data: {'csrfmiddlewaretoken': getCookie('csrftoken'), 'id': id},

            success: (data) => {
                        console.log('successRemoved')
                        let counter = data['counter']
                        if (counter == '0'){
                            location.reload()
                        }
                        par.attr('class', 'bookmarks')
                    }

        })
     })



$(document).ready(function(){
    $.ajaxSetup({
        beforeSend: (xhr, settings) => {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader('X-CSRFToken', getCookie('csrftoken'))
            }
        }
    })
    add_to_bookmarks()
    get_bookmarks_favorites()
})