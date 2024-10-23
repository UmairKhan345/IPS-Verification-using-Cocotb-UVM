import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def half_adder_test(dut):
    """Test the functionality of a half adder."""

    # Test vector 1: a=0, b=0 (expected sum=0, carry=0)
    dut.a.value = 0
    dut.b.value = 0
    await Timer(2, units='ns')  # Wait for the output to settle
    assert dut.sum.value == 0, f"Sum failed: {dut.sum.value}"
    assert dut.carry.value == 0, f"Carry failed: {dut.carry.value}"

    # Test vector 2: a=0, b=1 (expected sum=1, carry=0)
    dut.a.value = 0
    dut.b.value = 1
    await Timer(2, units='ns')
    assert dut.sum.value == 1, f"Sum failed: {dut.sum.value}"
    assert dut.carry.value == 0, f"Carry failed: {dut.carry.value}"

    # Test vector 3: a=1, b=0 (expected sum=1, carry=0)
    dut.a.value = 1
    dut.b.value = 0
    await Timer(2, units='ns')
    assert dut.sum.value == 1, f"Sum failed: {dut.sum.value}"
    assert dut.carry.value == 0, f"Carry failed: {dut.carry.value}"

    # Test vector 4: a=1, b=1 (expected sum=0, carry=1)
    dut.a.value = 1
    dut.b.value = 1
    await Timer(2, units='ns')
    assert dut.sum.value == 0, f"Sum failed: {dut.sum.value}"
    assert dut.carry.value == 1, f"Carry failed: {dut.carry.value}"

    print("All tests passed!")
