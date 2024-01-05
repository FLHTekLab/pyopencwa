import logging
from typing import List, Dict, Callable, Type  # , TYPE_CHECKING
from cwagent import config
from cwagent.domain import commands, events, model
from cwagent.adapters import cwa_open_api
# if TYPE_CHECKING:
#     from . import unit_of_work
from . import unit_of_work

logger = logging.getLogger(__name__)

EVENT_HANDLERS = {
    # events.UserRegistered: [fetch_user_dev_list],
}  # type: Dict[Type[events.Event], List[Callable]]

COMMAND_HANDLERS = {
    # commands.Register: register_user,
}  # type: Dict[Type[commands.Command], Callable]
