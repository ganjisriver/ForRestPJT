from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tmdb_id', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=50)),
                ('original_title', models.CharField(max_length=100)),
                ('release_date', models.CharField(max_length=50, null=True)),
                ('runtime', models.TextField(null=True)),
                ('overview', models.TextField(null=True)),
                ('popularity', models.FloatField(null=True)),
                ('vote_average', models.FloatField(null=True)),
                ('vote_count', models.FloatField(null=True)),
                ('adult', models.BooleanField(default=False)),
                ('genre', models.JSONField(null=True)),
                ('poster_path', models.TextField(default='https://image.tmdb.org/t/p/w500/d9C2H1qoFt9AL4DwRlqEEZK4hVa.jpg', null=True)),
                ('movie_like_users', models.ManyToManyField(related_name='user_like_movies', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
