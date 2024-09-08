import csv
import random
import time
import getpass
import requests, os
import sys
UPLOAD_DIR = "uploads"
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)
sys.path.insert(0, "/mnt/student/imports/.local/lib/python3.10/site-packages/")
import climage
import PIL  #this automatically is stored in the same folder as climage
img = climage.convert("/mnt/student/p12_intermediate_python_06/contact-manager/images/Screenshot 2024-07-17 at 10.10.02.png", is_unicode=True, width=25)  # Add the filename after `/mnt/student/` and the name of whatever folder it's in.
option_5 = img  # This will print a pixelated version of the image.
img = climage.convert("/mnt/student/p12_intermediate_python_06/contact-manager/images/Screenshot 2024-07-17 at 12.25.00.png", is_unicode=True, width=25)  # Add the filename after `/mnt/student/` and the name of whatever folder it's in.
option_6 = img  # This will print a pixelated version of the image.
def add_image():
    file = input("image url > ")
    while True:
        filename = "".join(random.choices("0123456789", k=25)) + ".png"
        if not os.path.exists(os.path.join(UPLOAD_DIR, filename)):
            break

    with requests.get(file) as image, open(os.path.join(UPLOAD_DIR, filename), "wb") as upload:
        upload.write(image.content)

    try:
        file = climage.convert(os.path.join(UPLOAD_DIR, filename), is_unicode=True, width=20)
        print(file)
    except (PIL.UnidentifiedImageError, FileNotFoundError):
        print("Cannot identify file; make sure it's an image!")
        os.unlink(os.path.join(UPLOAD_DIR, filename))



USER_FILE = 'users.txt'
CONTACT_FILE_TEMPLATE = '{}_contacts.txt'


def throwing_out_the_trash():
    garbage_animation = ["""
                      @@@@@@@@@@
                        @@@@@@@         
                        @@@@@@ 
                        @@@@@  
                      @@@@@@@@@@
                   @@@@@@@@@@@@@@@              
                 @@@@@@@@@@@@@@@@@@            
               @@@@@@@@@@@@@@@@@@@@@
              @@@@@@@@@@@@@@@@@@@@@@@     
             @@@@@@@@@@@@@@@@@@@@@@@@@             
            @@@@@@@@@@@@@@@@@@@@@@@@@@             
            @@@@@@@@@@@@@@@@@@@@@@@@@@             
            @@@@@@@@@@@@@@@@@@@@@@@@@@    
             @@@@@@@@@@@@@@@@@@@@@@@@              
                @@@@@@@@@@@@@@@@                   
                                                   
                                          
                                          
                                          
          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  
         @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ 
          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  
             @@@@@@@@@@@@@@@@@@@@@@@@     
             @@@@@@@@@@@@@@@@@@@@@@@@     
              @@@@@@@@@@@@@@@@@@@@@@@     
              @@@@@@@@@@@@@@@@@@@@@@      
              @@@@@@@@@@@@@@@@@@@@@@      
               @@@@@@@@@@@@@@@@@@@@       
               @@@@@@@@@@@@@@@@@@@@       
                @@@@@@@@@@@@@@@@@@@       
                @@@@@@@@@@@@@@@@@@        
                @@@@@@@@@@@@@@@@@@        
                 @@@@@@@@@@@@@@@@         
    """, """
                       @@@@@@@@@@
                        @@@@@@@         
                        @@@@@@ 
                        @@@@@  
                      @@@@@@@@@@
                   @@@@@@@@@@@@@@@              
                 @@@@@@@@@@@@@@@@@@            
               @@@@@@@@@@@@@@@@@@@@@
              @@@@@@@@@@@@@@@@@@@@@@@     
             @@@@@@@@@@@@@@@@@@@@@@@@@             
            @@@@@@@@@@@@@@@@@@@@@@@@@@             
            @@@@@@@@@@@@@@@@@@@@@@@@@@             
            @@@@@@@@@@@@@@@@@@@@@@@@@@    
             @@@@@@@@@@@@@@@@@@@@@@@@              
                @@@@@@@@@@@@@@@@                   
                                                   
                                          
                                          
          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  
         @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ 
          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  
             @@@@@@@@@@@@@@@@@@@@@@@@     
             @@@@@@@@@@@@@@@@@@@@@@@@     
              @@@@@@@@@@@@@@@@@@@@@@@     
              @@@@@@@@@@@@@@@@@@@@@@      
              @@@@@@@@@@@@@@@@@@@@@@      
               @@@@@@@@@@@@@@@@@@@@       
               @@@@@@@@@@@@@@@@@@@@       
                @@@@@@@@@@@@@@@@@@@       
                @@@@@@@@@@@@@@@@@@        
                @@@@@@@@@@@@@@@@@@        
                 @@@@@@@@@@@@@@@@         
    """, """
                        @@@@@@@@@@
                        @@@@@@@         
                        @@@@@@ 
                        @@@@@  
                      @@@@@@@@@@
                   @@@@@@@@@@@@@@@              
                 @@@@@@@@@@@@@@@@@@            
               @@@@@@@@@@@@@@@@@@@@@
              @@@@@@@@@@@@@@@@@@@@@@@     
             @@@@@@@@@@@@@@@@@@@@@@@@@             
            @@@@@@@@@@@@@@@@@@@@@@@@@@             
            @@@@@@@@@@@@@@@@@@@@@@@@@@             
            @@@@@@@@@@@@@@@@@@@@@@@@@@    
             @@@@@@@@@@@@@@@@@@@@@@@@              
                @@@@@@@@@@@@@@@@                   
                         
                         
                                                          
          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  
         @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ 
          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  
             @@@@@@@@@@@@@@@@@@@@@@@@     
             @@@@@@@@@@@@@@@@@@@@@@@@     
              @@@@@@@@@@@@@@@@@@@@@@@     
              @@@@@@@@@@@@@@@@@@@@@@      
              @@@@@@@@@@@@@@@@@@@@@@      
               @@@@@@@@@@@@@@@@@@@@       
               @@@@@@@@@@@@@@@@@@@@       
                @@@@@@@@@@@@@@@@@@@       
                @@@@@@@@@@@@@@@@@@        
                @@@@@@@@@@@@@@@@@@        
                 @@@@@@@@@@@@@@@@ 
    """, """
                          @@@@@@@@@@
                        @@@@@@@         
                        @@@@@@ 
                        @@@@@  
                      @@@@@@@@@@
                   @@@@@@@@@@@@@@@              
                 @@@@@@@@@@@@@@@@@@            
               @@@@@@@@@@@@@@@@@@@@@
              @@@@@@@@@@@@@@@@@@@@@@@     
             @@@@@@@@@@@@@@@@@@@@@@@@@             
            @@@@@@@@@@@@@@@@@@@@@@@@@@             
            @@@@@@@@@@@@@@@@@@@@@@@@@@             
            @@@@@@@@@@@@@@@@@@@@@@@@@@    
             @@@@@@@@@@@@@@@@@@@@@@@@              
                @@@@@@@@@@@@@@@@                   
                                                   
          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  
         @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ 
          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  
             @@@@@@@@@@@@@@@@@@@@@@@@     
             @@@@@@@@@@@@@@@@@@@@@@@@     
              @@@@@@@@@@@@@@@@@@@@@@@     
              @@@@@@@@@@@@@@@@@@@@@@      
              @@@@@@@@@@@@@@@@@@@@@@      
               @@@@@@@@@@@@@@@@@@@@       
               @@@@@@@@@@@@@@@@@@@@       
                @@@@@@@@@@@@@@@@@@@       
                @@@@@@@@@@@@@@@@@@        
                @@@@@@@@@@@@@@@@@@        
                 @@@@@@@@@@@@@@@@ 
    """, """
                          @@@@@@@@@@
                        @@@@@@@         
                        @@@@@@ 
                        @@@@@  
                      @@@@@@@@@@
                   @@@@@@@@@@@@@@@              
                 @@@@@@@@@@@@@@@@@@            
               @@@@@@@@@@@@@@@@@@@@@
              @@@@@@@@@@@@@@@@@@@@@@@     
             @@@@@@@@@@@@@@@@@@@@@@@@@             
            @@@@@@@@@@@@@@@@@@@@@@@@@@             
            @@@@@@@@@@@@@@@@@@@@@@@@@@             
            @@@@@@@@@@@@@@@@@@@@@@@@@@    
             @@@@@@@@@@@@@@@@@@@@@@@@              
                @@@@@@@@@@@@@@@@                   
                                                                    
          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  
         @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ 
          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  
             @@@@@@@@@@@@@@@@@@@@@@@@     
             @@@@@@@@@@@@@@@@@@@@@@@@     
              @@@@@@@@@@@@@@@@@@@@@@@     
              @@@@@@@@@@@@@@@@@@@@@@      
              @@@@@@@@@@@@@@@@@@@@@@      
               @@@@@@@@@@@@@@@@@@@@       
               @@@@@@@@@@@@@@@@@@@@       
                @@@@@@@@@@@@@@@@@@@       
                @@@@@@@@@@@@@@@@@@        
                @@@@@@@@@@@@@@@@@@        
                 @@@@@@@@@@@@@@@@ 
    """, """
                          @@@@@@@@@@
                        @@@@@@@         
                        @@@@@@ 
                        @@@@@  
                      @@@@@@@@@@
                   @@@@@@@@@@@@@@@              
                 @@@@@@@@@@@@@@@@@@            
               @@@@@@@@@@@@@@@@@@@@@
              @@@@@@@@@@@@@@@@@@@@@@@     
             @@@@@@@@@@@@@@@@@@@@@@@@@             
            @@@@@@@@@@@@@@@@@@@@@@@@@@             
            @@@@@@@@@@@@@@@@@@@@@@@@@@             
            @@@@@@@@@@@@@@@@@@@@@@@@@@                                        
          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  
         @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ 
          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  
             @@@@@@@@@@@@@@@@@@@@@@@@     
             @@@@@@@@@@@@@@@@@@@@@@@@     
              @@@@@@@@@@@@@@@@@@@@@@@     
              @@@@@@@@@@@@@@@@@@@@@@      
              @@@@@@@@@@@@@@@@@@@@@@      
               @@@@@@@@@@@@@@@@@@@@       
               @@@@@@@@@@@@@@@@@@@@       
                @@@@@@@@@@@@@@@@@@@       
                @@@@@@@@@@@@@@@@@@        
                @@@@@@@@@@@@@@@@@@        
                 @@@@@@@@@@@@@@@@ 
    """, """
                          @@@@@@@@@@
                        @@@@@@@         
                        @@@@@@ 
                        @@@@@  
                      @@@@@@@@@@
                   @@@@@@@@@@@@@@@              
                 @@@@@@@@@@@@@@@@@@            
               @@@@@@@@@@@@@@@@@@@@@
              @@@@@@@@@@@@@@@@@@@@@@@     
             @@@@@@@@@@@@@@@@@@@@@@@@@             
            @@@@@@@@@@@@@@@@@@@@@@@@@@             
            @@@@@@@@@@@@@@@@@@@@@@@@@@                                                 
          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  
         @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ 
          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  
             @@@@@@@@@@@@@@@@@@@@@@@@     
             @@@@@@@@@@@@@@@@@@@@@@@@     
              @@@@@@@@@@@@@@@@@@@@@@@     
              @@@@@@@@@@@@@@@@@@@@@@      
              @@@@@@@@@@@@@@@@@@@@@@      
               @@@@@@@@@@@@@@@@@@@@       
               @@@@@@@@@@@@@@@@@@@@       
                @@@@@@@@@@@@@@@@@@@       
                @@@@@@@@@@@@@@@@@@        
                @@@@@@@@@@@@@@@@@@        
                 @@@@@@@@@@@@@@@@ 
    """, """
                          @@@@@@@@@@
                        @@@@@@@         
                        @@@@@@ 
                        @@@@@  
                      @@@@@@@@@@
                   @@@@@@@@@@@@@@@              
                 @@@@@@@@@@@@@@@@@@            
               @@@@@@@@@@@@@@@@@@@@@
              @@@@@@@@@@@@@@@@@@@@@@@     
             @@@@@@@@@@@@@@@@@@@@@@@@@             
            @@@@@@@@@@@@@@@@@@@@@@@@@@             
            @@@@@@@@@@@@@@@@@@@@@@@@@@                                                 
          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  
         @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ 
          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  
             @@@@@@@@@@@@@@@@@@@@@@@@     
             @@@@@@@@@@@@@@@@@@@@@@@@     
              @@@@@@@@@@@@@@@@@@@@@@@     
              @@@@@@@@@@@@@@@@@@@@@@      
              @@@@@@@@@@@@@@@@@@@@@@      
               @@@@@@@@@@@@@@@@@@@@       
               @@@@@@@@@@@@@@@@@@@@       
                @@@@@@@@@@@@@@@@@@@       
                @@@@@@@@@@@@@@@@@@        
                @@@@@@@@@@@@@@@@@@        
                 @@@@@@@@@@@@@@@@ 
    """, """
                          @@@@@@@@@@
                        @@@@@@@         
                        @@@@@@ 
                        @@@@@  
                      @@@@@@@@@@
                   @@@@@@@@@@@@@@@              
                 @@@@@@@@@@@@@@@@@@            
               @@@@@@@@@@@@@@@@@@@@@                                         
          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  
         @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ 
          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  
             @@@@@@@@@@@@@@@@@@@@@@@@     
             @@@@@@@@@@@@@@@@@@@@@@@@     
              @@@@@@@@@@@@@@@@@@@@@@@     
              @@@@@@@@@@@@@@@@@@@@@@      
              @@@@@@@@@@@@@@@@@@@@@@      
               @@@@@@@@@@@@@@@@@@@@       
               @@@@@@@@@@@@@@@@@@@@       
                @@@@@@@@@@@@@@@@@@@       
                @@@@@@@@@@@@@@@@@@        
                @@@@@@@@@@@@@@@@@@        
                 @@@@@@@@@@@@@@@@ 
    """, """
                          @@@@@@@@@@
                        @@@@@@@         
                        @@@@@@ 
                        @@@@@  
                      @@@@@@@@@@
                   @@@@@@@@@@@@@@@              
                 @@@@@@@@@@@@@@@@@@            
               @@@@@@@@@@@@@@@@@@@@@                                    
          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  
         @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ 
          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  
             @@@@@@@@@@@@@@@@@@@@@@@@     
             @@@@@@@@@@@@@@@@@@@@@@@@     
              @@@@@@@@@@@@@@@@@@@@@@@     
              @@@@@@@@@@@@@@@@@@@@@@      
              @@@@@@@@@@@@@@@@@@@@@@      
               @@@@@@@@@@@@@@@@@@@@       
               @@@@@@@@@@@@@@@@@@@@       
                @@@@@@@@@@@@@@@@@@@       
                @@@@@@@@@@@@@@@@@@        
                @@@@@@@@@@@@@@@@@@        
                 @@@@@@@@@@@@@@@@ 
    """, """
                          @@@@@@@@@@
                        @@@@@@@         
                        @@@@@@ 
                        @@@@@  
                      @@@@@@@@@@
                   @@@@@@@@@@@@@@@              
                 @@@@@@@@@@@@@@@@@@                                                 
          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  
         @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ 
          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  
             @@@@@@@@@@@@@@@@@@@@@@@@     
             @@@@@@@@@@@@@@@@@@@@@@@@     
              @@@@@@@@@@@@@@@@@@@@@@@     
              @@@@@@@@@@@@@@@@@@@@@@      
              @@@@@@@@@@@@@@@@@@@@@@      
               @@@@@@@@@@@@@@@@@@@@       
               @@@@@@@@@@@@@@@@@@@@       
                @@@@@@@@@@@@@@@@@@@       
                @@@@@@@@@@@@@@@@@@        
                @@@@@@@@@@@@@@@@@@        
                 @@@@@@@@@@@@@@@@ 
    """, """
                          @@@@@@@@@@
                        @@@@@@@         
                        @@@@@@ 
                        @@@@@  
                      @@@@@@@@@@
                   @@@@@@@@@@@@@@@                                                   
          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  
         @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ 
          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  
             @@@@@@@@@@@@@@@@@@@@@@@@     
             @@@@@@@@@@@@@@@@@@@@@@@@     
              @@@@@@@@@@@@@@@@@@@@@@@     
              @@@@@@@@@@@@@@@@@@@@@@      
              @@@@@@@@@@@@@@@@@@@@@@      
               @@@@@@@@@@@@@@@@@@@@       
               @@@@@@@@@@@@@@@@@@@@       
                @@@@@@@@@@@@@@@@@@@       
                @@@@@@@@@@@@@@@@@@        
                @@@@@@@@@@@@@@@@@@        
                 @@@@@@@@@@@@@@@@ 
    """, """
                          @@@@@@@@@@
                        @@@@@@@         
                        @@@@@@ 
                        @@@@@  
                      @@@@@@@@@@                                     
          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  
         @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ 
          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  
             @@@@@@@@@@@@@@@@@@@@@@@@     
             @@@@@@@@@@@@@@@@@@@@@@@@     
              @@@@@@@@@@@@@@@@@@@@@@@     
              @@@@@@@@@@@@@@@@@@@@@@      
              @@@@@@@@@@@@@@@@@@@@@@      
               @@@@@@@@@@@@@@@@@@@@       
               @@@@@@@@@@@@@@@@@@@@       
                @@@@@@@@@@@@@@@@@@@       
                @@@@@@@@@@@@@@@@@@        
                @@@@@@@@@@@@@@@@@@        
                 @@@@@@@@@@@@@@@@ 
    """, """
                          @@@@@@@@@@
                        @@@@@@@         
                        @@@@@@ 
                        @@@@@                                      
          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  
         @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ 
          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  
             @@@@@@@@@@@@@@@@@@@@@@@@     
             @@@@@@@@@@@@@@@@@@@@@@@@     
              @@@@@@@@@@@@@@@@@@@@@@@     
              @@@@@@@@@@@@@@@@@@@@@@      
              @@@@@@@@@@@@@@@@@@@@@@      
               @@@@@@@@@@@@@@@@@@@@       
               @@@@@@@@@@@@@@@@@@@@       
                @@@@@@@@@@@@@@@@@@@       
                @@@@@@@@@@@@@@@@@@        
                @@@@@@@@@@@@@@@@@@        
                 @@@@@@@@@@@@@@@@ 
    """, """
                          @@@@@@@@@@
                        @@@@@@@                                             
          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  
         @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ 
          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  
             @@@@@@@@@@@@@@@@@@@@@@@@     
             @@@@@@@@@@@@@@@@@@@@@@@@     
              @@@@@@@@@@@@@@@@@@@@@@@     
              @@@@@@@@@@@@@@@@@@@@@@      
              @@@@@@@@@@@@@@@@@@@@@@      
               @@@@@@@@@@@@@@@@@@@@       
               @@@@@@@@@@@@@@@@@@@@       
                @@@@@@@@@@@@@@@@@@@       
                @@@@@@@@@@@@@@@@@@        
                @@@@@@@@@@@@@@@@@@        
                 @@@@@@@@@@@@@@@@ 
    """, """
                          @@@@@@@@@@
                        @@@@@@@                                             
          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  
         @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ 
          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  
             @@@@@@@@@@@@@@@@@@@@@@@@     
             @@@@@@@@@@@@@@@@@@@@@@@@     
              @@@@@@@@@@@@@@@@@@@@@@@     
              @@@@@@@@@@@@@@@@@@@@@@      
              @@@@@@@@@@@@@@@@@@@@@@      
               @@@@@@@@@@@@@@@@@@@@       
               @@@@@@@@@@@@@@@@@@@@       
                @@@@@@@@@@@@@@@@@@@       
                @@@@@@@@@@@@@@@@@@        
                @@@@@@@@@@@@@@@@@@        
                 @@@@@@@@@@@@@@@@ 
    """, """
                          @@@@@@@@@@                                    
          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  
         @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ 
          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  
             @@@@@@@@@@@@@@@@@@@@@@@@     
             @@@@@@@@@@@@@@@@@@@@@@@@     
              @@@@@@@@@@@@@@@@@@@@@@@     
              @@@@@@@@@@@@@@@@@@@@@@      
              @@@@@@@@@@@@@@@@@@@@@@      
               @@@@@@@@@@@@@@@@@@@@       
               @@@@@@@@@@@@@@@@@@@@       
                @@@@@@@@@@@@@@@@@@@       
                @@@@@@@@@@@@@@@@@@        
                @@@@@@@@@@@@@@@@@@        
                 @@@@@@@@@@@@@@@@ 
    """, """                                    
          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  
         @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ 
          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  
             @@@@@@@@@@@@@@@@@@@@@@@@     
             @@@@@@@@@@@@@@@@@@@@@@@@     
              @@@@@@@@@@@@@@@@@@@@@@@     
              @@@@@@@@@@@@@@@@@@@@@@      
              @@@@@@@@@@@@@@@@@@@@@@      
               @@@@@@@@@@@@@@@@@@@@       
               @@@@@@@@@@@@@@@@@@@@       
                @@@@@@@@@@@@@@@@@@@       
                @@@@@@@@@@@@@@@@@@        
                @@@@@@@@@@@@@@@@@@        
                 @@@@@@@@@@@@@@@@ 
    """]
    for frame in range(len(garbage_animation)):
        print(garbage_animation[frame])
        time.sleep(0.2)



def lightsaber_duel():
    print("Initiating Lightsaber Duel...\n")
    time.sleep(1)
    print("Loading characters...")
    time.sleep(1)
    print("Initializing battle scene...")
    time.sleep(1)
    print("Press 'Enter' to start the duel!\n")
    input("Press Enter to continue...")

    character1_frames = [
        r"""
          O-|
            |
          / \
        """,
        r"""
          O-|
         \|
          / \
        """,
        r"""
          O-|
         \|/
          / \
        """,
        r"""
          O-|
         \|
          / \
        """,
        r"""
          O-|
         /|
          / \
        """,
        r"""
          O-|
         /|
        |  / \
        """,
        r"""
          O-|
        / |
        |  / \
        """,
        r"""
          O-|
          |
          |  / \
        """,
        r"""
          O-|
          |
          |  / \
        """,
        r"""
          O-|
          |
          |  / \
        """,
        r"""
          O-|
          |
          |  / \
        """,
    ]

    character2_frames = [
        r"""
          |-O
            |
          / \
        """,
        r"""
          |-O
           |/
          / \
        """,
        r"""
          |-O
           |/
          / \
        """,
        r"""
          |-O
           |/
          / \
        """,
        r"""
          |-O
          \|
          / \
        """,
        r"""
          |-O
          \|
        |  / \
        """,
        r"""
          |-O
         \  |
        |  / \
        """,
        r"""
          |-O
         \  |
          |  / \
        """,
        r"""
          |-O
         \  |
          |  / \
        """,
        r"""
          |-O
          |  \
          |  / \
        """,
        r"""
          |-O
          |  \
          |  / \
        """,
    ]

    # Lightsaber sound effect
    def lightsaber_sound():
        sys.stdout.write("\033[K")  # Clear line
        sys.stdout.write("\r" + " " * 30 + "\r")  # Clear the line
        sys.stdout.flush()
        print("\a", end="")  # Beep sound

    print("\n\nLET THE DUEL BEGIN!\n\n")

    for i in range(11):
        sys.stdout.write("\033[F" * 10)  # Move cursor up 10 lines
        sys.stdout.flush()
        print(character1_frames[i])
        print(character2_frames[i])
        lightsaber_sound()  # Play lightsaber sound
        time.sleep(0.2)

    print("\nThe duel has ended.\n\n")


fireworks = r"""
  __    __    __
//  \\//  \\//  \\
\\__//\\__//\\__//
"""

game_over = r"""
   ____                                          _ 
  / ___|___  _ __ ___  _ __ ___   __ _ _ __   __| |
 | |   / _ \| '_ ` _ \| '_ ` _ \ / _` | '_ \ / _` |
 | |__| (_) | | | | | | | | | | | (_| | | | | (_| |
  \____\___/|_| |_| |_| |_| |_| |_|\__,_|_| |_|\__,_|
   ____                      _      _              
  / ___|___  _ __ ___  _ __ | | ___| |_ ___        
 | |   / _ \| '_ ` _ \| '_ \| |/ _ \ __/ _ \       
 | |__| (_) | | | | | | |_) | |  __/ ||  __/       
  \____\___/|_| |_| |_| .__/|_|\___|\__\___|       
                      |_|                          
    """



def clear_screen():
    print("\033[H\033[J")



def print_shaky_text(text):
    lines = text.split("\n")
    clear_screen()
    for line in lines:
        # Randomly offset the position horizontally and vertically
        horizontal_offset = random.randint(-2, 2)
        vertical_offset = random.randint(-1, 1)
        # Print the line with the offsets
        print(" " * (40 + horizontal_offset) + line)
    time.sleep(0.05)



# Shake effect loop
def welcome_screen():
    # Animated welcome message
    print("Welcome to Your Contact Manager!\n")
    time.sleep(0.5)
    print("Loading modules...")
    time.sleep(0.5)
    sys.stdout.write("\r" + " " * 30 + "\r")
    sys.stdout.flush()
    time.sleep(0.5)
    print("Initializing system...")
    time.sleep(0.5)
    sys.stdout.write("\r" + " " * 30 + "\r")
    sys.stdout.flush()
    time.sleep(0.5)
    print("Preparing interface...")
    time.sleep(0.5)
    sys.stdout.write("\r" + " " * 30 + "\r")
    sys.stdout.flush()
    time.sleep(0.5)
    print("Welcome Screen Ready!\n")
    time.sleep(0.5)



avatars = [
    """
       ____
     /     \\
    |  00  |
    | |__| |
     \\_____/
    """,
    """
       ____
     /     \\
    |  ^^  |
    | |  | |
     \\_____/
    """,
    """
       ____
     /     \\
    |  **  |
    | |  | |
     \\_____/
    """,
    """
       ____
     /     \\
    |  @@  |
    | |__| |
     \\_____/
    """, option_5, option_6
]


def animate_avatar(avatar):
    for frame in avatar.split("\n\n"):
        print(frame)
        time.sleep(0.3)  # Adjust the delay as needed



def animate_text(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.05)  # Adjust the delay as needed
    print()



def animate_movement(text):
    for _ in range(5):
        sys.stdout.write("\r" + " " * 30 + "\r")  # Clear the line
        sys.stdout.write(text)
        sys.stdout.flush()
        time.sleep(0.2)  # Adjust the delay as needed
        text = text[-1] + text[:-1]  # Rotate the text
    sys.stdout.write("\r" + " " * 30 + "\r")  # Clear the line
    sys.stdout.flush()



def load_contacts_from_file(username):
    contacts = {}
    filename = CONTACT_FILE_TEMPLATE.format(username)
    try:
        with open(filename, mode='r') as file:
            for line in file:
                name, number, profile_picture, *ascii_art = line.strip().split(',')
                if profile_picture.isdigit():
                    index = int(profile_picture) - 1
                    if 0 <= index < len(avatars):
                        ascii_art = avatars[index]
                    else:
                        ascii_art = ""  # Default to empty if index is out of range
                else:
                    ascii_art = "\n".join(ascii_art) if ascii_art else ""
                contacts[name] = {
                    'number': number,
                    'profile_picture': profile_picture,
                    'ascii_art': ascii_art.replace('\\n', '\n')
                }
    except FileNotFoundError:
        pass
    except ValueError as e:
        print(f"Error processing line: {line}. Error: {e}")
    return contacts







def save_contacts_to_file(username, contacts):
    filename = CONTACT_FILE_TEMPLATE.format(username)
    with open(filename, mode='w') as file:
        for name, contact_info in contacts.items():
            profile_picture = contact_info['profile_picture']
            ascii_art = contact_info.get('ascii_art', '').replace('\n', '\\n')  # Replace newlines with \n for saving
            file.write(f"{name},{contact_info['number']},{profile_picture},{ascii_art}\n")


def view_all_contacts(contacts):
    if not contacts:
        print("No contacts to view.")
        return

    animate_movement("Loading contacts...")
    time.sleep(1)

    while True:
        try:
            command = int(
                input("Would you like to view your contacts in horizontal view(1) or vertical view(2): ")
            )
            if command == 1:
                # Horizontal view: display contacts in a single line
                for name, contact_info in contacts.items():
                    print(f"Name: {name}, Number: {contact_info['number']}, Profile Picture: ")
                    animate_avatar(contact_info['ascii_art'])
                break
            elif command == 2:
                # Vertical view: display contacts one by one
                for name, contact_info in contacts.items():
                    print(f"Name: {name}\nNumber: {contact_info['number']}\nProfile Picture: ")
                    animate_avatar(contact_info['ascii_art'])
                break
            else:
                print("Invalid input. Please enter 1 for horizontal view or 2 for vertical view.")
        except ValueError:
            print("Invalid input. Please enter a number.")



def view_contact(contacts):
    if not contacts:
        print("No contacts available to search.")
        return

    animate_movement("Searching for contact...")
    time.sleep(1)

    contact_found = False
    search_name = input("Enter the contact's name: ").strip()

    for name, contact_info in contacts.items():
        if search_name.lower() == name.lower():
            print(f"Name: {name}\nNumber: {contact_info['number']}\nProfile Picture: ")
            animate_avatar(contact_info['ascii_art'])
            contact_found = True
            break

    if not contact_found:
        print("Contact not found.")
        print("Did you try the add contact function?")
    else:
        print("Contact found.")




def add_contact(username, contacts):
    animate_movement("Preparing to add contact...")
    time.sleep(1)

    # Get contact name
    while True:
        name = input("What is the contact's name (First name Last name): ").strip()
        if name.lower() in [contact.lower() for contact in contacts.keys()]:
            print("Contact already exists.")
        else:
            break

    # Get contact phone number
    print("Proceeding to phone number")
    while True:
        number = input("Enter the contact's phone number: ").strip()
        if number.replace(" ", "").isdigit():  # Checking if the input contains only digits
            break
        else:
            print("Invalid phone number. Please enter again.")

    # Display avatar options
    for i, avatar in enumerate(avatars, start=1):
        print(f"Option {i}:\n{avatar}")
        time.sleep(0.3)  # Add a delay of 0.3 seconds between each avatar frame

    # Get profile picture choice
    profile_picture = input("Enter your choice (1/2/3/4/5/6/7 for Custom): ").strip().lower()

    if profile_picture == "7":
        image_url = input("Enter an image URL for the contact: ").strip()
        filename = "".join(random.choices("0123456789", k=25)) + ".png"
        file_path = os.path.join(UPLOAD_DIR, filename)

        try:
            response = requests.get(image_url)
            response.raise_for_status()  # Check for HTTP errors

            with open(file_path, "wb") as upload:
                upload.write(response.content)

            ascii_art = climage.convert(file_path, is_unicode=True, width=20)
            os.unlink(file_path)  # Clean up the uploaded image file
        except (requests.exceptions.RequestException, PIL.UnidentifiedImageError, FileNotFoundError) as e:
            print(f"Error handling the image: {e}")
            ascii_art = ""
    else:
        try:
            profile_picture_index = int(profile_picture) - 1
            if 0 <= profile_picture_index < len(avatars):
                ascii_art = avatars[profile_picture_index]
            else:
                print("Invalid choice. Setting to default avatar.")
                ascii_art = avatars[0]
        except ValueError:
            print("Invalid input. Setting to default avatar.")
            ascii_art = avatars[0]

    contacts[name] = {
        'number': number,
        'profile_picture': profile_picture,
        'ascii_art': ascii_art,
    }

    save_contacts_to_file(username, contacts)
    print("Contact added successfully.")



def update_contact(username, contacts):
    animate_movement("Preparing to update contact...")
    time.sleep(1)
    command = input("Which contact would you like to change: ")

    if command not in contacts:
        print("Contact not found.")
        return

    original_contact = contacts[command]
    new_name = command
    new_number = original_contact['number']
    new_ascii_art = original_contact['ascii_art']
    
    # Change name
    if input("Press Enter to edit the name, or any other key to skip: ") == "":
        new_name = input(f"Change {command} to what? ").strip()
        if new_name.lower() in [name.lower() for name in contacts.keys()]:
            print("Contact with that name already exists.")
            merge_option = input("Do you want to merge contacts (Y/N)? ").lower()
            if merge_option == "y":
                contacts[new_name] = contacts.pop(command)
                print(f"The name {command} is now merged with {new_name}")
                save_contacts_to_file(username, contacts)
                return
            else:
                print("Operation aborted. Choose a different name.")
                return
        else:
            contacts[new_name] = contacts.pop(command)
            print(f"The name {command} is now set to {new_name}")

    # Change phone number
    if input("Press Enter to edit the phone number, or any other key to skip: ") == "":
        while True:
            new_number = input(f"Change {contacts[new_name]['number']} to what? ").strip()
            if new_number.replace(" ", "").isdigit():
                contacts[new_name]['number'] = new_number
                print(f"The phone number {contacts[new_name]['number']} is now set to {new_number}")
                break
            else:
                print("Invalid phone number. Please enter again.")

    save_contacts_to_file(username, contacts)



def remove_contact(username, contacts):
    throwing_out_the_trash()
    animate_movement("Preparing to remove contact...")
    time.sleep(1)
    command = input("Which contact would you like to remove: ")
    if command in contacts:
        removed_contact = contacts.pop(command)
        save_contacts_to_file(username, contacts)
        print(f"Contact '{command}', Number: {removed_contact['number']} has been removed")
    else:
        print("Contact not found.")



def options():
    while True:
        try:
            choice = int(
                input(
                    """\
(1) View All Contacts
(2) View Contact
(3) Add Contact
(4) Update Contact
(5) Remove Contact
(6) Add image
(7) Exit
Enter your choice: """
                )
            )
            return choice
        except ValueError:
            print("Invalid input. Please enter a number.")



def load_users():
    users = {}
    try:
        with open(USER_FILE, mode='r') as file:
            for line in file:
                username, password = line.strip().split(',')
                users[username] = password
    except FileNotFoundError:
        pass
    return users


def save_users(users):
    with open(USER_FILE, mode='w') as file:
        for username, password in users.items():
            file.write(f"{username},{password}\n")


def login(users):
    while True:
        username = input("Enter your username: ")
        if username in users:
            password = getpass.getpass("Enter your password: ")
            if users[username] == password:
                print("Login successful!")
                return username
            else:
                print("Incorrect password. Try again.")
        else:
            print("Username not found. Try again.")


def create_account(users):
    while True:
        username = input("Choose a username: ")
        if username in users:
            print("Username already taken. Try again.")
        else:
            password = getpass.getpass("Choose a password: ")
            users[username] = password
            save_users(users)
            print("Account created successfully!")
            return username


def main():
    users = load_users()
    print("""
Contact Manager
    """)
    print("1. Login")
    print("2. New Account")
    
    choice = input("> ")

    if choice == '1':
        username = login(users)
    elif choice == '2':
        username = create_account(users)
    else:
        print("Invalid choice.")
        return

    contacts = load_contacts_from_file(username)
    welcome_screen()

    while True:
        choice = options()
        if choice == 1:
            view_all_contacts(contacts)
        elif choice == 2:
            view_contact(contacts)
        elif choice == 3:
            add_contact(username, contacts)
        elif choice == 4:
            update_contact(username, contacts)
        elif choice == 5:
            remove_contact(username, contacts)
        elif choice == 6:
            add_image()
        elif choice == 7:
            break
        else:
            print(f"{choice} is not a valid option")

    lightsaber_duel()
    for i in range(0, 30):
        print_shaky_text(game_over)
        time.sleep(0.2)


if __name__ == "__main__":
    main()
