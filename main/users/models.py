from __future__ import unicode_literals

from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin, Permission
from django.contrib.auth.base_user import AbstractBaseUser

from django.utils.translation import gettext_lazy as _

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):

    COUNTRIES = [
        ('Россия', 'Россия')
    ]

    STATES = [
        ('Краснодарский край', 'Краснодарский край')
    ]

    CITY = [
        ('Краснодар', 'Краснодар')
    ]

    email = models.EmailField(_('Почта'), unique=True)
    first_name = models.CharField(_('Имя'), max_length=30, blank=True)
    last_name = models.CharField(_('Фамилия'), max_length=30, blank=True)
    country = models.CharField(_('Страна'), choices=COUNTRIES,max_length=100, blank=True)
    state = models.CharField(_('Регион'),choices=STATES, max_length=255, blank=True)
    city = models.CharField(_('Город'),choices=CITY,max_length=255, blank=True)

    is_superuser = models.BooleanField(
        _("Суперпользователь"),
        default=False,
        help_text=_(
            "Пользователь имеет все разрешения "
            "без явного их обозначения."
        ),
    )


    last_login = models.DateTimeField(_("Последний вход"), blank=True, null=True)
    date_joined = models.DateTimeField(_('Дата регистрации'), auto_now_add=True)
    is_active = models.BooleanField(_('Аккаунт активирован'), default=True)
    phone = models.CharField(_('Телефон'), max_length=11)
    is_staff = models.BooleanField(
        _("Администратор"),
        default=False,
        help_text=_("Может ли пользователь входить в админку."),
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = ('Пользователь')
        verbose_name_plural = ('Пользователи')


    def __str__(self):
        return self.email
    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)
