window.onscroll = function () {
  scroll();
};

function scroll() {
  const linkScroll = document.getElementById('link-scroll');
  if (document.documentElement.scrollTop > 20) {
    linkScroll.style.display = 'block';
  } else {
    linkScroll.style.display = 'none';
  }
}

const button = document.querySelector('[data-link-scroll]');
console.log(button);

button.addEventListener('click', () => {
  window.scrollTo(0, 0);
});
