import time as time_
import pygame

class title_screen_options:
    def __init__(self,font):
        self.font=font
    def add_text(self,text_str,pos):
        self.text=self.font.render(text_str,False,'black')
        self.rect=self.text.get_rect()
        self.rect.center=(pos[0],pos[1])
    def print_screen(self,screen):
        screen.blit(self.text,self.rect)
class highlightable_title_screen_options(title_screen_options):
    def add_text(self,text_str,pos,mouse_pos):
        self.text=self.font.render(text_str,False,'black')
        self.rect=self.text.get_rect()
        self.rect.center=(pos[0],pos[1])
        self.text_copy=None
        if(self.rect.collidepoint(mouse_pos)==True):
            self.text_copy=self.font.render(text_str,False,'black')
            self.text_copy.fill('red')
            self.text_copy.set_alpha(100)
    def print_screen(self,screen):
        screen.blit(self.text,self.rect)
        if(self.text_copy!=None):
            screen.blit(self.text_copy,self.rect)
            

def define_title_screen(screen,font,width,height,time,mouse_pos):
    str_title='duality'
    str_menu='play'
    i=int(time // (0.1))
    if(i>len(str_title)):
        title_string=str_title
        time_.sleep(0.2)
        j=int(time//(0.1))-len(str_title)
        menu_string=str_menu[0:j:1]
    else:
        title_string=str_title[0:i:1]
        menu_string=None
    title=title_screen_options(font)
    title.add_text(title_string,pos=[width //2 ,height//2])
    play_button=highlightable_title_screen_options(font)
    play_button.add_text(menu_string,pos=[width //2 ,(height+0.2*height)//2],mouse_pos=mouse_pos)
    title.print_screen(screen)
    play_button.print_screen(screen)
