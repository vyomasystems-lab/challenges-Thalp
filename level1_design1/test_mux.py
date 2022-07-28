# See LICENSE.vyoma for details
# simple tests for an multiplexer
import cocotb
from cocotb.triggers import Timer
import random
@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""
     cocotb.log.info('### selecting input ###")
     sel=5'b00000:y0=2;
     sel=5'b00001:y1=1;
     sel=5'b00010:y2=4;
     sel=5'b00011:y3=5;
     sel=5'b00100:y4=9;
     sel=5'b00101:y5=3;
     sel=5'b00110:y6=2;
     sel=5'b00111:y7=6;
     sel=5'b01000:y8=9;
     sel=5'b01001:y9=2;
     sel=5'b01010:y10=8;
     sel=5'b01011:y11=2;
     sel=5'b01100:y12=6;
     sel=5'b01101:y13=9;
     sel=5'b01110:y14=2;
     sel=5'b01111:y15=1;
     sel=5'b10000:y16=0;
     sel=5'b10001:y17=9;
     sel=5'b10010:y18=1;
     sel=5'b10011:y19=5;
     sel=5'b10100:y20=7;
     sel=5'b10101:y21=1;
     sel=5'b10110:y22=9;
     sel=5'b10111:y23=4;
     sel=5'b11000:y24=9;
     sel=5'b11001:y25=2;
     sel=5'b11010:Y26=1;
     sel=5'b11011:y27=0;
     sel=5'b11100:y28=2;
     sel=5'b11101:y29=9;
     sel=5'b11110:y30=2;
     sel=5'b11111:y31=9;
     #input driving
     dut.inp0.value=y0;
     dut.inp1.value=y1;
     dut.inp2.value=y2;
     dut.inp3.value=y3;
     dut.inp4.value=y4;
     dut.inp5.value=y5;
     dut.inp6.value=y6;
     dut.inp7.value=y7;
     dut.inp8.value=y8;
     dut.inp9.value=y9;
     dut.inp1.value=y10;
     dut.inp11.value=y11;
     dut.inp12.value=y12;
     dut.inp13.value=y13;
     dut.inp14.value=y14;
     dut.inp15.value=y15;
     dut.inp16.value=y16;
     dut.inp17.value=y17;
     dut.inp18.value=y18;
     dut.inp19.value=y19;
     dut.inp20.value=y20;
     dut.inp21.value=y21;
     dut.inp22.value=y22;
     dut.inp23.value=y23;
     dut.inp24.value=y24;
     dut.inp25.value=y25;
     dut.inp26.value=y26;
     dut.inp27.value=y27;
     dut.inp28.value=y28;
     dut.inp29.value=y29;
     dut.inp30.value=y30;
     dut.inp31.value=y31;
     await Timer(2,units='ns')
     assert dut.sel.value==sel,f"sel result is incorrect:{dut.sel.value}!=5'b11111"




       

