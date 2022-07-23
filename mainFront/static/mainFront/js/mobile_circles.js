$(document).ready(function(){
    const circle = document.querySelectorAll('.mobile-circle')
    const circle1 = document.querySelector('.circle1')
    const circle2 = document.querySelector('.circle2')
    const circle3 = document.querySelector('.circle3')
    const icons = document.querySelector('.mobile-icons')
    const hidden_icons = document.querySelectorAll('.hidden-icon')

    circle.forEach(item =>{
        item.addEventListener('click', function(){
            icons.classList.remove('blink')
            circle1.classList.add('circle1-move')
            circle2.classList.add('circle2-move')
            circle3.classList.add('circle3-move')
            hidden_icons.forEach(item =>{
                item.classList.remove('hidden-icon')
                item.classList.add('show-icon')
            })

        })

    })
})
