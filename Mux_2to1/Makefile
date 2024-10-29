# Makefile for Cocotb simulation
# SIM ?= icarus
# TOPLEVEL_LANG ?= verilog

TOPLEVEL_LANG =verilog
# Module to be tested
MODULE = "test_mux_2to1"
TOPLEVEL ="mux_2to1_top"

# Paths to your Verilog source files
# VERILOG_SOURCES = $(shell pwd)/and_gate_top.v
VERILOG_SOURCES = ./mux_2to1.v \
                                                                        ./mux_2to1_top.v

# Include Cocotb's makefile
include $(shell cocotb-config --makefiles)/Makefile.simS