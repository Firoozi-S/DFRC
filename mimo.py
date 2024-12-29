
class _MIMO():
    def __init__(self,
                 num_bs: int,
                 num_ue: int) -> None:
        
        if num_bs <= 0 or num_ue <= 0:
            return
        
        self._num_bs = num_bs
        self._num_ue = num_ue
        pass

    def get_num_bs(self) -> int:
        return self._num_bs

