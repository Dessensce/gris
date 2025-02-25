import webbrowser
import time

print("Welcome to Gris Launcher\n1 to Launch Program\n2 to Open Documentation\n3 to Check for Updates")
numinput = input()

if numinput == "1":
    print("Exit Code: Status -1")
elif numinput == "2":
    print("Opening..")
    webbrowser.open_new_tab("https://example.com")
elif numinput == "3":
    print("Please Stand By.")
    time.sleep(5)
    print("Contacting Server.")
    time.sleep(4)
    print("Error Contacting Server: 404")