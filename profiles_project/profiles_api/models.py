from django.db import models
# These are the 2 basic standard classes that we need use when overridding the default django model this is described in the official document which is linked to the reources in this video.
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

class UserProfileManager(BaseUserManager):
    '''Manager for user profile'''

    def create_user(self, email, name, password=None):
        '''Create a new user profile'''
        if not email:
            raise ValueError('User must have an email address')

        email = self.normilize_mail(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        '''Create and save a new superuser with given details'''
        user = create_user(email, user, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return users


''' Underneth the import let us create a new class called user profile and inherit from the base class
    the abstract base user and permission mixin classes so add below the class '''

class UserProfile(AbstractBaseUser, PermissionsMixin):
    ''' Database model for users in the system '''
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)


    ''' Next we need to specify the model manager that we are going to use for the objects, this is required because we need
        use our custom user model with the Django CLI, so Django needs to have a custom model manager for the user model
        so it knows how to create users and control users using the Django command line tools which will be shown in a future video'''

    objects = UserProfileManager()

    ''' Below we need to add a couple of more fields to our class and this is for it to again to work with the Django admin
        and also the Django autheitication system so we need to specify the following'''

    USERNAME_FIELD = 'email' # This is to override the Django default user name
    REQUIRED_FIELDS = ['name'] # To have name as a required field

    ''' Below this we are going to add a couple of functions for Django to interact with our custom user model
        the first one is get full namee, we need Django to give the ability to retrive the full name of the user'''

    def get_full_name(self):
        ''' Retrive full name of user '''
        return self.name

    def get_short_name(self):
        ''' Retrive short name of user '''
        return self.name

    ''' Finally we need to specifiy the string representation of our model, now this is the item we want to return
        when we convert a user profile object to a string in Python you do as below'''

    ''' This is recommended for all Django models because otherwise when you convert it to a string it wont necessarily
        be a meaningful output, so in order to customize how you convert this to a string you want to specify this function
        and return the field you want to use to identify this model if you're just reading it in the Django admin or in
        some python code where you print in, so other than below we'll see rest in action later when we look at These
        Django admin and see all the users listed by their email address '''

    def __str__(self):
        ''' Return string representation of our user '''
        return self.email

#
