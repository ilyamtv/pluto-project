# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ExampleModel'
        db.create_table('example', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('example', ['ExampleModel'])


    def backwards(self, orm):
        # Deleting model 'ExampleModel'
        db.delete_table('example')


    models = {
        'example.examplemodel': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'ExampleModel', 'db_table': "'example'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['example']