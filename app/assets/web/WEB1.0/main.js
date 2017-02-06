/* JS Document */

$(document).ready(function() {
    
    /*Blacken text in header navigation bar as user hovers*/
    
    $(".navWord a").hover(
        function() {
            $(this).addClass("black");
        },
        function() {
            $(this).removeClass("black");
        }
    );
    
    $(this).removeClass("active");
    
    /*Add hover effect to info bar*/
    $(".info ul li").hover(
        function() {
            $(this).addClass("active");
            console.log("henry");
        },
        function() {
            $(this).removeClass("active");
        }
    );
    
    
    /*Shade the list element of sidebar as user hovers*/
    
    $(".sidebarSuper li").hover(
        function() {
            $(this).addClass("redBack");
        },
        function() {
            $(this).removeClass("redBack");
        }
    );
    
    
    /*Fixing sidebar while scrolling*/
    
    $(window).scroll(function() {
        
        var top = $(".wrapper").offset().top,
            scrollTop = $(this).scrollTop()
        
        if (scrollTop < (top - 5)) {  /*-5 for margin; so sidebar doesn't jump immediately to top: 5px*/
            $("#sidebar").css({
                position: 'absolute',
                top: '0px'
            });
        }
        
        else {
            $("#sidebar").css({
                position: 'fixed',
                top: '5px'
            });
        }
    });
    
    
    /*Adding drop-downs to sidebar*/
    
    $(".dropdown").click(function() {
        if ($('.sidebarSub').is(':visible')) {
            $(this).css({"border-bottom": "1px solid red"}).children('.sidebarSub').slideUp(200);
            $(this).css({"color": "white"});
        }
        else {
            $(this).css({"border-bottom": "none"}).children('.sidebarSub').slideDown(200).css({position: "static"});
            $(this).css({"color": "#F78181"});
        }
    });
    
    /*Implementing slider banner & nav dots*/
    $("#button1").prop("checked", true);
    
    $(function() {
        
        //configure
        var width = 945,
            animationSpeed = 1000,
            navigationSpeed = 800,
            pause = 5000, 
            currentSlide = parseInt($("input[type='radio']:checked").val()),
            links = ["wii_controller.html", "electric_longboard.html", "rocket_motor.html", "tesla_coil.html"] //must be correct order determined by slides
            
        
        //cache DOM;
        var $slider = $("#slider"),
            $slideContainer = $slider.find(".slides"),
            $slide = $slideContainer.find(".slide"),
            slideList = Array.apply(null, Array($slide.length - 1)).map(function (_, i) {return i;}),
            margVal = slideList.map(function(i) {
                return i * 945
            });
        
        var interval;
        
        function startSlider() {
            $("#slider .sliderOverlay").animate({opacity: "-=1"}, 100);
            $(".summary" + currentSlide).css({visibility: "hidden"});
            interval = setInterval(function() {
                if (currentSlide === $slide.length - 1) {
                    $("#button1").prop("checked", true);
                }
                else {
                    $("#button" + (currentSlide + 1)).prop("checked", true);
                }
                currentSlide++;
                $slideContainer.animate({"margin-left": "-="+width}, animationSpeed, function() {
                    if (currentSlide === $slide.length) {
                        currentSlide = 1;
                        $slideContainer.css("margin-left", 0);
                    }
                });
            }, pause); 
        }
        
        function stopSlider() {
            clearInterval(interval);
            if (currentSlide === $slide.length) {
                $(".summary1").css({visibility: "visible"});
                $("#sliderOverlayLink").attr("href", links[0])
            }
            else {
                $(".summary" + currentSlide).css({visibility: "visible"});
                $("#sliderOverlayLink").attr("href", links[(currentSlide % 5) - 1])
            }
            $("#slider .sliderOverlay").animate({opacity: "+=1"}, 100);
        }
        
        function NavClick() {
            clearInterval(interval);
            var change = margVal[$("input[type='radio']:checked").val() - 1] - margVal[currentSlide - 1];
            $slideContainer.animate({"margin-left": "-="+change}, navigationSpeed);
            currentSlide = parseInt($("input[type='radio']:checked").val());
            startSlider();
        }
            
        
        $slider.on('mouseenter', stopSlider).on('mouseleave', startSlider);
        
        $("input[type='radio']").click(NavClick);
        
        startSlider();
        
    });
    
});