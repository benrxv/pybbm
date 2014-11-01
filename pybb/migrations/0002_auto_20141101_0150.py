# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models
from django.conf import settings
import pybb.util
import annoying.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pybb', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='body_html',
        ),
        migrations.RemoveField(
            model_name='post',
            name='body_text',
        ),
        migrations.AlterField(
            model_name='attachment',
            name='post',
            field=models.ForeignKey(related_name='attachments', verbose_name='Post', to='pybb.Post'),
        ),
        migrations.AlterField(
            model_name='forum',
            name='category',
            field=models.ForeignKey(related_name='forums', verbose_name='Category', to='pybb.Category'),
        ),
        migrations.AlterField(
            model_name='forum',
            name='parent',
            field=models.ForeignKey(related_name='child_forums', verbose_name='Parent forum', blank=True, to='pybb.Forum', null=True),
        ),
        migrations.AlterField(
            model_name='forum',
            name='readed_by',
            field=models.ManyToManyField(related_name='readed_forums', through='pybb.ForumReadTracker', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='pollanswer',
            name='topic',
            field=models.ForeignKey(related_name='poll_answers', verbose_name='Topic', to='pybb.Topic'),
        ),
        migrations.AlterField(
            model_name='pollansweruser',
            name='poll_answer',
            field=models.ForeignKey(related_name='users', verbose_name='Poll answer', to='pybb.PollAnswer'),
        ),
        migrations.AlterField(
            model_name='pollansweruser',
            name='user',
            field=models.ForeignKey(related_name='poll_answers', verbose_name='User', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='body',
            field=tinymce.models.HTMLField(verbose_name='Message'),
        ),
        migrations.AlterField(
            model_name='post',
            name='topic',
            field=models.ForeignKey(related_name='posts', verbose_name='Topic', to='pybb.Topic'),
        ),
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.ForeignKey(related_name='posts', verbose_name='User', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(upload_to=pybb.util.FilePathGenerator(to=b'devote/media/images/avatar'), null=True, verbose_name='Avatar', blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='language',
            field=models.CharField(default=b'en-us', max_length=10, verbose_name='Language', blank=True, choices=[(b'af', b'Afrikaans'), (b'ar', b'Arabic'), (b'ast', b'Asturian'), (b'az', b'Azerbaijani'), (b'bg', b'Bulgarian'), (b'be', b'Belarusian'), (b'bn', b'Bengali'), (b'br', b'Breton'), (b'bs', b'Bosnian'), (b'ca', b'Catalan'), (b'cs', b'Czech'), (b'cy', b'Welsh'), (b'da', b'Danish'), (b'de', b'German'), (b'el', b'Greek'), (b'en', b'English'), (b'en-au', b'Australian English'), (b'en-gb', b'British English'), (b'eo', b'Esperanto'), (b'es', b'Spanish'), (b'es-ar', b'Argentinian Spanish'), (b'es-mx', b'Mexican Spanish'), (b'es-ni', b'Nicaraguan Spanish'), (b'es-ve', b'Venezuelan Spanish'), (b'et', b'Estonian'), (b'eu', b'Basque'), (b'fa', b'Persian'), (b'fi', b'Finnish'), (b'fr', b'French'), (b'fy', b'Frisian'), (b'ga', b'Irish'), (b'gl', b'Galician'), (b'he', b'Hebrew'), (b'hi', b'Hindi'), (b'hr', b'Croatian'), (b'hu', b'Hungarian'), (b'ia', b'Interlingua'), (b'id', b'Indonesian'), (b'io', b'Ido'), (b'is', b'Icelandic'), (b'it', b'Italian'), (b'ja', b'Japanese'), (b'ka', b'Georgian'), (b'kk', b'Kazakh'), (b'km', b'Khmer'), (b'kn', b'Kannada'), (b'ko', b'Korean'), (b'lb', b'Luxembourgish'), (b'lt', b'Lithuanian'), (b'lv', b'Latvian'), (b'mk', b'Macedonian'), (b'ml', b'Malayalam'), (b'mn', b'Mongolian'), (b'mr', b'Marathi'), (b'my', b'Burmese'), (b'nb', b'Norwegian Bokmal'), (b'ne', b'Nepali'), (b'nl', b'Dutch'), (b'nn', b'Norwegian Nynorsk'), (b'os', b'Ossetic'), (b'pa', b'Punjabi'), (b'pl', b'Polish'), (b'pt', b'Portuguese'), (b'pt-br', b'Brazilian Portuguese'), (b'ro', b'Romanian'), (b'ru', b'Russian'), (b'sk', b'Slovak'), (b'sl', b'Slovenian'), (b'sq', b'Albanian'), (b'sr', b'Serbian'), (b'sr-latn', b'Serbian Latin'), (b'sv', b'Swedish'), (b'sw', b'Swahili'), (b'ta', b'Tamil'), (b'te', b'Telugu'), (b'th', b'Thai'), (b'tr', b'Turkish'), (b'tt', b'Tatar'), (b'udm', b'Udmurt'), (b'uk', b'Ukrainian'), (b'ur', b'Urdu'), (b'vi', b'Vietnamese'), (b'zh-cn', b'Simplified Chinese'), (b'zh-hans', b'Simplified Chinese'), (b'zh-hant', b'Traditional Chinese'), (b'zh-tw', b'Traditional Chinese')]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=annoying.fields.AutoOneToOneField(related_name='pybb_profile', verbose_name='User', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='topic',
            name='forum',
            field=models.ForeignKey(related_name='topics', verbose_name='Forum', to='pybb.Forum'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='readed_by',
            field=models.ManyToManyField(related_name='readed_topics', through='pybb.TopicReadTracker', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='topic',
            name='subscribers',
            field=models.ManyToManyField(related_name='subscriptions', verbose_name='Subscribers', to=settings.AUTH_USER_MODEL, blank=True),
        ),
    ]
