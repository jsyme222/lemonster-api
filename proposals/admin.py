from proposals.models import Proposal, ProposalTheme
from django.contrib import admin


@admin.register(Proposal, ProposalTheme)
class ProposalAdmin(admin.ModelAdmin):
    pass
