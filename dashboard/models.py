from django.db import models

class Nuson(models.Model):
    nilai1 = models.FloatField()
    nilai2 = models.FloatField()
    nilai3 = models.FloatField()
    nilai4 = models.FloatField()
    nilai5 = models.FloatField()
    waktu = models.DateTimeField(auto_now_add=True)
    deviceName = models.CharField(max_length=100)

    def __str__(self):
        return f'ID: {self.id}, Nilai1: {self.nilai1}, Nilai2: {self.nilai2}, Nilai3: {self.nilai3}, Nilai4: {self.nilai4}, Nilai5: {self.nilai5}, Waktu: {self.waktu}, DeviceName: {self.deviceName}'
