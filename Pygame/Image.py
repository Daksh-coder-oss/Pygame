import pygame

pygame.init()
window=pygame.display.set_mode((700,800))

pygame.display.set_caption("Adding Image and Background!")
bg_image=pygame.image.load("bg2.png")
character_image=pygame.image.load("Character.jpeg")
bg=pygame.transform.scale(bg_image.convert(),(0,0))
character=pygame.transform.scale(character_image.convert_alpha(),(350,400))
character_rect=character.get_rect(center=(350,400))
while True:
    for event in pygame.event.get():
        if event==pygame.QUIT:
            pygame.quit()
    window.blit(bg,(0,0))
    window.blit(character,character_rect)
    pygame.display.flip()
    