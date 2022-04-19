import os
import environ

env = environ.Env()

environ.Env.read_env(env_file='./.env')

URL = env.str("URL", default="http://jservice.io/api/random?count=2")