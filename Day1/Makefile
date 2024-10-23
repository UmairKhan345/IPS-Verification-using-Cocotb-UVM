# Makefile for Cocotb simulation
# SIM ?= icarus
# TOPLEVEL_LANG ?= verilog

TOPLEVEL_LANG =verilog
# Module to be tested
MODULE = "test_Half_adder"
TOPLEVEL = "Half_adder_top"

# Paths to your Verilog source files
# VERILOG_SOURCES = $(shell pwd)/and_gate_top.v
VERILOG_SOURCES = ./Half_adder.v \
                                                                        ./Half_adder_top.v

# Include Cocotb's makefile
include $(shell cocotb-config --makefiles)/Makefile.sim
