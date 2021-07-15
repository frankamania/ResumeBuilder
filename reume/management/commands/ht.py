from django.core.management.base import BaseCommand, CommandError

import json
import glob
from django.contrib.staticfiles.storage import staticfiles_storage


class Command(BaseCommand):

    def handle(self, *args, **options):

        meta_data_social = {
            "linkdin_url": {
                "name": "linkdin_url",
                "placeholder": "linkdin_url",
                "label": "linkdin_url"
            },

            "facebook_url": {
                "name": "facebook_url",
                "placeholder": "facebook_url",
                "label": "facebook_url"
            },

            "twitter_url": {
                "name": "twitter_url",
                "placeholder": "twitter_url",
                "label": "twitter_url"
            },

            "youtube_url": {
                "name": "youtube_url",
                "placeholder": "youtube_url",
                "label": "youtube_url"
            },

            "whatsapp_url": {
                "name": "whatsapp_url",
                "placeholder": "whatsapp_url",
                "label": "whatsapp_url"
            },

            "telegram_url": {
                "name": "telegram_url",
                "placeholder": "telegram_url",
                "label": "telegram_url"
            },


        }

        fdata = []
        for i in meta_data_social.keys():
            main_f = i
            sub_f = 'show_'+i
            data = """<div class="form-group col">
                <label for="|| metadata.{}.name ||">|| metadata.{}.label ||</label>
                <div class="form-check form-switch">
                  <input type="checkbox" id="|| metadata.{}.name ||" name="|| metadata.{}.name ||"  value="1" |% if instance.{} %|checked|% endif %|>
                  <label class="form-check-label" for="|| metadata.{}.name ||">|| metadata.{}.label ||</label>
                </div>
                <input type="text" class="container-text input" id="|| metadata.{}.name ||" name="|| metadata.{}.name ||" placeholder="|| metadata.{}.placeholder ||" |% if instance != None %| value="|| instance.{} ||"|% endif %|>
            </div>""".format(main_f,main_f,sub_f,sub_f,sub_f,sub_f,sub_f,main_f,main_f,main_f,main_f).replace('"||',"{{").replace('||"',"}}").replace('|%',"{%").replace('%|',"%}").replace('>||',">{{").replace('||<',"}}<")

            fdata.append(data)


        with open('m.txt',"w")  as f:

            f.write("\n\n".join(fdata))