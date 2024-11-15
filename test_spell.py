from flask import Flask, render_template, request, redirect, url_for
from game_objects.player import Player
from game_objects.game import load
from game_objects.demon import get_demon_by_name
from game_objects.items import Spell
import random


player = Player("roy", 100)

counter = 0

while True:
    spell = Spell(1)
    for player_spell in player.get_inventory().get_spells():
        if spell.name == player_spell.name:
            break
    else:
        player.get_inventory().add_item(spell)
        counter += 1
        if counter == 15:
            break


for spell in player.inventory.get_spells():
    print(spell.name)
