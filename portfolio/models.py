from django.db import models

# Create your models here.
class Project(models.Model):
    title=models.CharField(max_length=200,verbose_name="Títol")
    description=models.TextField(verbose_name="Descripció")
    image=models.ImageField(verbose_name="Imatge",upload_to="projects")
    created=models.DateTimeField(auto_now_add=True,verbose_name="Data de Creació") #al atribut es guarda la data de creacio del objecte de manera automatica
    updated=models.DateTimeField(auto_now=True,verbose_name="Data d'Edició") #al atribut es guarda la data de la ultima modificacio del object

    class Meta:
        verbose_name="projecte"
        verbose_name_plural="projectes" #si no especifiquem aquesta variable, per defecte afegeix una S al nom definit (per defecte o al verbose_name)
        ordering=["-created"] # posem un guio - per indicar que el ordre ha de ser a la inversa, en aquest cas no volem que sigui del registre mes antic al mes nou sino al contrari, del mes nou al mes antic

    def __str__(self):
        return(self.title)
