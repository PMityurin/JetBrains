from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from .logiс import file_comparison
import json
from django.utils.timezone import now


class New_File(models.Model):
    file = models.FileField(upload_to='downloaded', null=True, blank=True)
    description = models.TextField(default='...')
    data = models.DateTimeField(default=now)


class Result(models.Model):
    result = models.CharField(max_length=255)
    new_file_id = models.ForeignKey(New_File, on_delete=models.CASCADE)
    data = models.DateTimeField(default=now)


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
    Result.objects.create(new_file_id=obj, result=f'{result}')
    return result