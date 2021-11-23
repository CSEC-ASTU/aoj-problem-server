from django.contrib import admin

from core.models import Contest, Problem, SampleInput, SampleOutput, Sponsor

@admin.register(Contest)
class ContestAdmin(admin.ModelAdmin):
	model = Contest

class SampleInputInline(admin.TabularInline):
	model = SampleInput
	extra = 0

class SampleOutputInline(admin.TabularInline):
	model = SampleOutput
	extra = 0

@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
	model = Problem
	inlines = [
		SampleInputInline,
		SampleOutputInline
	]

@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
	model = Sponsor
	
	