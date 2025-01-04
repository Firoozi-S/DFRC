

from typing import Any
import numpy as np
from scipy.special import comb
from itertools import product


class _SIM():
    def __init__(self) -> None:
        pass

    def _generate_sim(self, total_c: int, sim_size: int):
        sim_combs = list(product([0, 1], repeat=total_c))
        filter_sim_combs = [sim for sim in sim_combs if sum(sim) == sim_size]
        symbol_combs = list(product([0, 1], repeat=sim_size))
        self._sim_dict = dict(zip(symbol_combs, filter_sim_combs))
        return
    
    def _get_sim_dict(self) -> dict:
        return self._sim_dict

    def __call__(self, total_c: int, num_c: int) -> Any:
        if total_c < num_c:
            return
        sim_size = self.get_sim_symbol_size(total_c, num_c)
        self._generate_sim(total_c, sim_size)
        pass

    def get_sim_symbol_size(self, total_c: int, num_c: int) -> int:
        return int(np.floor(np.log2(comb(total_c, num_c))))
    
    def get_sim_mod(self, mod: tuple[int]) -> np.ndarray:
        if self._sim_dict.get(mod) == None:
            return
        return np.array(self._sim_dict[mod])