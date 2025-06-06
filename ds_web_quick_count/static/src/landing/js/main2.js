(function($) {

	"use strict";

	var fullHeight = function() {

		$('.js-fullheight').css('height', $(window).height());
		$(window).resize(function(){
			$('.js-fullheight').css('height', $(window).height());
		});

	};
	fullHeight();

	var carousel = function() {
		$('.featured-carousel').owlCarousel({
	    loop:true,
	    autoplay: true,
	    margin:30,
	    animateOut: 'fadeOut',
	    animateIn: 'fadeIn',
	    nav:true,
	    dots: true,
	    autoplayHoverPause: false,
	    items: 1,
	    navText : ["<span class='ion-ios-arrow-back'></span>","<span class='ion-ios-arrow-forward'></span>"],
	    responsive:{
	      0:{
	        items:1
	      },
	      600:{
	        items:2
	      },
	      1000:{
	        items:3
	      }
	    }
		});

	};
	carousel();

	var carousel1 = function() {
		$('.featured-carousel1').owlCarousel({
	    loop:true,
	    autoplay: true,
	    margin:30,
	    animateOut: 'fadeOut',
	    animateIn: 'fadeIn',
	    nav:true,
	    dots: true,
	    autoplayHoverPause: false,
	    items: 1,
	    navText : ["<span class='ion-ios-arrow-back'></span>","<span class='ion-ios-arrow-forward'></span>"],
	    responsive:{
	      0:{
	        items:1
	      },
	      600:{
	        items:2
	      },
	      1000:{
	        items:3
	      }
	    }
		});

	};
	carousel();


})(jQuery);

const countdown = () => {
    const targetDate = new Date('Nov 27, 2024 00:00:00').getTime();
    const now = new Date().getTime();
    const gap = targetDate - now;

    const days = Math.floor(gap / (1000 * 60 * 60 * 24));
    const hours = Math.floor((gap % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((gap % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((gap % (1000 * 60)) / 1000);

    document.querySelector('.countdown').innerHTML = `
        <div class="col-xs-3 mx-2 text-center shadow">
          <p class="display-4 fw-bold">${days}</p>
          <p class="text-muted hilangg">Hari</p>
        </div>
        <div class="col-xs-3 mx-2 text-center shadow">
          <p class="display-4 fw-bold">${hours}</p>
          <p class="text-muted hilangg">Jam</p>
        </div>
        <div class="col-xs-3 mx-2 text-center shadow">
          <p class="display-4 fw-bold">${minutes}</p>
          <p class="text-muted hilangg">Menit</p>
        </div>
        <div class="col-xs-3 mx-2 text-center shadow">
          <p class="display-4 fw-bold">${seconds}</p>
          <p class="text-muted hilangg">Detik</p>
        </div>
    `;
};

setInterval(countdown, 1000);