// encoder ,the transmission link uses fewer lines to transmit the encoded information
//
//on saturday JULY 30 
//
// Ports
// Name            I/O size
// enc_y7value      0   2bits
// enc_y6value      0   2bits
// enc_y5value      0   2bits
// enc_y4value      0   2bits
// enc_y3value      0   2bits
// enc_y2value      0   2bits
// enc_y1value      0   2bits
// enc_y0value      0   2bits
// out_a2value      0   2bits
// out_a1value      0   2bits
// out_a0value      0   2bits
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
//
//
`ifdef BSV_ASSIGNMENT_DELAY
`else
  `define BSV_ASSIGNMENT_DELAY
`endif

`ifdef BSV_POSITIVE_RESET
  `define BSV_RESET_VALUE 1'b1
  `define BSV_RESET_EDGE posedge
`else
  `define BSV_RESET_VALUE 1'b0
  `define BSV_RESET_EDGE negedge
`endif
module encoder(enc_y7,
     enc_y6,
     enc_y5,
     enc_y4,
     enc_y3,
     enc_y2,
     enc_y1,
     enc_y0
     EN_enc);
input [1:0] enc_y7;
input [1:0] enc_y6;
input [1:0] enc_y5;
input [1:0] enc_y4;
input [1:0] enc_y3;
input [1:0] enc_y2;
input [1:0] enc_y1;
input [1:0] enc_y0;
input EN_enc;
output [1:0] out_a2value;
output [1:0] out_a1value;
output [1:0] out_a0value;
output RDY_out;

// value method mv_scopbusy
output mv_scopbusy;
output RDY_mv_scopbusy;

// signals for module outputs
wire [1:0] mav_putvalue;
wire RDY_mav_putvalue,RDY_mv_scopbusy,mv_scopbusy;

 // rule scheduling signals
  wire CAN_FIRE_mav_putvalue, WILL_FIRE_mav_putvalue;
    wire [1 : 0] IF_mav_putvalue_enc_y7_BITS_27_TO_24_EQ_0_THEN_1_ETC__q3,
		IF_mav_putvalue_enc_y7_BIT_0_05_THEN_IF_mav_putv_ETC___d807,
        IF_mav_putvalue_enc_y7_BIT_0_05_THEN_IF_mav_putv_ETC___d807,
		IF_mav_putvalue_enc_y7_BIT_10_95_THEN_IF_mav_put_ETC___d1106,
		IF_mav_putvalue_enc_y7_BIT_10_95_THEN_IF_mav_put_ETC___d1957,
 assign mav_putvalue =
	     { x__h33,
	       (mav_putvalue_instr[6:0] == 7'b0110011 ||
		mav_putvalue_instr[6:0] == 7'b0010011) &&
	       mav_putvalue_instr_BITS_31_TO_25_EQ_0b100000_A_ETC___d2336 } ;
 assign x__h13442 =
	     mav_putvalue_src1[31] ?
	       6'd0 :
	       (mav_putvalue_src1[30] ?
		  6'd1 :
		  (mav_putvalue_src1[29] ?
		     6'd2 :
		     (mav_putvalue_src1[28] ?
			6'd3 :
			(mav_putvalue_src1[27] ?
			   6'd4 :
			   (mav_putvalue_src1[26] ?
			      6'd5 :
			      (mav_putvalue_src1[25] ?
				 6'd6 :
				 (mav_putvalue_src1[24] ?
				    6'd7 :
				    (mav_putvalue_src1[23] ?
				       6'd8 :
				       (mav_putvalue_src1[22] ?
					  6'd9 :
					  (mav_putvalue_src1[21] ?
					     6'd10 :
					     (mav_putvalue_src1[20] ?
						6'd11 :
						(mav_putvalue_src1[19] ?
						   6'd12 :
						   (mav_putvalue_src1[18] ?
						      6'd13 :
						      (mav_putvalue_src1[17] ?
							 6'd14 :
							 (mav_putvalue_src1[16] ?
							    6'd15 :
							    (mav_putvalue_src1[15] ?
							       6'd16 :
							       (mav_putvalue_src1[14] ?
								  6'd17 :
								  (mav_putvalue_src1[13] ?
								     6'd18 :
								     (mav_putvalue_src1[12] ?
									6'd19 :
									(mav_putvalue_src1[11] ?
									   6'd20 :
									   (mav_putvalue_src1[10] ?
									      6'd21 :
									      (mav_putvalue_src1[9] ?
										 6'd22 :
										 (mav_putvalue_src1[8] ?
										    6'd23 :
										    (mav_putvalue_src1[7] ?
										       6'd24 :
										       (mav_putvalue_src1[6] ?
											  6'd25 :
											  (mav_putvalue_src1[5] ?
											     6'd26 :
											     (mav_putvalue_src1[4] ?
												6'd27 :
												(mav_putvalue_src1[3] ?
												   6'd28 :
												   (mav_putvalue_src1[2] ?
												      6'd29 :
												      (mav_putvalue_src1[1] ?
													 6'd30 :
													 (mav_putvalue_src1[0] ?
													    6'd31 :
													    6'd32))))))))))))))))))))))))))))))) ;        