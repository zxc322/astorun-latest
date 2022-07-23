document.addEventListener('DOMContentLoaded', function(){

	let input = document.querySelector('input[data-tel-input]')

	let getInputNumberValue = function(input){
		return input.value.replace(/\D/g, "")
	}

	let phoneInput = function(e){
		let input = e.target,
			inputNumberValue = getInputNumberValue(input),
			formatedInputValue = '',
			selectionStart = input.selectionStart


		if (!inputNumberValue){
			return input.value = "+";
		}

		if (input.value.length != selectionStart){
			if (e.data && /\D/g.test(e.data)){
				input.value = inputNumberValue  
			}
			return
		}

		if (['3', '0'].indexOf(inputNumberValue[0]) > -1){
			// ua number
			if (inputNumberValue[0] == '0' || inputNumberValue[0] == '3'){
				formatedInputValue = '+38 (0'
			}
						 
			if (inputNumberValue.length > 1){
				formatedInputValue += inputNumberValue.substring(3, 5)
			}

			if (inputNumberValue.length >= 5){
				formatedInputValue += ') ' + inputNumberValue.substring(5, 8)
			}
			if (inputNumberValue.length > 8){
				formatedInputValue += '-' + inputNumberValue.substring(8, 10)
			}
			if (inputNumberValue.length > 10){
				formatedInputValue += '-' + inputNumberValue.substring(10, 13)
			}

		} else{
			// not ua number
			formatedInputValue = '+' + inputNumberValue
		}

		input.value = formatedInputValue	
	}

	let onPhoneKeyDown = function(e){
		
		let input = e.target
		if (e.keyCode == 8 && getInputNumberValue(input).length == 5){
			input.value = e.target.value.slice(0, 8)
		}
		if (e.keyCode == 8 && getInputNumberValue(input).length == 3){
			input.value = ''
		}
	}

	let onPhonePaste = function(e){
		let pasted = e.clipboardData || window.clipboardData,
			input = e.target,
			inputNumberValue = getInputNumberValue(input);

		if (pasted){
			let pastedText = pasted.getData('Text')
			if (/\D/g.test(pastedText)){
				input.value = inputNumberValue;
			}
		}
	}

	input.addEventListener('input', phoneInput)
	input.addEventListener('keydown', onPhoneKeyDown)
	input.addEventListener('paste', onPhonePaste)
})