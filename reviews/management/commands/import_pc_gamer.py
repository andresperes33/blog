from django.core.management.base import BaseCommand
import create_guia_pc_gamer_1800

class Command(BaseCommand):
    help = 'Importa ou atualiza o guia de compra PC Gamer Barato de R$ 1.800 (categoria, guia e itens)'

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE('Iniciando importacao do guia PC Gamer...'))
        create_guia_pc_gamer_1800.main()
        self.stdout.write(self.style.SUCCESS('Guia PC Gamer importado/atualizado com sucesso!'))
