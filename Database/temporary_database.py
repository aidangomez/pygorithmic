import os

from . import database


class TemporaryDatabase(database.Database):

    def __del__(self):
            super().__del__
            os.remove(self.name + ".db")
