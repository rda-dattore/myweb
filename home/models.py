from django.db import models
from wagtail.admin.panels import (
    FieldPanel,
    MultiFieldPanel,
    PageChooserPanel
)
from wagtail.fields import RichTextField
from wagtail.models import Page


@register_snippet
class DecsStaff(models.Model):
    """ DECS staff members for snippets """

    name = models.CharField(
        max_length=100,
        help_text='DECS staff member name',
    )
    email = models.EmailField(
        max_length=100,
        default='rdahelp@ucar.edu',
    )
    image = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="+",
        help_text='DECS staff image (optional)',
    )

    panels = [
        MultiFieldPanel(
            [
                FieldPanel("name"),
                FieldPanel("email"),
                ImageChooserPanel("image"),
            ],
            heading="Name, Email, and Image"
        )
    ]

    def __str__(self):
        """ String repr of this class """
        return self.name

    class Meta:
        verbose_name = "DECS Staff Member"
        verbose_name_plural = "DECS Staff Members"


class HomePage(Page):
    tagline = models.CharField(max_length=100, blank=False, default="")
    welcome = RichTextField(blank=False, default="")
    search_box_title = models.CharField(max_length=255, blank=False, default="",
        verbose_name="Search Box Title")
    search_box_placeholder = models.CharField(max_length=255, blank=False, default="",
        verbose_name="Search Box Placeholder")
    card_1_title = models.CharField(max_length=255, blank=False, default="",
        verbose_name="Title")
    card_1_icon_name = models.CharField(max_length=50, blank=False, default="",
        verbose_name="Icon")
    card_1_text = RichTextField(blank=False, default="",
        verbose_name="Body Text")
    card_1_footer_text = models.CharField(max_length=255, blank=False,
        default="", verbose_name="Footer Text")
    card_1_footer_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    card_2_title = models.CharField(max_length=255, blank=False, default="",
        verbose_name="title")
    card_2_icon_name = models.CharField(max_length=50, blank=False, default="",
        verbose_name="Icon")
    card_2_text = RichTextField(blank=False, default="",
         verbose_name="Body Text")
    card_2_footer_text = models.CharField(max_length=255, blank=False,
        default="", verbose_name="Footer Text")
    card_2_footer_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    card_3_title = models.CharField(max_length=255, blank=False, default="",
        verbose_name="Title")
    card_3_icon_name = models.CharField(max_length=50, blank=False, default="",
        verbose_name="Icon")
    card_3_text = RichTextField(blank=False, default="",
        verbose_name="Body Text")
    card_3_footer_text = models.CharField(max_length=255, blank=False,
        default="", verbose_name="Footer Text")
    card_3_footer_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    
    content_panels = Page.content_panels + [
        FieldPanel('tagline', classname="collapsible collapsed"),
        FieldPanel('welcome', classname="collapsible collapsed"),
        MultiFieldPanel([
            FieldPanel('search_box_title'),
            FieldPanel('search_box_placeholder'),
        ], heading="Search Box", classname="collapsible collapsed"),
        MultiFieldPanel([
            FieldPanel('card_1_title'),
            FieldPanel('card_1_icon_name'),
            FieldPanel('card_1_text'),
            FieldPanel('card_1_footer_text'),
            PageChooserPanel('card_1_footer_page'),
        ], heading="Card 1", classname="collapsible collapsed"),
        MultiFieldPanel([
            FieldPanel('card_2_title'),
            FieldPanel('card_2_icon_name'),
            FieldPanel('card_2_text'),
            FieldPanel('card_2_footer_text'),
            PageChooserPanel('card_2_footer_page'),
        ], heading="Card 2", classname="collapsible collapsed"),
        MultiFieldPanel([
            FieldPanel('card_3_title'),
            FieldPanel('card_3_icon_name'),
            FieldPanel('card_3_text'),
            FieldPanel('card_3_footer_text'),
            PageChooserPanel('card_3_footer_page'),
        ], heading="Card 3", classname="collapsible collapsed"),
    ]
    is_creatable = False
