# See LICENSE.vyoma for details
# simple tests for an multiplexer
import cocotb
from cocotb.triggers import Timer
import random
@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""
 begin
 sel0=1
 sel1=1
 sel2=1
 sel3=1
 sel4=1
 sel5=1
 sel6=1
 sel7=0
 sel8=1
 sel9=1
 sel10=1
 sel11=1
 sel12=1
 sel13=0
 sel14=1
 sel15=1
 sel16=1
 sel17=1
 sel18=1
 sel19=0 
 sel20=0
 sel21=1
 sel22=1
 sel23=0
 sel24=1
 sel25=0
 sel26=1 
 sel27=1
 sel28=0
 sel29=1
 sel30=0
 sel31=1
       #input driving
dut.inp0.value=sel0
dut.inp1.value=sel1
dut.inp2.value=sel2
dut.inp3.value=sel3
dut.inp4.value=sel4
dut.inp5.value=sel5
dut.inp6.value=sel6
dut.inp7.value=sel7
dut.inp8.value=se18
dut.inp9.value=sel9
dut.inp1.value=sel10
dut.inp11.value=sel11
dut.inp12.value=sel12
dut.inp13.value=sel13
dut.inp14.value=sel14
dut.inp15.value=sel15
dut.inp16.value=sel16
dut.inp17.value=sel17
dut.inp18.value=sel18
dut.inp19.value=sel19
dut.inp20.value=sel20
dut.inp21.value=sel21
dut.inp22.value=sel22
dut.inp23.value=sel23
dut.inp24.value=sel24
dut.inp25.value=sel25
dut.inp26.value=sel26
dut.inp27.value=sel27
dut.inp28.value=sel28
dut.inp29.value=sel29
dut.inp30.value=sel30
dut.inp31.value=sel31
await Timer(2,units='ns')
assert dut.sel.value==sel,f"sel result is incorrect:{dut.sel.value}!=sel[4:0]"