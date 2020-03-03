"""
Arcade example testing. BREAK IT THEN FIX IT. UNDERSTAND IT. 
"""

import arcade
import os

#constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Platformer"

#Constants used to scale our sprites from their original size
CHARACTER_SCALING = 1
TILE_SCALING = 0.5
COIN_SCALING = 0.5
SPRITE_PIXEL_SIZE = 128
GRID_PIXEL_SIZE = (SPRITE_PIXEL_SIZE * TILE_SCALING)

#Movement speed of player, in pixels per frame
PLAYER_MOVEMENT_SPEED = 10
GRAVITY = 1
PLAYER_JUMP_SPEED = 20

#How many pixels to keep as a minimum margin between the character and the edge of the screen
LEFT_VIEWPORT_MARGIN = 200
RIGHT_VIEWPORT_MARGIN = 200
BOTTOM_VIEWPORT_MARGIN = 150
TOP_VIEWPORT_MARGIN = 100

PLAYER_START_X = 64
PLAYER_START_Y = 225


class MyGame(arcade.Window):
  """
  Main application class.
  """

  def __init__(self):

    #call the parent class and set up the window
    super().__init__(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TITLE)

    self.coin_list = None
    self.wall_list = None
    self.player_list = None
    self.star_list = None
    self.foreground_list = None
    self.background_list = None
    self.dont_touch_list = None

    #variable to hold player sprite
    self.player_sprite = None

    #variable to hold physics engine
    self.physics_engine = None

    #used to keep track of our scrolling
    self.view_bottom = 0
    self.view_left = 0

    #Load Sounds
    self.collect_coin_sound = arcade.load_sound(":resources:sounds/coin1.wav")
    # self.collect_star_sound = arcade.load_sound(":resources:sounds/coin3.wav")
    self.jump_sound = arcade.load_sound(":resources:sounds/jump1.wav")
    self.game_over = arcade.load_sound(":resources:sounds/gameover1.wav")
    

    #keep track of score
    self.score = 0

    #level tracker
    self.level = 1


    arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)


    """
    Note about __init__ : init only sets up the variables, but doesn't create any class instances.
    They just deault to 0 or None. The setup method actually creates the object instances, such as graphical sprites.
    Theres a reason they are split into two.  With a setup method split out, later we can easily
    add 'restart/play again' features.  A simple call to setup will reset everything. 
    We can also add additional levels and have setup_level_1 and setup_level_2 etc. 

    """

    
  def setup(self, level):
    """
    Set up the game here.  Call this function to start or restart the game.
    """

    #Used to keep track of scrolling
    self.view_bottom = 0
    self.view_left = 0 

    #create sprite lists
    self.player_list = arcade.SpriteList()
    self.wall_list = arcade.SpriteList()
    self.coin_list = arcade.SpriteList()
    self.star_list = arcade.SpriteList()
    self.foreground_list = arcade.SpriteList()
    self.background_list = arcade.SpriteList()

    
    #keep track of score
    self.score = 0


    #Set up the player, specifically placing it at the coordinates.
    image_source = ":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png"
    self.player_sprite = arcade.Sprite(image_source, CHARACTER_SCALING)
    self.player_sprite.center_x = PLAYER_START_X
    self.player_sprite.center_y = PLAYER_START_Y
    self.player_list.append(self.player_sprite)

    # --- Load in a map from the tiled editor ---
    #Name of layer in the file that has our platforms/walls
    platforms_layer_name = 'Platforms'
    #Name of the layer that has items for pick-up
    coins_layer_name = 'Coins'
    #Name of the layer that has items for foreground
    foreground_layer_name = 'Foreground'
    #Name of the layer that has items for background
    background_layer_name = 'Background'
    #Name of the layer that has items we shouldn't touch
    dont_touch_layer_name = "Don't Touch"

    #map name
    map_name = f"C:/Users/12146/Desktop/fun/platform_fun/map2_level_{level}.tmx"

    #read in the tiled map
    my_map = arcade.tilemap.read_tmx(map_name)

    #calculate the right edge of the my_map in pixels
    self.end_of_map = my_map.map_size.width * GRID_PIXEL_SIZE

    # -- Baackground
    self.background_list = arcade.tilemap.process_layer(my_map, background_layer_name, TILE_SCALING)
    # -- Foreground
    self.foreground_list = arcade.tilemap.process_layer(my_map, foreground_layer_name, TILE_SCALING)
    # -- Platforms
    self.wall_list = arcade.tilemap.process_layer(my_map,platforms_layer_name,TILE_SCALING)
    # -- Coins
    self.coin_list = arcade.tilemap.process_layer(my_map, coins_layer_name,TILE_SCALING)
    # --Don't Touch Layer
    self.dont_touch_list = arcade.tilemap.process_layer(my_map, dont_touch_layer_name, TILE_SCALING)

    #other stuff
    #set background color
    if my_map.background_color:
      arcade.set_background_color(my_map.background_color)
    #Create the 'physics engine'
    self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite, self.wall_list, GRAVITY)

    # #Create the ground
    # #this shows using a loop to place multiple sprites horizontally
    # for x in range(0, 1250,64):
    #     wall = arcade.Sprite(":resources:/images/tiles/grassMid.png", TILE_SCALING)
    #     wall.center_x = x
    #     wall.center_y = 32
    #     self.wall_list.append(wall)

    # #put some crates on the ground
    # #This shows using a coordinate list to place sprites
    # coordinate_list = [
    #     [512,96],
    #     [256,96],
    #     [768,96]
    # ]
    # for coordinate in coordinate_list:
    #     wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", TILE_SCALING)
    #     wall.position = coordinate
    #     self.wall_list.append(wall)

    # for x in range(128,1250,256):
    #   coin = arcade.Sprite(":resources:/images/items/coinGold.png", COIN_SCALING)
    #   coin.center_x = x
    #   coin.center_y = 96
    #   self.coin_list.append(coin)

    # #trying to add a star somewhere
    # star_coordinate_list = [
    #     [512,242],
    #     [768,272],
    # ]
    # for coordinate in star_coordinate_list:
    #   star = arcade.Sprite(":resources:images/items/star.png", TILE_SCALING)
    #   star.position = coordinate
    #   self.star_list.append(star)
    

  def on_draw(self):
    """render the screen"""

    #Clear the screen to the background color
    arcade.start_render()

    #Draw our sprites
    self.wall_list.draw()
    self.background_list.draw()
    self.wall_list.draw() #extra?
    self.coin_list.draw()
    self.dont_touch_list.draw()
    self.player_list.draw()
    # self.star_list.draw()
    self.foreground_list.draw()


    #draw our score on the screen, scrolling it with the viewport
    score_text = f"Score: {self.score}"
    arcade.draw_text(score_text, 10 +self.view_left, 10 +self.view_bottom, arcade.csscolor.BLACK, 18)


  def on_key_press(self, key, modifiers):
    """Called whenever a key is pressed. """
    if key == arcade.key.UP or key == arcade.key.W:
      if self.physics_engine.can_jump():
        self.player_sprite.change_y = PLAYER_JUMP_SPEED
    # elif key ==arcade.key.DOWN or key == arcade.key.S:
    #   self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED
    elif key ==arcade.key.LEFT or key == arcade.key.A:
      self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
    elif key ==arcade.key.RIGHT or key == arcade.key.D:
      self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED
  
  def on_key_release(self, key, modifiers):
    """Called when the user releases a key. """
    # if key == arcade.key.UP or key == arcade.key.W:
    #   self.player_sprite.change_y = 0
    # elif key ==arcade.key.DOWN or key == arcade.key.S:
    #   self.player_sprite.change_y = 0
    if key ==arcade.key.LEFT or key == arcade.key.A:
      self.player_sprite.change_x = 0
    elif key ==arcade.key.RIGHT or key == arcade.key.D:
      self.player_sprite.change_x = 0

  def on_update(self, delta_time):
    """movement and game logic """
    #move the player with the physics engine
    self.physics_engine.update()

    #See if we hit any coins
    coin_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)
    # star_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.star_list)

    #loop through each coin we hit (if any) and remove it
    for coin in coin_hit_list:
      #remove the coin
      coin.remove_from_sprite_lists()
      #play a sound
      arcade.play_sound(self.collect_coin_sound)
      #add one to the score
      self.score +=1
    
    # for star in star_hit_list:
    #   #remove the coin
    #   star.remove_from_sprite_lists()
    #   #play a sound
      # arcade.play_sound(self.collect_star_sound)
    #   #add one to the score
    #   self.score += 10

    

    #track if we need to change the viewport

    changed_viewport = False

    #Did the player fall off the map?
    if self.player_sprite.center_y < -100:
      self.player_sprite.center_x = PLAYER_START_X
      self.player_sprite.center_y = PLAYER_START_Y

      #set the camera to the start
      self.view_left = 0
      self.view_bottom = 0
      changed_viewport = True
      arcade.play_sound(self.game_over) #add to load sounds

    #Did the player touch something they should not?
    if arcade.check_for_collision_with_list(self.player_sprite, self.dont_touch_list):
      self.player_sprite.change_x = 0
      self.player_sprite.change_y = 0
      self.player_sprite.center_x = PLAYER_START_X
      self.player_sprite.center_y = PLAYER_START_Y

      #set the camera to the start
      self.view_left = 0
      self.view_bottom = 0
      changed_viewport = True
      arcade.play_sound(self.game_over)

    #See if the user got  to the end of the level
    if self.player_sprite.center_x >= self.end_of_map:
      # Avance to the next level
      self.level+= 1
      
      #Load the next level
      self.setup(self.level)

      #Set the camera to the start
      self.view_left = 0
      self.view_bottom = 0
      changed_viewport = True

    # ---- MANAGE SCROLLING ----

    #Scroll left
    left_boundary = self.view_left + LEFT_VIEWPORT_MARGIN
    if self.player_sprite.left < left_boundary:
      self.view_left -= left_boundary - self.player_sprite.left
      changed_viewport = True

    #Scroll right
    right_boundary = self.view_left + SCREEN_WIDTH - RIGHT_VIEWPORT_MARGIN
    if self.player_sprite.right > right_boundary:
      self.view_left += self.player_sprite.right - right_boundary
      changed_viewport = True

    #Scroll Up
    top_boundary = self.view_bottom + SCREEN_HEIGHT - TOP_VIEWPORT_MARGIN
    if self.player_sprite.top > top_boundary:
      self.view_bottom += self.player_sprite.top - top_boundary
      changed_viewport = True

    #Scroll down
    bottom_boundary = self.view_bottom + BOTTOM_VIEWPORT_MARGIN
    if self.player_sprite.bottom < bottom_boundary:
      self.view_bottom -= bottom_boundary - self.player_sprite.bottom
      changed_viewport = True

    if changed_viewport:
      #only scroll to integers. Otherwise we end up with pixels that don't line up on the screen
      self.view_bottom = int(self.view_bottom)
      self.view_left = int(self.view_left)

      #Do the scrolling
      arcade.set_viewport(self.view_left,SCREEN_WIDTH + self.view_left, self.view_bottom, SCREEN_HEIGHT + self.view_bottom)

def main():
    """main method"""
    window = MyGame()
    window.setup(window.level)
    arcade.run()

if __name__ == "__main__":
    main()