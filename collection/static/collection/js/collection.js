const ASD = document.querySelectorAll('.col-nav-but')
const hrefs = document.querySelectorAll('.hrefs')
const collections = document.querySelector('.all_collections')

const but1 = ASD[0]
const but2 = ASD[1]
const but3 = ASD[2]

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms))
}

ASD.forEach( function (item){
		item.addEventListener('click', async function(){
			if (!item.classList.contains('chosen_button')){
				but1.classList.remove('chosen_button')
				but2.classList.remove('chosen_button')
				but3.classList.remove('chosen_button')
				item.classList.add('chosen_button')
				collections.classList.add('swipe')
				await sleep(1000)
				collections.classList.remove('swipe')


			}
		})
	})


hrefs.forEach(function(item){
    item.addEventListener('click', function(e){
        const chosen = document.getElementsByClassName('chosen_button');
        gender = chosen[0].value
        let tmp_url = item.href
        window.location.href = tmp_url + '/' + gender;
        e.preventDefault()
    })
})