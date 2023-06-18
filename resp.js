burger = document.querySelector('.burger')
navbar = document.querySelector('.navbar')
navList = document.querySelector('.nav-list')
rightNav = document.querySelector('.rightNav')

burger.addEventListener('click', ()=>{
    rightNav.classList.toggle('v-class-resp');
    navList.classList.toggle('v-class-resp'); 
    navbar.classList.toggle('h-nav-resp'); 
})

function searchGoogle() {
  var query = document.getElementById("search").value;
  var searchUrl = "https://www.google.com/search?q=" + encodeURIComponent(query);

  window.open(searchUrl, "_blank");
}
