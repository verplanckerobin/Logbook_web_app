from django.db import models

# Create your models here.


class People(models.Model):
    name = models.CharField(max_length=255)
    company_function = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, blank=True)
    email = models.CharField(max_length=255, blank=True)
    remarks = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name


class Airport(models.Model):
    ICAO_code = models.CharField(max_length=50)
    IATA_code = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.IATA_code


class Aircraft(models.Model):
    aircraft_id = models.CharField(max_length=50)
    aircraft_type = models.CharField(max_length=50)
    notes = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.aircraft_id


class Log(models.Model):
    date = models.DateField()
    departure = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='departure')
    block_out = models.TimeField()
    arrival = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='arrival')
    block_in = models.TimeField()
    aircraft = models.ForeignKey(Aircraft, on_delete=models.CASCADE)
    pic = models.ForeignKey(People, on_delete=models.CASCADE)
    landings = models.IntegerField()
    take_off = models.IntegerField()
    remarks = models.CharField(max_length=255, blank=True)

