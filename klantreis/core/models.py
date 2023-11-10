from django.db import models


class Organisation(models.Model):
    name = models.CharField(max_length=255)


class Step(models.Model):
    name = models.CharField(max_length=255)
    organisation = models.ForeignKey(Organisation, null=True, blank=True, on_delete=models.SET_NULL)


class Edge(models.Model):
    prev = models.ForeignKey(Step, null=True, blank=True, related_name='prev_step', on_delete=models.SET_NULL)
    next = models.ForeignKey(Step, null=True, blank=True, related_name='next_step', on_delete=models.SET_NULL)


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

