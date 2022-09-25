# 40KSim
A tool for comparing 40K unit effectiveness


## WHY

With the growing inflation of unit lethality in Warhammer 40K 9th edition (and really every edition since the whipe from 2nd to 3rd edition), it becomes increasingly hard to compare one unit to another.  Points fail to capture the absolute utility of a unit, and more so does the laughable metric of "power level".  Yes, within a given army there is some level of subjectivity due to the key functionality that a powerful ranged unit may lend to a melee heavy army, and vice versa.  However, the aim of this tool is to firstly compute the utility of any given unit against a common metric for later rebasing the point structure of the Warhammer 40K universe.  Secondly, and later, it aims to create an engine for combat simulation of the 40K universe that can then be leveraged for single and multi-run simulations.

## Modules

### Utility Computation

A unit effectiveness calculator.  This model takes the dot product of stats * weapons per model to create a baseline for points.

### Combat Simulation

#### Dojo

A single turn iteration of combat.  Size and distance from units are selectable as inputs, along with who goes first.  Units loaded in by the user in CSV.


#### Game

Multiple turns of combat with multiple units.  Unit actions are run against a playbook based on what the agent believes is the best course.  The initial aim is to always target the closest & strongest unit, simply as a standin for future AI agents.  Later, AI agents can be trained and placed into action.  Additionally, a scene animator can show what is happening turn-by-turn for the amusement of all!


#### Special Thanks To Wahapedia

This project leverages data ingested from the open source commuity of Wahapedia.ru.  

Despite the national origin of its host, their contributions to our hobby prove to be exceptional and of merit.  Slava Ukraini


Data Sources:
https://wahapedia.ru/wh40k9ed/the-rules/about/
https://wahapedia.ru/wh40k9ed/Export%20Data%20Specs.xlsx
http://wahapedia.ru/wh40k9ed/Factions.csv
http://wahapedia.ru/wh40k9ed/Source.csv
http://wahapedia.ru/wh40k9ed/Datasheets.csv
http://wahapedia.ru/wh40k9ed/Datasheets_abilities.csv
http://wahapedia.ru/wh40k9ed/Datasheets_damage.csv
http://wahapedia.ru/wh40k9ed/Datasheets_keywords.csv
http://wahapedia.ru/wh40k9ed/Datasheets_models.csv
http://wahapedia.ru/wh40k9ed/Datasheets_options.csv
http://wahapedia.ru/wh40k9ed/Datasheets_wargear.csv
http://wahapedia.ru/wh40k9ed/Datasheets_stratagems.csv
http://wahapedia.ru/wh40k9ed/Wargear.csv
http://wahapedia.ru/wh40k9ed/Wargear_list.csv
http://wahapedia.ru/wh40k9ed/Stratagems.csv
http://wahapedia.ru/wh40k9ed/StratagemPhases.csv
http://wahapedia.ru/wh40k9ed/Abilities.csv
http://wahapedia.ru/wh40k9ed/Warlord_traits.csv
http://wahapedia.ru/wh40k9ed/PsychicPowers.csv
http://wahapedia.ru/wh40k9ed/Secondaries.csv
http://wahapedia.ru/wh40k9ed/Last_update.csv