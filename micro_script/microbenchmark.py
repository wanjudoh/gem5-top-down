
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
    # ---------------Control--------------- #
    if workloads[0] == "random_0":
        random_0().cmd.append(m5.params.String(workloads[1]))
        process = random_0()
    elif workloads[0] == "random_25":
        random_25().cmd.append(m5.params.String(workloads[1]))
        process = random_25()
    elif workloads[0] == "random_50":
        random_50().cmd.append(m5.params.String(workloads[1]))
        process = random_50()
    elif workloads[0] == "random_75":
        random_75().cmd.append(m5.params.String(workloads[1]))
        process = random_75()
    elif workloads[0] == "random_100":
        random_100().cmd.append(m5.params.String(workloads[1]))
        process = random_100()

    # ---------------Dependency--------------- #
    elif workloads[0] == "chain_2":
        chain_2().cmd.append(m5.params.String(workloads[1]))
        process = chain_2()
    elif workloads[0] == "chain_4":
        chain_4().cmd.append(m5.params.String(workloads[1]))
        process = chain_4()
    elif workloads[0] == "chain_6":
        chain_6().cmd.append(m5.params.String(workloads[1]))
        process = chain_6()
    elif workloads[0] == "chain_8":
        chain_8().cmd.append(m5.params.String(workloads[1]))
        process = chain_8()

    # ---------------Execution--------------- #
    elif workloads[0] == "int_add":
        int_add().cmd.append(m5.params.String(workloads[1]))
        process = int_add()
    elif workloads[0] == "int_mul":
        int_mul().cmd.append(m5.params.String(workloads[1]))
        process = int_mul()
    elif workloads[0] == "int_div":
        int_div().cmd.append(m5.params.String(workloads[1]))
        process = int_div()
    elif workloads[0] == "fp_add":
        fp_add().cmd.append(m5.params.String(workloads[1]))
        process = fp_add()
    elif workloads[0] == "fp_mul":
        fp_mul().cmd.append(m5.params.String(workloads[1]))
        process = fp_mul()
    elif workloads[0] == "fp_div":
        fp_div().cmd.append(m5.params.String(workloads[1]))
        process = fp_div()

    # ---------------Memory--------------- #
    elif workloads[0] == "load_dependent":
        load_dependent().cmd.append(m5.params.String(workloads[1]))
        load_dependent().cmd.append(m5.params.String(workloads[2]))
        process = load_dependent()
    elif workloads[0] == "load_independent":
        load_independent().cmd.append(m5.params.String(workloads[1]))
        load_independent().cmd.append(m5.params.String(workloads[2]))
        process = load_independent()
    elif workloads[0] == "load_random":
        load_random().cmd.append(m5.params.String(workloads[1]))
        load_random().cmd.append(m5.params.String(workloads[2]))
        process = load_random()
    elif workloads[0] == "store_independent":
        store_independent().cmd.append(m5.params.String(workloads[1]))
        store_independent().cmd.append(m5.params.String(workloads[2]))
        process = store_independent()
    elif workloads[0] == "store_random":
        store_random().cmd.append(m5.params.String(workloads[1]))
        store_random().cmd.append(m5.params.String(workloads[2]))
        process = store_random()
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
    help="Bench directory of microbenchmark",)

Options.addCommonOptions(parser)
Options.addSEOptions(parser)

args = parser.parse_args()

# ---------------Control--------------- #
class random_0(Process):
    cwd = args.benchdir + "/control"
    executable = args.benchdir + "/control/random_0"
    cmd = ["random_0"]

class random_25(Process):
    cwd = args.benchdir + "/control"
    executable = args.benchdir + "/control/random_25"
    cmd = ["random_25"]

class random_50(Process):
    cwd = args.benchdir + "/control"
    executable = args.benchdir + "/control/random_50"
    cmd = ["random_50"]

class random_75(Process):
    cwd = args.benchdir + "/control"
    executable = args.benchdir + "/control/random_75"
    cmd = ["random_75"]

class random_100(Process):
    cwd = args.benchdir + "/control"
    executable = args.benchdir + "/control/random_100"
    cmd = ["random_100"]

# ---------------Dependency--------------- #
class chain_2(Process):
    cwd = args.benchdir + "/dependency"
    executable = args.benchdir + "/dependency/chain_2"
    cmd = ["chain_2"]

class chain_4(Process):
    cwd = args.benchdir + "/dependency"
    executable = args.benchdir + "/dependency/chain_4"
    cmd = ["chain_4"]

class chain_6(Process):
    cwd = args.benchdir + "/dependency"
    executable = args.benchdir + "/dependency/chain_6"
    cmd = ["chain_6"]

class chain_8(Process):
    cwd = args.benchdir + "/dependency"
    executable = args.benchdir + "/dependency/chain_8"
    cmd = ["chain_8"]

# ---------------Execution--------------- #
class int_add(Process):
    cwd = args.benchdir + "/execution"
    executable = args.benchdir + "/execution/int_add"
    cmd = ["int_add"]

class int_mul(Process):
    cwd = args.benchdir + "/execution"
    executable = args.benchdir + "/execution/int_mul"
    cmd = ["int_mul"]

class int_div(Process):
    cwd = args.benchdir + "/execution"
    executable = args.benchdir + "/execution/int_div"
    cmd = ["int_div"]

class fp_add(Process):
    cwd = args.benchdir + "/execution"
    executable = args.benchdir + "/execution/fp_add"
    cmd = ["fp_add"]

class fp_mul(Process):
    cwd = args.benchdir + "/execution"
    executable = args.benchdir + "/execution/fp_mul"
    cmd = ["fp_mul"]

class fp_div(Process):
    cwd = args.benchdir + "/execution"
    executable = args.benchdir + "/execution/fp_div"
    cmd = ["fp_div"]

# ---------------Memory--------------- #
class load_dependent(Process):
    cwd = args.benchdir + "/memory"
    executable = args.benchdir + "/memory/load_dependent"
    cmd = ["load_dependent"]

class load_independent(Process):
    cwd = args.benchdir + "/memory"
    executable = args.benchdir + "/memory/load_independent"
    cmd = ["load_independent"]

class load_random(Process):
    cwd = args.benchdir + "/memory"
    executable = args.benchdir + "/memory/load_random"
    cmd = ["load_random"]

class store_independent(Process):
    cwd = args.benchdir + "/memory"
    executable = args.benchdir + "/memory/store_independent"
    cmd = ["store_independent"]

class store_random(Process):
    cwd = args.benchdir + "/memory"
    executable = args.benchdir + "/memory/store_random"
    cmd = ["store_random"]


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
