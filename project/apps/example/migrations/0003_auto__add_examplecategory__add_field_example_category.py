# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ExampleCategory'
        db.create_table('example_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
        ))
        db.send_create_signal('example', ['ExampleCategory'])

        # Adding field 'Example.category'
        db.add_column('example', 'category',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['example.ExampleCategory'], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'ExampleCategory'
        db.delete_table('example_category')

        # Deleting field 'Example.category'
        db.delete_column('example', 'category_id')


    models = {
        'example.example': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'Example', 'db_table': "'example'"},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['example.ExampleCategory']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'example.examplecategory': {
            'Meta': {'object_name': 'ExampleCategory', 'db_table': "'example_category'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        }
    }

    complete_apps = ['example']