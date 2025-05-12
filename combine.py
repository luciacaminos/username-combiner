import shutil
import random
import os
import pyperclip
from colorama import Fore, Style, init
from InquirerPy import inquirer
import subprocess
import sys

# Fonction pour vérifier et installer les dépendances si nécessaire
def install_requirements():
    try:
        import pyperclip
        import colorama
        import InquirerPy
    except ImportError:
        print(Fore.RED + "🔴 Missing required packages. Installing now...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", 'pyperclip', 'colorama', 'InquirerPy'])
        print(Fore.GREEN + "✔ Packages installed successfully. Restarting the program...")
        sys.exit()  # Quitter pour que le script redémarre après l'installation

install_requirements()  # Vérifier et installer les packages nécessaires

init(autoreset=True)

def center_text(text, color=Fore.WHITE):
    terminal_width = shutil.get_terminal_size().columns
    return color + text.center(terminal_width)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def advanced_combine(user1, user2):
    cut1 = random.randint(1, len(user1)-1) if len(user1) > 1 else 1
    cut2 = random.randint(1, len(user2)-1) if len(user2) > 1 else 1
    part1 = user1[:cut1]
    part2 = user2[cut2:]

    if part1 and part2 and part1[-1].lower() == part2[0].lower():
        part2 = part2[1:]
    return part1 + part2

def apply_style(pseudo, style):
    if style == "Normal":
        return pseudo
    elif style == "Uppercase":
        return pseudo.upper()
    elif style == "Lowercase":
        return pseudo.lower()
    elif style == "Soft Fantasy":
        table = str.maketrans(
            "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
            "𝒶𝒷𝒸𝒹𝑒𝒻𝑔𝒽𝒾𝒿𝓀𝓁𝓂𝓃𝑜𝓅𝓆𝓇𝓈𝓉𝓊𝓋𝓌𝓍𝓎𝓏"
            "𝒜𝐵𝒞𝒟𝐸𝐹𝒢𝐻𝐼𝒻𝒿𝓀𝓁𝓂𝓃𝑜𝒫𝓆𝓇𝓈𝓉𝓊𝓋𝓌𝓍𝓎𝓏"
        )
        return pseudo.translate(table)
    elif style == "L33t sp34k":
        translation = str.maketrans("aeiost", "43105+")
        return pseudo.translate(translation)
    elif style == "Strikethrough":
        return ''.join([c + '\u0336' for c in pseudo])
    elif style == "Shadow":
        return ''.join([c + ' ' for c in pseudo])
    elif style == "Italic":
        table = str.maketrans(
            "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
            "𝑎𝑏𝑐𝑑𝑒𝑓𝑔𝑕𝑖𝑗𝑘𝑙𝑚𝑛𝑜𝑝𝑞𝑟𝑠𝑡𝑢𝑣𝑤𝑥𝑦𝑧"
            "𝐴𝐵𝐶𝐷𝐸𝐹𝐺𝐻𝐼𝑱𝐾𝐿𝑀𝑁𝑂𝑃𝑄𝑅𝑆𝑇𝑈𝑉𝑊𝑋𝑌𝑍"
        )
        return pseudo.translate(table)
    elif style == "Underline":
        return ''.join([c + '\u0332' for c in pseudo])
    else:
        return pseudo

def style_selector():
    styles = [
        "Normal",
        "Uppercase",
        "Lowercase",
        "Soft Fantasy",
        "L33t sp34k",
        "Strikethrough",
        "Shadow",
        "Italic",
        "Underline"
    ]
    selected = inquirer.select(
        message="🎨 Choose a style for your username:",
        choices=styles,
        pointer=">"
    ).execute()
    return selected

def show_copyright():
    clear()
    print(center_text("╔════════════════════════════════╗", Fore.CYAN))
    print(center_text("║        Copyright & Credits     ║", Fore.CYAN))
    print(center_text("╚════════════════════════════════╝", Fore.CYAN))
    print()
    print(center_text("Created by: luciacaminos", Fore.MAGENTA))
    print(center_text("GitHub: https://github.com/luciacaminos", Fore.GREEN))
    print(center_text("Discord: 6de6", Fore.BLUE))
    print(center_text("Free to use — Just for fun :3", Fore.YELLOW))
    print()
    input(Fore.BLUE + "↩ Press Enter to return to the menu...")

def menu():
    while True:
        clear()
        print(center_text("╔══════════════════════════════════════╗", Fore.CYAN))
        print(center_text("║          username combiner           ║", Fore.CYAN))
        print(center_text("╚══════════════════════════════════════╝", Fore.CYAN))
        print()
        print(center_text("[1] Combine two usernames", Fore.YELLOW))
        print(center_text("[2] Show Copyright", Fore.YELLOW))
        print(center_text("[3] Quit", Fore.YELLOW))
        print()

        choice = input(Fore.GREEN + "→ Choose an option (1, 2 or 3): ").strip()

        if choice == '1':
            clear()
            print(center_text("🎨 CREATIVE COMBINATION 🎨", Fore.MAGENTA))
            print()
            pseudo1 = input(Fore.CYAN + "• First username: ")
            pseudo2 = input(Fore.CYAN + "• Second username: ")
            print()

            combined = advanced_combine(pseudo1, pseudo2)
            style = style_selector()
            styled_result = apply_style(combined, style)

            pyperclip.copy(styled_result)

            print()
            print(center_text("✨ Your styled username:", Fore.GREEN))
            print(center_text(f">>> {styled_result} <<<", Fore.LIGHTWHITE_EX + Style.BRIGHT))
            print()
            print(Fore.LIGHTBLACK_EX + "(Automatically copied to clipboard)")
            print()
            input(Fore.BLUE + "↩ Press Enter to return to the menu...")
        elif choice == '2':
            show_copyright()
        elif choice == '3':
            print()
            print(center_text("Thanks for using the Username Combiner 💫 See you soon!", Fore.LIGHTMAGENTA_EX))
            break
        else:
            print(Fore.RED + "⛔ Invalid option. Try again.")
            input("↩ Press Enter to try again...")

if __name__ == "__main__":
    menu()
