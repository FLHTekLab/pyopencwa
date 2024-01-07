import logging
from cwagent.domain import model

logger = logging.getLogger(__name__)


class Station:
    """todo: implement testcase"""
    def test_station_update_time_observation(self):
        """"""
        # will skip ObsTime.DataTime == '-99

        # will keep station observations count within config.get_max_station_observation_count()

        # will skip duplicated ObsTime.DataTime
