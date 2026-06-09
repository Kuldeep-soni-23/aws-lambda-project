import random

def battle():

    player_health = random.randint(50, 100)
    monster_health = random.randint(50, 100)

    while player_health > 0 and monster_health > 0:

        player_attack = random.randint(10, 25)
        monster_health -= player_attack

        if monster_health <= 0:
            return {
                "winner": "Player",
                "player_health": player_health,
                "monster_health": 0
            }

        monster_attack = random.randint(5, 20)
        player_health -= monster_attack

    return {
        "winner": "Monster",
        "player_health": max(player_health, 0),
        "monster_health": monster_health
    }