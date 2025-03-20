from django.db import models
from wagtail.admin.panels import (
    FieldPanel,
    MultiFieldPanel,
    PageChooserPanel
)
from django.utils import timezone
from wagtail.fields import RichTextField
from wagtail.models import Page
from wagtail.snippets.models import register_snippet


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
                FieldPanel("image"),
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


@register_snippet
class SocialMedia(models.Model):
    """ Social media links for snippets """

    name = models.CharField(max_length=50)
    related_url = models.URLField(
        blank=False,
        null=False,
        help_text='Link to social media page',
    )
    aria_label=models.CharField(
        max_length=50,
        help_text='Aria label to apply to the <a href> tag',
    )
    icon_style=models.CharField(
        max_length=50,
        default="",
        verbose_name='Icon style',
        help_text="Icon style class to render the social media icon. Specify 'fab' for brands and 'fas' for solid.  See fontawesome version 5 documentation for more info.",
    )
    icon_name=models.CharField(
        max_length=50,
        default="",
        verbose_name='Icon name',
        help_text='Icon name class from the fontawesome icon set',
    )

    panels = [
        MultiFieldPanel(
            [
                FieldPanel("name"),
                FieldPanel("related_url"),
                FieldPanel("aria_label"),
                FieldPanel("icon_style"),
                FieldPanel("icon_name"),
            ]
        )
    ]

    def __str__(self):
        """ String repr of this class """
        return self.name

    class Meta:
        verbose_name = "Social Media Link"
        verbose_name_plural = "Social Media Links"


@register_snippet
class AlertMessage(models.Model):
    """ Alert message for snippets """

    DANGER = 'danger'
    WARNING = 'warning'
    INFO = 'info'
    LEVEL_CHOICES = [
        (DANGER, 'danger'),
        (WARNING, 'warning'),
        (INFO, 'info'),
    ]
    message = RichTextField(blank=False, default="")
    name = models.CharField(max_length=100)
    level = models.CharField(
        max_length=7,
        choices=LEVEL_CHOICES,
        default=INFO,
    )
    related_url = models.URLField(
        blank=True,
        null=True,
        help_text='Optional.  Related page takes precedence over related URL.',
    )
    related_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Optional.  Related page takes precedence over related URL.',
    )
    start_date = models.DateField('Start date', default=timezone.now())
    end_date = models.DateField('End date', default=timezone.now())

    panels = [
        MultiFieldPanel(
            [
                FieldPanel("name"),
                FieldPanel("message"),
                FieldPanel("level"),
            ],
            heading="Alert name, message, and level",
        ),
        MultiFieldPanel(
            [
                PageChooserPanel("related_page"),
                FieldPanel("related_url"),
            ],
            heading="Related URL or page",
        ),
        MultiFieldPanel(
            [
                FieldPanel("start_date"),
                FieldPanel("end_date"),
            ],
            heading="Start and end dates to display message",
        ),
    ]

    def __str__(self):
        """ String repr of this class """
        return self.name

    class Meta:
        verbose_name = "Alert Message"
        verbose_name_plural = "Alert Messages"


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
