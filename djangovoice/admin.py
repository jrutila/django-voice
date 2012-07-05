from django.contrib import admin
from djangovoice.models import Feedback, Status, Type


class SlugFieldAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

try:
    import reversion
    class FeedbackAdmin(reversion.VersionAdmin):
        pass
    admin.site.register(Feedback, FeedbackAdmin)
except ImportError:
    admin.site.register(Feedback)


admin.site.register([Status, Type], SlugFieldAdmin)
