from django.db import migrations


def add_data(apps, schema_editor):
    PriceType = apps.get_model("bicycles", "PriceType")

    data = [
        {'id': 1, 'name': 'дешевый', 'price': 10},
        {'id': 2, 'name': 'cредний', 'price': 30},
        {'id': 3, 'name': 'дорогой', 'price': 50},
    ]
    for row in data:
        PriceType.objects.update_or_create(**row)


class Migration(migrations.Migration):

    dependencies = [
        ('bicycles', '0005_remove_rentedbicycle_final_price'),
    ]

    operations = [
        migrations.RunPython(add_data),
    ]
