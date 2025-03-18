from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField
from wagtail.models import Page


class HomePage(Page):
    body = RichTextField(blank=False, default="")
    content_panels = Page.content_panels + [
        FieldPanel("welcome", classname="collapsible collapsed"),
    ]
    is_creatable = False
