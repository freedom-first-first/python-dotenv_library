import  os # a python library for dealing with environment variables and operating system
from dotenv import find_dotenv, load_dotenv 
#dotenv : a python library use to hide credentials.
# find_dotenv: find automatically a .env file in you project folder and  parents folder
# load_dotenv: load the variables inside the .env to memory so that the os.getenv can use get them.

DOT_PATH = find_dotenv() # this line work in in background finding the .env file whereever it is.
load_dotenv(DOT_PATH) 
print(F" .ENV_PATH :{DOT_PATH}")

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

print(f"YOUTUBE API KEY : {YOUTUBE_API_KEY}")
