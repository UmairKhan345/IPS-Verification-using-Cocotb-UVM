// mux_2to1.v
module mux_2to1 (
    input wire a,
    input wire b,
    input wire sel,
    output wire y
);
assign y = sel ? b : a;  // Output y is b if sel is 1, otherwise a
endmodule
