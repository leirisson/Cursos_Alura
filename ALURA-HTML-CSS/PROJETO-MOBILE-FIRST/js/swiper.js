const swiper = new Swiper('.swiper',{
  // If we need pagination
  spaceBetween:100,
  slidePerView:1,
  // Navigation arrows
  navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
  },
  pagination: {
      el: '.swiper-pagination',
      type: 'bullets',
  },

    
});