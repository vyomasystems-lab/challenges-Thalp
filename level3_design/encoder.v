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
 