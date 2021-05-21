from python_settings import settings
from connect_four import ConnectFour

# Initialize settings.py as environment variable
import os
os.environ["SETTINGS_MODULE"] = 'settings' 

def replay() -> bool:
    play_again_input = None

    while play_again_input != "yes" and play_again_input != "no":
        play_again_input = input("Do you wish to play again? ('yes' or 'no'): ").lower()

    return play_again_input

def main():
    connect_four = ConnectFour(settings.HUMAN_PLAYER, settings.AI_PLAYER)
    is_playing = True

    while is_playing:
        connect_four.play()
        connect_four.display_game_results()
        connect_four.display_overall_results()
        
        play_again = replay()

        if play_again == "no":
            is_playing = False
        else:
            connect_four.restart()
        
    print("Thank you for playing!")

if __name__ == '__main__':
    main()