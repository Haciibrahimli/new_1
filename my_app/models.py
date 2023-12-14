from django.db import models


SOCIAL_CHOICES = (
    ("insta", "Instagram"),
    ("fb", "Facebook"),
    ("wp", "WhatsApp"),
    ("twitter", "Twitter"),
    ("linkedin", "Linkedin"),
    ("tiktok", "Tiktok"),
    ("github", "GitHub")
)


class About(models.Model):
    name = models.CharField(max_length=255,verbose_name='ad')
    surname = models.CharField(max_length=255,verbose_name='soyad')
    adress = models.CharField(max_length=255,verbose_name='adress')
    telephone = models.CharField(max_length=255,verbose_name='telefon')
    email = models.EmailField()
    description = models.TextField(verbose_name='movzu')
    image = models.ImageField(upload_to='media/',null=True,blank=True)

    def __str__(self):
        return self.name
    
    class Meta:

        verbose_name = 'haqqinda'
        verbose_name_plural = 'haqqinda'

class Experience(models.Model):
    position = models.CharField(max_length=255,verbose_name='pesesi')
    company_name = models.CharField(max_length=255,verbose_name='sirket adi')
    description = models.TextField(verbose_name='movzu')
    working_years = models.CharField(max_length=255,verbose_name='isleme vaxtlari')

    def __str__(self):
        return self.position
    
    class Meta:

        verbose_name = 'tecrube'
        verbose_name_plural = 'tecrube'

class Education(models.Model):
    university_name = models.CharField(max_length=255,verbose_name='uni adi')
    degree = models.CharField(max_length=255,verbose_name='derece')
    profession = models.CharField(max_length=255,verbose_name='ixtisas')
    education_years = models.CharField(max_length=255,verbose_name='tehsil muddeti')
    
    def __str__(self):
        return self.university_name
    
    class Meta:

        verbose_name = 'tehsil'
        verbose_name_plural = 'tehsil'


class Interests(models.Model):
    description = models.TextField(verbose_name='movzu')

    def __str__(self):
        return self.description[:10]
    
    class Meta:

        verbose_name = 'maraqlar'
        verbose_name_plural = 'maraqlar'

class Awards(models.Model):
    name = models.CharField(max_length=255,verbose_name='adi')
    company_name = models.CharField(max_length=255,verbose_name='sert.ver. comp')
    date_of = models.CharField(max_length=255,verbose_name='cert. ver. tarixi')

    def __str__(self):
        return self.name
    
    class Meta:

        verbose_name = 'sertifikatlar'
        verbose_name_plural = 'sertifikatlar'

class SosialMedia(models.Model):
    sosial_name = models.CharField(max_length=255,verbose_name='sosial media hesabi',choices=SOCIAL_CHOICES)
    sosial_link = models.TextField(verbose_name='sosial media linki')

    def __str__(self):
        return self.sosial_name

    class Meta:
        ordering = ("sosial_name", )
        verbose_name = "sosial media hesabi"
        verbose_name_plural = "sosial media hesablari"



