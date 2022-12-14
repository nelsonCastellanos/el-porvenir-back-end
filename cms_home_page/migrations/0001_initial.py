# Generated by Django 4.1.1 on 2022-10-05 03:34

import cms_home_page.field_block
from django.db import migrations, models
import django.db.models.deletion
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0076_modellogentry_revision'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('slider', wagtail.fields.StreamField([('slider', wagtail.blocks.StructBlock([('imagen', wagtail.images.blocks.ImageChooserBlock()), ('pagina', wagtail.blocks.PageChooserBlock(label='page', required=False))]))], use_json_field=True)),
                ('secciones', wagtail.fields.StreamField([('seccion', wagtail.blocks.StructBlock([('largo', wagtail.blocks.IntegerBlock()), ('titulo', wagtail.blocks.CharBlock()), ('descripcion', wagtail.blocks.CharBlock()), ('imagen', wagtail.images.blocks.ImageChooserBlock()), ('page', wagtail.blocks.PageChooserBlock(label='page', required=False)), ('color', cms_home_page.field_block.ColorFieldBlock(default='#000000'))]))], blank=True, use_json_field=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
