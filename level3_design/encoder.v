// encoder ,the transmission link uses fewer lines to transmit the encoded information
//
//on saturday JULY 30 
//
// Ports
// Name            I/O size
// enc_y7value      0   8bits
// enc_y6value      0   8bits
// enc_y5value      0   8bits
// enc_y4value      0   8bits
// enc_y3value      0   8bits
// enc_y2value      0   8bits
// enc_y1value      0   8bits
// enc_y0value      0   8bits
// out_a2value      0   1bits
// out_a1value      0   1bits
// out_a0value      0   1bits
//
// encoded information signal from input to output ports:
//  (enc_y7,
     enc_y6,
     enc_y5,
     enc_y4,
     enc_y3,
     enc_y2,
     enc_y1,
     enc_y0) ->out_a0value,out_a1value,out_a2value
// input Ports ,output ports declaration 
module encoder(enc_y7,
     enc_y6,
     enc_y5,
     enc_y4,
     enc_y3,
     enc_y2,
     enc_y1,
     enc_y0
     EN_enc);
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

// value method mv_scopbusy
output mv_scopbusy;
output RDY_mv_scopbusy;

// signals for module outputs
wire mav_putvalue;
wire RDY_mav_putvalue,RDY_mv_scopbusy,mv_scopbusy;

 // scheduling encoding signals
  assign EN_enc=
	       (mav_putvalue_enc_y7 ?
	       8'b10000000 :
	       (mav_putvalue_enc_y6 ?
		     8'b01000000 :
		     (mav_putvalue_enc_y5 ?
		     8'b00100000 :
		     (mav_putvalue_enc_y4 ?
			   8'b00010000 :
			   (mav_putvalue_enc_y3 ?
			   8'b00001000 :
			   (mav_putvalue_enc_y2 ?
			   8'b0000100 :
			   (mav_putvalue_enc_y1 ?
				 8'b0000010 :
				 (mav_putvalue_enc_y0 ?
				 8'b0000001))))))));
 // scheduling output signals
 assign out_a2value = { mav_putvalue_enc_y7|mav_putvalue_enc_y6|mav_putvalue_enc_y5|mav_putvalue_enc_y4};
 assign out_a1value = { mav_putvalue_enc_y7|mav_putvalue_enc_y6|mav_putvalue_enc_y3|mav_putvalue_enc_y2};
 assign out_a0value = { mav_putvalue_enc_y7|mav_putvalue_enc_y5|mav_putvalue_enc_y3|mav_putvalue_enc_y1};
 assign RDY_out ={out_a2value,out_a1value,out_a0value};
 endmodule
