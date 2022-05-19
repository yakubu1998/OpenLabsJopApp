
const txtFields = document.querySelectorAll(".txtField");

txtFields.forEach((txtField) => {
  txtField.addEventListener("click", function () {
    console.log(event.target.lastElementChild.value);
    if (event.target.lastElementChild.value) {
      event.target.lastElementChild.focus();
      return;
    } else {
      if (event.target.classList.contains("active")) {
        event.target.lastElementChild.classList.remove("active");
        event.target.classList.remove("active");
      } else {
        event.target.lastElementChild.classList.add("active");
        event.target.classList.add("active");
        event.target.lastElementChild.focus();
      }
    }
  });
});

txtFields.forEach((element) => {
  element.addEventListener("focusout", function () {
    if (
      !element.lastElementChild.value &&
      element.classList.contains("active")
    ) {
      element.lastElementChild.classList?.remove("active");
      element.classList?.remove("active");
    }
  });
});

// const toggleLabel = (event) => {
//   if (event.lastElementChild.value) {
//     return;
//   }
// };
