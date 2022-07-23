$(document).ready(function(){
    const news = $('.news-article')
    for (let i=0; i<news.length;  i++){
        if (i>=1){
            news[i].classList.add('hide-news')
        }
    }
    $('.load-news').on('click', function(){
        let hidden = $('.hide-news')

        if (hidden.length>0){
            hidden[0].classList.remove('hide-news')
            let closest = hidden[0].closest('.news-article')
            closest.classList.add('appear')
        }

    })
})