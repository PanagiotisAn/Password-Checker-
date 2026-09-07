import os
import sys

# ANSI Color Codes
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"

def banner():
    print(" (                                                                       ")
    print(" )\\ )                           (        (      )            )           ")
    print("(()/(   )       (  (       (    )\\ )     )\\  ( /(   (     ( /(   (  (    ")
    print(" /(_)| /( (  (  )\\))(   (  )(  (()/(   (((_) )\\()) ))\\ (  )\\()) ))\\ )(   ")
    print("(_)) )(_)))\\ )\\((_)()\\  )\\(()\\  ((_))  )\\___((_)\\ /((_))\\((_)\\ /((_|()\\  ")
    print("| _ ((_)_((_|(_)(()((_)((_)((_) _| |  ((/ __| |(_|_)) ((_) |(_|_))  ((_) ")
    print("|  _/ _` (_-<_-< V  V / _ \\ '_/ _` |   | (__| ' \\/ -_) _|| / // -_)| '_| ")
    print("|_| \\__,_/__/__/\\_/\\_/\\___/_| \\__,_|    \\___|_||_\\___\\__||_\\_\\\\___||_|")
    print("")
    print("")
def clear_screen():
    os.system("clear" if os.name == "posix" else "cls")

def main():
    banner()
    flag = True
    while flag:
        password = input("put your password here: ")
        print(f"your password is: {RED}{password}{RESET}")
        mhkos = len(password)

        if mhkos < 12:
            print(f"{YELLOW}Weak Password{RESET}")
            continue
        else:
            lexh = 0
            for word in password:
                if word == '@':
                    lexh += 1
                elif word == '#':
                    lexh += 1
                elif word == '!':
                    lexh += 1
                elif word == '$':
                    lexh += 1
                elif word == '%':
                    lexh += 1
                elif word == '^':
                    lexh += 1
                elif word == '*':
                    lexh += 1

            if lexh > 2:
                print(f"{GREEN}Your Password is Strong GJ!!{RESET}")
                flag = False
            else:
                print(f"{YELLOW}Your password has strong length but not many special codes{RESET}\nSpecial codes: {lexh}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{CYAN}[*] Exiting...{RESET}")
        sys.exit(0)
