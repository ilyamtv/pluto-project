# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'ExampleModel'
        db.delete_table('example')

        # Adding model 'Example'
        db.create_table('example', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('example', ['Example'])


    def backwards(self, orm):
        # Adding model 'ExampleModel'
        db.create_table('example', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('example', ['ExampleModel'])

        # Deleting model 'Example'
        db.delete_table('example')


    models = {
        'example.example': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'Example', 'db_table': "'example'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['example']