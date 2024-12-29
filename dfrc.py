from typing import Optional
from mimo import _MIMO
from ofdm import _OFDM


class DFRC():
    def __init__(self,
                 carrier_freq: float,
                 subcarrier_interval: float,
                 ofdm_symbol_period: float,
                 num_bs: int,
                 num_c: int,
                 num_ue: int
                 ) -> None:
        
        if num_bs <= 0 or num_c <= 0 or num_ue <= 0:
            return
        
        if carrier_freq <= 0 or subcarrier_interval <= 0 or ofdm_symbol_period <= 0:
            return
        
        self._mimo = _MIMO(num_bs,
                           num_ue)
        
        self._ofdm = _OFDM(num_c,
                           ofdm_symbol_period,
                           subcarrier_interval,
                           carrier_freq)
        pass

    def __call__(self, ofdm_mode: str ) -> tuple:
        freqs = self._ofdm.sub_carrier_freqs(self._mimo.get_num_bs())

        return
