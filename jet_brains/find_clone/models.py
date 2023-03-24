from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from .logiс import file_comparison
import json

# Create your models here.


class New_File(models.Model):
    title = models.CharField(max_length=200, blank=True, default='Nothing')
    file = models.FileField(upload_to='downloaded', null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.title

@receiver(post_save, sender=New_File)
def my_handler(sender, **kwargs):
    field_name = 'description'
    obj = sender.objects.last()
    source_code = getattr(obj, field_name)
    token_value_dict = {'Text' : []}
    tokenvalue = source_code
    value = tokenvalue.split('\n')
    lang = 'Text'
    for string in value:
        words = string.split(' ')
        for word in words:
            if word:
                if '\r' in word:
                    word = word[:-2]
                token_value_dict.get(lang, []).append(word)
    with open('New_tokens.json', 'w', encoding='utf-8') as new_f:
        json.dump(token_value_dict, new_f)

    result = file_comparison(f'#id{obj.id}')
    New_File.objects.filter(id=f'{obj.id}').update(title=f'{result}')
