from typing import List, Optional
import numpy as np
import matplotlib.pyplot as plt

from .water import WaterAdjustment


class MashStep:

    def __init__(self, duration: int, temperature: float) -> None:
        self.duration = duration
        self.temperature = temperature


class Mash:

    def __init__(self,
                 steps: List[MashStep],
                 start: Optional[int]=None,
                 water_adjustments: Optional[List[WaterAdjustment]]=None) -> None:
        self._steps = steps
        self._start = start
        self._water_adjustments = water_adjustments

    def set_mash_start(self, start_time) -> None:
        self._start = start_time

    def temperature(self, curr_time: int) -> float:
        if self.start_time > curr_time > self.end_time:
            return 0.0
        tmp = self.start_time
        for step in self._steps:
            tmp += step.duration
            if curr_time < tmp:
                return step.temperature
        else:
            return 0.0

    @property
    def num_steps(self) -> int:
        return len(self._steps)

    @property
    def duration(self) -> int:
        return sum([s.duration for s in self._steps])

    @property
    def start_time(self) -> int:
        return self._start

    @property
    def end_time(self) -> int:
        return self._start + self.duration

    def time_remaining(self, curr_time: int) -> int:
        if self._start <= curr_time <= self.end_time:
            return self.end_time - curr_time
        elif curr_time >= self.end_time:
            return 0
        return np.nan


def mash_example():
    mash_steps = [
        MashStep(duration=60*30, temperature=64.),
        MashStep(duration=60*30, temperature=68.),
        MashStep(duration=60*15, temperature=80.),
    ]
    mash = Mash(steps=mash_steps, start=0)
    assert mash.temperature(1) == 64.
    ts = np.arange(0, 60*75, 60, dtype='i')
    temperature = np.fromiter((mash.temperature(t) for t in ts), dtype="f", count=len(ts))
    plt.figure()
    plt.plot(ts, temperature)
    plt.show(block=True)

