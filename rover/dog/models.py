from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse
from stdimage import StdImageField

# Helper functions
def content_file_name(self, filename):
    """
    Correctly dynamically
    define upload path for
    images
    """
    return '/'.join(['dog',
                     '%s' % self.pk,
                     filename])


# Create your models here.
class Owner(models.Model):
    """
    Owner class

    An owner can have many dogs
    """
    fname = models.CharField(_('First name'),
                             max_length=30,
                             help_text="Owner first name")
    lname = models.CharField(_('Last name'),
                             max_length=30,
                             help_text="Owner last name")
    email = models.EmailField(_('Email address'),
                              max_length=100,
                              help_text="Owner email address")
    full_name = models.CharField(_('Full name'),
                                 max_length=100,
                                 help_text="Owner full name")

    def __unicode__(self):
        return u'%s, %s' % (self.lname, self.fname)

    def save(self, *args, **kwargs):
        # Convienient for searching
        self.full_name = u'%s %s' % (self.fname, self.lname)
        super(Owner, self).save(*args, **kwargs)

    class Meta:
        ordering = ('lname','fname',)


class Breed(models.Model):
    """
    Breed class

    A single dog can have many breeds :)

    Ideally we have a global helper library
    with a list of all approved breeds
    """
    breed = models.CharField(_('Breed'),
                             max_length=30,
                             help_text="Breed of dog")
    kennel_club_recognized = models.BooleanField()
    official_website = models.URLField(null=True,
                                       blank=True)

    def __unicode__(self):
        return u'%s' % self.breed


class Dog(models.Model):
    """
    Dog class

    A dog can have multiple owners:
     - family
     - divorced owners
     - pound / adopted / adopted
    A dog can have multiple breeds
    A dog can have many attributes
    """
    name = models.CharField(_('Dog name'),
                            max_length=100,
                            help_text="Dog name")
    owner = models.ManyToManyField(Owner)
    breed = models.ManyToManyField(Breed)
    weight = models.IntegerField()
    slug = models.SlugField(_('Slug Field'),
                            help_text='Auto built from title',
                            max_length=150)
    # Images - use stdimage
    profile_photo = StdImageField(blank=True,
                                  upload_to='dog',
                                  thumbnail_size=(150, 150, True))
    # Extras - not required
    friendly_to_dogs = models.BooleanField()
    friendly_to_kids = models.BooleanField()
    friendly_to_cats = models.BooleanField()
    chases_postman = models.BooleanField()
    collects_newspaper = models.BooleanField()

    def __unicode__(self):
        return u'%s' % self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Dog, self).save(*args, **kwargs)

    def get_absolute_url(self):
        # For the CBV ModelForm
        return reverse('dog-detail', kwargs={'pk':self.pk})

    class Meta:
        ordering = ('name',)


class DogPhoto(models.Model):
    """
    Dog photo class

    A dog can have lots of photos
    """
    dog = models.ForeignKey(Dog)
    title = models.CharField(_('Title'),
                             max_length=100,
                             help_text='Photo title')
    img_width = models.PositiveIntegerField(editable=False)
    img_height = models.PositiveIntegerField(editable=False)
    caption = models.TextField(null=True,
                               blank=True)
    photo = models.ImageField(blank=True,
                              max_length=200,
                              upload_to=content_file_name,
                              height_field='img_height',
                              width_field='img_width')
    display_height = models.IntegerField(blank=True)
    display_width = models.IntegerField(blank=True)

    def __unicode__(self):
        return u'%s' % (self.photo)

    def save(self, *args, **kwargs):
        ratio = float(self.display_width) / float(self.img_width)
        self.display_height = int(self.img_height * ratio)
        super(DogPhoto, self).save(*args, **kwargs)

    class Meta:
        ordering = ('title', 'caption',)
