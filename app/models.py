from django.db import models
from collections import Counter

# Create your models here.

class Evento(models.Model):
    nome = models.CharField(max_length=160)
    data = models.DateField()
    usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.nome
    
class Round(models.Model):
    nome = models.CharField(max_length=40)
    equipe = models.ForeignKey('Equipe', on_delete=models.CASCADE, related_name='rounds')
    autonomo_foco = models.CharField(max_length=40, blank=True, null=True)
    autonomo_pontuacao = models.IntegerField(blank=True, null=True)
    teleoperado_foco = models.CharField(max_length=40, blank=True, null=True)
    teleoperado_pontuacao = models.IntegerField(blank=True, null=True)
    
class Equipe(models.Model):
    foto = models.ImageField(upload_to='equipes', blank=True, null=True)
    nome = models.CharField(max_length=160)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, default=1)

    def quantidade_rounds(self):
        return self.rounds.count()
    
    def autonomo_pontuacao_media(self):
        return (sum(round.autonomo_pontuacao for round in self.rounds.all() if round.autonomo_pontuacao is not None)) / self.quantidade_rounds()
    
    def teleoperado_pontuacao_media(self):
        return (sum(round.teleoperado_pontuacao for round in self.rounds.all() if round.teleoperado_pontuacao is not None)) / self.quantidade_rounds()
    
    def pontuacao_media(self):
        return self.autonomo_pontuacao_media() + self.teleoperado_pontuacao_media()
    
    def autonomo_foco_geral(self):
        focos = [round.autonomo_foco for round in self.rounds.all() if round.autonomo_foco]
        return Counter(focos).most_common(1)[0][0] if focos else None

    def teleoperado_foco_geral(self):
        focos = [round.teleoperado_foco for round in self.rounds.all() if round.teleoperado_foco]
        return Counter(focos).most_common(1)[0][0] if focos else None

    def __str__(self):
        return self.nome