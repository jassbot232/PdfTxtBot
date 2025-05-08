import os
from dotenv import load_dotenv
TOKEN = "7886020131:AAFzmV-oIbKY8YvV7RazvqHAt5Jzwm4svK0"

def gettoken():
    global TOKEN
    load_dotenv("config.env")
    TOKEN = os.environ.get("TOK")

gettoken()
if TOKEN == None:
    token = input("Please enter the TOKEN\nGenerated from Botfather : ")
    with open("config.env", "w") as f:
        f.write(f"TOK={token}")
    gettoken()
