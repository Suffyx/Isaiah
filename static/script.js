window.onscroll = function() {
  if (window.pageYOffset > document.getElementById("page-header").offsetTop) {
    document.getElementById("page-header").classList.add("sticky");
  } else {
    document.getElementById("page-header").classList.remove("sticky");
  }
}
