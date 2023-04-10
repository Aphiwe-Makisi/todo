// Need to figure out how I can link this to my HTML, it works.

const usernameField = document.getElementById("username");
const usernameValidator = document.getElementById("username-error");

usernameField.addEventListener("blur", () => {
  if (usernameField.value.length <= 3) {
    usernameValidator.classList.add("display");
    usernameValidator.classList.remove("hide");
  } else {
    usernameValidator.classList.remove("display");
    usernameValidator.classList.add("hide");
  }
});
