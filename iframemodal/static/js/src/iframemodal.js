/* Javascript for IFrameModalXBlock. */
function IFrameModalXBlock(runtime, element) {

  function close_modal(modal_id) {
    const $modal = $(modal_id);
    $('select, input, textarea, button, a').off('focus');
    $("#" + overlay_id).fadeOut(200);
    $modal.css({ "display": "none" });
    $modal.attr('aria-hidden', true);
    $modal.find('iframe').attr('src', '');
    $('body').css('overflow', 'auto');
    $('button[data-target]', element).focus();
  }

    $('button[data-target]', element).click(function(eventObject) {

      const modal_id = eventObject.target.data("target");
      const closeButton = $('.close-modal');
      const defaults = { top: 100, overlay: 0.5, closeButton: null };
      const overlay_id = (modal_id + '_lean-overlay').replace('#', '');
      const overlay = $("<div id='" + overlay_id + "' class='lean-overlay'></div>");
      $("body").append(overlay);
      const $modal = $(modal_id);
      $modal.find('iframe').attr('src', $modal.data('launch-url'));
      $("#" + overlay_id).click(function () {
          close_modal(modal_id)
      });
      closeButton.click(function () {
        close_modal(modal_id)
      })
      $("#" + overlay_id).css({ "display": "block", opacity: 0 });
      $("#" + overlay_id).fadeTo(200, o.overlay);
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
