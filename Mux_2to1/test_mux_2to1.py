import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def mux_2to1_test(dut):
    # Test case 1: sel=0, a=0, b=0, expecting y=0
    dut.sel.value = 0
    dut.a.value = 0
    dut.b.value = 0
    await Timer(10, units='ns')
    assert dut.y.value == 0, "Test failed with sel=0, a=0, b=0"

    # Test case 2: sel=0, a=1, b=0, expecting y=1
    dut.a.value = 1
    await Timer(10, units='ns')
    assert dut.y.value == 1, "Test failed with sel=0, a=1, b=0"

    # Test case 3: sel=1, a=1, b=0, expecting y=0
    dut.sel.value = 1
    await Timer(10, units='ns')
    assert dut.y.value == 0, "Test failed with sel=1, a=1, b=0"

    # Test case 4: sel=1, a=1, b=1, expecting y=1
    dut.b.value = 1
    await Timer(10, units='ns')
    assert dut.y.value == 1, "Test failed with sel=1, a=1, b=1"

    print("All tests passed!")
