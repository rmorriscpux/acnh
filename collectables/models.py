from django.db import models

class Shadow(models.Model):
    # Unique Fields
    size = models.CharField(max_length=45)

    # Relationships
    # fishes
    # sea_creatures

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Hour(models.Model):
    # Unique Fields
    time = models.IntegerField()
    @property
    def time_12hr(self):
        time_int = self.time % 12
        if time_int == 0:
            time_int = 12
        return str(time_int)
    @property
    def time_am_pm(self):
        if self.time < 12:
            return self.time_12hr + " AM"
        else:
            return self.time_12hr + " PM"

    # Relationships
    # bugs
    # fishes
    # sea_creatures

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class MonthMgr(models.Manager):
    def all_southern(self):
        northern = self.all()
        southern = northern[6:11]
        southern.extend(northern[0:5])
        return southern

    def get_southern(self, id):
        return self.get(id=(id+6)%12)

class Month(models.Model):
    # Unique Fields
    name = models.CharField(max_length=45)
    @property
    def short_name(self):
        return self.name[0:2]
    @property
    def initial(self):
        return self.name[0]

    # Relationships
    # bugs
    # fishes
    # sea_creatures

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Manager
    objects = MonthMgr()

class Bug(models.Model):
    # Unique Fields
    name = models.CharField(max_length=45)
    location = models.CharField(max_length=45)
    price = models.IntegerField()

    # Relationships
    hours = models.ManyToManyField(Hour, related_name="bugs")
    months = models.ManyToManyField(Month, related_name="bugs")

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Fish(models.Model):
    # Unique Fields
    name = models.CharField(max_length=45)
    location = models.CharField(max_length=45)
    price = models.IntegerField()
    fin = models.BooleanField(default=False)

    # Relationships
    shadow = models.ForeignKey(Shadow, related_name="fishes", on_delete=models.CASCADE)
    hours = models.ManyToManyField(Hour, related_name="fishes")
    months = models.ManyToManyField(Month, related_name="fishes")

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class SeaCreature(models.Model):
    # Unique Fields
    name = models.CharField(max_length=45)
    price = models.IntegerField()

    # Relationships
    shadow = models.ForeignKey(Shadow, related_name="sea_creatures", on_delete=models.CASCADE)
    hours = models.ManyToManyField(Hour, related_name="sea_creatures")
    months = models.ManyToManyField(Month, related_name="sea_creatures")

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
