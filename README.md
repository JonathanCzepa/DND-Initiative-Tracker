# Yet Another DND initiative Tracker

Many DMs use initiative trackers to save time. Issue is, that most are web based so you can't prepare an encounter ahead of time. This slows things down a bit since you have to punch in each value into the tracker right before combat. This project seeks to make an initiative/combat tracker that can save the data currently displayed for later use

# Features

## This tracker will be able to display the following values:

1. Initative Score & Modifer
2. Armor Class
3. Character/NPC Name
4. Whether or not a NPC is an enemy or ally
5. Status conditions
8. Track the number of rounds (Starting at 0)
9. Death saves. There should be a way for the DM to specify whether or not an NPC has death saves or just dies instantly

These values can be changed by the DM at any point.

## Sorting

The DM will be able to add as many entries as they so desire. Then they will be able to push the "Roll initiative" Button


The tracker will be able to then roll for initiative. If a preselected value has not been entered for a player/NPC then the tracker will roll for them. This will add their modifer.


pushing the button should re-roll initiative for all NPCs.


It's assumed that PC initiative is manually entered in. There should be an options menu to specify otherwise 

## Saving
The tracker should be able to save the values currently stored in the tracker. This will be done using a CSV files. 

## The weird stuff

### Rounding

DND is a game that only uses integers. It's usually up to the DM whether to round up/down. Accoding to pg. 7 of the Player's Handbook:

***"There’s one more general rule you need to know at the outset. Whenever you divide a number in the game, round down if you end up with a fraction, even if the fraction is one-half or greater." ***

This is easily handled with integer truncation

### Rolling the same initative
The PHB states that:

*** If a tie occurs, the DM decides the order among tied DM-controlled creatures, and the players decide the order among their tied characters. The DM can decide the order if the tie is between a monster and a player character. Optionally, the DM can have the tied characters and monsters each roll a d20 to determine the order, highest roll going first. ***

To streamline things it can be assumed that the DM will break ties between monsters the same between monsters and initiative the same way. Naturally, this means that even if two entries have the same initiative values one can still be sorted ahead of the other

This means that PCs and Monsters shouldn't be sorted by their pure initiative value. Instead there should be a function that compares each initiative value and returns their place in turn order. When comparing two initiative values that are the same it should break the tie using the following steps:

1. Compare initiative modifers with higher modifer going first
2. If there's still a tie then the tracker should have the tied entries re-roll to see which one goes first
3. Should there still be a tie after this then it should repeat step 2 until the tie is broken

# GUI
There should be two GUIs. One for the tracker and one for an options menu. 

# TO-DO
- [ ] Make a better introduction
- [ ] Before presentation make the README descriptive rather than prescriptive 
- [ ] Read this out loud to Caden since he can't read. 



# DND-Initiative-Tracker
