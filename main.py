import pygame
import title_screen
import Utils
import time
from pygame_screen_record import ScreenRecorder
if __name__ == "__main__":
    pygame.init()

    font = pygame.font.Font('MTF Kim.ttf', 32) #Loads the font
    width = 800
    height = 600
    screen = pygame.display.set_mode((width, height))

    pygame.display.set_caption("My RPG Game")

    running = True
    title_screen_=True
    t_init=time.perf_counter()
    player=Utils.Player(file_name="player.png",pos=[width//2,height//2])
    #recorder = ScreenRecorder(60) # pass your desired fps
    #recorder.start_rec() # start recording
    while running:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        if(title_screen_==True):  
            screen.fill((255, 255, 255))
            mouse_pos=pygame.mouse.get_pos()
            title_screen.define_title_screen(screen,font,width,height,time.perf_counter()-t_init,mouse_pos)
            pygame.display.flip()
        else:
            keys = pygame.key.get_pressed()
            player.move_player(keys=keys,player_speed=1)
            player.print_screen(screen=screen)
            pygame.display.flip()
    #recorder.stop_rec()	# stop recording
    #recorder.save_recording("my_recording.avi") # saves the last recording
    pygame.quit()