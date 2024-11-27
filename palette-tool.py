import os
import subprocess
from colorama import Fore, Style, Back, init

# Initialize colorama
init(autoreset=True)

# Compact ASCII Art Banner
def print_ascii_banner():
    print(Fore.MAGENTA + Style.BRIGHT + """
   ███████╗ ██████╗██████╗  █████╗ ██████╗ ███████╗██████╗   
   ██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
   ███████╗██║     ██████╔╝███████║██████╔╝█████╗  ██████╔╝
   ╚════██║██║     ██╔══██╗██╔══██║██╔═══╝ ██╔══╝  ██╔══██╗
   ███████║╚██████╗██║  ██║██║  ██║██║     ███████╗██║  ██║
   ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝                                                                                   
    """ + Style.RESET_ALL)

# Menu options
def main_menu():
    print(Fore.MAGENTA + Style.BRIGHT + Back.BLACK + "\n╔══════════════════════════════════════════════════════════╗" + Style.RESET_ALL)
    print(Fore.MAGENTA + Style.BRIGHT + Back.BLACK + "║          █▓▒░ Pokémon Palette Scraper Tool ░▒▓█          ║" + Style.RESET_ALL)
    print(Fore.MAGENTA + Style.BRIGHT + Back.BLACK + "╚══════════════════════════════════════════════════════════╝" + Style.RESET_ALL)
    print(Fore.WHITE + Style.BRIGHT + "  1. " + Fore.LIGHTBLUE_EX + "Non-Shiny Scraping" + Style.RESET_ALL)
    print(Fore.WHITE + Style.BRIGHT + "  2. " + Fore.LIGHTYELLOW_EX + "Shiny Scraping" + Style.RESET_ALL)
    print(Fore.WHITE + Style.BRIGHT + "  3. " + Fore.LIGHTGREEN_EX + "Merge " + Fore.LIGHTBLUE_EX + "Non-Shiny " + Fore.WHITE + Style.BRIGHT + "and " + Fore.LIGHTYELLOW_EX + "Shiny " + Fore.WHITE + Style.BRIGHT + "Databases" + Style.RESET_ALL)
    print(Fore.WHITE + Style.BRIGHT + "  4. " + Fore.RED + Style.BRIGHT + "Exit" + Style.RESET_ALL)
    print(Fore.MAGENTA + Style.BRIGHT + Back.BLACK + "\n╔══════════════════════════════════════════════════════════╗" + Style.RESET_ALL)
    print(Fore.MAGENTA + Style.BRIGHT + Back.BLACK + "║              █▓▒░ Database File Status ░▒▓█              ║" + Style.RESET_ALL)
    print(Fore.MAGENTA + Style.BRIGHT + Back.BLACK + "╠══════════════════════════════════════════════════════════╣" + Style.RESET_ALL)
    # File status checks
    non_shiny_status = "[Present]" if os.path.exists('pokemon_palettes_base.db') else "[Missing]"
    shiny_status = "[Present]" if os.path.exists('pokemon_palettes_shiny.db') else "[Missing]"
    merged_status = "[Present]" if os.path.exists('pokemon_palettes_merged.db') else "[Missing]"
    
    print(Fore.CYAN + Style.BRIGHT + f"\n   {'Non-shiny DB:':<13} " + (Fore.GREEN if 'Present' in non_shiny_status else Fore.RED) + f"{non_shiny_status:<10} " + (Fore.YELLOW if 'Present' in non_shiny_status else Fore.CYAN) + "pokemon_palettes_base.db" + Style.RESET_ALL)
    print(Fore.CYAN + Style.BRIGHT + f"   {'Shiny DB:':<13} " + (Fore.GREEN if 'Present' in shiny_status else Fore.RED) + f"{shiny_status:<10} " + (Fore.YELLOW if 'Present' in shiny_status else Fore.CYAN) + "pokemon_palettes_shiny.db" + Style.RESET_ALL)
    print(Fore.CYAN + Style.BRIGHT + f"   {'Merge DB:':<13} " + (Fore.GREEN if 'Present' in merged_status else Fore.RED) + f"{merged_status:<10} " + (Fore.YELLOW if 'Present' in merged_status else Fore.CYAN) + "pokemon_palettes_merged.db" + Style.RESET_ALL)
    
    print(Fore.MAGENTA + Style.BRIGHT + Back.BLACK + "\n╠══════════════════════════════════════════════════════════╣" + Style.RESET_ALL)
    print(Fore.MAGENTA + Style.BRIGHT + Back.BLACK + "╚══════════════════════════════════════════════════════════╝" + Style.RESET_ALL)
    choice = input(Fore.LIGHTGREEN_EX + "\n  Select an option " + Fore.GREEN + "(1-4): " + Style.RESET_ALL)
    return choice

# Run non-shiny scraper
def run_non_shiny_scraper():
    print(Fore.CYAN + "\nRunning non-shiny scraper..." + Style.RESET_ALL)
    try:
        subprocess.run(["python", "scraper.py"], check=True)
        print(Fore.GREEN + "Non-shiny scraping completed successfully!" + Style.RESET_ALL)
    except subprocess.CalledProcessError as e:
        print(Fore.RED + f"Error running non-shiny scraper: {e}" + Style.RESET_ALL)

# Run shiny scraper
def run_shiny_scraper():
    print(Fore.CYAN + "\nRunning shiny scraper..." + Style.RESET_ALL)
    try:
        subprocess.run(["python", "shiny_scraper.py"], check=True)
        print(Fore.GREEN + "Shiny scraping completed successfully!" + Style.RESET_ALL)
    except subprocess.CalledProcessError as e:
        print(Fore.RED + f"Error running shiny scraper: {e}" + Style.RESET_ALL)

# Merge databases
def merge_databases():
    print(Fore.CYAN + "\nMerging non-shiny and shiny databases..." + Style.RESET_ALL)
    # Check if the required database files exist
    if not os.path.exists('pokemon_palettes_base.db'):
        print(Fore.RED + "Base database (pokemon_palettes_base.db) not found. Please run the non-shiny scraper first." + Style.RESET_ALL)
        return
    if not os.path.exists('pokemon_palettes_shiny.db'):
        print(Fore.RED + "Shiny database (pokemon_palettes_shiny.db) not found. Please run the shiny scraper first." + Style.RESET_ALL)
        return
    try:
        subprocess.run(["python", "pokemon_palette_db_merger.py"], check=True)
        print(Fore.GREEN + "Database merge completed successfully!" + Style.RESET_ALL)
    except subprocess.CalledProcessError as e:
        print(Fore.RED + f"Error merging databases: {e}" + Style.RESET_ALL)

# Main loop
if __name__ == "__main__":
    print_ascii_banner()
    while True:
        user_choice = main_menu()
        if user_choice == "1":
            run_non_shiny_scraper()
        elif user_choice == "2":
            run_shiny_scraper()
        elif user_choice == "3":
            merge_databases()
        elif user_choice == "4":
            print(Fore.MAGENTA + "Exiting the tool. Goodbye!" + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "Invalid option. Please select a valid option." + Style.RESET_ALL)
