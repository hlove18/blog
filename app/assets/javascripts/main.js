/* JS Document */

var homeIsNotRunning = true
var interval;

function home() {
//Implementing slider banner & nav dots
    if (homeIsNotRunning) {
        homeIsNotRunning = false
        $("#button1").prop("checked", true);
        $(".summary1").css({visibility: "visible"});
        

        $("#content").css({"min-height": $(".sidebar").height() - 10}); //minus 10 for padding
        
        $(function() {
            
            //configure
            var width = 825,
                animationSpeed = 1000,
                navigationSpeed = 800,
                pause = 5000, 
                currentSlide = parseInt($("input[type='radio']:checked").val())
                //links = ["wii_controller.html", "electric_longboard.html", "rocket_motor.html", "tesla_coil.html"] //must be correct order determined by slides
                //console.log(links)
                
            
            //cache DOM;
            var $slider = $("#slider"),
                $slideContainer = $slider.find(".slides"),
                $slide = $slideContainer.find(".slide"),
                slideList = Array.apply(null, Array($slide.length - 1)).map(function (_, i) {return i;}),
                margVal = slideList.map(function(i) {
                    return i * width
                });
            
            
            
            function startSlider() {
                $("#slider .sliderOverlay").animate({opacity: "-=1"}, 100);
                //$(".summary" + currentSlide).css({visibility: "hidden"});
                interval = setInterval(function() {
                    console.log('2');
                    if (currentSlide === $slide.length - 1) {
                        $(".summary" + currentSlide).css({visibility: "hidden"});
                        $("#button1").prop("checked", true);
                        $(".summary1").css({visibility: "visible"});
                        
                        $("#main").css({marginTop: String($(".summary" + (currentSlide + 1)).height())});
                        
                    }
                    else {
                        $(".summary" + currentSlide).css({visibility: "hidden"});
                        $("#button" + (currentSlide + 1)).prop("checked", true);
                        $(".summary" + (currentSlide + 1)).css({visibility: "visible"});

                        
                        //var margin = ($(".summary" + (currentSlide + 1)).height());
                        
                        //console.log(margin);
                        
                        //document.getElementById("body").style.marginTop = String(margin + 15) + "px";
                        
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
                    //$(".summary1").css({visibility: "visible"});
                    //$("#sliderOverlayLink").attr("href", links[0])
                }
                else {
                    //$(".summary" + currentSlide).css({visibility: "visible"});
                    //$("#sliderOverlayLink").attr("href", links[(currentSlide % 5) - 1])
                }
                $("#slider .sliderOverlay").animate({opacity: "+=1"}, 100);
            }
            
            function NavClick() {
                clearInterval(interval);
                var change = margVal[$("input[type='radio']:checked").val() - 1] - margVal[currentSlide - 1];
                $(".summary" + currentSlide).css({visibility: "hidden"});  //hide old summary
                currentSlide = parseInt($("input[type='radio']:checked").val());
                $(".summary" + currentSlide).css({visibility: "visible"});  //show new summary
                $slideContainer.animate({"margin-left": "-="+change}, navigationSpeed);
                
                startSlider();
            }
          
            function Prev() {
                clearInterval(interval);
                if (currentSlide === 1) {  //if on first slide, go to last slide
                    $(".summary" + currentSlide).css({visibility: "hidden"});  //hide old summary
                    currentSlide = $slide.length - 1;
                    $(".summary" + currentSlide).css({visibility: "visible"});  //show new summary
                    $("#button" + (currentSlide)).prop("checked", true);
                    var change = width * ($slide.length - 2);
                    $slideContainer.animate({"margin-left": "-="+change}, navigationSpeed);
                    startSlider();
                }                
                else {  //else just go to prev slide
                    $slideContainer.animate({"margin-left": "+="+width}, navigationSpeed);
                    $(".summary" + currentSlide).css({visibility: "hidden"});  //hide old summary
                    currentSlide -= 1;
                    $(".summary" + currentSlide).css({visibility: "visible"});  //show new summary
                    if (currentSlide === $slide.length - 1) {
                        $("#button1").prop("checked", true); //<------------------------------------------------------------------CHECK THIS LINE???????
                        $(".summary1").css({visibility: "hidden"});
                        $(".summary4").css({visibility: "visible"});
                    }
                    else {
                        $("#button" + (currentSlide)).prop("checked", true);
                    }
                    startSlider();
                }
            }
            
            function Next() {
                clearInterval(interval);
                if (currentSlide === $slide.length - 1) {  //if on last slide, go to first slide
                    $(".summary" + currentSlide).css({visibility: "hidden"});  //hide old summary
                    currentSlide = 1;
                    $(".summary" + currentSlide).css({visibility: "visible"});  //show new summary
                    $("#button" + (currentSlide)).prop("checked", true);
                    var change = width * ($slide.length - 2);
                    $slideContainer.animate({"margin-left": "+="+change}, navigationSpeed);
                    startSlider();
                }                
                else {  //else just go to next slide
                    $slideContainer.animate({"margin-left": "-="+width}, navigationSpeed);
                    $(".summary" + currentSlide).css({visibility: "hidden"});  //hide old summary
                    currentSlide += 1;
                    $(".summary" + currentSlide).css({visibility: "visible"});  //show new summary
                    if (currentSlide === $slide.length) {
                        $("#button1").prop("checked", true);
                    }
                    else {
                        $("#button" + (currentSlide)).prop("checked", true);
                    }
                    startSlider();
                }
            }
            
            $slider.on('mouseenter', stopSlider).on('mouseleave', startSlider);
            
            $("input[type='radio']").click(NavClick);
            
            $(".prev").click(Prev);
            
            $(".next").click(Next);
            
            startSlider();
        });
    }

    else {
        clearInterval(interval);
        $("#button1").prop("checked", true);
        $(".summary1").css({visibility: "visible"});
        

        $("#content").css({"min-height": $(".sidebar").height() - 10}); //minus 10 for padding
        
        $(function() {
            
            //configure
            var width = 825,
                animationSpeed = 1000,
                navigationSpeed = 800,
                pause = 5000, 
                currentSlide = parseInt($("input[type='radio']:checked").val())
                //links = ["wii_controller.html", "electric_longboard.html", "rocket_motor.html", "tesla_coil.html"] //must be correct order determined by slides
                //console.log(links)
                
            
            //cache DOM;
            var $slider = $("#slider"),
                $slideContainer = $slider.find(".slides"),
                $slide = $slideContainer.find(".slide"),
                slideList = Array.apply(null, Array($slide.length - 1)).map(function (_, i) {return i;}),
                margVal = slideList.map(function(i) {
                    return i * width
                });
            
            function startSlider() {
                $("#slider .sliderOverlay").animate({opacity: "-=1"}, 100);
                //$(".summary" + currentSlide).css({visibility: "hidden"});
                interval = setInterval(function() {
                    console.log('2');
                    if (currentSlide === $slide.length - 1) {
                        $(".summary" + currentSlide).css({visibility: "hidden"});
                        $("#button1").prop("checked", true);
                        $(".summary1").css({visibility: "visible"});
                        
                        $("#main").css({marginTop: String($(".summary" + (currentSlide + 1)).height())});
                        
                    }
                    else {
                        $(".summary" + currentSlide).css({visibility: "hidden"});
                        $("#button" + (currentSlide + 1)).prop("checked", true);
                        $(".summary" + (currentSlide + 1)).css({visibility: "visible"});

                        
                        //var margin = ($(".summary" + (currentSlide + 1)).height());
                        
                        //console.log(margin);
                        
                        //document.getElementById("body").style.marginTop = String(margin + 15) + "px";
                        
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
                    //$(".summary1").css({visibility: "visible"});
                    //$("#sliderOverlayLink").attr("href", links[0])
                }
                else {
                    //$(".summary" + currentSlide).css({visibility: "visible"});
                    //$("#sliderOverlayLink").attr("href", links[(currentSlide % 5) - 1])
                }
                $("#slider .sliderOverlay").animate({opacity: "+=1"}, 100);
            }
            
            function NavClick() {
                clearInterval(interval);
                var change = margVal[$("input[type='radio']:checked").val() - 1] - margVal[currentSlide - 1];
                $(".summary" + currentSlide).css({visibility: "hidden"});  //hide old summary
                currentSlide = parseInt($("input[type='radio']:checked").val());
                $(".summary" + currentSlide).css({visibility: "visible"});  //show new summary
                $slideContainer.animate({"margin-left": "-="+change}, navigationSpeed);
                
                startSlider();
            }
          
            function Prev() {
                clearInterval(interval);
                if (currentSlide === 1) {  //if on first slide, go to last slide
                    $(".summary" + currentSlide).css({visibility: "hidden"});  //hide old summary
                    currentSlide = $slide.length - 1;
                    $(".summary" + currentSlide).css({visibility: "visible"});  //show new summary
                    $("#button" + (currentSlide)).prop("checked", true);
                    var change = width * ($slide.length - 2);
                    $slideContainer.animate({"margin-left": "-="+change}, navigationSpeed);
                    startSlider();
                }                
                else {  //else just go to prev slide
                    $slideContainer.animate({"margin-left": "+="+width}, navigationSpeed);
                    $(".summary" + currentSlide).css({visibility: "hidden"});  //hide old summary
                    currentSlide -= 1;
                    $(".summary" + currentSlide).css({visibility: "visible"});  //show new summary
                    if (currentSlide === $slide.length - 1) {
                        $("#button1").prop("checked", true); //<------------------------------------------------------------------CHECK THIS LINE???????
                        $(".summary1").css({visibility: "hidden"});
                        $(".summary4").css({visibility: "visible"});
                    }
                    else {
                        $("#button" + (currentSlide)).prop("checked", true);
                    }
                    startSlider();
                }
            }
            
            function Next() {
                clearInterval(interval);
                if (currentSlide === $slide.length - 1) {  //if on last slide, go to first slide
                    $(".summary" + currentSlide).css({visibility: "hidden"});  //hide old summary
                    currentSlide = 1;
                    $(".summary" + currentSlide).css({visibility: "visible"});  //show new summary
                    $("#button" + (currentSlide)).prop("checked", true);
                    var change = width * ($slide.length - 2);
                    $slideContainer.animate({"margin-left": "+="+change}, navigationSpeed);
                    startSlider();
                }                
                else {  //else just go to next slide
                    $slideContainer.animate({"margin-left": "-="+width}, navigationSpeed);
                    $(".summary" + currentSlide).css({visibility: "hidden"});  //hide old summary
                    currentSlide += 1;
                    $(".summary" + currentSlide).css({visibility: "visible"});  //show new summary
                    if (currentSlide === $slide.length) {
                        $("#button1").prop("checked", true);
                    }
                    else {
                        $("#button" + (currentSlide)).prop("checked", true);
                    }
                    startSlider();
                }
            }
            
            $slider.on('mouseenter', stopSlider).on('mouseleave', startSlider);
            
            $("input[type='radio']").click(NavClick);
            
            $(".prev").click(Prev);
            
            $(".next").click(Next);
            
            startSlider();
        });
    }
};


function toc() {

 /*Implementing Table of Contents "hide" and "show"*/
    
    var contracted = false;
    $(".toc-toggle").click(function() {
        if (! contracted) {
            $(".toc-toggle a").text("show");
            contracted = true;
        }
        else {
            $(".toc-toggle a").text("hide");
            contracted = false;
        }
        $(".toc-list").animate({height: "toggle", width: "toggle"});
        return false; //prevent default of page reset
    })

};

// function owner_badge_coloring() {
//     var owner = $(".owner").html().trim();
//     console.log(owner=="Love");
//     if (owner == "Love") {
//         $(".owner").css("background-color", "#E07572")
//     }
//     if (owner == "Bianchini") {
//         $(".owner").css("background-color", "#F4C46F")
//     }
//     if (owner == "Bianchini-Love") {
//         $(".owner").css("background-color", "#BFD7D9")
//     }
// }


$(document).ready(function() {
    toc();
});