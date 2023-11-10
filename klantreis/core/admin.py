from django.contrib import admin
from django.db import models


from core.models import (
    Organisation,
    Step,
    Edge,
    Process
)

class OrganisationAdmin(admin.ModelAdmin):
    pass


class StepAdmin(admin.ModelAdmin):
    pass


class EdgeAdmin(admin.ModelAdmin):
    pass


class ProcessAdmin(admin.ModelAdmin):
    pass


admin.site.register(Organisation, OrganisationAdmin)
admin.site.register(Step, StepAdmin)
admin.site.register(Edge, EdgeAdmin)
admin.site.register(Process, ProcessAdmin)
