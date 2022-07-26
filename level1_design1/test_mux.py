# See LICENSE.vyoma for details
# simple tests for an multiplexer
import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""
    begin
       
       sel0=0:inp0
       sel1=1:inp1
       sel2=1:inp12
       sel3=1:inp3
       sel4=0:inp4
       sel5=1:inp5
       sel6=0:inp6
       sel7=1:inp7
       sel8=0:inp8
       sel9=1:inp9
       sel10=1:inp10
       sel11=1:inp11
       sel12=0:inp12
       sel13=1:inp13
       sel14=1:inp14
       sel15=0:inp15
       sel16=1:inp16
       sel17=1:inp17
       sel18=1:inp18
       sel19=0:inp19
       sel20=1:inp20
       sel21=1:inp21
       sel22=0:inp22
       sel23=1:inp23
       sel24=0:inp24
       sel25=1:inp24
       sel26=0:inp26
       sel27=1:inp27
       sel28=0:inp28
       sel29=0:inp29
       sel30=1:inp30
       sel31=0:inp31
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