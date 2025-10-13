import pygame
import numpy 
from numba import njit, prange
def floorCast():
    pygame.init()
    screen = pygame.display.set_mode((400, 300))
    pygame.display.set_caption(".py_caster")
    pygame.display.set_icon(pygame.image.load("icon.png"))
    clock = pygame.time.Clock()
    running = True
    hres = 400
    halfvres = 300
    mod = hres/60
    posx, posy, rot = 0, 0, 0
    size = 6
    maph = numpy.random.choice([0, 0, 0, 1], (size, size))
    frame = numpy.random.uniform(0, 1, (hres, halfvres*2, 3)).astype(numpy.uint8)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        frame = new_frame(posx, posy, rot, frame, hres, halfvres, mod, maph, size, )
        for i in range(hres):
            rot_i = rot + numpy.deg2rad(i/mod - 30)
            sin, cos = numpy.sin(rot_i), numpy.cos(rot_i)
            for j in range(halfvres):
                n = halfvres/(halfvres - j)
                x, y = posx + cos*n, posy + sin*n
                if int(x) %2 == int(y) %2:
                    frame[i] [halfvres*2-j-1] = [1, 62, 62]
                else:
                    frame[i] [halfvres*2-j-1] = [0, 1, 53]
        surf = pygame.surfarray.make_surface(frame*255)
        surf = pygame.transform.scale(surf, (400, 300))
        screen.blit(surf, (0, 0))
        pygame.display.update()
        posx, posy, rot = movement(posx, posy, rot, pygame.key.get_pressed())
def movement(posx, posy, rot, keys): 
    if keys[pygame.K_LEFT] or keys[ord('a')]:
        rot = rot - 0.1
        print("py_caster.input[K_LEFT]")
        print("cam.rot[LEFT]")
    if keys[pygame.K_RIGHT] or keys[ord('d')]:
        rot = rot + 0.1
        print("py_caster.input[K_RIGHT]")
        print("cam.rot[RIGHT]")
    if keys[pygame.K_UP] or keys[ord('w')]:
        posx, posy = posx + numpy.cos(rot)*0.5, posy + numpy.sin(rot)*0.5
        print("py_caster.input[K_UP]")
    if keys[pygame.K_DOWN] or keys[ord('s')]:
        posx, posy = posx - numpy.cos(rot)*0.5, posy - numpy.sin(rot)*0.5
        print("py_caster.input[K_DOWN]")
    return posx, posy, rot
def new_frame(posx, posy, rot, frame, hres, halfvres, mod, maph, size):
    for i in range(hres):
        rot_i = rot + numpy.deg2rad(i/mod - 30)
        sin, cos = numpy.sin(rot_i), numpy.cos(rot_i)
        for j in range(halfvres):
            n = (halfvres/(halfvres-j))
            x,y = posx + cos*n, posy + sin*n
            shade = 0.2 + 0.8*(1 - j/halfvres)
            if maph[int(x)%(size-1)] [int(y)%(size-1)]:
                h = halfvres - j
                c = shade*numpy.ones(3)
                for k in range(h*2):
                    frame[i] [halfvres -h +k] = c
                break
    return frame 
if __name__ == "__main__":
    floorCast()
    pygame.quit()      


