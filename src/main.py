from python_settings import settings
from connect_four import ConnectFour

# Initialize settings.py as environment variable
import os
os.environ["SETTINGS_MODULE"] = 'settings' 

def main():
    connect_four = ConnectFour(settings.HUMAN_PLAYER, settings.AI_PLAYER)
    is_playing = True

    while is_playing:
        connect_four.play()
        connect_four.display_winner()
        connect_four.display_overall_results()

        user_play_input = None

        while user_play_input != "yes" and user_play_input != "no":
            user_play_input = input("Do you wish to play again? ('yes' or 'no'): ").lower()

        if user_play_input == "no":
            is_playing = False
        else:
            connect_four.restart()
        
    print("Thank you for playing!")

if __name__ == '__main__':
    main()