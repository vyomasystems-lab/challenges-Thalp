# See LICENSE.vyoma for details
# simple tests for an multiplexer
import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""
    
       sel0=0
       sel1=1
       sel2=1
       sel3=1
       sel4=0
       sel5=1
       sel6=0
       sel7=1
       sel8=0
       sel9=1
       sel10=1
       sel11=1
       sel12=0
       sel13=1
       sel14=1
       sel15=0
       sel16=1
       sel17=1
       sel18=1
       sel19=0
       sel20=1
       sel21=1
       sel22=0
       sel23=1
       sel24=0
       sel25=1
       sel26=0
       sel27=1
       sel28=0
       sel28=1
       sel29=0
       sel30=1
       sel31=0
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