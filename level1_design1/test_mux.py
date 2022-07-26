# See LICENSE.vyoma for details
# simple tests for an multiplexer
import cocotb
from cocotb.triggers import Timer
import random
@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""
 begin 
 case(inp,sel)
 inp0=5'b00000; sel=5'b00000;
 inp1=5'b00001; sel=5'b00001;
 inp2=5'b00010; sel=5'b00010;
 inp3=5'b00011; sel=5'b00011;
 inp4=5'b00100; sel=5'b00100;
 inp5=5'b00101; sel=5'b00101;
 inp6=5'b00110; sel=5'b00110;
 inp7=5'b00111; sel=5'b00111;
 inp8=5'b01000; sel=5'b01000;
 inp19=5'b01001; sel=5'b01001;
 inp10=5'b01010; sel=5'b01010;
 inp11=5'b01011; sel=5'b01011;
 inp12=5'b01100; sel=5'b01100;
 inp13=5'b01101; sel=5'b01101;
 inp14=5'b01110; sel=5'b01110;
 inp15=5'b01111; sel=5'b01111;
 inp16=5'b10000; sel=5'b10000;
 inp17=5'b10001; sel=5'b10001;
 inp18=5'b10010; sel=5'b00010;
 inp19=5'b10011; sel=5'b10011;
 inp20=5'b10100; sel=5'b10100;
 inp21=5'b10101; sel=5'b10101;
 inp22=5'b10110; sel=5'b10110;
 inp23=5'b10111; sel=5'b10111;
 inp24=5'b11000; sel=5'b11000;
 inp25=5'b11001; sel=5'b11001;
 inp26=5'b11010; sel=5'b11011;
 inp27=5'b11011; sel=5'b11011;
 inp28=5'b11100; sel=5'b11100;
 inp29=5'b11101; sel=5'b11101;
 inp30=5'b11110; sel=5'b11110;
 inp31=5'b11111; sel=5'b11111;
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