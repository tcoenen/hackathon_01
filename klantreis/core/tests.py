from django.test import TestCase

from core.models import Organisation, Step, Edge, Process, Phase
from core.services import get_mermaid_markup

import re

RENDERED_OUTPUT = """journey
title Klantreis ik heb een schuld
section Eerste Fase
  Boete: X: Organisatie A
  Aanmaning: X: Organisatie B"""


class TestMermaidGeneration(TestCase):
    def setUp(self):
        phase_1 = Phase.objects.create(name='Eerste Fase')

        orgA = Organisation.objects.create(name='Organisatie A')
        orgB = Organisation.objects.create(name='Organisatie B')

        stap1 = Step.objects.create(name='Boete', organisation=orgA, phase=phase_1)
        stap2 = Step.objects.create(name='Aanmaning', organisation=orgB, phase=phase_1)

        Edge.objects.create(prev=stap1, next=stap2, order=1)

        self.klantreis = Process.objects.create(first_step=stap1)

    def test_get_mermaid_markup(self):
        markup = get_mermaid_markup(self.klantreis.id)
        # the numbers are random for now, so replace with X as in example output
        markup = re.sub('\d', 'X', markup)

        self.assertEqual(markup, RENDERED_OUTPUT)
