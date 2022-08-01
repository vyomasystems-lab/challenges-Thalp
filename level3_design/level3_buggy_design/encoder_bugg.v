// encoder ,the transmission link uses fewer lines to transmit the encoded information
//
//on saturday JULY 30 
//
// Ports
// Name            I/O size
// enc_y7value      16bits
// enc_y6value      16bits
// enc_y5value      16bits
// enc_y4value      16bits
// enc_y3value      16bits
// enc_y2value      16bits
// enc_y1value      16bits
// enc_y0value      16bits
// out_a3value      1bits
// out_a2value      1bits
// out_a1value      1bits
// out_a0value      1bits
//
// encoded information signal from input to output ports
// (enc_y7, enc_y6,enc_y5, enc_y4,enc_y3,enc_y2,enc_y1,enc_y0) ->out_a0value,out_a1value,out_a2value,out_a3value
// input Ports ,output ports declaration 
module encoder(enc_y7,
     enc_y6,
     enc_y5,
     enc_y4,
     enc_y3,
     enc_y2,
     enc_y1,
     enc_y0,
     out_a3value,
     out_a2value,
     out_a1value,
     out_a0value);
input [7:0] enc_y7;
input [7:0] enc_y6;
input [7:0] enc_y5;
input [7:0] enc_y4;
input [7:0] enc_y3;
input [7:0] enc_y2;
input [7:0] enc_y1;
input [7:0] enc_y0;
output out_a3value;
output out_a2value;
output out_a1value;
output out_a0value;
reg out_a3value;
reg out_a2value;
reg out_a1value;
reg out_a0value;

// based on the input signal resultant output signal wil be Generated
// for resultant 1'd5 output signal the  input signal will be 8'b00100000  
// scheduling encoding signals

  assign enc_y7=16'b0000000010000000;
  assign enc_y6=16'b0000000001000000;
  assign enc_y5=16'b0000000000100000;
  assign enc_y4=16'b0000000000010000;
  assign enc_y3=16'b0000000000001000;
  assign enc_y2=16'b0000000000000100;
  assign enc_y1=16'b0000000000000010;
  assign enc_y0=16'b0000000000000001;
 // scheduling output signals
 //
 assign out_a3value ={1};
 assign out_a2value = { enc_y7|enc_y6|enc_y5|enc_y4};
 assign out_a1value = { enc_y7|enc_y6|enc_y3|enc_y2};
 assign out_a0value = { enc_y7|enc_y5|enc_y3|enc_y1};
 endmodule
