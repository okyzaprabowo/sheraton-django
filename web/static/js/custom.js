(function($) {

  // Add smooth scrolling to all links in navbar
  $(".navbar a,a.btn-appoint, .quick-info li a, .overlay-detail a").on('click', function(event) {

    var hash = this.hash;
    if (hash) {
      event.preventDefault();
      $('html, body').animate({
        scrollTop: $(hash).offset().top
      }, 900, function() {
        window.location.hash = hash;
      });
    }

  });

  $(".navbar-collapse a").on('click', function() {
    $(".navbar-collapse.collapse").removeClass('in');
  });

  //jQuery to collapse the navbar on scroll
  $(window).scroll(function() {
    if ($(".navbar-default").offset().top > 50) {
      $(".navbar-fixed-top").addClass("top-nav-collapse");
    } else {
      $(".navbar-fixed-top").removeClass("top-nav-collapse");
    }
  });

  $('.carousel[data-type="multi"] .item').each(function() {
    var next = $(this).next();
    if (!next.length) {
      next = $(this).siblings(':first');
    }
    next.children(':first-child').clone().appendTo($(this));

    for (var i = 0; i < 2; i++) {
      next = next.next();
      if (!next.length) {
        next = $(this).siblings(':first');
      }

      next.children(':first-child').clone().appendTo($(this));
    }
  });

  // video player
  $(document).on('click','.js-videoPoster',function(ev) {
      ev.preventDefault();
      var $poster = $(this);
      var $wrapper = $poster.closest('.js-videoWrapper');
      videoPlay($wrapper);
    });

    // play the targeted video (and hide the poster frame)
    function videoPlay($wrapper) {
      var $iframe = $wrapper.find('.js-videoIframe');
      var src = $iframe.data('src');
      // hide poster
      $wrapper.addClass('videoWrapperActive');
      // add iframe src in, starting the video
      $iframe.attr('src',src);
    }

    // stop the targeted/all videos (and re-instate the poster frames)
    function videoStop($wrapper) {
      // if we're stopping all videos on page
      if (!$wrapper) {
        var $wrapper = $('.js-videoWrapper');
        var $iframe = $('.js-videoIframe');
      // if we're stopping a particular video
      } else {
        var $iframe = $wrapper.find('.js-videoIframe');
      }
      // reveal poster
      $wrapper.removeClass('videoWrapperActive');
      // remove youtube link, stopping the video from playing in the background
      $iframe.attr('src','');
    }

    // modal
    $('.thumbnail').click(function(e){
        $('#myModal').modal('show');
    });

})(jQuery);
