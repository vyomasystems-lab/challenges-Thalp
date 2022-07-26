# See LICENSE.vyoma for details
# simple tests for an multiplexer
import cocotb
from cocotb.triggers import Timer
import random
@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""
     5'b00000: out = inp0;  
      5'b00001: out = inp1;  
      5'b00010: out = inp2;  
      5'b00011: out = inp3;  
      5'b00100: out = inp4;  
      5'b00101: out = inp5;  
      5'b00110: out = inp6;  
      5'b00111: out = inp7;  
      5'b01000: out = inp8;  
      5'b01001: out = inp9;  
      5'b01010: out = inp10;
      5'b01011: out = inp11;
      5'b01101: out = inp12;
      5'b01101: out = inp13;
      5'b01110: out = inp14;
      5'b01111: out = inp15;
      5'b10000: out = inp16;
      5'b10001: out = inp17;
      5'b10010: out = inp18;
      5'b10011: out = inp19;
      5'b10100: out = inp20;
      5'b10101: out = inp21;
      5'b10110: out = inp22;
      5'b10111: out = inp23;
      5'b11000: out = inp24;
      5'b11001: out = inp25;
      5'b11010: out = inp26;
      5'b11011: out = inp27;
      5'b11100: out = inp28;
      5'b11101: out = inp29;
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