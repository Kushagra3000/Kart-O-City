from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image2',
            field=models.ImageField(default='', upload_to='uploads/products/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='image3',
            field=models.ImageField(default='', upload_to='uploads/products/'),
            preserve_default=False,
        ),
    ]