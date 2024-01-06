# pylint: disable=attribute-defined-outside-init
from __future__ import annotations
import abc
import os
import shutil
import logging
from cwagent.adapters import repository, file_datastore

logger = logging.getLogger(__name__)


class AbstractUnitOfWork(abc.ABC):
    stations: repository.AbstractRepository

    def __enter__(self) -> AbstractUnitOfWork:
        return self

    def __exit__(self, *args):
        self.rollback()

    def commit(self):
        self._commit()

    def collect_new_events(self):
        for s in self.stations.seen:
            logger.debug(f"current existing unhandled events {s.events} ")
            while s.events:
                yield s.events.pop(0)

    @abc.abstractmethod
    def rollback(self):
        raise NotImplementedError

    @abc.abstractmethod
    def _commit(self):
        raise NotImplementedError


class JsonFileUnitOfWork(AbstractUnitOfWork):
    def __init__(self, json_file='.datastore.json'):
        super().__init__()
        self._json_file = json_file
        self._origin = f'{json_file}.swap'
        self.session_factory = file_datastore.session_factory

    def __enter__(self):
        if os.path.exists(self._json_file):
            shutil.copyfile(self._json_file, self._origin)
        self.session = self.session_factory(self._json_file)
        self.stations = repository.JsonFileRepository(self.session)
        # self.api_server = FakeApiServer()
        return super().__enter__()

    def __exit__(self, *args):
        if os.path.exists(self._origin):
            os.remove(self._origin)
        super().__exit__(*args)

    def _commit(self):
        self.session.commit()

    def rollback(self):
        if os.path.exists(self._origin):
            shutil.copyfile(self._origin, self._json_file)
