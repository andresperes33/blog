from django.db import migrations


def populate_placas_video(apps, schema_editor):
    try:
        import create_guia_placas_video_2026
        create_guia_placas_video_2026.main()
    except Exception as e:
        print(f"Aviso ao popular Placas de Video na migration: {e}")


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0013_guide_faq'),
    ]

    operations = [
        migrations.RunPython(populate_placas_video, reverse_code=migrations.RunPython.noop),
    ]
