import  os
from dotenv import find_dotenv, load_dotenv

DOT_PATH = find_dotenv() # this line work in in background finding the .env file whereever it is.
load_dotenv(DOT_PATH) 
print(F" .ENV_PATH :{DOT_PATH}")

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

print(f"YOUTUBE API KEY : {YOUTUBE_API_KEY}")
