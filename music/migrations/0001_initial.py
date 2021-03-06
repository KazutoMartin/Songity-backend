# Generated by Django 3.1.6 on 2022-03-07 11:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('personality', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('link', models.URLField(verbose_name='Link')),
                ('artist_id', models.CharField(max_length=50, verbose_name='ID')),
                ('uri', models.URLField(verbose_name='URI')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created at')),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('album', models.CharField(max_length=50, verbose_name='Album')),
                ('song_id', models.CharField(max_length=50, verbose_name='ID')),
                ('link', models.URLField(verbose_name='Link')),
                ('image_link', models.URLField(verbose_name='Image Link')),
                ('preview_url', models.URLField(verbose_name='Preview URL')),
                ('uri', models.URLField(verbose_name='URI')),
                ('duration_ms', models.IntegerField(verbose_name='Duration(ms)')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created at')),
                ('artist', models.ManyToManyField(to='music.Artist', verbose_name='Artist')),
            ],
        ),
        migrations.CreateModel(
            name='SpotifyAnalysis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('danceability', models.FloatField(verbose_name='danceability')),
                ('energy', models.FloatField(verbose_name='energy')),
                ('loudness', models.FloatField(verbose_name='loudness')),
                ('speechiness', models.FloatField(verbose_name='speechiness')),
                ('acousticness', models.FloatField(verbose_name='acousticness')),
                ('instrumentalness', models.FloatField(verbose_name='instrumentalness')),
                ('liveness', models.FloatField(verbose_name='liveness')),
                ('valence', models.FloatField(verbose_name='valence')),
                ('tempo', models.FloatField(verbose_name='tempo')),
                ('time_signature', models.FloatField(verbose_name='time_signature')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created at')),
            ],
        ),
        migrations.CreateModel(
            name='SuggestedSongs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('personality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personality.personality', verbose_name='Personality')),
                ('songs', models.ManyToManyField(to='music.Song', verbose_name='Songs')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.AddField(
            model_name='song',
            name='spotify_analysis',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='music.spotifyanalysis', verbose_name='spotify analysis'),
        ),
        migrations.CreateModel(
            name='ShareSong',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liked_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Liked at')),
                ('personality', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='personality.personality', verbose_name='Personality')),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.song', verbose_name='Song')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='PreviewListen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0, verbose_name='Count')),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.song', verbose_name='Song')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='LikeSong',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liked_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Liked at')),
                ('personality', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='personality.personality', verbose_name='Personality')),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.song', verbose_name='Song')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='LikeArtist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liked_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Liked at')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.artist', verbose_name='Artist')),
                ('personality', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='personality.personality', verbose_name='Personality')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='DislikeSong',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disliked_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Disliked at')),
                ('personality', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='personality.personality', verbose_name='Personality')),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.song', verbose_name='Song')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='DislikeArtist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isliked_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Disliked at')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.artist', verbose_name='Artist')),
                ('personality', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='personality.personality', verbose_name='Personality')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
    ]
