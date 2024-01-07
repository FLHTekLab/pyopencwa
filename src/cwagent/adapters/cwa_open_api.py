import abc
import time
import requests
import logging
from typing import List
from cwagent import config
from cwagent.domain import model

logger = logging.getLogger(__name__)
timer_logger = logging.getLogger('timer')
ob_logger = logging.getLogger('O-A0001-001')


class CwaApiError(Exception):
    pass


class AbstractCWAOpenAPI(abc.ABC):
    @abc.abstractmethod
    def pull_all_stations_observation(self) -> List[model.StationObservation]:
        raise NotImplementedError


class CWAOpenAPI(AbstractCWAOpenAPI):
    def pull_all_stations_observation(self) -> List[model.StationObservation]:
        response = self._get_cwa_api_response(path='/v1/rest/datastore/O-A0001-001', params=None)
        if not isinstance(response.get('records').get('Station'), list):
            raise CwaApiError(f"response.records.Station is not list: {response}")
        ob_logger.info(f'{response}')
        return [model.StationObservation.load(dto) for dto in response.get('records').get('Station')]

    @staticmethod
    def _get_cwa_api_response(path: str, params: dict = None):
        """取得 cwa api 回應，並解計算http request 執行時間"""
        api_uri = f'{config.get_cwa_uri()}{path}'
        params = params or {}
        logger.debug(f'api path: {api_uri}, params: {params}')
        start_time = time.time()
        r = requests.get(
            headers={'Authorization': config.get_cwa_auth_key()},
            url=api_uri,
            params=params,
            verify=config.get_api_ssl_check_flag()
        )
        end_time = time.time()
        elapsed_time = end_time - start_time
        elapsed_time_formatted = format(elapsed_time, '5.2f')  # 将秒数格式化为两位小数
        timer_logger.info(f'{elapsed_time_formatted}, {api_uri}')
        logger.debug(f'{r.status_code} {r.reason}')
        if r.text.find("{") != 0:
            raise CwaApiError(r.text)
        response = r.json()
        if not response.get('success'):
            raise CwaApiError(response)
        logger.info(f'HTTP GET {api_uri}, {r.status_code}, {elapsed_time_formatted} sec')
        return response
