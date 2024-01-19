"""TO-DO: Write a description of what this XBlock is."""

import pkg_resources
from web_fragments.fragment import Fragment
from xblock.core import XBlock
from xblock.fields import String, Scope
try:
    from xblock.utils.resources import ResourceLoader
    from xblock.utils.studio_editable import StudioEditableXBlockMixin
except ModuleNotFoundError:  # For backward compatibility with releases older than Quince.
    from xblockutils.resources import ResourceLoader
    from xblockutils.studio_editable import StudioEditableXBlockMixin

@XBlock.wants('settings')
class IFrameModalXBlock(StudioEditableXBlockMixin, XBlock):
    """
    TO-DO: document what your XBlock does.
    """

    editable_fields = ('title', 'iframe_url', 'btn_text')

    # TO-DO: delete count, and define your own fields.
    title = String(
        display_name="Title",
        default='',
        help="title",
        scope=Scope.settings
    )
    btn_text = String(
        display_name="Button text",
        default='',
        help="Button text",
        scope=Scope.settings
    )
    iframe_url = String(
        display_name="IFrame URL",
        default='',
        help="IFrame URL display in modal",
        scope=Scope.settings
    )

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    # TO-DO: change this view to display your data your own way.
    def student_view(self, context=None):
        """
        The primary view of the IFrameModalXBlock, shown to students
        when viewing courses.
        """
        html = self.resource_string("static/html/iframemodal.html")
        frag = Fragment(html.format(self=self))
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
