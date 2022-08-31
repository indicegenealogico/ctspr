from django.db import models
from phone_field import PhoneField



# Create your models here.

BRANCHES = (
  ('BA', 'Barceloneta'),
  ('LP', 'Las Piedras'),
  ('SA', 'Santurce'),
  ('SG', 'San Germán'),
  ('SL', 'Salinas')
)

#=================================================================================
class Branch(models.Model):
  name     = models.CharField('Sucursal', max_length=2, blank=False, null=False, choices=BRANCHES)
  address1 = models.CharField(max_length=30, blank=False, null=False)
  address2 = models.CharField(max_length=30, blank=True, null=True)
  city     = models.CharField(max_length=20, blank=False, null=False)
  state    = models.CharField(max_length=2, blank=False, null=False)
  zip_code = models.CharField(max_length=9, blank=False, null=False)
  phone    = PhoneField(blank=True, help_text='Contact phone number')
  fax      = PhoneField(blank=True, help_text='Contact fax number')
  manager  = models.CharField(max_length=20, blank=False, null=False)

  class Meta:
    verbose_name_plural = 'Branches'
    ordering = ['name']

  def __str__(self) :
    return (self.get_name_display())


#=================================================================================
class Town(models.Model):
  name   = models.CharField('Pueblo', max_length=20, null=False, blank=False)
  branch = models.ForeignKey(Branch, on_delete=models.DO_NOTHING)

  class Meta:
    ordering = ['name']

  def __str__(self):
    return (self.name)


#=================================================================================
class Recruiter(models.Model):
  name   = models.CharField(max_length=30, blank=False, null=False)
  email  = models.EmailField()
  branch = models.ForeignKey(Branch, on_delete=models.DO_NOTHING)

  class Meta:
    ordering = ['name']

  def __str__(self):
    return (self.name)

#=================================================================================
class Requirement(models.Model):
  description = models.CharField(max_length=30, blank=False)

  def __str__(self):
    return (self.description)


#=================================================================================
class Job(models.Model):
  job_id      = models.IntegerField(primary_key = True)
  title       = models.CharField(max_length=30, null=False, blank=False)
  description = models.TextField(null=True, blank=True)
  requiremets = models.ManyToManyField(Requirement)
  town        = models.ForeignKey(Town, on_delete=models.CASCADE)
  recruiter   = models.ForeignKey(Recruiter, on_delete=models.CASCADE)

  def __str__(self):
    return ("%s - %s" % (self.job_id, self.title))
  
