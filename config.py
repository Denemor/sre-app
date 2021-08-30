import os
from flask_dotenv import DotEnv

search_paths = ['/vault/secrets/.env', './.env', './.env_template']


class Config:

    @staticmethod
    def vault_dotenv():
        for p in search_paths:
            if os.path.exists(p):
                print(f'Env file: {p}')
                return p
            return None

    @classmethod
    def init_app(cls, app, verbose_mode=True):
        env = DotEnv()
        env.init_app(app=app, env_file=cls.vault_dotenv(), verbose_mode=verbose_mode)
