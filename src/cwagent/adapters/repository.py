import abc
import logging
from typing import Set, List
from cwagent.domain import model

logger = logging.getLogger(__name__)


class AbstractRepository(abc.ABC):
    """"""

    def __init__(self):
        self.seen = set()  # type: Set[model.Station]


class MemoryRepository(AbstractRepository):
    pass


class JsonFileRepository(AbstractRepository):

    def __init__(self, session):
        super().__init__()
        self.session = session  # type:'file_datastore.FileDatastore'

# class SqlAlchemyRepository(AbstractRepository):
#     def __init__(self, session):
#         super().__init__()
#         self.session = session
