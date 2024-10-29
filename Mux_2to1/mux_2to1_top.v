  GNU nano 6.2                                                                 mux_2to1_top.v                                                                           // testbench.v
module mux_2to1_top(
    input wire sel,
    input wire a,
    input wire b,
    output wire y
);

    // Instantiate the mux_2to1 module
    mux_2to1 uut (
        .sel(sel),
        .a(a),
        .b(b),
        .y(y)
    );

    initial begin
        // Dump waveform data
        $dumpfile("mux_2to1.vcd");
        $dumpvars(0, mux_2to1_top);
    end

endmodule
