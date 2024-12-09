import pygame
# My code as no spaces because i'm not payed by the line
class object(): #Just an object
    def __init__(self,file_name,pos):
        image = pygame.image.load(file_name)
        rect = image.get_rect()
        rect.center = (pos[0],pos[1])
        self.image=image
        self.rect=rect
    def move(self,dx,dy):
        self.rect.center[0]=self.rect.center[0]+dx
        self.rect.center[1]=self.rect.center[1]+dy   
    def print_screen(self,screen):
        screen.blit(self.image,self.rect)     
class Player(object): #Subclass of object whose movement can be controlled !
    def move_player(self,keys,player_speed):
            if keys[pygame.K_LEFT]:
                self.rect.move_ip(-player_speed, 0)
            if keys[pygame.K_RIGHT]:
                self.rect.move_ip(player_speed, 0)
            if keys[pygame.K_UP]:
                self.rect.move_ip(0, -player_speed)
            if keys[pygame.K_DOWN]:
                self.rect.move_ip(0, player_speed)  

