
from typing import Any, Union
from scipy.special import comb
import numpy as np
from itertools import product

class _GSSK():
    def __init__(self) -> None:
        pass

    def _generate_constellation(self, total_bs: int, num_bs: int):
        antenna_combs = list(product([0, 1], repeat=total_bs))
        filtered_antenna_combs = [comb for comb in antenna_combs if sum(comb) == num_bs]
        symbol_combs = list(product([0,1], repeat=num_bs))
        self._symbol_dict = dict(zip(symbol_combs, filtered_antenna_combs))
        pass
    
    def _get_symbol_dict(self) -> dict:
        return self._symbol_dict

    def __call__(self, total_bs: int, num_bs: int) -> bool:
        if total_bs < num_bs:
            return
        symbol_combinations = self.get_gssk_symbol_size(total_bs, num_bs)
        self._generate_constellation(total_bs, symbol_combinations)
        return
    
    def get_gssk_symbol_size(self, total_bs: int, num_bs: int) -> int:
        return int(np.floor(np.log2(comb(total_bs, num_bs))))
    
    def get_gssk_mod(self, mod: tuple[int]) -> np.ndarray:
        if self._symbol_dict.get(mod) == None:
            return
        return np.array(self._symbol_dict[mod])

