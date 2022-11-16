import math
import random
from asyncio import sleep, BoundedSemaphore
from typing import Awaitable

from asyncio_throttle import Throttler


async def with_throttle_and_semaphore(throttler: Throttler, semaphore: BoundedSemaphore, func: Awaitable):
    async with semaphore:
        async with throttler:
            return await func


class ExponentialSleeping:
    def __init__(self, start: float, step: float, max_exp: float, rand_start: float = 0.0, rand_end: float = 1.0):
        self.start = start
        self.step = step
        self.max_exp = max_exp
        self.current = self.start
        self.rand_start = rand_start
        self.rand_end = rand_end
        self.deviation = random.uniform(self.rand_start, self.rand_end)

    async def wait(self):
        await sleep(self.current)
        self.current = self.current + self.step
        self.deviation = random.uniform(self.rand_start, self.rand_end)

    def get_current(self) -> float:
        return min(math.exp(self.current), self.max_exp)

    def get_next(self) -> float:
        return min(math.exp(self.current + self.step), self.max_exp)

    def is_maximum_reached(self) -> bool:
        return self.get_current() >= self.max_exp

    def reset(self):
        self.current = self.start
