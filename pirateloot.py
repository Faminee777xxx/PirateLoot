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
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
from datetime import datetime
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

def datet():
    return datetime.now().strftime("%Y%m%d-%H%M%S")


def domain(url):
    parsed = urlparse(url)
    return parsed.netloc or parsed.path.split("/")[0]
    

def save_output(file_path, content, url, time_out):

    
    folder_output = "Output"
    if os.path.exists(folder_output):
        pass
    else:
        os.mkdir(folder_output)

    
    out = f"{folder_output}/{file_path}_{datet()}.txt"
    try:
        with open(out, 'w', encoding='utf-8') as f:
            f.write(f"{show_info(url, time_out)}\n\n\n{content}")
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
    print(f"\n  [{fore_colors['blue']}INFO{fore_colors['reset']}]-[{fore_colors['yellow']}${fore_colors['reset']}] Dumping Link..")
    result = []
    try:
        for a in soup.find_all("a", href=True):
            print("  -", a["href"])
            result.append(a["href"])
        return "\n".join(result)
    except Exception as e:
        print(f"  [{fore_colors['red']}!{fore_colors['reset']}] {e}")


def download_img(url):
    folder_path = domain(url)
    full_folder = f"Output/{folder_path}/Img"
    os.makedirs(full_folder, exist_ok=True)

    file_name = url.split("/")[-1]
    save_path = os.path.join(full_folder, file_name)

    try:
        r = requests.get(url, stream=True)
        r.raise_for_status()

        with open(save_path, "wb") as f:
            for chunk in r.iter_content(1024):
                f.write(chunk)

        print(f"\n  [{fore_colors['blue']}INFO{fore_colors['reset']}]-[{fore_colors['yellow']}$${fore_colors['reset']}] Loot acquired! Saved: {styles['bright']}{save_path}{styles['reset']}")

    except Exception as e:
        print(f"\n  [{fore_colors['blue']}INFO{fore_colors['reset']}]-[{fore_colors['red']}!{fore_colors['reset']}] Failed to loot Image{url} → {e}")


def img_dump(soup, base_url, save_img):

    print(f"\n  [{fore_colors['blue']}INFO{fore_colors['reset']}]-[{fore_colors['yellow']}${fore_colors['reset']}] Dumping Image..")
    result = []
    try:
        for img in soup.find_all("img", src=True):
            img_url = img["src"]

            # relative path → absolute URL
            full_url = urljoin(base_url, img_url)

            print("  -", full_url)
            if save_img == True:

                download_img(full_url)
            result.append(full_url)

        return "\n".join(result)
    except Exception as e:
        print(f"  [{fore_colors['red']}!{fore_colors['reset']}] {e}")




def dump_all(url, time_outt, time_sleep, s_or_n):
    try:
        print(f"  [{fore_colors['blue']}INFO{fore_colors['reset']}]-[{fore_colors['yellow']}${fore_colors['reset']}] Start Dumping..")

        response = requests.get(url, timeout=time_outt)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")

        con_1 = text_dump(soup)
        time.sleep(time_sleep)
        con_2 = link_dump(soup)
        time.sleep(time_sleep)
        con_3 = img_dump(soup, url, s_or_n)
        time.sleep(time_sleep)

        contentt = f"[TEXT]\n{con_1}\n\n[LINKS]\n{con_2}\n\n[IMAGES]\n{con_3}"

        clean = domain(url)
        save_output(clean, contentt, url, time_outt)

    except Exception as e:
        print(f"  [{fore_colors['red']}!{fore_colors['reset']}] Error while looting: {e}")




def show_banner():
    random_banner = random.choice(baner_list)
    print(random_banner)
    print(f"  Github : {fore_colors['green']}https://github.com/Faminee777xxx/PirateLoot{fore_colors['reset']}")
    print(f"  Version: {fore_colors['green']}2.0{fore_colors['reset']}\n")
    

def show_help_menu():
    print(r"""
Options:
|----------------------------------------------------|
| -h                : Show Help Menu                 |
| -v, --version     : Show Version's tool            |
| -u, --url         : Target URL                     |
| -to, --time-out   : Time out          (default: 10)|
| -f, --fast        : Fast Mode                      |
| +Save                                              |
| -\ --save-img     : Save img as a file             |
|----------------------------------------------------|
""")

def show_info(url, time_out):
    return f"""
  [INFO]
    +----------------------------------+
    -Target Url  : {url}
    -Date        : {datet()}
    -Time out    : {time_out}
    +----------------------------------+
    """



# Main
def main():
    parser = argparse.ArgumentParser(description="PirateLoot!", add_help=False)
    parser.add_argument("-help", "--help-menu", required=False, action='store_true', dest="help_menu", help="Help Menu")
    parser.add_argument("-u", "--url", required=True, type=str, help="Target URL")
    parser.add_argument("-v","--version", action="version", version="==PirateLoot 1.0")

    parser.add_argument("--fast", "-f", required=False, action='store_true', help="Faster!")

    # Dump img
    parser.add_argument("--save-img", required=False, action='store_true', help="Save img in webpage")

    # Time Out
    parser.add_argument("-to", "--time-out", required=False, default=10, type=int, help="Enter Time out (default: 10)")

    ar = parser.parse_args()
    help_menu = ar.help_menu
    target_url = ar.url

    time_out = ar.time_out

    if ar.fast:
        time_out = 5
    else:
        time_out = ar.time_out

    # Check
    if help_menu:
        show_help_menu()
        sys.exit(0)
    else:
        pass
    

        
    print(show_info(target_url, time_out))
    print(f"  [{fore_colors['blue']}INFO{fore_colors['reset']}] {styles['bright']}Time to Dump!{styles['reset']}")

    if ar.fast:
        time_sleep = 0.5
    else:
        time_sleep = 2

    if ar.save_img:
        save_img_or_not = True
    else:
        save_img_or_not = False
    

    time.sleep(time_sleep)
    looting()
    time.sleep(time_sleep)
    
    dump_all(target_url, time_out, time_sleep, save_img_or_not)


if __name__ == "__main__":
    main()
