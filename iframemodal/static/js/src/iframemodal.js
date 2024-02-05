/* Javascript for IFrameModalXBlock. */
function IFrameModalXBlock(runtime, element) {
  function createIframeElelment(wrapper) {
    const iframe = $('<iframe>').attr({
      title: wrapper.data('title'),
      name: `iframe-${wrapper.data('target')}`,
      id: `iframe-${wrapper.data('target')}`,
      src: wrapper.data('iframe-url'),
      allowfullscreen: "true",
      webkitallowfullscreen: "true",
      mozallowfullscreen: "true",
      allow: "microphone *; camera *; midi *; geolocation *; encrypted-media *"
    }).css({
      width: '100%',
      height: '100%'
    });
    iframe.on('message', console.log)
  }

  function handleOpenModalButtonClick(eventObject) {
    const wrapper = $(eventObject.target.parent);
    if (window !== window.parent) {
      window.parent.addEventListener('message', console.log)
      window.parent.postMessage(
          {
              'type': 'plugin.modal',
              'payload': {
                  'url': wrapper.data('iframe-url'),
                  'title': wrapper.data('title'),
                  'width': $modal.data('width')
              }
          },
          document.referrer
      );
      return;
    }
    
    const closeButton = $('<button>');
    closeButton.addClass('close-modal');
    closeButton.append('<i class="icon fa fa-remove"></i>');
    closeButton.append('<span class="sr">Close</span>')
    const defaults = { top: 100, overlay: 0.5, closeButton: null };
    const overlay_id = 'lean_overlay';
    const iframe = createIframeElelment(wrapper);
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
  }

  function handleOpenNewWindowButtonClick(eventObject) {
    const wrapper = $(eventObject.target.parent);
    const newWindow = window.open(wrapper.data('iframe-url'));
    newWindow.addEventListener('message', console.log);
  }

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

    $(function ($) {
      if (wrapper.data('display') === 'inline') {
        wrapper.append(createIframeElelment(wrapper));
      } else if (wrapper.data('display') === 'modal') {
        const button = $('<button>');
        button.addClass("btn btn-pl-primary btn-base");
        button.text(wrapper.data('btn-text'));
        button.click(handleOpenModalButtonClick);
        wrapper.append(button);
      } else if (wrapper.data('display') === 'modalWithInline') {
        wrapper.append(createIframeElelment(wrapper));
      } else if (wrapper.data('display') === 'newWindow') {
        const button = $('<button>');
        button.addClass("btn btn-pl-primary btn-base");
        button.text(wrapper.data('btn-text'));
        button.click(handleOpenNewWindowButtonClick);
        wrapper.append(button);
      }
    });
}
