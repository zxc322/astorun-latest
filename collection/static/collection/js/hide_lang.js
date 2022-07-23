const lang_bar = document.querySelector('.header__section2'),
    current_url = window.location.href


if (current_url.indexOf('buy_collection') > 1){
    lang_bar.classList.add('hidden')
}

document.querySelector('.header-content').classList.add('show-header')