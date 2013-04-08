# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ExampleImage'
        db.create_table('example_images', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('example', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['example.Example'])),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('sort', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('example', ['ExampleImage'])


    def backwards(self, orm):
        # Deleting model 'ExampleImage'
        db.delete_table('example_images')


    models = {
        'example.example': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'Example', 'db_table': "'example'"},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['example.ExampleCategory']", 'null': 'True', 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'date_state': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'example.examplecategory': {
            'Meta': {'object_name': 'ExampleCategory', 'db_table': "'example_category'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        'example.exampleimage': {
            'Meta': {'object_name': 'ExampleImage', 'db_table': "'example_images'"},
            'example': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['example.Example']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'sort': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['example']