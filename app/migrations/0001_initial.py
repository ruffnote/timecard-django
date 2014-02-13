# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Comments'
        db.create_table('comments', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('body', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('issue_id', self.gf('django.db.models.fields.IntegerField')()),
            ('user_id', self.gf('django.db.models.fields.IntegerField')()),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'app', ['Comments'])

        # Adding model 'Issues'
        db.create_table('issues', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('subject', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('will_start_at', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('status', self.gf('django.db.models.fields.IntegerField')()),
            ('closed_on', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('project_id', self.gf('django.db.models.fields.IntegerField')()),
            ('author_id', self.gf('django.db.models.fields.IntegerField')()),
            ('assignee_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('info', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'app', ['Issues'])

        # Adding model 'Members'
        db.create_table('members', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('user_id', self.gf('django.db.models.fields.IntegerField')()),
            ('project_id', self.gf('django.db.models.fields.IntegerField')()),
            ('is_admin', self.gf('django.db.models.fields.IntegerField')()),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'app', ['Members'])

        # Adding model 'Projects'
        db.create_table('projects', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('is_public', self.gf('django.db.models.fields.IntegerField')()),
            ('parent_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('status', self.gf('django.db.models.fields.IntegerField')()),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'app', ['Projects'])

        # Adding model 'Providers'
        db.create_table('providers', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('foreign_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('provided_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('provided_type', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('info', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'app', ['Providers'])

        # Adding model 'SchemaMigrations'
        db.create_table('schema_migrations', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('class_field', self.gf('django.db.models.fields.CharField')(max_length=255, db_column='class')),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('created', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'app', ['SchemaMigrations'])

        # Adding model 'Users'
        db.create_table('users', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('email', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('encrypted_password', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('reset_password_token', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255, blank=True)),
            ('reset_password_sent_at', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('remember_created_at', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('sign_in_count', self.gf('django.db.models.fields.IntegerField')()),
            ('current_sign_in_at', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('last_sign_in_at', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('current_sign_in_ip', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('last_sign_in_ip', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'app', ['Users'])

        # Adding model 'Workloads'
        db.create_table('workloads', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('start_at', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('end_at', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('issue_id', self.gf('django.db.models.fields.IntegerField')()),
            ('user_id', self.gf('django.db.models.fields.IntegerField')()),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'app', ['Workloads'])


    def backwards(self, orm):
        # Deleting model 'Comments'
        db.delete_table('comments')

        # Deleting model 'Issues'
        db.delete_table('issues')

        # Deleting model 'Members'
        db.delete_table('members')

        # Deleting model 'Projects'
        db.delete_table('projects')

        # Deleting model 'Providers'
        db.delete_table('providers')

        # Deleting model 'SchemaMigrations'
        db.delete_table('schema_migrations')

        # Deleting model 'Users'
        db.delete_table('users')

        # Deleting model 'Workloads'
        db.delete_table('workloads')


    models = {
        u'app.comments': {
            'Meta': {'object_name': 'Comments', 'db_table': "'comments'"},
            'body': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'issue_id': ('django.db.models.fields.IntegerField', [], {}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'user_id': ('django.db.models.fields.IntegerField', [], {})
        },
        u'app.issues': {
            'Meta': {'object_name': 'Issues', 'db_table': "'issues'"},
            'assignee_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'author_id': ('django.db.models.fields.IntegerField', [], {}),
            'closed_on': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'project_id': ('django.db.models.fields.IntegerField', [], {}),
            'status': ('django.db.models.fields.IntegerField', [], {}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'will_start_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
        },
        u'app.members': {
            'Meta': {'object_name': 'Members', 'db_table': "'members'"},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'is_admin': ('django.db.models.fields.IntegerField', [], {}),
            'project_id': ('django.db.models.fields.IntegerField', [], {}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'user_id': ('django.db.models.fields.IntegerField', [], {})
        },
        u'app.projects': {
            'Meta': {'object_name': 'Projects', 'db_table': "'projects'"},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'is_public': ('django.db.models.fields.IntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'parent_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
        },
        u'app.providers': {
            'Meta': {'object_name': 'Providers', 'db_table': "'providers'"},
            'foreign_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'provided_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'provided_type': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'app.schemamigrations': {
            'Meta': {'object_name': 'SchemaMigrations', 'db_table': "'schema_migrations'"},
            'class_field': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_column': "'class'"}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'app.users': {
            'Meta': {'object_name': 'Users', 'db_table': "'users'"},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'current_sign_in_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'current_sign_in_ip': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'encrypted_password': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'last_sign_in_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'last_sign_in_ip': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'remember_created_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'reset_password_sent_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'reset_password_token': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255', 'blank': 'True'}),
            'sign_in_count': ('django.db.models.fields.IntegerField', [], {}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
        },
        u'app.workloads': {
            'Meta': {'object_name': 'Workloads', 'db_table': "'workloads'"},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'end_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'issue_id': ('django.db.models.fields.IntegerField', [], {}),
            'start_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'user_id': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['app']