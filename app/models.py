from django.db import models

class Comments(models.Model):
    id = models.IntegerField(primary_key=True)
    body = models.TextField(blank=True)
    issue_id = models.IntegerField()
    user_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = True
        db_table = 'comments'

class Issues(models.Model):
    id = models.IntegerField(primary_key=True)
    subject = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    will_start_at = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField()
    closed_on = models.DateTimeField(blank=True, null=True)
    project_id = models.IntegerField()
    author_id = models.IntegerField()
    assignee_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    info = models.TextField(blank=True)
    class Meta:
        managed = True
        db_table = 'issues'

class Members(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    project_id = models.IntegerField()
    is_admin = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = True
        db_table = 'members'

class Projects(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    is_public = models.IntegerField()
    parent_id = models.IntegerField(blank=True, null=True)
    status = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = True
        db_table = 'projects'

class Providers(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True)
    foreign_id = models.IntegerField(blank=True, null=True)
    provided_id = models.IntegerField(blank=True, null=True)
    provided_type = models.CharField(max_length=255, blank=True)
    info = models.TextField(blank=True)
    class Meta:
        managed = True
        db_table = 'providers'

class SchemaMigrations(models.Model):
    id = models.IntegerField(primary_key=True)
    class_field = models.CharField(db_column='class', max_length=255) # Field renamed because it was a Python reserved word.
    type = models.CharField(max_length=50)
    created = models.DateTimeField()
    class Meta:
        managed = True
        db_table = 'schema_migrations'

class Users(models.Model):
    id = models.IntegerField(primary_key=True)
    email = models.CharField(unique=True, max_length=255)
    encrypted_password = models.CharField(max_length=255)
    reset_password_token = models.CharField(unique=True, max_length=255, blank=True)
    reset_password_sent_at = models.DateTimeField(blank=True, null=True)
    remember_created_at = models.DateTimeField(blank=True, null=True)
    sign_in_count = models.IntegerField()
    current_sign_in_at = models.DateTimeField(blank=True, null=True)
    last_sign_in_at = models.DateTimeField(blank=True, null=True)
    current_sign_in_ip = models.CharField(max_length=255, blank=True)
    last_sign_in_ip = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    class Meta:
        managed = True
        db_table = 'users'

class Workloads(models.Model):
    id = models.IntegerField(primary_key=True)
    start_at = models.DateTimeField(blank=True, null=True)
    end_at = models.DateTimeField(blank=True, null=True)
    issue_id = models.IntegerField()
    user_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = True
        db_table = 'workloads'

