from django.core.management.base import BaseCommand
from core.models import Organisation, Step, Edge, Process, Phase


class Command(BaseCommand):
    help = "Put an instance of client journey in the database"

    def handle(self, *args, **options):
        fase1 = Phase.objects.create(name='Ik heb financiële problemen')
        fase2 = Phase.objects.create(name='Ik zoek hulp bij schulden')
        fase3 = Phase.objects.create(name='Ik zoek contact met de gemeente')
        fase4 = Phase.objects.create(name='Hulp krijgen')

        belast = Organisation.objects.create(name='Belastingdienst')
        cjib = Organisation.objects.create(name='CJIB')
        utrecht = Organisation.objects.create(name='Gemeente Utrecht')
        rijksoverheid = Organisation.objects.create(name='Rijksoverheid')
        schuldhulp = Organisation.objects.create(name='Schulhulpverlening')
        vriend = Organisation.objects.create(name='Vriend')

        boete = Step.objects.create(name='Boete', organisation=cjib, phase=fase1)
        aanmaning = Step.objects.create(name='Aanmaning', organisation=cjib, phase=fase1)
        brief = Step.objects.create(name='Brief', organisation=belast, phase=fase1)

        Edge.objects.create(prev=boete, next=aanmaning)
        Edge.objects.create(prev=aanmaning, next=brief)

        zoek = Step.objects.create(name='Zoeken naar hulp', organisation=rijksoverheid, phase=fase2)
        praat = Step.objects.create(name='praten met een vriend', organisation=vriend, phase=fase2)

        Edge.objects.create(prev=brief, next=zoek)
        Edge.objects.create(prev=zoek, next=praat)

        zoek2 = Step.objects.create(name='informatie zoeken op de website', organisation=utrecht, phase=fase3)
        bel = Step.objects.create(name='bellen met de gemeente', organisation=utrecht, phase=fase3)
        praat2 = Step.objects.create(name='Een eerste gesprek', organisation=utrecht, phase=fase3)

        Edge.objects.create(prev=praat, next=zoek2)
        Edge.objects.create(prev=zoek2, next=bel)
        Edge.objects.create(prev=bel, next=praat2)

        praat3 = Step.objects.create(name='intake gesprek', organisation=schuldhulp, phase=fase4)
        Edge.objects.create(prev=praat2, next=praat3)

        klantreis = Process.objects.create(first_step=boete)
        self.stdout.write(f'Klantreis met .id={klantreis.id} is aangemaakt.')
