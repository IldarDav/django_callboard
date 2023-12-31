# Generated by Django 4.2.7 on 2023-11-10 12:11

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ads', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_type', models.CharField(choices=[('tanks', 'Танки'), ('healers', 'Хилы'), ('damage_dealers', 'ДД'), ('merchants', 'Торговцы'), ('gildmasters', 'Гилдмастеры'), ('quest_givers', 'Квестгиверы'), ('blacksmiths', 'Кузнецы'), ('tanners', 'Кожевники'), ('potion_makers', 'Зельевары'), ('spell_masters', 'Мастера заклинаний')], max_length=15, verbose_name='Категория')),
                ('time_in', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=255, verbose_name='Название объявления')),
                ('text', ckeditor.fields.RichTextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='announcementcategory',
            name='announcement',
        ),
        migrations.RemoveField(
            model_name='announcementcategory',
            name='category',
        ),
        migrations.RemoveField(
            model_name='category',
            name='subscribers',
        ),
        migrations.RemoveField(
            model_name='response',
            name='announcement',
        ),
        migrations.RemoveField(
            model_name='response',
            name='user',
        ),
        migrations.DeleteModel(
            name='Announcement',
        ),
        migrations.DeleteModel(
            name='AnnouncementCategory',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Response',
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ads.post'),
        ),
    ]
