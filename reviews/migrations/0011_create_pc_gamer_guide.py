from django.db import migrations

def populate_pc_gamer(apps, schema_editor):
    try:
        import create_guia_pc_gamer_1800
        create_guia_pc_gamer_1800.main()
    except Exception as e:
        print(f"Aviso ao popular PC Gamer na migration: {e}")

class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0010_delete_comment'),
    ]

    operations = [
        migrations.RunPython(populate_pc_gamer, reverse_code=migrations.RunPython.noop),
    ]
