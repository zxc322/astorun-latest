$(document).ready(function(){
    const but1 = document.querySelector('.completed-nav-but1')
    const but2 = document.querySelector('.completed-nav-but2')
    const box1 = document.querySelector('.com-order-wrap')
    const box2 = document.querySelector('.com-c-order-wrap')

    function sleep(ms) {
        return new Promise(resolve => setTimeout(resolve, ms))
    }

    if (but1){
        but1.addEventListener('click', async function(){
            if (!but1.classList.contains('chosen_completed_button')){
                but2.classList.remove('chosen_completed_button')
                but1.classList.add('chosen_completed_button')
                box2.classList.remove('swipe-in')
                box2.classList.add('swipe-out')
                console.log('swipe')
                await sleep(500)
                box2.classList.remove('z-class1')
                box2.classList.add('z-class0')
                box1.classList.remove('z-class0', 'swipe-out')
                box1.classList.add('z-class1', 'swipe-in')
            }

        })

        but2.addEventListener('click', async function(){
            if (!but2.classList.contains('chosen_completed_button')){
                but1.classList.remove('chosen_completed_button')
                but2.classList.add('chosen_completed_button')
                box1.classList.remove('swipe-in')
                box1.classList.add('swipe-out')
                console.log('swipe')
                await sleep(500)
                box1.classList.remove('z-class1')
                box1.classList.add('z-class0')
                box2.classList.remove('z-class0', 'swipe-out')
                box2.classList.add('z-class1', 'swipe-in')

            }

        })
    }
})