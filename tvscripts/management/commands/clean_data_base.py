#coding: utf8
from django.core.management.base import BaseCommand
from tvscripts.models import Script, Script_Tag
import glob
import linecache
import fnmatch
import os
import re

class Command(BaseCommand):
    help = 'Load subtitles files into the Script model'

    def handle(self, *args, **options):
        FILTER_LIST = [
        "font color",
        "www.forom.com",
        "www.geocities.com",
        "www.addic7ed.com",
        "Transcript by",
        "Subtitles:"
        "Sync by",
        "Downloaded From"]

        BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        SCRIPT_FOLDERS = BASE_DIR + '/tv_script_files/'
        ERROR_LIST = []
        files = glob.glob(SCRIPT_FOLDERS +'*/Season */*.srt')
        for f in files:
            fp = open (f, 'r', encoding='latin1')
            try:
                filename = os.path.basename(fp.name)
                show_name = ''.join(filename.partition('-')[:1])
                season = int(re.search(r'\d', filename).group())
                epi_number = int(re.search(r'\d\d', filename).group())
                epi_name = re.search('%s(.*)%s' % (' - ', '.en'), filename).group(1)
                for i, line in enumerate(fp):
                    # The Timestamp
                    if re.search(r'-->',linecache.getline(f, i+1)):
                        position = line
                        script_content = []
                        script_content.append(linecache.getline(f, i+2))

                        if linecache.getline(f, i+3).isspace()==False:
                            script_content.append(linecache.getline(f, i+3))
                        script_content = '\r'.join(script_content)

                        one_line = Script(
                        scripts=script_content,
                        position=position,
                        epi_number=int(epi_number),
                        epi_name = epi_name,
                        season=int(season),
                        show_name = show_name,
                        )
                        one_line.save()
            except UnicodeDecodeError or SyntaxError as e:
                ERROR_LIST.append(f)
                ERROR_LIST.append(e)
                pass
            fp.close()
