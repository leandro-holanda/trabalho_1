from django.db import models

NATIONALITY_CHOICES = [
    ('BR', 'Brasil'),
    ('US', 'Estados Unidos'),
    ('UK', 'Reino Unido'),
    ('FR', 'França'),
    ('JP', 'Japão'),
    ('KR', 'Coreia do Sul'),
    ('IN', 'Índia'),
    ('MX', 'México'),
    ('IT', 'Itália'),
    ('DE', 'Alemanha'),
]

class Actor(models.Model):
    name = models.CharField(max_length=250)
    birthday = models.DateField()
    nationality = models.CharField(max_length=2, choices=NATIONALITY_CHOICES)

    def __str__(self):
        return self.name
