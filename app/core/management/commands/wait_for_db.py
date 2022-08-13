"""
Django command to wait for db to be ready
"""

from typing import Any

from psycopg2 import OperationalError as Psycopg2Error

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand

import time


class Command(BaseCommand):
    """Djando Command to wait for db"""

    def handle(self, *args: Any, **options: Any):
        """Entry Point for command"""
        self.stdout.write("Waiting for database...")
        db_up = False

        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2Error, OperationalError):
                self.stdout.write("Database Unavailable waiting 1sec")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database Available!!"))
