# Generated by Django 4.1.3 on 2022-11-05 21:49
import random

from django.db import migrations

from applications.core.models import ActivityLog


def create_users(apps, schema_editor):
    user_model = apps.get_model('auth', 'User')
    with open('applications/core/fixtures/users.csv', 'r') as fixture:
        for line_index, line in enumerate(fixture):
            print(f'Processing user {line_index + 1}')
            username = line.split(',')[4]
            user_model.objects.create(username=username)


def create_activity_logs(apps, schema_editor):
    activity_log_model = apps.get_model('core', 'ActivityLog')
    counter = 1
    for index in range(0, 100):
        print(f'Creating activity log bulk {index + 1}/100')
        user_id = index + 1
        user_activities = []
        for _ in range(0, 10000):
            interaction_type = random.choice(ActivityLog.InteractionTypes.choices)
            activity = activity_log_model(id=counter, user_id=user_id, interaction_type=interaction_type)
            user_activities.append(activity)
            counter += 1
        activity_log_model.objects.bulk_create(user_activities)


def create_posts(apps, schema_editor):
    post_model = apps.get_model('core', 'Post')
    for index in range(0, 20):
        print(f'Creating Post {index + 1}/20')
        title = f'Post {index + 1}'
        description = f'Description for post {index + 1}'
        image_url = 'https://picsum.photos/200/300'
        post_model.objects.create(title=title, description=description, image_src=image_url)


class Migration(migrations.Migration):
    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_users),
        migrations.RunPython(create_activity_logs),
        migrations.RunPython(create_posts),
    ]