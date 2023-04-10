const closePopup = document.getElementById('close')
const addTodoBtn = document.getElementById('new')
const popup = document.querySelector('.pop-up')

closePopup.addEventListener('click', () => {
  popup.classList.remove('show-popup')
  popup.classList.add('hide')
})

addTodoBtn.addEventListener('click', () => {
  popup.classList.remove('hide')
  popup.classList.add('show-popup')
})