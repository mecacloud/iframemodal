/* Javascript for IFrameModalXBlock. */
function IFrameModalXBlock(runtime, element) {

  function close_modal(modal_id) {
    const $modal = $(modal_id);
    $('select, input, textarea, button, a').off('focus');
    const overlay_id = 'lean_overlay';
    $("#" + overlay_id).fadeOut(200);
    $("#" + overlay_id).css({ "display": "none" });
    $modal.css({ "display": "none" });
    $modal.attr('aria-hidden', true);
    $modal.find('iframe').attr('src', '');
    $('body').css('overflow', 'auto');
    $('button[data-target]', element).focus();
  }

    $('button[data-target]', element).click(function(eventObject) {
      const modal_id = $(eventObject.target).data("target");
      const closeButton = $('.close-modal');
      const defaults = { top: 100, overlay: 0.5, closeButton: null };
      const overlay_id = 'lean_overlay';
      const $modal = $(modal_id);
      

      // If we are already in an iframe, skip creation of the modal, since
      // it won't look good, anyway. Instead, we post a message to the parent
      // window, requesting creation of a modal there.
      // This is used by the courseware microfrontend.
      if (window !== window.parent) {
        var launch_url = $modal.data('launch-url');
        window.parent.postMessage(
            {
                'type': 'plugin.modal',
                'payload': {
                    'url': launch_url,
                    'title': $modal.find('iframe').attr('title'),
                    'width': $modal.data('width')
                }
            },
            document.referrer
        );
        return;
    }

      $modal.find('iframe').attr('src', $modal.data('launch-url'));
      $("#" + overlay_id).click(function () {
          close_modal(modal_id)
      });
      closeButton.click(function () {
        close_modal(modal_id)
      })
      $("#" + overlay_id).css({ "display": "block", opacity: 0 });
      $("#" + overlay_id).fadeTo(200, 0.5);
      $(modal_id).css({
          "display": "block"
      });
      $(modal_id).fadeTo(200, 1);
      $(modal_id).attr('aria-hidden', false);
      $('body').css('overflow', 'hidden');

      eventObject.preventDefault();

      /* Manage focus for modal dialog */
      /* Set focus on close button */
      closeButton.focus();

      /* Redirect close button to iframe */
      closeButton.on('keydown', function (e) {
          if (e.which === 9) {
              e.preventDefault();
              // This is a workaround due to Firefox triggering focus calls oddly.
              setTimeout(function () {
                  $modal.find('iframe')[0].contentWindow.focus();
              }, 1);
          }
      });
      document.addEventListener('keydown', (event) => {
        if (event.code === 'Escape') {
          close_modal(modal_id)
        }
      });
    });

    $(function ($) {});
}
