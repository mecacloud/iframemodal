"""TO-DO: Write a description of what this XBlock is."""

import pkg_resources
from web_fragments.fragment import Fragment
from xblock.core import XBlock
from xblock.fields import String, Scope, Integer
from django.db.models import Q
# from common.djangoapps.third_party_auth.api.utils import filter_user_social_auth_queryset_by_provider
try:
    from xblock.utils.resources import ResourceLoader
    from xblock.utils.studio_editable import StudioEditableXBlockMixin
except ModuleNotFoundError:  # For backward compatibility with releases older than Quince.
    from xblockutils.resources import ResourceLoader
    from xblockutils.studio_editable import StudioEditableXBlockMixin

@XBlock.wants('settings')
@XBlock.wants('user')
class IFrameModalXBlock(StudioEditableXBlockMixin, XBlock):
    """
    TO-DO: document what your XBlock does.
    """

    # editable_fields = ('title', 'aetool', 'iframe_url', 'btn_text', 'width', 'height', 'display')

    # TO-DO: delete count, and define your own fields.
    title = String(
        display_name="Title",
        default='',
        help="title",
        scope=Scope.settings
    )
    aetool = String(
        display_name="AE Tool",
        choices=[
            ('simulator', 'Simulator'),
            ('chatbot', 'Chatbot'),
            ('bookroll', 'Bookroll'),
            ('iframe', 'External URL')
        ],
        default='iframe',
        help="Select AE Tool",
        scope=Scope.settings
    )
    btn_text = String(
        display_name="Button text",
        default='Button',
        help="Button text",
        scope=Scope.settings
    )
    iframe_url = String(
        display_name="IFrame URL",
        default='',
        help="IFrame URL display in modal",
        scope=Scope.settings
    )
    width = String(
        display_name="Width",
        default='80%',
        help="Element Width",
        scope=Scope.settings
    )
    height = String(
        display_name="Height",
        default='600',
        help="Element Height",
        scope=Scope.settings
    )
    display = String(
        display_name="Display mode",
        values=[
            {"value": 'inline', "display_name": 'Embedded inline'},
            {"value": 'modal', "display_name": 'Open modal by button'},
            {"value": 'modalWithInline', "display_name": 'Embedded inline with modal'},
            {"value": 'newWindow', "display_name": 'Open new window by button'}
        ],
        default='modal',
        help="Element display option",
        scope=Scope.settings
    )

    @property
    def lms_role(self):
        """
        Get system user role.
        """
        user = self.runtime.service(self, 'user').get_current_user()
        return user.opt_attrs.get('edx-platform.user_role', 'student')

    @property
    def lms_user_name(self):
        """
        Returns the edx-platform database user id for the current user.
        """
        username = self.runtime.service(self, 'user').get_current_user().opt_attrs.get(
            'edx-platform.username', '')
        return username

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    def _get_context_for_template(self):
        return {
            'scope_ids': self.scope_ids,
            'element_id': str(self.scope_ids.usage_id),
            'title': self.title,
            'btn_text': self.btn_text,
            'iframe_url': self.iframe_url,
            'width': self.width,
            'height': self.height,
            'display': self.display,
        }

    # TO-DO: change this view to display your data your own way.
    def student_view(self, context=None):
        """
        The primary view of the IFrameModalXBlock, shown to students
        when viewing courses.
        """
        html = self.resource_string("static/html/student.html")
        frag = Fragment(html.format(self=self, view='student'))
        # frag.add_css(self.resource_string("static/css/lms.css"))
        frag.add_css(self.resource_string("static/css/iframemodal.css"))
        frag.add_javascript(self.resource_string("static/js/src/iframemodal.js"))
        frag.initialize_js('IFrameModalXBlock')
        return frag
    
    def author_view(self, context=None):
        """
        The primary view of the IFrameModalXBlock, shown to students
        when viewing courses.
        """
        html = self.resource_string("static/html/student.html")
        frag = Fragment(html.format(self=self, view='studio'))
        # frag.add_css(self.resource_string("static/css/lms.css"))
        frag.add_css(self.resource_string("static/css/iframemodal.css"))
        frag.add_javascript(self.resource_string("static/js/src/iframemodal.js"))
        frag.initialize_js('IFrameModalXBlock')
        return frag

    # TO-DO: change this handler to perform your own actions.  You may need more
    # than one handler, or you may not need any handlers at all.
    @XBlock.json_handler
    def increment_count(self, data, suffix=''):
        """
        An example handler, which increments the data.
        """
        # Just to show data coming in...
        assert data['hello'] == 'world'

        self.count += 1
        return {"count": self.count}

    # TO-DO: change this to create the scenarios you'd like to see in the
    # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("IFrameModalXBlock",
             """<iframemodal display_name="iframe modal" />
             """),
            ("Multiple IFrameModalXBlock",
             """<vertical_demo>
                <iframemodal display_name="iframe modal" />
                <iframemodal display_name="iframe modal" />
                <iframemodal display_name="iframe modal" />
                </vertical_demo>
             """),
        ]
