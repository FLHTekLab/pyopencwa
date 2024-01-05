""""""
import inspect
from cwagent.service_layer import handlers, messagebus, unit_of_work
from cwagent.adapters import orm, cwa_open_api


def bootstrap(
        uow: unit_of_work.AbstractUnitOfWork = unit_of_work.JsonFileUnitOfWork(),
        start_orm: bool = False,
        cwa_api: cwa_open_api.AbstractCWAOpenAPI = cwa_open_api.CWAOpenAPI()
) -> messagebus.MessageBus:

    if start_orm:
        orm.start_mappers()

    dependencies = {'uow': uow, 'cwa_api': cwa_api}
    injected_event_handlers = {
        event_type: [
            inject_dependencies(handler, dependencies)
            for handler in event_handlers
        ]
        for event_type, event_handlers in handlers.EVENT_HANDLERS.items()
    }
    injected_command_handlers = {
        command_type: inject_dependencies(handler, dependencies)
        for command_type, handler in handlers.COMMAND_HANDLERS.items()
    }

    return messagebus.MessageBus(
        uow=uow,
        event_handlers=injected_event_handlers,
        command_handlers=injected_command_handlers,
    )


def inject_dependencies(handler, dependencies):
    params = inspect.signature(handler).parameters
    deps = {
        name: dependency
        for name, dependency in dependencies.items()
        if name in params
    }
    return lambda message: handler(message, **deps)
