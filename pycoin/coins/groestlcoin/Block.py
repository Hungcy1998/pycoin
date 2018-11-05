import io

from pycoin.encoding.hash import groestlHash
from pycoin.block import Block as BaseBlock

from .Tx import Tx

class Block(BaseBlock):
    Tx = Tx
    def _calculate_hash(self):
        s = io.BytesIO()
        self.stream_header(s)
        return groestlHash(s.getvalue())
