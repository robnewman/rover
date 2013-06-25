# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Owner.full_name'
        db.add_column(u'dog_owner', 'full_name',
                      self.gf('django.db.models.fields.CharField')(default='John Smith', max_length=30),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Owner.full_name'
        db.delete_column(u'dog_owner', 'full_name')


    models = {
        u'dog.breed': {
            'Meta': {'object_name': 'Breed'},
            'breed': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kennel_club_recognized': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'official_website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'dog.dog': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Dog'},
            'breed': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['dog.Breed']", 'symmetrical': 'False'}),
            'chases_postman': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'collects_newspaper': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'friendly_to_cats': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'friendly_to_dogs': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'friendly_to_kids': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'owner': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['dog.Owner']", 'symmetrical': 'False'}),
            'profile_photo': ('stdimage.fields.StdImageField', [], {'max_length': '100', 'upload_to': "'dog'", 'thumbnail_size': "{'width': 150, 'force': True, 'height': 150}", 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '150'}),
            'weight': ('django.db.models.fields.IntegerField', [], {})
        },
        u'dog.dogphoto': {
            'Meta': {'ordering': "('title', 'caption')", 'object_name': 'DogPhoto'},
            'caption': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'display_height': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'display_width': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'dog': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dog.Dog']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img_height': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'img_width': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '200', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'dog.owner': {
            'Meta': {'ordering': "('lname', 'fname')", 'object_name': 'Owner'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '100'}),
            'fname': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lname': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['dog']