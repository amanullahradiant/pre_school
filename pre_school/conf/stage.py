from .common import *
import os

# import environ
# # Initialise environment variables
# env = environ.Env()
# environ.Env.read_env()

from dotenv import load_dotenv
load_dotenv()

SECRET_KEY=os.environ.get('SECRET_KEY')
DEBUG=os.environ.get('DEBUG')
ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS').split(" ")
