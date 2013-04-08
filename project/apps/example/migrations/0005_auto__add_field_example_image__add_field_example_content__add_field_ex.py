# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Example.image'
        db.add_column('example', 'image',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Example.content'
        db.add_column('example', 'content',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Example.date_state'
        db.add_column('example', 'date_state',
                      self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Example.image'
        db.delete_column('example', 'image')

        # Deleting field 'Example.content'
        db.delete_column('example', 'content')

        # Deleting field 'Example.date_state'
        db.delete_column('example', 'date_state')


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
        }
    }

    complete_apps = ['example']