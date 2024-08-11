//SWIPER PARA LAS PROMOCIONES
var swiper = new Swiper(".mySwiperPromotion", {
    loop: true,
    effect: "faded",
    grapCursor:"true",
    centerSlide:"true",
    autoplay: {
        delay: 8000,
        disableOnInteraction: false,
      },
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
      dynamicBullets: false,
    },
});
//SWIPER PARA LAS NOTICIAS
var swiper = new Swiper(".mySwiperNews", {
  loop: true,
  fade:"true",
  grapCursor:"true",
  centerSlide:"true",
  autoplay: {
      delay: 8000,
      disableOnInteraction: false,
    },
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
    dynamicBullets: false,
  },
  breakpoints: {
    0:{
      slidesPerView: 1,
    },
    768:{
      slidesPerView: 2,
      spaceBetween: 20,
    },
    1200:{
      slidesPerView: 2,
      spaceBetween: 20,
    },
    1400:{
      slidesPerView: 2,
      spaceBetween: 20,
    },
  },
});
//SWIPER PARA LOS TESTIMONIOS
var swiper = new Swiper(".mySwiperTestimonials", {
  slidesPerView: 1,
  spaceBetween: 30,
  loop: true,
  autoplay: {
    delay: 8000,
    disableOnInteraction: false,
  },
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
  },
  breakpoints: {
    1200:{
      navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
      },
    },
    1400:{
      navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
      },
    },
  },
});

//SweetAlert para los errores
function notificationError(message){
  Swal.fire({
    title: 'Error!',
    text: message,
    icon: 'error',
    confirmButtonText: 'Aceptar'
  });
}

//SweetAlert para acciones realizadas con éxito
function notificationSuccess(message){
  Swal.fire({
    title: 'Notificación!',
    text: message,
    icon: 'success',
    confirmButtonText: 'Aceptar'
  });
}