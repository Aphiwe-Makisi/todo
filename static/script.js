const usernameField = document.getElementById('username')
const ErrorText = document.getElementById('username-error')

usernameField.addEventListener('blur', () => {
  if (usernameField.value.length <= 2) {
    ErrorText.classList.remove('hide')
    ErrorText.classList.add('display')
  } else {
    ErrorText.classList.remove('display')
    ErrorText.classList.add('hide')
  }
})