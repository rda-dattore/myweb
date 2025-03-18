from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page


class HomePage(Page):
    body = RichTextField(blank=False, default="")
    content_panels = Page.content_panels + [
        FieldPanel("welcome", classname="collapsible collapsed"),
    ]
    is_creatable = False
