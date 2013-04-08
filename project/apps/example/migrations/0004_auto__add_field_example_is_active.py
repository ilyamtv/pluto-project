# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Example.is_active'
        db.add_column('example', 'is_active',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Example.is_active'
        db.delete_column('example', 'is_active')


    models = {
        'example.example': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'Example', 'db_table': "'example'"},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['example.ExampleCategory']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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