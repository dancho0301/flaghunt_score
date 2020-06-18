# Generated by Django 2.2.13 on 2020-06-17 00:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='開催日')),
                ('name', models.CharField(max_length=256, verbose_name='イベント名')),
            ],
            options={
                'db_table': 'event',
            },
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='flaghunt_score.Event', verbose_name='イベント')),
            ],
            options={
                'db_table': 'game',
            },
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='氏名')),
                ('nickname', models.CharField(max_length=256, verbose_name='ニックネーム')),
                ('sex', models.CharField(choices=[('man', '男性'), ('woman', '女性'), ('other', 'その他')], max_length=5, verbose_name='性別')),
            ],
            options={
                'db_table': 'player',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='チーム名')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='flaghunt_score.Event', verbose_name='イベント')),
            ],
            options={
                'db_table': 'team',
            },
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='flaghunt_score.Player', verbose_name='メンバー')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='flaghunt_score.Team', verbose_name='チーム')),
            ],
            options={
                'db_table': 'team_member',
            },
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='flaghunt_score.Event', verbose_name='イベント')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='flaghunt_score.Game', verbose_name='ゲーム')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='flaghunt_score.Player', verbose_name=' プレイヤー')),
            ],
            options={
                'db_table': 'result',
            },
        ),
        migrations.AddField(
            model_name='game',
            name='flaghunter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='flaghunt_score.Player', verbose_name=' フラッグハンター'),
        ),
        migrations.AddField(
            model_name='game',
            name='team1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='team1', to='flaghunt_score.Team', verbose_name=' チーム1'),
        ),
        migrations.AddField(
            model_name='game',
            name='team2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='team2', to='flaghunt_score.Team', verbose_name=' チーム2'),
        ),
        migrations.AddField(
            model_name='game',
            name='winner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='winner', to='flaghunt_score.Team', verbose_name=' 勝利チーム'),
        ),
    ]
