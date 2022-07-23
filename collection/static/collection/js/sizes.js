let select = function () {

    // sizes choise + hide colors choise
    
    let selectHeaderSize = document.querySelectorAll('.select__header_size');
    let selectItemSize = document.querySelectorAll('.select__item_size');
    let selectBodySize = document.querySelectorAll('.select__body_size');

    selectHeaderSize.forEach(item => {
        item.addEventListener('mouseenter', selectAdd)
    });

    selectBodySize.forEach(item => {
        item.addEventListener('mouseenter', selectAdd)
    });

     selectBodySize.forEach(item => {
        item.addEventListener('mouseleave', selectRemove)
    });

    selectHeaderSize.forEach(item => {
        item.addEventListener('mouseleave', selectRemove)

    });

    selectItemSize.forEach(item => {
        item.addEventListener('click', selectSizeChoose)
    });

    function selectAdd() {
        this.parentElement.classList.add('is-active');
        let color_block = document.querySelectorAll('.color-select')
        color_block.forEach(item => {
            item.classList.add('hidden')
        })

    }

    function selectRemove() {
        this.parentElement.classList.remove('is-active');
        let color_block = document.querySelectorAll('.color-select')
        color_block.forEach(item => {
            item.classList.remove('hidden')
        })
    }

    function selectSizeChoose() {

        let text = this.innerText,
            select = this.closest('.select-size'),
            currentText = select.querySelector('.select__current_size');
            currentText.innerText = text;
            currentValue = select.querySelector('.chosen-size').value
            newValue = ''
            for (let i = 0; i < currentValue.length; i++){

                if (currentValue[i] != '='){
                    newValue += currentValue[i]
                } else {
                    newValue += '='
                    break
                }
            }

            select.querySelector('.chosen-size').value = newValue + text



        select.classList.remove('is-active');
        let color_block = document.querySelectorAll('.color-select')
        color_block.forEach(item => {
            item.classList.remove('hidden')
        })

    }
    
    // colors choise
    
    let selectHeaderColor = document.querySelectorAll('.select__header_color');
    let selectItemColor = document.querySelectorAll('.select__item_color');
    let selectBodyColor = document.querySelectorAll('.select__body_color');
    
    selectHeaderColor.forEach(item => {
        item.addEventListener('mouseenter', selectColorAdd)
    });

    selectBodyColor.forEach(item => {
        item.addEventListener('mouseenter', selectColorAdd)
    });

     selectBodyColor.forEach(item => {
        item.addEventListener('mouseleave', selectColorRemove)
    });

    selectHeaderColor.forEach(item => {
        item.addEventListener('mouseleave', selectColorRemove)

    });

    selectItemColor.forEach(item => {
        item.addEventListener('click', selectColorChoose)
    });

    function selectColorAdd() {
        this.parentElement.classList.add('is-active');
    }

    function selectColorRemove() {
        this.parentElement.classList.remove('is-active');
    }

    function selectColorChoose() {

        let text = this.innerText,
            select = this.closest('.color-select')
            currentText = select.querySelector('.select__current_color');
            currentValue = select.querySelector('.chosen-color').value
            newValue = ''
            for (let i = 0; i < currentValue.length; i++){

                if (currentValue[i] != '='){
                    newValue += currentValue[i]
                } else {
                    newValue += '='
                    break
                }
            }

            select.querySelector('.chosen-color').value = newValue + text

        currentText.innerText = text;
        select.classList.remove('is-active');
    }
};


select();


