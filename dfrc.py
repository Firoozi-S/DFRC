from typing import Optional, Union
from mimo import _MIMO
from ofdm import _OFDM
from gssk import _GSSK
from sim import _SIM
import numpy as np


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
        
        self._sim = _SIM()
        
        self._gssk = _GSSK()
        
        self._mimo = _MIMO(num_bs,
                           num_ue)
        
        self._ofdm = _OFDM(num_c,
                           ofdm_symbol_period,
                           subcarrier_interval,
                           carrier_freq)
        pass

    def __call__(self, packet: np.ndarray, num_c: int, num_bs: int) -> tuple:
        self._gssk(self._mimo.get_num_bs(), num_bs)
        num_gssk_bits = self._gssk.get_gssk_symbol_size(self._mimo.get_num_bs(), num_bs)
        antenna_mod = self._gssk.get_gssk_mod(tuple(packet[:num_gssk_bits])).reshape(-1,1)
        G = np.concatenate([antenna_mod]*self._ofdm.get_num_c(), 1)

        self._sim(self._ofdm.get_num_c(), num_c)
        num_sim_bits = self._sim.get_sim_symbol_size(self._ofdm.get_num_c(), num_c)
        sim_mod = self._sim.get_sim_mod(tuple(packet[num_gssk_bits:num_sim_bits + num_gssk_bits]))
        sim_mod = sim_mod.reshape(1,-1)
        H = np.concatenate([sim_mod]*self._mimo.get_num_bs(), 0)
        
        freqs = self._ofdm.sub_carrier_freqs(self._mimo.get_num_bs())

        
        return
