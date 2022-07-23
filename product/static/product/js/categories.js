$(document).ready(function(){
    const buttons = document.querySelectorAll('.cat-nav-but')
    const button1 = buttons[0]
    const button2 = buttons[1]
    const button3 = buttons[2]

    const mens = document.querySelector('.mens_products')


    function sleep(ms) {
        return new Promise(resolve => setTimeout(resolve, ms))
    }

    buttons.forEach( function (item){
            item.addEventListener('click', async function(){
                let chosen = document.querySelector('.swipe-in') || mens
                if (!item.classList.contains('chosen_cat_button')){
                    button1.classList.remove('chosen_cat_button')
                    button2.classList.remove('chosen_cat_button')
                    button3.classList.remove('chosen_cat_button')
                    item.classList.add('chosen_cat_button')

                    // Get chosen block to swipe-out and swipe-in new block
                    let chosen_block = '.' + item.value + '_products'
                    let newChose = document.querySelector(chosen_block)
                    chosen.classList.remove('swipe-in')
                    chosen.classList.add('swipe-out')
                    await sleep(500)
                    chosen.classList.remove('z-class1')
                    chosen.classList.add('z-class0')
                    newChose.classList.remove('z-class0', 'swipe-out')
                    newChose.classList.add('z-class1', 'swipe-in')
                }
            })
        })
})