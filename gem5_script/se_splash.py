# Copyright (c) 2012-2013 ARM Limited
# All rights reserved.
#
# The license below extends only to copyright in the software and shall
# not be construed as granting a license to any other intellectual
# property including but not limited to intellectual property relating
# to a hardware implementation of the functionality of the software
# licensed hereunder.  You may use the software subject to the license
# terms below provided that you ensure that this notice is replicated
# unmodified and in its entirety in all distributions of the software,
# modified or unmodified, in source code or in binary form.
#
# Copyright (c) 2006-2008 The Regents of The University of Michigan
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met: redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer;
# redistributions in binary form must reproduce the above copyright
# notice, this list of conditions and the following disclaimer in the
# documentation and/or other materials provided with the distribution;
# neither the name of the copyright holders nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

# Simple test script
#
# "m5 test.py"

import argparse
import sys
import os

import m5
from m5.defines import buildEnv
from m5.objects import *
from m5.params import NULL
from m5.util import addToPath, fatal, warn
from gem5.isas import ISA
from gem5.runtime import get_runtime_isa

addToPath("../gem5/configs")

from ruby import Ruby

from common import Options
from common import Simulation
from common import CacheConfig
from common import CpuConfig
from common import ObjectList
from common import MemConfig
from common.FileSystemConfig import config_filesystem
from common.Caches import *
from common.cpu2000 import *

def get_processes(args):
    """Interprets provided args and returns a list of processes"""

    multiprocesses = []

    workloads = args.cmd.split(";")

    idx = 0
    for wrkld in workloads:

        if wrkld == "barnes":
            process = BARNES()
        elif wrkld == "fmm":
            process = FMM()
        elif wrkld == "ocean-cont":
            process = OCEAN_CONT()
        elif wrkld == "ocean-nocont":
            process = OCEAN_NOCONT()
        elif wrkld == "radiosity":
            process = RADIOSITY()
        elif wrkld == "raytrace":
            process = RAYTRACE()
        elif wrkld == "volrend":
            process = VOLREND()
        elif wrkld == "volrend-npl":
            process = VOLREND_NPL()
        elif wrkld == "water-nsquared":
            process = WATER_NSQUARED()
        elif wrkld == "water-spatial":
            process = WATER_SPATIAL()
        elif wrkld == "cholesky":
            process = CHOLESKY()
        elif wrkld == "fft":
            process = FFT()
        elif wrkld == "lu-cont":
            process = LU_CONT()
        elif wrkld == "lu-nocont":
            process = LU_NOCONT()
        elif wrkld == "radix":
            process = RADIX()
        else:
            print("error!")

        multiprocesses.append(process)
        idx += 1

    if args.smt:
        assert args.cpu_type == "DerivO3CPU"
        return multiprocesses, idx
    else:
        return multiprocesses, 1

parser = argparse.ArgumentParser()
parser.add_argument(
    "--benchdir",
    help="Bench directory of Splash2",
)

Options.addCommonOptions(parser)
Options.addSEOptions(parser)

args = parser.parse_args()

class BARNES(Process):
    cwd = args.benchdir + "/barnes"
    executable = args.benchdir + "/barnes/BARNES"
    cmd = ["BARNES"]
    input = args.benchdir + "/barnes/inputs/n16384-p1"

class FMM(Process):
    cwd = args.benchdir + "/fmm"
    executable = args.benchdir + "/fmm/FMM"
    input = args.benchdir + "/fmm/inputs/input.1.16384"
    cmd = ["FMM"]

class OCEAN_CONT(Process):
    cwd = args.benchdir + "/ocean-contiguous_partitions"
    executable = args.benchdir + "/ocean-contiguous_partitions/OCEAN-CONT"
    cmd = ["OCEAN-CONT", "-p1", "-n258"]

class OCEAN_NOCONT(Process):
    cwd = args.benchdir + "/ocean-non_contiguous_partitions"
    executable = args.benchdir + "/ocean-non_contiguous_partitions/OCEAN-NOCONT"
    cmd = ["OCEAN-NOCONT", "-p1", "-n258"]

class RADIOSITY(Process):
    cwd = args.benchdir + "/radiosity"
    executable = args.benchdir + "/radiosity/RADIOSITY"
    cmd = ["RADIOSITY", "-p", "1", "-ae", "5000", "-bf", "0.1", "-en", "0.05", "-room", "-batch"]

class RAYTRACE(Process):
    cwd = args.benchdir + "/raytrace"
    executable = args.benchdir + "/raytrace/RAYTRACE"
    cmd = ["RAYTRACE", "-p", "1", "-m64", "inputs/car.env"]

class VOLREND(Process):
    cwd = args.benchdir + "/volrend"
    executable = args.benchdir + "/volrend/VOLREND"
    cmd = ["VOLREND", "1", "inputs/head", "8"]

class VOLREND_NPL(Process):
    cwd = args.benchdir + "/volrend-no_print_lock"
    executable = args.benchdir + "/volrend-no_print_lock/VOLREND-NPL"
    cmd = ["VOLREND-NPL", "1", "inputs/head", "8"]

class WATER_NSQUARED(Process):
    cwd = args.benchdir + "/water-nsquared"
    executable = args.benchdir + "/water-nsquared/WATER-NSQUARED"
    input = args.benchdir + "/water-nsquared/inputs/n512-p1"
    cmd = ["WATER-NSQUARED"]

class WATER_SPATIAL(Process):
    cwd = args.benchdir + "/water-spatial"
    executable = args.benchdir + "/water-spatial/WATER-SPATIAL"
    input = args.benchdir + "/water-spatial/inputs/n512-p1"
    cmd = ["WATER-SPATIAL"]

class CHOLESKY(Process):
    cwd = args.benchdir + "/cholesky"
    executable = args.benchdir + "/cholesky/CHOLESKY"
    input = args.benchdir + "/cholesky/inputs/tk15.O"
    cmd = ["CHOLESKY", "-p1"]

class FFT(Process):
    cwd = args.benchdir + "/fft"
    executable = args.benchdir + "/fft/FFT"
    cmd = ["FFT", "-p1", "-m16"]

class LU_CONT(Process):
    cwd = args.benchdir + "/lu-contiguous_blocks"
    executable = args.benchdir + "/lu-contiguous_blocks/LU-CONT"
    cmd = ["LU-CONT", "-p1", "-n512"]

class LU_NOCONT(Process):
    cwd = args.benchdir + "/lu-non_contiguous_blocks"
    executable = args.benchdir + "/lu-non_contiguous_blocks/LU-NOCONT"
    cmd = ["LU-NOCONT", "-p1", "-n512"]

class RADIX(Process):
    cwd = args.benchdir + "/radix"
    executable = args.benchdir + "/radix/RADIX"
    cmd = ["RADIX", "-p1", "-n1048576"]

multiprocesses = []
numThreads = 1

if args.bench:
    apps = args.bench.split("-")
    if len(apps) != args.num_cpus:
        print("number of benchmarks not equal to set num_cpus!")
        sys.exit(1)

    for app in apps:
        try:
            if get_runtime_isa() == ISA.ARM:
                exec(
                    "workload = %s('arm_%s', 'linux', '%s')"
                    % (app, args.arm_iset, args.spec_input)
                )
            else:
                # TARGET_ISA has been removed, but this is missing a ], so it
                # has incorrect syntax and wasn't being used anyway.
                exec(
                    "workload = %s(buildEnv['TARGET_ISA', 'linux', '%s')"
                    % (app, args.spec_input)
                )
            multiprocesses.append(workload.makeProcess())
        except:
            print(
                f"Unable to find workload for {get_runtime_isa().name()}: {app}",
                file=sys.stderr,
            )
            sys.exit(1)
elif args.cmd:
    multiprocesses, numThreads = get_processes(args)
else:
    print("No workload specified. Exiting!\n", file=sys.stderr)
    sys.exit(1)


(CPUClass, test_mem_mode, FutureClass) = Simulation.setCPUClass(args)
CPUClass.numThreads = numThreads

# Check -- do not allow SMT with multiple CPUs
if args.smt and args.num_cpus > 1:
    fatal("You cannot use SMT with multiple CPUs!")

np = args.num_cpus
mp0_path = multiprocesses[0].executable
system = System(
    cpu=[CPUClass(cpu_id=i) for i in range(np)],
    mem_mode=test_mem_mode,
    mem_ranges=[AddrRange(args.mem_size)],
    cache_line_size=args.cacheline_size,
)

if numThreads > 1:
    system.multi_thread = True

# Create a top-level voltage domain
system.voltage_domain = VoltageDomain(voltage=args.sys_voltage)

# Create a source clock for the system and set the clock period
system.clk_domain = SrcClockDomain(
    clock=args.sys_clock, voltage_domain=system.voltage_domain
)

# Create a CPU voltage domain
system.cpu_voltage_domain = VoltageDomain()

# Create a separate clock domain for the CPUs
system.cpu_clk_domain = SrcClockDomain(
    clock=args.cpu_clock, voltage_domain=system.cpu_voltage_domain
)

# All cpus belong to a common cpu_clk_domain, therefore running at a common
# frequency.
for cpu in system.cpu:
    cpu.clk_domain = system.cpu_clk_domain

for i in range(np):
    if args.smt:
        system.cpu[i].workload = multiprocesses
    elif len(multiprocesses) == 1:
        system.cpu[i].workload = multiprocesses[0]
    else:
        system.cpu[i].workload = multiprocesses[i]

    if args.simpoint_profile:
        system.cpu[i].addSimPointProbe(args.simpoint_interval)

    if args.checker:
        system.cpu[i].addCheckerCpu()

    if args.bp_type:
        bpClass = ObjectList.bp_list.get(args.bp_type)
        system.cpu[i].branchPred = bpClass()

    if args.indirect_bp_type:
        indirectBPClass = ObjectList.indirect_bp_list.get(
            args.indirect_bp_type
        )
        system.cpu[i].branchPred.indirectBranchPred = indirectBPClass()

    system.cpu[i].createThreads()


MemClass = Simulation.setMemClass(args)
system.membus = SystemXBar()
system.system_port = system.membus.cpu_side_ports
CacheConfig.config_cache(args, system)
MemConfig.config_mem(args, system)
config_filesystem(system, args)

system.workload = SEWorkload.init_compatible(mp0_path)

if args.wait_gdb:
    system.workload.wait_for_remote_gdb = True

root = Root(full_system=False, system=system)
Simulation.run(args, root, system, FutureClass)
