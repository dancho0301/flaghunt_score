from django.db import models
from django.utils import timezone

# Create your models here.

class Player(models.Model):
    """ プレイヤーモデル """
    class Meta:
        db_table = 'player'
        verbose_name_plural = 'プレイヤー'
    
    SEXES = (('man', '男性'), ('woman', '女性'), ('other', 'その他'))

    name = models.CharField(verbose_name='氏名', max_length=256)
    nickname = models.CharField(verbose_name='ニックネーム', max_length=256)
    sex = models.CharField(verbose_name='性別', choices=SEXES, max_length=5)
    created_date = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.name

class Event(models.Model):
    """ イベントモデル """
    class Meta:
        db_table = 'event'
        verbose_name_plural = 'イベント'
    
    date = models.DateField(verbose_name='開催日')
    name = models.CharField(verbose_name='イベント名', max_length=256)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Team(models.Model):
    """ チームモデル """
    class Meta:
        db_table = 'team'
        verbose_name_plural = 'チーム'

    event = models.ForeignKey(Event, verbose_name='イベント', on_delete=models.PROTECT)
    name = models.CharField(verbose_name='チーム名', max_length=256)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class TeamMember(models.Model):
    """ チームメンバーモデル """
    class Meta:
        db_table = 'team_member'
        verbose_name_plural = 'チームメンバー'

    team   = models.ForeignKey(Team, verbose_name='チーム', on_delete=models.PROTECT)
    player = models.ForeignKey(Player, verbose_name='メンバー', on_delete=models.PROTECT)
    created_date = models.DateTimeField(default=timezone.now)

class Game(models.Model):
    """ ゲームモデル """
    class Meta:
        db_table = 'game'
        verbose_name_plural = 'ゲーム'

    event      = models.ForeignKey(Event, verbose_name='イベント', on_delete=models.PROTECT)
    team1      = models.ForeignKey(Team, verbose_name=' チーム1', on_delete=models.PROTECT, related_name='team1')
    team2      = models.ForeignKey(Team, verbose_name=' チーム2', on_delete=models.PROTECT, related_name='team2')
    winner     = models.ForeignKey(Team, verbose_name=' 勝利チーム', on_delete=models.PROTECT, related_name='winner', null=True, blank=True)
    flaghunter = models.ForeignKey(Player, verbose_name=' フラッグハンター', on_delete=models.PROTECT, null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now)

class Result(models.Model):
    """ 戦績モデル """
    class Meta:
        db_table = 'result'
        verbose_name_plural = '戦績'

    event  = models.ForeignKey(Event, verbose_name='イベント', on_delete=models.PROTECT)
    game   = models.ForeignKey(Game, verbose_name='ゲーム', on_delete=models.PROTECT)
    player = models.ForeignKey(Player, verbose_name=' プレイヤー', on_delete=models.PROTECT)
    created_date = models.DateTimeField(default=timezone.now)


