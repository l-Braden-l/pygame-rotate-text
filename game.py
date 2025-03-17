# -- Pygame Game Template -- #

import pygame
import sys
import config # Import the config module 
def init_game (): 
    pygame.init()
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT)) # Use constants from config
    pygame.display.set_caption(config.TITLE)
    return screen


def handle_events ():
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
          return False
       elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_ESCAPE:
             return False
    return True

# --- Draw Text Function --- #
def draw_text(screen,text, font_size, color, x, y, font_name = None, bold = False, italic = False, rotation = 0):
   pygame.font.init()

   if font_name:
      font = pygame.font.Font(font_name, font_size)
   else:
      font = pygame.font.Font(None, font_size)
   font.set_bold(bold)
   font.set_italic(italic)
   # -- Make Text Surface/Render Text -- #
   text_surface = font.render(text, True, color)

   # -- Rotate Text Surface -- #
   if rotation != 0:
      text_surface = pygame.transform.rotate(text_surface, rotation)

   # -- Get The New rect For The Rotated Surface-- #
   text_rect = text_surface.get_rect(center=(x,y))

   # -- Blit The Rotated Text Surface Onto The Main Surface -- #
   screen.blit(text_surface, text_rect.topleft)




def main():
   screen = init_game()
   clock = pygame.time.Clock() # Initialize the clock here



   running = True
   while running:
      running = handle_events()
      screen.fill(config.WHITE) # Use color from config

      pygame.draw.rect(screen, config.SKY_BLUE, [0,170,900,500],0)
      pygame.draw.rect(screen, config.GREEN, [0,170,900,5],0)
      # -- Define text properties -- #
      font_name1 = None
      text1 = "Hello, Pygame!"
      font_size1 = 60
      color1 = config.BLACK
      x1, y1 = 400, 150

      font_name2 = "c:\Fonts\LVDCGO__.TTF"
      text2 = "Bold Text!"
      font_size2 = 25
      color2 = config.RED
      x2, y2 = 180, 100

      font_name3 = "c:\Fonts\RobotoMono-VariableFont_wght.ttf"
      text3 = "Italic Text!"
      font_size3 = 30
      color3 = config.GREEN
      x3, y3 = 600, 50

      text4 = "!emagyP ,olleH"
      font_size4 = 60
      color4 = config.BLACK
      x4, y4 = 400, 200

      # -- Draw text on screen using variables -- #
      draw_text(screen, text1, font_size1, color1, x1, y1, font_name1)
      draw_text(screen, text2, font_size2, color2, x2, y2, font_name2, bold=True, )
      draw_text(screen, text3, font_size3, color3, x3, y3, font_name3, italic=True, rotation= 15)
      draw_text(screen, text4, font_size4, color4, x4, y4, italic=False, rotation= 180)
      

      pygame.display.flip()

      # -- Limit the frame rate to the specified frames per second (FPS) -- #
      clock.tick(config.FPS) # Use the clock to control the frame rate

   pygame.quit()
   sys.exit()

if __name__ == "__main__":
   main()