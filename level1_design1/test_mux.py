# See LICENSE.vyoma for details
# simple tests for an multiplexer
import cocotb
from cocotb.triggers import Timer
import random
@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""
cocotb.log.info('#### CTB: Develop your test here ####')
    #input driving
dut.inp0.value=2;
dut.inp1.value=5;
dut.inp2.value=2;
dut.inp3.value=3;
dut.inp4.value=4;
dut.inp5.value=5;
dut.inp6.value=6;
dut.inp7.value=7;
dut.inp8.value=8;
dut.inp9.value=9;
dut.inp1.value=10;
dut.inp11.value=11;
dut.inp12.value=12;
dut.inp13.value=13;
dut.inp14.value=14;
dut.inp15.value=15;
dut.inp16.value=16;
dut.inp17.value=17;
dut.inp18.value=18;
dut.inp19.value=19;
dut.inp20.value=20;
dut.inp21.value=21;
dut.inp22.value=22;
dut.inp23.value=23;
dut.inp24.value=24;
dut.inp25.value=25;
dut.inp26.value=26;
dut.inp27.value=27;
dut.inp28.value=28;
dut.inp29.value=29;
dut.inp30.value=30;
dut.inp31.value=31;
def jls_extract_def():
    return await Timer


jls_extract_def()(1,units='ns')

assert dut.sel.value==sel,f"sel result is incorrect:{dut.sel.value}!=5'b11111"