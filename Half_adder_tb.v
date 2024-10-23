  `timescale 1ns / 1ps 
   Half_adder_top.v                                                                          
   module Half_adder_top;


    reg a;
    reg b;
    wire sum;
    wire carry;


    half_adder uut (
        .a(a),
        .b(b),
        .sum(sum),
        .carry(carry)
    );

     initial begin
        $dumpfile("half_adder.vcd");
        $dumpvars(0, Half_adder_top);


        a = 0; b = 0;
        #10;


        a = 0; b = 1;
        #10;


        a = 1; b = 0;
        #10;


        a = 1; b = 1;
        #10;

        $finish;
    end
