# Generated by Django 3.2.16 on 2023-08-21 06:51

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
            name='MarkaVehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MarkaModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=100)),
                ('name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.markavehicle')),
            ],
        ),
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_rudder', models.CharField(choices=[('левый', 'Левый'), ('правый', 'Правый')], max_length=20)),
                ('type_vehicle', models.CharField(choices=[('легковой', ' Легковой'), ('коммерческий', 'Грузовой'), ('мотоцикл', 'Мотоцикл')], max_length=30)),
                ('type_transmission', models.CharField(choices=[('передний', 'Передний'), ('задний', 'Задний'), ('олный', 'Полный')], max_length=20)),
                ('type_drive', models.CharField(choices=[('механическая', 'Механическая'), ('робот', 'Робот'), ('автоматическая', 'Автоматическая')], max_length=20)),
                ('type_body', models.CharField(choices=[('седан', 'Седан'), ('хетчбек', 'Хетчбек'), ('купе', 'Купе'), ('внедорожник', 'Внедорожник'), ('пикап', 'Пикап'), ('универсал', 'Универсал'), ('лифтбек', 'Лифтбек'), ('кабриолет', 'Кабриолет'), ('минивен', 'Минивен')], max_length=20)),
                ('type_engine', models.CharField(choices=[('дизель', 'Дизель'), ('бензин', 'Бензин'), ('электро', ' Электро'), ('гибрид', 'Гибрид'), ('газ', 'Газ')], max_length=20)),
                ('date', models.DateField()),
                ('type_ad', models.CharField(choices=[('обычное', 'Обычное'), ('вип', 'Вип'), ('ремиум', 'Премиум')], max_length=20)),
                ('marka', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.markavehicle')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
