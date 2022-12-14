

__all__ = ['get_collection']

import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from motor.core import AgnosticClient, AgnosticDatabase, AgnosticCollection
from YUI import MONGO_DB_URI as DB_URL

print("Connecting to Database ...")

_MGCLIENT: AgnosticClient = AsyncIOMotorClient(DB_URL)
_RUN = asyncio.get_event_loop().run_until_complete

if "YUI" in _RUN(_MGCLIENT.list_database_names()):
    print("Yui Database Found :) => Now Logging to it...")
else:
    print("Yui Database Not Found :( => Creating New Database...")

_DATABASE: AgnosticDatabase = _MGCLIENT["TOGA"]


def get_collection(name: str) -> AgnosticCollection:
    """ Create or Get Collection from your database """
    return _DATABASE[name]


def _close_db() -> None:
    _MGCLIENT.close()
