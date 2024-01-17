"""TO-DO: Write a description of what this XBlock is."""

import pkg_resources
from web_fragments.fragment import Fragment
from xblock.core import XBlock
from xblock.fields import String, Scope

class IFrameModalXBlock(StudioEditableXBlockMixin, XBlock):
    """
    TO-DO: document what your XBlock does.
    """

    # Fields are defined on the class.  You can access them in your code as
    # self.<fieldname>.

    # TO-DO: delete count, and define your own fields.
    iframe_url = String(
        default='https://grafana.learning.app.meca.in.th/d/c303c3f8-8709-41db-91a9-806cd5ae3006/e0b980-e0b8a3-e0b8b5-e0b8a2-e0b899-e0b894-e0b8b5?orgId=1&amp;showCategory=Panel+options&amp;from=1695007267018&amp;to=1695028867018&amp;theme=light&amp;kiosk', scope=Scope.user_state,
        help="iframe URL",
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
        frag.add_css(self.resource_string("static/css/bulma.min.css"))
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
