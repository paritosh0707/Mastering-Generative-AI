from dataclasses import dataclass
from DynamicPrompt.constants import *
from dotenv import load_dotenv
import os
import logging

load_dotenv()

@dataclass
class LoginCredentials:
    USERNAME:str = USERNAME
    TOKEN:str = os.getenv("TOKEN")
    SERVER:str = SERVER