"""
Migration para remover a coluna 'description' da tabela reviews_category no Postgres.
Essa coluna foi criada manualmente no banco de producao mas nao existe no modelo Django,
causando NotNullViolation ao tentar inserir novas categorias.
"""
from django.db import migrations, connection


def remove_description_column(apps, schema_editor):
    """Remove a coluna description de reviews_category se ela existir."""
    db_engine = schema_editor.connection.vendor
    if db_engine == 'postgresql':
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT column_name 
                FROM information_schema.columns 
                WHERE table_name='reviews_category' AND column_name='description';
            """)
            if cursor.fetchone():
                cursor.execute("ALTER TABLE reviews_category DROP COLUMN description;")
                print("   => Coluna 'description' removida de reviews_category.")
            else:
                print("   => Coluna 'description' nao existe em reviews_category, nada a fazer.")


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0010_delete_comment'),
    ]

    operations = [
        migrations.RunPython(remove_description_column, reverse_code=migrations.RunPython.noop),
    ]
