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
          <p class="image is-4by3">
            <img src="https://bulma.io/images/placeholders/1280x960.png" alt="">
          </p>
        </div>
        <button class="modal-close is-large" aria-label="close"></button>
      </div>`)
        $("body").append(modalEle);
        
    });

    $(function ($) {
      function openModal($el) {
        $el.classList.add('is-active');
      }
    
      function closeModal($el) {
        $el.classList.remove('is-active');
      }
    
      function closeAllModals() {
        (document.querySelectorAll('.modal') || []).forEach(($modal) => {
          closeModal($modal);
        });
      }
    
      // Add a click event on buttons to open a specific modal
      (document.querySelectorAll('.js-modal-trigger') || []).forEach(($trigger) => {
        const modal = $trigger.dataset.target;
        const $target = document.getElementById(modal);
    
        $trigger.addEventListener('click', () => {
          openModal($target);
        });
      });
    
      // Add a click event on various child elements to close the parent modal
      (document.querySelectorAll('.modal-background, .modal-close, .modal-card-head .delete, .modal-card-foot .button') || []).forEach(($close) => {
        const $target = $close.closest('.modal');
    
        $close.addEventListener('click', () => {
          closeModal($target);
        });
      });
    
      // Add a keyboard event to close all modals
      document.addEventListener('keydown', (event) => {
        if (event.code === 'Escape') {
          closeAllModals();
        }
      });
    });
}
