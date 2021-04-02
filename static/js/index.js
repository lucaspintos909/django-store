window.onload = function() {
    var swiper = new Swiper('.swiper-container', {
        slidesPerView: 4,
        spaceBetween: 40,
        slidesPerGroup: 3,
        loop: true,
        loopFillGroupWithBlank: false,
        pagination: {
        el: '.swiper-pagination',
        clickable: true,
        },
        navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
        },
        breakpoints: {
            // when window width is >= 320px
            320: {
              slidesPerView: 2,
              spaceBetween: 20,
              slidesPerGroup: 2,
            },
            // when window width is >= 480px
            480: {
              slidesPerView: 2,
              spaceBetween: 30,
              slidesPerGroup: 2,
            },
            // when window width is >= 640px
            640: {
              slidesPerView: 4,
              spaceBetween: 40
            }
        }
    });
    
  };