from django.db import models

# Create your models here.

class Passenger (models.Model):
    no = models.CharField(max_length=1000 , null=True , blank = True)
    name = models.CharField(max_length=1000 , null=True , blank = True)
    card = models.CharField(max_length=1000 , null=True , blank = True)
    funds = models.IntegerField()
    def __str__(self) :
        return self.name



class Travel(models.Model) :
    name = models.CharField(max_length=1000 , null=True , blank=True)

    
    price = models.IntegerField()
    def __str__(self) :
        return self.name


class Captine(models.Model) :
     name = models.CharField(max_length=1000 , null=True , blank = True)
     travel = models.ForeignKey(Travel,
                                blank=False,
                                null=False,
                                related_name="travel1",
                                related_query_name="travel1",
                                on_delete=models.DO_NOTHING)
     bus_no = models.IntegerField(default= 1) 
     
     def __str__(self) :
        return self.name


class Bus(models.Model):
        passenger = models.ManyToManyField(Passenger,
                                blank=True,
                                null=True,
                               )
        


        travel = models.ForeignKey(Travel,
                                blank=True,
                                null=True,
                                related_name="travel",
                                related_query_name="travel",
                                on_delete=models.DO_NOTHING)
        
        captine = models.ForeignKey(Captine,
                                blank=True,
                                null=True,
                                related_name="captine",
                                related_query_name="captine",
                                on_delete=models.DO_NOTHING)
        date =models.DateTimeField(auto_now=True , null=True , blank=True)
        
        

        

    


