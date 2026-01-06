from Enemy import Enemy
from Hero import Hero
from Ogre import Ogre
from Weapon import Weapon
from Zombie import Zombie


# def battle(hero: Enemy, enemy: Enemy):
#     hero.talk()
#     enemy.attack()
    
#     while hero.health_points > 0 and enemy.health_points > 0:
#         print('---------------------------------')
#         hero.special_attack()
#         enemy.special_attack()
#         print(f'{hero.get_type_of_enemy()}: {hero.health_points} HP left')
#         print(f'{enemy.get_type_of_enemy()}: {enemy.health_points} HP left')
#         enemy.attack()
#         hero.health_points -= enemy.attack_damage
#         hero.attack()
#         enemy.health_points -= hero.attack_damage
#     print('---------------------------------')
    
#     if hero.health_points > 0:
#         print(f'{hero.get_type_of_enemy()} wins!')
#     else:
#         print(f'{enemy.get_type_of_enemy()} wins!')
        
def hero_battle(hero: Hero, enemy: Enemy):
    while hero.health_points > 0 and enemy.health_points > 0:
        print('---------------------------------')
        print(f'Hero: {hero.health_points} HP left')
        print(f'{enemy.get_type_of_enemy()}: {enemy.health_points} HP left')
        enemy.attack()
        hero.health_points -= enemy.attack_damage
        hero.attack()
        enemy.health_points -= hero.attack_damage
    print('---------------------------------')
    
    if hero.health_points > 0:
        print('Hero wins!')
    else:
        print(f'{enemy.get_type_of_enemy()} wins!')
        
zombie = Zombie(10, 1)
ogre = Ogre(20, 3)
hero = Hero(10, 1)
weapon = Weapon('Sword', 155)
hero.weapon = weapon
hero.equip_weapon

hero_battle(hero, ogre)
