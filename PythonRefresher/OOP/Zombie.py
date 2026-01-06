from Enemy import Enemy
import random

class Zombie(Enemy):
    
    def __init__(self, health_points, attack_damage):
        super().__init__(
            type_of_enemy='Zombie', 
            health_points=health_points, 
            attack_damage=attack_damage
        )
    
    def talk(self):
        print('*Grumbling...*')
    
    def spread_disease(self):
        print("The zombie is trying to spread a infection.")

    def special_attack(self):
        did_special_attack = random.random() < 0.50  # 50% chance
        if did_special_attack:
            self.health_points += 2
            print('Zombie regenerated 2HP')