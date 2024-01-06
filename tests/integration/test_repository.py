import json
import os.path

from cwagent.domain import model
from cwagent.adapters import repository, file_datastore


def test_repository():
    with open('./tests/O-A0001-001.json') as fh:
        content = json.loads(fh.read())
        if not isinstance(content.get('records').get('Station'), list):
            raise ValueError
    st_observations = [model.StationObservation.load(dto) for dto in content.get('records').get('Station')]
    id1 = 'C0R890'
    so1 = next((s for s in st_observations if s.station_id == id1), None)
    s1 = model.Station(
        station_id=so1.station_id,
        station_name=so1.station_name,
        geo_info=so1.geo_info,
        observations=[model.TimeObservation(
            obs_time=so1.obs_time,
            weather_element=so1.weather_element
        )])

    id2 = 'C0V900'
    so2 = next((s for s in st_observations if s.station_id == id2), None)
    s2 = model.Station(
        station_id=so2.station_id,
        station_name=so2.station_name,
        geo_info=so2.geo_info,
        observations=[model.TimeObservation(
            obs_time=so2.obs_time,
            weather_element=so2.weather_element
        )])
    id3 = 'C0N020'
    so3 = next((s for s in st_observations if s.station_id == id3), None)
    s3 = model.Station(
        station_id=so3.station_id,
        station_name=so3.station_name,
        geo_info=so3.geo_info,
        observations=[model.TimeObservation(
            obs_time=so3.obs_time,
            weather_element=so3.weather_element
        )])

    if os.path.exists('.teststore.json'):
        os.remove('.teststore.json')
    repo = repository.JsonFileRepository(session=file_datastore.FileDatastore(file='.teststore.json'))

    # test add
    repo.add(s1)
    repo.add(s2)
    repo.add(s3)
    assert repo.count() == 3

    # test __iter__ and __next__
    for s in repo:
        print(s)

    # test delete
    repo.delete(s1.station_id)
    assert repo.count() == 2

    # test get_by_station_id
    verify = repo.get_by_station_id(station_id=id2)
    assert verify.station_id == id2
    assert verify == s2
    assert verify.station_name == so2.station_name
    assert verify.geo_info.dump() == so2.geo_info.dump()
    assert verify.observations[0].obs_time.dump() == so2.obs_time.dump()
    assert verify.observations[0].weather_element.dump() == so2.weather_element.dump()
