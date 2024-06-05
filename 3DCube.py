#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pygame

class Model:

    def __init__(self, vertices, faces):
        self.vertices = vertices
        self.faces = faces

    def draw(self, screen):
        for face in self.faces:
            pygame.draw.polygon(screen, (255, 0, 0), face)

if __name__ == "__main__":

    vertices = np.array([
        (0, 0, 0),
        (1, 0, 0),
        (1, 1, 0),
        (0, 1, 0),
        (0, 0, 1),
        (1, 0, 1),
        (1, 1, 1),
        (0, 1, 1)
    ])

    faces = np.array([
        (0, 1, 2),
        (2, 3, 0),
        (4, 5, 6),
        (6, 7, 4),
        (0, 4, 5),
        (5, 1, 0),
        (2, 6, 7),
        (7, 3, 2)
    ])

    model = Model(vertices, faces)

    pygame.init()
    screen = pygame.display.set_mode((800, 600))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill((255, 255, 255))
        model.draw(screen)
        pygame.display.update()

