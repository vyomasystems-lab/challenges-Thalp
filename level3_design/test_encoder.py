# See LICENSE.vyoma for details
# simple tests for an multiplexer
import cocotb
from cocotb.triggers import Timer
import random

@cocotb.test()
async def test_encoder(dut):
    """Test for encoder"""

    cocotb.log.info('#### CTB: Develop your test here ####')
    enc_decla_y7=0,
    enc_decla_y6=1,
    enc_decla_y5=1,
    enc_decla_y4=1,
    enc_decla_y3=0,
    enc_decla_y2=1,
    enc_decla_y1=1,
    enc_decla_y0=1,
    
    #input driving
    dut.enc_y7.value=enc_decla_y7
    dut.enc_y6.value=enc_decla_y6
    dut.enc_y5.value=enc_decla_y5
    dut.enc_y4.value=enc_decla_y4
    dut.enc_y3.value=enc_decla_y3
    dut.enc_y2.value=enc_decla_y2
    dut.enc_y1.value=enc_decla_y1
    dut.enc_y0.value=enc_decla_y0

    await Timer(1,units='ns')

    assert dut.RDY_out.value==0,f"encoder result is incorrect:{dut.RDY_out.value!=1}"