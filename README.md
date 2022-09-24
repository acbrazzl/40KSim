# 40KSim
A tool for comparing 40K unit effectiveness


## WHY

With the growing inflation of unit lethality in Warhammer 40K 9th edition (and really every edition since the whipe from 2nd to 3rd edition), it becomes increasingly hard to compare one unit to another.  Points fail to capture the absolute utility of a unit, and more so does the laughable metric of "power level".  Yes, within a given army there is some level of subjectivity due to the key functionality that a powerful ranged unit may lend to a melee heavy army, and vice versa.  However, the aim of this tool is to firstly compute the utility of any given unit against a common metric for later rebasing the point structure of the Warhammer 40K universe.  Secondly, and later, it aims to create an engine for combat simulation of the 40K universe that can then be leveraged for single and multi-run simulations.

## Modules

### Utility Computation

A dot-product computation of unit effectiveness calculator

### Combat Simulation

#### Dojo

A single turn iteration of combat.  Size and distance from units are selectable as inputs, along with who goes first.  Units loaded in by the user in CSV.


#### Game

Multiple turns of combat with multiple units.  Unit actions are run against a playbook based on what the agent believes is the best course.  The initial aim is to always target the closest & strongest unit, simply as a standin for future AI agents.  Later, AI agents can be trained and placed into action.  Additionally, a scene animator can show what is happening turn-by-turn for the amusement of all!

