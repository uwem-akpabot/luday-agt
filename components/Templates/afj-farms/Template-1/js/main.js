(function($) {

	"use strict";

	// Preloader
	$(window).on('load', function() {
		if ($('#preloader').length) {
		  $('#preloader').delay(100).fadeOut('slow', function() {
			$(this).remove();
		  });
		}
	});

	$(window).stellar({
    responsive: true,
    parallaxBackgrounds: true,
    parallaxElements: true,
    horizontalScrolling: false,
    hideDistantElements: false,
    scrollProperty: 'scroll'
  });  
	
  	// Init AOS
  function aos_init() {
    AOS.init({
      duration: 1000,
      once: true
    });
  }
  $(window).on('load', function() {
    aos_init();
  });  

	var fullHeight = function() {

		$('.js-fullheight').css('height', $(window).height());
		$(window).resize(function(){
			$('.js-fullheight').css('height', $(window).height());
		});

	};
	fullHeight();

	// loader
	// var loader = function() {
	// 	setTimeout(function() { 
	// 		if($('#ftco-loader').length > 0) {
	// 			$('#ftco-loader').removeClass('show');
	// 		}
	// 	}, 1);
	// };
	// loader();

	var carousel = function() {
		$('.carousel-testimony').owlCarousel({
			center: true,
			loop: true,
			autoplay: true,
			autoplaySpeed:2000,
			items:1,
			margin: 30,
			stagePadding: 0,
			nav: false,
			navText: ['<span class="ion-ios-arrow-back">', '<span class="ion-ios-arrow-forward">'],
			responsive:{
				0:{
					items: 1
				},
				600:{
					items: 2
				},
				1000:{
					items: 3
				}
			}
		});

	};
	carousel();

	$('nav .dropdown').hover(function(){
		var $this = $(this);
		// 	 timer;
		// clearTimeout(timer);
		$this.addClass('show');
		$this.find('> a').attr('aria-expanded', true);
		// $this.find('.dropdown-menu').addClass('animated-fast fadeInUp show');
		$this.find('.dropdown-menu').addClass('show');
	}, function(){
		var $this = $(this);
			// timer;
		// timer = setTimeout(function(){
			$this.removeClass('show');
			$this.find('> a').attr('aria-expanded', false);
			// $this.find('.dropdown-menu').removeClass('animated-fast fadeInUp show');
			$this.find('.dropdown-menu').removeClass('show');
		// }, 100);
	});


	$('#dropdown04').on('show.bs.dropdown', function () {
	  console.log('show');
	});

	// scroll
	var scrollWindow = function() {
		$(window).scroll(function(){
			var $w = $(this),
					st = $w.scrollTop(),
					navbar = $('.ftco_navbar'),
					sd = $('.js-scroll-wrap');

			if (st > 150) {
				if ( !navbar.hasClass('scrolled') ) {
					navbar.addClass('scrolled');	
				}
			} 
			if (st < 150) {
				if ( navbar.hasClass('scrolled') ) {
					navbar.removeClass('scrolled sleep');
				}
			} 
			if ( st > 350 ) {
				if ( !navbar.hasClass('awake') ) {
					navbar.addClass('awake');	
				}
				
				if(sd.length > 0) {
					sd.addClass('sleep');
				}
			}
			if ( st < 350 ) {
				if ( navbar.hasClass('awake') ) {
					navbar.removeClass('awake');
					navbar.addClass('sleep');
				}
				if(sd.length > 0) {
					sd.removeClass('sleep');
				}
			}
		});
	};
	scrollWindow();

	// Back to top button
	$(window).scroll(function() {
		if ($(this).scrollTop() > 100) {
		  $('.back-to-top').fadeIn('slow');
		} else {
		  $('.back-to-top').fadeOut('slow');
		}
	  });
	
	  $('.back-to-top').click(function() {
		$('html, body').animate({
		  scrollTop: 0
		}, 1500, 'easeInOutExpo');
		return false;
	  });

	var counter = function() {
		
		$('#section-counter, .wrap-about, .ftco-counter').waypoint( function( direction ) {

			if( direction === 'down' && !$(this.element).hasClass('ftco-animated') ) {

				var comma_separator_number_step = $.animateNumber.numberStepFactories.separator(',')
				$('.number').each(function(){
					var $this = $(this),
						num = $this.data('number');
						console.log(num);
					$this.animateNumber(
					  {
					    number: num,
					    numberStep: comma_separator_number_step
					  }, 7000
					);
				});
				
			}

		} , { offset: '95%' } );

	}
	counter();


	var contentWayPoint = function() {
		var i = 0;
		$('.ftco-animate').waypoint( function( direction ) {

			if( direction === 'down' && !$(this.element).hasClass('ftco-animated') ) {
				
				i++;

				$(this.element).addClass('item-animate');
				setTimeout(function(){

					$('body .ftco-animate.item-animate').each(function(k){
						var el = $(this);
						setTimeout( function () {
							var effect = el.data('animate-effect');
							if ( effect === 'fadeIn') {
								el.addClass('fadeIn ftco-animated');
							} else if ( effect === 'fadeInLeft') {
								el.addClass('fadeInLeft ftco-animated');
							} else if ( effect === 'fadeInRight') {
								el.addClass('fadeInRight ftco-animated');
							} else {
								el.addClass('fadeInUp ftco-animated');
							}
							el.removeClass('item-animate');
						},  k * 50, 'easeInOutExpo' );
					});
					
				}, 100);
				
			}

		} , { offset: '95%' } );
	};
	contentWayPoint();

	/*price range*/

	$('#sl2').slider();

	var RGBChange = function() {
	$('#RGB').css('background', 'rgb('+r.getValue()+','+g.getValue()+','+b.getValue()+')')
	};	


	/* ..............................................
	   Slider Range
	   ................................................. */

	// $(function() {
	// 	$("#slider-range").slider({
	// 		range: true,
	// 		min: 0,
	// 		max: 4000,
	// 		values: [1000, 3000],
	// 		slide: function(event, ui) {
	// 			$("#amount").val("₦" + ui.values[0] + " - ₦" + ui.values[1]);
	// 		}
	// 	});
	// 	$("#amount").val("₦" + $("#slider-range").slider("values", 0) +
	// 		" - ₦" + $("#slider-range").slider("values", 1));
	// });


	
	// magnific popup
	$('.image-popup').magnificPopup({
    type: 'image',
    closeOnContentClick: true,
    closeBtnInside: false,
    fixedContentPos: true,
    mainClass: 'mfp-no-margins mfp-with-zoom', // class to remove default margin from left and right side
     gallery: {
      enabled: true,
      navigateByImgClick: true,
      preload: [0,1] // Will preload 0 - before current, and 1 after the current image
    },
    image: {
      verticalFit: true
    },
    zoom: {
      enabled: true,
      duration: 300 // don't foget to change the duration also in CSS
    }
  });

  $('.popup-youtube, .popup-vimeo, .popup-gmaps').magnificPopup({
    disableOn: 700,
    type: 'iframe',
    mainClass: 'mfp-fade',
    removalDelay: 160,
    preloader: false,

    fixedContentPos: false
  });

  $('[data-toggle="popover"]').popover()
	$('[data-toggle="tooltip"]').tooltip()

})(jQuery);

/* ..............................................
	Product page 
	................................................. */


// Category filter
// const selectors = document.querySelectorAll(".selector").children;
// const poultryProducts = document.querySelectorAll(".product").children;

// for (i = 0; i < selectors.length; i++) {

// 	selectors[i].addEventListener("click", (e) => {
// 		e.preventDefault();

// 		const filter = e.target.dataset.filter;
// 		console.log(filter);
// 	})

	// selectors[i].onclick = function(){
	// 	for(let x = 0; x < selectors.length; x++) {
	// 		selectors[x].classList.remove('active');
	// 	}
	// 	this.classList.add('active');
	// 	const displayItems = this.getAttribute('data-filter');
	// 	for(let z = 0; z < poultryProducts.length; z++) {
	// 		poultryProducts[z].style.transform = 'scale(0)';
	// 		setTimeout(() => {
	// 			poultryProducts[z].style.display = 'none';
	// 		}, 500);

	// 		if ((poultryProducts[z].getAttribute('data-category') == displayItems) || 
	// 		displayItems == 'all'){
	// 			poultryProducts[z].style.transform = 'scale(1)';
	// 			setTimeout(() => {
	// 			poultryProducts[z].style.display = 'block';
	// 		}, 500);
	// 		}
	// 	}
	// }		
//}

// const categoryTitle = document.querySelectorAll('category-title');
// const allCategoryProducts = document.querySelectorAll("products");

// for(let i = 0; i < categoryTitle.length; i++){
// 	categoryTitle[i].addEventListener('click', 
// 	filterProducts.bind(this, categoryTitle[i]));
// }

// function filterProducts(item){
// 	changeActivePosition(item);
// 	for(let i = 0; i < allCategoryProducts.length; i++){
// 		if(allCategories[i].classList.contains(item.attributes.id.value)){
// 			allCategoryProducts[i].style.display = "block";
// 		} else {
// 			allCategoryProducts[i].style.display = "none";
// 		}
// 	}
// }

function changeActivePosition(activeItem){
	for(let i = 0; i < categoryTitle.length; i++){
		categoryTitle[i].classList.remove('active');
	}
	activities.classList.add('active');
}

