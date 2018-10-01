# -*- coding: utf-8 -*-

"""
    settings.base
    ~~~~~~~~~~~~~
    Base settings for the app.
"""

# stdlib
import os  # NOQA
from typing import Optional

# 3rd party
import envkey  # NOQA
from molten import Settings

# Project
from smpa.helpers.console import console


class EnvSettings:

    """Base settings object.
    """

    settings: dict = {}

    def get_settings(self, env: str) -> Settings:
        """Returns a Settings object to be passed to the SettingsComponent in the
        app factory. The settings object is built by calling the method matching
        the passed in env var so that different settings can be used on different
        environments.

        Args:
            env (str): The environment we're running in

        Returns:
            Settings: The settings object
        """
        db_name: Optional[str] = os.environ.get('POSTGRES_DB', None)
        db_user: Optional[str] = os.environ.get('POSTGRES_USER', None)
        db_pass: Optional[str] = os.environ.get('POSTGRES_PASSWORD', None)
        db_host: Optional[str] = os.environ.get('POSTGRES_HOST', None)
        dsn: str = f"postgresql+psycopg2://{ db_user }:{ db_pass }@{ db_host }/{ db_name }"

        self.settings['database_engine_dsn'] = dsn

        if hasattr(self, env) and callable(getattr(self, env)):
            try:
                meth = getattr(self, env)
                meth(self.settings)
            except Exception as e:
                console.error('Failed to call the settings env')
                raise

        return Settings(self.settings)

    def development(self, settings: dict) -> None:
        """Add development server settings here.
        """
        console.info('Running with development settings')
        settings['debug'] = True

    def staging(self, settings: dict) -> None:
        """Add staging server settings here.
        """
        settings['debug'] = False

    def production(self, settings: dict) -> None:
        """Add production server settings here.
        """
        settings['debug'] = False
