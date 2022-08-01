# See LICENSE.vyoma for details
# simple tests for an multiplexer
import cocotb
from cocotb.triggers import Timer
import random

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""

    cocotb.log.info('#### CTB: Develop your test here ####')
    inp0=0;
    inp1=1;
    inp2=2;
    inp3=2;
    inp4=3;
    inp5=1;
    inp6=2;
    inp7=3;
    inp8=2;
    inp9=2;
    inp10=3;
    inp11=3;
    inp12=2;
    inp13=3;
    inp14=2;
    inp15=1;
    inp16=2;
    inp17=3;
    inp18=3;
    inp19=2;
    inp20=1;
    inp21=3;
    inp22=2;
    inp23=1;
    inp24=3;
    inp25=1;
    inp26=2;
    inp27=3;
    inp28=3;
    inp29=1;
    inp30=3;
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

    