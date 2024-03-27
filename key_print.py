import pygame
import sys 


class Print:
    def __init__(self,event):
        pygame.init()       # Initialize Pygame 

        self.screen = pygame.display.set_mode((400,300))
        pygame.display.set_caption("Pygame texts are printed here.")

        self.font = pygame.font.Font(None, 36) # font and size can be chosen from here.

        if event.type == pygame.QUIT:
            self.text = "Quit game!"
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self.text = "Right Click"
            elif event.key == pygame.K_LEFT:
                self.text = "Left Click"

    def print(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit() 
        # Clear the screen 
            self.screen.fill((255,255,255))

        # Renders the text 
            text_render = self.font.render(self.text,True,(0,0,0)) # Text color is black 

        #Get the rectangle containing the text 
            text_rect = text_render.get_rect()
        # Center the text on the screen 
            text_rect.center = (200,150)

        # Blit the text onto the screen 
            self.screen.blit(text_render, text_rect)

        # Update the display 
            pygame.display.flip()
