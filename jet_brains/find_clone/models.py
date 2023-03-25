from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_init
from .logiс import file_comparison
import json
from django.utils.timezone import now


# gets the text and converts it into tokens and calls the comparison function
def my_handler(source_code: str, id: int) -> str:
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

    return file_comparison(f'#id{id}')


class New_File(models.Model):
    file = models.FileField(upload_to='downloaded', null=True, blank=True)
    description = models.TextField(default='...')
    data = models.DateTimeField(default=now)
    result = models.CharField(max_length=255, default="Nothing")

    # inserts the result into the result field
    def save(self, *args, **kwargs):
        text = self.description
        id = New_File.objects.last()
        print(New_File.objects)
        self.result = my_handler(text, id)
        super().save()

