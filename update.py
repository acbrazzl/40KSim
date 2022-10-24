
import logging
import os
from pathlib import Path
import requests

#TODO: Tell user to pip install requests!

cache_dir = "cache/"
sources = [
#"https://wahapedia.ru/wh40k9ed/the-rules/about/",
#"https://wahapedia.ru/wh40k9ed/Export%20Data%20Specs.xlsx",
"http://wahapedia.ru/wh40k9ed/Factions.csv",
"http://wahapedia.ru/wh40k9ed/Source.csv",
"http://wahapedia.ru/wh40k9ed/Datasheets.csv",
"http://wahapedia.ru/wh40k9ed/Datasheets_abilities.csv",
"http://wahapedia.ru/wh40k9ed/Datasheets_damage.csv",
"http://wahapedia.ru/wh40k9ed/Datasheets_keywords.csv",
"http://wahapedia.ru/wh40k9ed/Datasheets_models.csv",
"http://wahapedia.ru/wh40k9ed/Datasheets_options.csv",
"http://wahapedia.ru/wh40k9ed/Datasheets_wargear.csv",
#"http://wahapedia.ru/wh40k9ed/Datasheets_stratagems.csv",
"http://wahapedia.ru/wh40k9ed/Wargear.csv",
"http://wahapedia.ru/wh40k9ed/Wargear_list.csv"]
#"http://wahapedia.ru/wh40k9ed/Stratagems.csv",
#"http://wahapedia.ru/wh40k9ed/StratagemPhases.csv",
#"http://wahapedia.ru/wh40k9ed/Abilities.csv",
#"http://wahapedia.ru/wh40k9ed/Warlord_traits.csv",
#"http://wahapedia.ru/wh40k9ed/PsychicPowers.csv",
#"http://wahapedia.ru/wh40k9ed/Secondaries.csv",
#"http://wahapedia.ru/wh40k9ed/Last_update.csv"

logger = logging.getLogger(__name__)
logger.setLevel('INFO')

def update():
    logger.info('Updating...')
    f = Path(cache_dir).mkdir(parents=True, exist_ok=True)
    for url in sources:
        name = cache_dir + url.split("/")[-1]
        logger.info(f'Attempting to DL {name} from {url}')
       # urllib.request.urlretrieve(url, name)
        #(url, cache_dir + url.split("/")[-1])

        r = requests.get(url)
        open(name, 'wb').write(r.content)
    logger.info('Update Complete!')
       


