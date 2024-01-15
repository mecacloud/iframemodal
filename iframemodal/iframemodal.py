"""TO-DO: Write a description of what this XBlock is."""

import pkg_resources
from lti_consumer import LtiConsumerXBlock
from lti_consumer.utils import _
from web_fragments.fragment import Fragment
from xblock.core import XBlock
from xblock.fields import String, Scope
from xblockutils.resources import ResourceLoader

class IFrameModalXBlock(LtiConsumerXBlock):
    override_launch_url = String(
        display_name=_("Launch URL"),
        default='https://applications.zoom.us/lti/rich',
        scope=Scope.settings
    )

    lti_id = 'zoom'
    display_name = String(
        display_name=_("Display Name"),
        help=_(
            "Enter the name that students see for this component. "
            "Analytics reports may also use the display name to identify this component."
        ),
        scope=Scope.settings,
        default=_("Zoom"),
    )
    description = String(
        display_name=_("Application Information"),
        help=_(
            "Enter a description of your use of Zoom. "
        ),
        default=_("Use Zoom to host office hours and other course meetings"),
        scope=Scope.settings
    )
    block_settings_key = 'edx_zoom'

    editable_fields = (
        'display_name', 'description', 'custom_parameters', 'override_launch_url',
        'inline_height', 'modal_height', 'modal_width'
    )
    ask_to_send_username = ask_to_send_email = True
    has_author_view = True

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    def _get_context_for_template(self):
        ctx = super()._get_context_for_template()
        ctx['missing_credentials'] = self.lti_provider_key_secret[0] is None
        ctx['ask_to_send_username'] = ctx['ask_to_send_email'] = True
        return ctx

    # TO-DO: change this view to display your data your own way.
    def student_view(self, context=None):
        fragment = Fragment()
        lti_loader = ResourceLoader('lti_consumer')
        loader = ResourceLoader(__name__)
        context = self._get_context_for_template()
        fragment.add_content(loader.render_mako_template('/templates/student.html', context))
        fragment.add_css(loader.load_unicode('static/css/student.css'))
        fragment.add_javascript(lti_loader.load_unicode('static/js/xblock_lti_consumer.js'))
        fragment.initialize_js('LtiConsumerXBlock')
        return fragment

    def author_view(self, context):
        fragment = Fragment()
        loader = ResourceLoader(__name__)
        context.update(self._get_context_for_template())
        fragment.add_content(loader.render_mako_template('/templates/author.html', context))
        return fragment

    # TO-DO: change this to create the scenarios you'd like to see in the
    # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("IFrameModalXBlock",
             """<iframemodal/>
             """),
            ("Multiple IFrameModalXBlock",
             """<vertical_demo>
                <iframemodal/>
                <iframemodal/>
                <iframemodal/>
                </vertical_demo>
             """),
        ]
