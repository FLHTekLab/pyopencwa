from dataclasses import dataclass


class Command:
    pass


@dataclass
class PullAllStationObservations(Command):
    """Pull All Station Observations"""
    pass
