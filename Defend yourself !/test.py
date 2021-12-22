import random
import pygame

a = (12, 13, 14)
for elt in reversed(a):
    print(elt)

print(a)
print('\n')

towers = (
    (5, 4, 'rapid'),
    (30, 0.4, 'long'),
    (8, 2, 'normal')
)


def attack(n, a, b, S):
    U = S
    for i in range(n):
        U *= a
        U += 3
    return U


def attack_speed(n, a, S):
    U = S
    for i in range(n):
        U *= a
    return U


for tower in towers:
    for i in range(1, 11):
        print('\n', tower)
        print(round(attack(i, 1.1, 10, tower[0]) * attack_speed(i, 1.2, tower[1])))

image = pygame.image.load(f'assets/projectiles/rapid.png')

orig_rect = image.get_rect()
rot_image = pygame.transform.rotate(image, -225)
pygame.image.save(rot_image, 'image.png')
rot_rect = orig_rect.copy()
rot_rect.center = rot_image.get_rect().center
rot_image = rot_image.subsurface(rot_rect).copy()

pygame.image.save(rot_image, 'rot_image.png')


tab_str = ['lr']
print(tab_str)
print(tab_str[0])
print(str(tab_str))

for i in range(10):
    print(random.choices((True, False), (0.1, 0.9)))

