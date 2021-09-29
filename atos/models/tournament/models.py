from django.db import models

# Create your models here.


class Team(models.Model):
    """
    Represents a team in the tournament.
    """

    player_id = models.PositiveIntegerField(
        verbose_name="Player ID",
        primary_key=True,
    )
    name = models.CharField(
        verbose_name="Name",
        max_length=64,
    )
    checked_in = models.BooleanField(
        verbose_name="Has checked-in",
        default=False,
    )
    match_checked_in = models.BooleanField(
        verbose_name="Checked-in for match",
        default=False,
    )


class Player(models.Model):
    """
    Represents a single player part of a team.
    """

    discord_id = models.PositiveIntegerField(
        verbose_name="Discord ID",
        primary_key=True,
    )
    name = models.CharField(
        verbose_name="Name",
        max_length=64,
    )
    team = models.ForeignKey(
        Team,
        verbose_name="Team",
        on_delete=models.CASCADE,
    )


class Match(models.Model):
    """
    Represents a match between two players or two teams.
    """

    round = models.IntegerField(
        verbose_name="Round",
    )
    set = models.CharField(
        verbose_name="Set",
        max_length=3,
    )
    id = models.IntegerField(
        verbose_name="ID",
        primary_key=True,
    )
    team1 = models.OneToOneField(
        Team,
        verbose_name="Team 1",
        related_name="team1",
        on_delete=models.CASCADE,
    )
    team2 = models.OneToOneField(
        Team,
        verbose_name="Team 2",
        related_name="team2",
        on_delete=models.CASCADE,
    )
