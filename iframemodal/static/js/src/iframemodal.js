/* Javascript for IFrameModalXBlock. */
function IFrameModalXBlock(runtime, element) {

    function updateCount(result) {
        // $('.count', element).text(result.count);
    }

    // var handlerUrl = runtime.handlerUrl(element, 'increment_count');

    $('button[data-target]', element).click(function(eventObject) {
      const modalEle = $(`<div class="modal is-active">
        <div class="modal-background"></div>
        <div class="modal-content">
          DEMO
        </div>
        <button class="modal-close is-large" aria-label="close"></button>
      </div>`)
        $("body").append(modalEle);
        
    });

    $(function ($) {
      
        /* Here's where you'd do things on page load. */
        // $.fn.extend({
        //   iframeModal: function (options) {
        //     var $trigger = $(this);
        //     var modal_id = $trigger.data("target");
        //     var defaults = { top: 100, overlay: 0.5, closeButton: null };
        //     var overlay_id = (modal_id + '_lean-overlay').replace('#', '');
        //     var overlay = $("<div id='" + overlay_id + "' class='lean-overlay'></div>");
        //     $("body").append(overlay);
        //     return this.each(function () {
        //       var o = options;

        //       var $modal = $(modal_id);
        //       return $modal;
        //     })
        //   }
        // })
    });
}
