# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AppsCart(models.Model):
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    is_active = models.BooleanField()
    user = models.ForeignKey('AppsUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'apps_cart'
        unique_together = (('user', 'is_active'),)


class AppsCartitem(models.Model):
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    price = models.IntegerField()
    quantity = models.IntegerField()
    cart = models.ForeignKey(AppsCart, models.DO_NOTHING)
    product = models.ForeignKey('AppsProduct', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'apps_cartitem'


class AppsCategory(models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(unique=True, max_length=255)
    lft = models.PositiveIntegerField()
    rght = models.PositiveIntegerField()
    tree_id = models.PositiveIntegerField()
    level = models.PositiveIntegerField()
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apps_category'


class AppsProduct(models.Model):
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    title = models.CharField(max_length=255)
    price = models.IntegerField()
    short_description = models.TextField()
    description = models.TextField(blank=True, null=True)
    discount = models.IntegerField(blank=True, null=True)
    quantity = models.IntegerField()
    is_premium = models.BooleanField()
    shopping_cost = models.SmallIntegerField()
    specification = models.JSONField()
    author = models.ForeignKey('AppsUser', models.DO_NOTHING)
    category = models.ForeignKey(AppsCategory, models.DO_NOTHING)
    tags = models.ForeignKey('AppsTag', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'apps_product'


class AppsProductimage(models.Model):
    image = models.CharField(max_length=100)
    product = models.ForeignKey(AppsProduct, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'apps_productimage'


class AppsTag(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'apps_tag'


class AppsUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    status = models.CharField(max_length=50)
    email = models.CharField(unique=True, max_length=254)

    class Meta:
        managed = False
        db_table = 'apps_user'


class AppsUserGroups(models.Model):
    user = models.ForeignKey(AppsUser, models.DO_NOTHING)
    group = models.ForeignKey('AuthGroup', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'apps_user_groups'
        unique_together = (('user', 'group'),)


class AppsUserUserPermissions(models.Model):
    user = models.ForeignKey(AppsUser, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'apps_user_user_permissions'
        unique_together = (('user', 'permission'),)


class AppsWishlist(models.Model):
    product = models.ForeignKey(AppsProduct, models.DO_NOTHING)
    user = models.ForeignKey(AppsUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'apps_wishlist'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class DjangoAdminLog(models.Model):
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AppsUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
