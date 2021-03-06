# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        badges_pk_list = [36, 22, 47, 27, 8]

        for badge_pk in badges_pk_list:
            badge = orm.Badge.objects.get(pk=badge_pk)
            badge.featured = True
            badge.save()

    def backwards(self, orm):
        raise RuntimeError('Cannot reverse this migration.')

    models = {
        'badge.award': {
            'Meta': {'object_name': 'Award'},
            'badge': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['badge.Badge']"}),
            'date_awarded': ('django.db.models.fields.DateTimeField', [], {}),
            'evidence_url': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'expert_uri': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ob_date_published': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'ob_date_revoked': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'ob_state': ('django.db.models.fields.CharField', [], {'default': "'NOT_PUBLISHED'", 'max_length': '20'}),
            'user_uri': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'badge.badge': {
            'Meta': {'object_name': 'Badge'},
            'author_uri': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {}),
            'date_published': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_uri': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'partner_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'requirements': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        }
    }

    complete_apps = ['badge']
    symmetrical = True
