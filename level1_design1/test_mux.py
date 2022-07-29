# See LICENSE.vyoma for details
# simple tests for an multiplexer
import cocotb
from cocotb.triggers import Timer
import random

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""

    cocotb.log.info('#### CTB: Develop your test here ####')
    inp0=2;
    inp1=1;
    inp2=5;
    inp3=6;
    inp4=7;
    inp5=8;
    inp6=9;
    inp7=3;
    inp8=1;
    inp9=5;
    inp10=6;
    inp11=7;
    inp12=4;
    inp13=5;
    inp14=6;
    inp15=7;
    inp17=4;
    inp18=3;
    inp19=2;
    inp20=7;
    inp21=3;
    inp22=4;
    inp23=5;
    inp24=6;
    inp25=7;
    inp26=8;
    inp27=9;
    inp28=3;
    inp29=1;
    inp30=7;
    inp31=2;

    #input driving
    dut.inp0.value=inp0
    dut.inp1.value=inp1
    dut.inp2.value=inp2
    dut.inp3.value=inp3
    dut.inp4.value=inp4
    dut.inp5.value=inp5
    dut.inp6.value=inp6
    dut.inp7.value=inp7
    dut.inp8.value=inp8
    dut.inp9.value=inp9
    dut.inp10.value=inp10
    dut.inp11.value=inp11
    dut.inp12.value=inp12
    dut.inp13.value=inp13
    dut.inp14.value=inp14
    dut.inp15.value=inp15
    dut.inp16.value=inp16
    dut.inp17.value=inp17
    dut.inp18.value=inp18
    dut.inp19.value=inp19
    dut.inp20.value=inp20
    dut.inp21.value=inp21
    dut.inp22.value=inp22
    dut.inp23.value=inp23
    dut.inp24.value=inp24
    dut.inp25.value=inp25
    dut.inp26.value=inp26
    dut.inp27.value=inp27
    dut.inp28.value=inp28
    dut.inp29.value=inp29
    
    await Timer(1,units="ns")

    assert dut.out.value==0,f"Mux result is incorrect:{dut.out.value!=1}"

    