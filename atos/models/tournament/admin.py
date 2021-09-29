from django.contrib import admin
from atos.models.tournament import models

# Register your models here.


@admin.register(models.Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "checked_in",
        "match_checked_in",
    )

    list_filter = ("checked_in",)


@admin.register(models.Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "discord_id",
    )


@admin.register(models.Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = (
        "set",
        "round",
        "team1",
        "team2",
    )
    list_filter = ("round",)
