# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Owner'
        db.create_table(u'dog_owner', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fname', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('lname', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=100)),
        ))
        db.send_create_signal(u'dog', ['Owner'])

        # Adding model 'Breed'
        db.create_table(u'dog_breed', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('breed', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('kennel_club_recognized', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('official_website', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal(u'dog', ['Breed'])

        # Adding model 'Dog'
        db.create_table(u'dog_dog', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('weight', self.gf('django.db.models.fields.IntegerField')()),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=150)),
            ('friendly_to_dogs', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('friendly_to_kids', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('friendly_to_cats', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('chases_postman', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('collects_newspaper', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'dog', ['Dog'])

        # Adding M2M table for field owner on 'Dog'
        m2m_table_name = db.shorten_name(u'dog_dog_owner')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('dog', models.ForeignKey(orm[u'dog.dog'], null=False)),
            ('owner', models.ForeignKey(orm[u'dog.owner'], null=False))
        ))
        db.create_unique(m2m_table_name, ['dog_id', 'owner_id'])

        # Adding M2M table for field breed on 'Dog'
        m2m_table_name = db.shorten_name(u'dog_dog_breed')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('dog', models.ForeignKey(orm[u'dog.dog'], null=False)),
            ('breed', models.ForeignKey(orm[u'dog.breed'], null=False))
        ))
        db.create_unique(m2m_table_name, ['dog_id', 'breed_id'])

        # Adding model 'DogPhoto'
        db.create_table(u'dog_dogphoto', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('dog', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dog.Dog'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('caption', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=200, blank=True)),
            ('display_height', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('display_width', self.gf('django.db.models.fields.IntegerField')(blank=True)),
        ))
        db.send_create_signal(u'dog', ['DogPhoto'])


    def backwards(self, orm):
        # Deleting model 'Owner'
        db.delete_table(u'dog_owner')

        # Deleting model 'Breed'
        db.delete_table(u'dog_breed')

        # Deleting model 'Dog'
        db.delete_table(u'dog_dog')

        # Removing M2M table for field owner on 'Dog'
        db.delete_table(db.shorten_name(u'dog_dog_owner'))

        # Removing M2M table for field breed on 'Dog'
        db.delete_table(db.shorten_name(u'dog_dog_breed'))

        # Deleting model 'DogPhoto'
        db.delete_table(u'dog_dogphoto')


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
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '200', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'dog.owner': {
            'Meta': {'ordering': "('lname', 'fname')", 'object_name': 'Owner'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '100'}),
            'fname': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lname': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['dog']