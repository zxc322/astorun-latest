//
//const ASD = document.querySelectorAll('[data-tab]');
//console.log(ASD)
//const but1 = ASD[0]
//const but2 = ASD[1]
//const but3 = ASD[2]
//const tab1 = document.querySelector('#tab-1');
//const tab2 = document.querySelector('#tab-2');
//const tab3 = document.querySelector('#tab-3');
//
//tab1.classList.add('slide_in')
//
//ASD.forEach( function (item){
//		item.addEventListener('click', function(){
//			if (!item.classList.contains('active')){
//				but1.classList.remove('active')
//				but2.classList.remove('active')
//				but3.classList.remove('active')
//			}
//			console.log(item == but1)
//			item.classList.add('active')
//			const box = document.querySelector('#' + this.dataset.tab)
//			if (!box.classList.contains('slide_in')){
//				if (tab1.classList.contains('slide_in')){
//					tab1.classList.remove('slide_in')
//					tab1.classList.add('slide_out')
//					box.classList.remove('slide_out')
//					box.classList.add('slide_in')
//				}
//				else if (tab2.classList.contains('slide_in')){
//					tab2.classList.remove('slide_in')
//					tab2.classList.add('slide_out')
//					box.classList.remove('slide_out')
//					box.classList.add('slide_in')
//				}
//				else if (tab3.classList.contains('slide_in')){
//					tab3.classList.remove('slide_in')
//					tab3.classList.add('slide_out')
//					box.classList.remove('slide_out')
//					box.classList.add('slide_in')
//				}
//			}
//		})
//		console.log('script is good')
//	})
//
//
//function reset(){
//	const tab1 = document.querySelector('#tab-1');
//	console.log(tab1.classList.contains('slide_out'));
//	if (!tab1.classList.contains('slide_out')){
//		console.log('true')
//	} else {
//		console.log('else')
//		};
//	tab1.classList.remove('slide_out')
//	console.log('removed')
//	}
//
//
/////////////////////////////////////////////////
//
//
