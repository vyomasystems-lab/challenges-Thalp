// encoder ,the transmission link uses fewer lines to transmit the encoded information
//
//on saturday JULY 30 
//
// Ports
// Name            I/O size
// enc_y7value      8bits
// enc_y6value      8bits
// enc_y5value      8bits
// enc_y4value      8bits
// enc_y3value      8bits
// enc_y2value      8bits
// enc_y1value      8bits
// enc_y0value      8bits
// out_a2value      1bits
// out_a1value      1bits
// out_a0value      1bits
// out RDY_out      3bits
//
// encoded information signal from input to output ports
// (enc_y7, enc_y6,enc_y5, enc_y4,enc_y3,enc_y2,enc_y1,enc_y0) ->out_a0value,out_a1value,out_a2value
// input Ports ,output ports declaration 
module encoder(enc_y7,
     enc_y6,
     enc_y5,
     enc_y4,
     enc_y3,
     enc_y2,
     enc_y1,
     enc_y0,
     EN_enc,
     out_a2value,
     out_a1value,
     out_a0value,
     RDY_out);
input [7:0] enc_y7;
input [7:0] enc_y6;
input [7:0] enc_y5;
input [7:0] enc_y4;
input [7:0] enc_y3;
input [7:0] enc_y2;
input [7:0] enc_y1;
input [7:0] enc_y0;
input EN_enc;
output out_a2value;
output out_a1value;
output out_a0value;
output RDY_out;
reg out_a2value;
reg out_a1value;
reg out_a0value;
reg RDY_out;

// based on the input signal resultant output signal wil be Generated
// for resultant 1'd5 output signal the  input signal will be 8'b00100000  
// scheduling encoding signals
always @(enc_y0 or enc_y1 or enc_y2 or enc_y3 or enc_y3 or enc_y4 or enc_y5 or enc_y6 or enc_y7 )
//
  assign EN_enc=
	       (enc_y7 ?
	       8'b10000000 :
	       (enc_y6 ?
		     8'b01000000 :
		     (enc_y5 ?
		     8'b00100000 :
		     (enc_y4 ?
			   8'b00010000 :
			   (enc_y3 ?
			   8'b00001000 :
			   (enc_y2 ?
			   8'b0000100 :
			   (enc_y1 ?
				 8'b0000010 :
				 (enc_y0 ?
				 8'b0000001))))))));
 // scheduling output signals
 //
 assign out_a2value = { enc_y7|enc_y6|enc_y5|enc_y4};
 assign out_a1value = { enc_y7|enc_y6|enc_y3|enc_y2};
 assign out_a0value = { enc_y7|enc_y5|enc_y3|enc_y1};
 assign RDY_out ={out_a2value,out_a1value,out_a0value};
 endmodule
