from django.db import models


class Phase(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Organisation(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Step(models.Model):
    name = models.CharField(max_length=255)
    organisation = models.ForeignKey(Organisation, null=True, blank=True, on_delete=models.SET_NULL)
    phase = models.ForeignKey(Phase, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} (org={self.organisation.name})'

class Edge(models.Model):
    prev = models.ForeignKey(Step, null=True, blank=True, related_name='+', on_delete=models.SET_NULL)
    next = models.ForeignKey(Step, null=True, blank=True, related_name='+', on_delete=models.SET_NULL)

    order = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.prev.name} ({self.prev.organisation.name}) -> {self.next.name} ({self.next.organisation.name})'   

    class Meta:
        unique_together = [['prev', 'next']]
        ordering = ['order', 'id']

class Process(models.Model):  # klantreis
    first_step = models.ForeignKey(Step, null=True, blank=True, on_delete=models.SET_NULL)


# --- nice to have:


class Citizen(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, )


class Trace(models.Model):
    citizen = models.ForeignKey(Citizen, on_delete=models.CASCADE)
    first_step = models.ForeignKey(Step, null=True, blank=True, on_delete=models.SET_NULL)
    # process = models.ForeignKey ...


class Problem(models.Model):
    name = models.CharField(max_length=255, unique=True)


class Feedback(models.Model):
    complaint = models.TextField(max_length=2000)
    problem = models.ForeignKey(Problem, null=True, blank=True, on_delete=models.SET_NULL)
