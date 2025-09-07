baner_list = [
    r"""
 _______   _                  _          _____                     _    
|_   __ \ (_)                / |_       |_   _|                   / |_  
  | |__) |__   _ .--.  ,--. `| |-'.---.   | |       .--.    .--. `| |-' 
  |  ___/[  | [ `/'`\]`'_\ : | | / /__\\  | |   _ / .'`\ \/ .'`\ \| |   
 _| |_    | |  | |    // | |,| |,| \__., _| |__/ || \__. || \__. || |,  
|_____|  [___][___]   \'-;__/\__/ '.__.'|________| '.__.'  '.__.' \__/  
                                                                        """,

    r"""
8888888b.  d8b                 888            888                       888    
888   Y88b Y8P                 888            888                       888    
888    888                     888            888                       888    
888   d88P 888 888d888 8888b.  888888 .d88b.  888      .d88b.   .d88b.  888888 
8888888P"  888 888P"      "88b 888   d8P  Y8b 888     d88""88b d88""88b 888    
888        888 888    .d888888 888   88888888 888     888  888 888  888 888    
888        888 888    888  888 Y88b. Y8b.     888     Y88..88P Y88..88P Y88b.  
888        888 888    "Y888888  "Y888 "Y8888  88888888 "Y88P"   "Y88P"   "Y888 
                                                                               """,

    r"""
888~-_   ,e,                    d8             888                         d8   
888   \   "  888-~\   /~~~8e  _d88__  e88~~8e  888      e88~-_   e88~-_  _d88__ 
888    | 888 888          88b  888   d888  88b 888     d888   i d888   i  888   
888   /  888 888     e88~-888  888   8888__888 888     8888   | 8888   |  888   
888_-~   888 888    C888  888  888   Y888    , 888     Y888   ' Y888   '  888   
888      888 888     "88_-888  "88_/  "88___/  888____  "88_-~   "88_-~   "88_/ 
                                                                                """
]


def looting():
    print(r"""
                 _____
              .-" .-. "-.
            _/ '=(0.0)=' \_
          /`   .='|m|'=.   `\
          \________________ /
      .--.__///`'-,__~\\\\~`
     / /6|__\// a (__)-\\\\
     \ \/--`((   ._\   ,)))
     /  \\  ))\  -==-  (O)(
    /    )\((((\   .  /)))))
   /  _.' /  __(`~~~~`)__
  //"\\,-'-"`   `~~~~\\~~`"-.
 //  /`"              `      `\
// Art by 'https://ascii.co.uk/art/pirate'
""")


import os, sys
import random
import requests
import argparse
import time

from bs4 import BeautifulSoup

from colorama import Fore, Back, Style
fore_colors = {
	"black": Fore.BLACK,
	"red": Fore.RED,
	"green": Fore.GREEN,
	"yellow": Fore.YELLOW,
	"blue": Fore.BLUE,
	"magenta": Fore.MAGENTA,
	"cyan": Fore.CYAN,
	"white": Fore.WHITE,
	"reset": Fore.RESET
}

back_colors = {
	"black": Back.BLACK,
	"red": Back.RED,
	"green": Back.GREEN,
	"yellow": Back.YELLOW,
	"blue": Back.BLUE,
	"magenta": Back.MAGENTA,
	"cyan": Back.CYAN,
	"white": Back.WHITE,
	"reset": Back.RESET
}

styles = {
	"dim": Style.DIM,
	"normal": Style.NORMAL,
	"bright": Style.BRIGHT,
	"reset": Style.RESET_ALL
}

DUMP_LIST = ["pic", "text", "link"]

def datet():
    from datetime import datetime
    return datetime.today().date()

def save_output(file_path, content, url, mode, time_out):

    
    folder_output = "Output"
    if os.path.exists(folder_output):
        pass
    else:
        os.mkdir(folder_output)

    
    out = f"{folder_output}/{file_path}_{datet()}.txt"
    try:
        with open(out, 'w', encoding='utf-8') as f:
            f.write(f"{show_info(url, mode, time_out)}{datet()}\n\n\n{content}")
        print(f"\n  [{fore_colors['blue']}INFO{fore_colors['reset']}]-[{fore_colors['green']}${fore_colors['reset']}] Saved: {out}")
    except Exception as e:
        print(f"  [{fore_colors['red']}!{fore_colors['reset']}] Error: {e}")


def text_dump(soup):
    print(f"\n  [{fore_colors['blue']}INFO{fore_colors['reset']}]-[{fore_colors['yellow']}${fore_colors['reset']}] Dumping Text..")
    result = []
    try:
        full_text = soup.get_text(separator="\n", strip=True)
        if full_text:
                print("  -", full_text)
                result.append(full_text)
        return "\n".join(result)
    except Exception as e:
        print(f"  [{fore_colors['red']}!{fore_colors['reset']}] {e}")
    
def link_dump(soup):
    print(f"\n  [{fore_colors['blue']}INFO{fore_colors['reset']}]-[{fore_colors['yellow']}${fore_colors['reset']}] Dumping Links..")
    result = []
    try:
        for a in soup.find_all("a", href=True):
            print("  -", a["href"])
            result.append(a["href"])
        return "\n".join(result)
    except Exception as e:
        print(f"  [{fore_colors['red']}!{fore_colors['reset']}] {e}")

def img_dump(soup):
    print(f"\n  [{fore_colors['blue']}INFO{fore_colors['reset']}]-[{fore_colors['yellow']}${fore_colors['reset']}] Dumping Images..")
    result = []
    try:
        for img in soup.find_all("img", src=True):
            print("  -", img["src"])
            result.append(img["src"])
        return "\n".join(result)
    except Exception as e:
        print(f"  [{fore_colors['blue']}INFO{fore_colors['reset']}] {e}")

def dump_all(url, time_outt, mode):
    try:
        print(f"  [{fore_colors['blue']}INFO{fore_colors['reset']}]-[{fore_colors['yellow']}${fore_colors['reset']}] Start Dumping..")

        response = requests.get(url, timeout=time_outt)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")

        con_1 = text_dump(soup)
        time.sleep(2)
        con_2 = link_dump(soup)
        time.sleep(2)
        con_3 = img_dump(soup)
        time.sleep(2)

        contentt = f"{con_1}\n{con_2}\n{con_3}"

        domain = url.split("://")[1].split("/")[0]
        save_output(domain, contentt, url, mode, time_outt)
    except Exception as e:
        print(f"  [{fore_colors['red']}!{fore_colors['reset']}] Error while looting: {e}")


def show_banner():
    random_banner = random.choice(baner_list)
    print(random_banner)
    print("  Github: https://github.com/Faminee777xxx/PirateLoot")
    print("  Version: 1.0\n")
    

def show_help_menu():
    print(r"""
Options:
|-----------------------------------------------------
| -h                : Show Help Menu                 |
| -v, --version     : Show Version's tool            |
| -u, --url         : Target URL                     |
| -to, --time-out   : Time out          (default: 10)|
|-----------------------------------------------------
|+ Mode +                                            |
|-\ --dump-all      : Dump Everythings on url        |
|-\ --dump          : Dump only topics(Not Done yet) |
|                                                    |
|-----------------------------------------------------
""")

def show_info(url, mode, time_out):
    return f"""
  [{fore_colors['blue']}INFO{fore_colors['reset']}]
    +----------------------------------+
    -Target Url  : {url}
    -Time out    : {time_out}
    +-Mode
        -| {mode}
    +----------------------------------+
    """



# Main
def main():
    parser = argparse.ArgumentParser(description=show_banner(), add_help=False)
    parser.add_argument("--help-menu", required=False, action='store_true', dest="help_menu", help="Help Menu")
    parser.add_argument("-u", "--url", required=True, type=str, help="Target URL")
    parser.add_argument("-v","--version", action="version", version="==PirateLoot 1.0")

    # Dump
    parser.add_argument("--dump-all", required=True, action='store_true', default=False, help="Dump Everything on url page")

    # Time Out
    parser.add_argument("-to", "--time-out", required=False, default=10, type=int, help="Enter Time out (default: 10)")

    ar = parser.parse_args()
    help_menu = ar.help_menu
    target_url = ar.url
    dump_a = ar.dump_all
    time_out = ar.time_out

    if time_out:
        pass
    else:
        time_out = 10

    # Check
    if help_menu:
        show_help_menu()
        sys.exit(0)
    else:
        pass
    

    # Mode Checker
    if dump_a:
        mode = "Dump All"

    else:
        print(f"  [{fore_colors['red']}!{fore_colors['reset']}] Can't do anything T_T")
        time.sleep(2)
        print(f"  [{fore_colors['red']}!{fore_colors['reset']}] Please Use option (--dump-all or --dump)")
        sys.exit(0)
    

        
    show_info(target_url, mode, time_out)
    print(f"  [{fore_colors['blue']}INFO{fore_colors['reset']}] {styles['bright']}Time to Dump!{styles['reset']}")

    
    time.sleep(3)
    looting()
    time.sleep(2)
    if dump_a:
        dump_all(target_url, time_out, mode)


if __name__ == "__main__":
    main()
