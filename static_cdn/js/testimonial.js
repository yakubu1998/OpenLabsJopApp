

$(".carousel-testimony").owlCarousel({
    // stagePadding: 60,
    loop: true,
    margin: 10,
    // autoplay: true,
    autoplayTimeout: 3000,
    dots: true,
    // nav: true,
    navText: [$('.owl-navigation .owl-nav-prev'), $('.owl-navigation .owl-nav-next')],

    responsive: {
        0: {
            items: 1,
            // nav:true,
            // margin:1,

            // stagePadding: 60,
        },
        320: {
            items: 1,
        },
        560: {
            items: 2,
            // nav:false,
            // stagePadding: 30,

        },
        960: {
            items: 3,
            // nav:true,
            loop:true,
            // stagePadding: 90,
        }
    }
});