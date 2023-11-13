import random

from core.models import Edge, Process


def get_mermaid_markup(klantreis_id):
    to_process = []

    klantreis = Process.objects.get(pk=klantreis_id)

    chunks = []

    chunks.append('journey')
    chunks.append('title Klantreis ik heb een schuld')

    to_process = [klantreis.first_step]
    current_phase = None

    while to_process:
        current_step = to_process.pop(0)
        if current_phase != current_step.phase:
            current_phase = current_step.phase
            chunks.append(f'section {current_phase.name}')

        # Currently no support for happiness in data model, hence the random.randrange
        chunks.append(f'  {current_step.name}: {random.randrange(5)}: {current_step.organisation.name}')

        outgoing_edges = Edge.objects.filter(prev_id=current_step.id)
        for edge in outgoing_edges:
            next_step = edge.next
            to_process.append(next_step)

    return '\n'.join(chunks)
