# See LICENSE.vyoma for details
# simple tests for an multiplexer
import cocotb
from cocotb.triggers import Timer
import random

@cocotb.test()
async def test_encoder(dut):
    """Test for encoder"""

    cocotb.log.info('#### CTB: Develop your test here ####')
    