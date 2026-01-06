import random
from Enemy import Enemy

class Ogre(Enemy):
    
    def __init__(self, health_points, attack_damage):
        super().__init__(
            type_of_enemy='Ogre', 
            health_points=health_points, 
            attack_damage=attack_damage
        )
    
    def talk(self):
        print("Ogre is slamming hands all around!")
    
    def special_attack(self):
        did_special_attack = random.random() < 0.20  # 50% chance
        if did_special_attack:
            self.health_points += 4
            print('Ogre gets angry and increses attack by 4')
    