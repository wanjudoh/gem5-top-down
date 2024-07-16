
import sys
import os

if len(sys.argv) < 2:
    print("Usage: python3", sys.argv[0], "<result_directory_path>")
    print("Ex) python3", sys.argv[0], "./results/12-28-19-01-riscv/fft")
    exit(1)

os.chdir(sys.argv[1])
file_names = os.listdir()
for filename in file_names:
    if os.path.splitext(filename)[1] == ".result":
        result_file = filename
    elif os.path.splitext(filename)[1] == ".ini":
        config_file = filename

simOps = 0
numCycles = 0
squashCycles = 0
dispatchedInsts = 0
uOpsNotDelivered = 0
issueWidth = 0
dispatchWidth = 0

with open(result_file, 'r') as f:
    lines = f.readlines()

    for line in lines:
        if len(line) < 2: continue
        key = line.split()[0]
        value = line.split()[1]
        if "simOps" in key:
            simOps = int(value)
        elif "numCycles" in key:
            numCycles = int(value)
        elif "system.cpu.iew.squashCycles" in key:
            squashCycles = int(value)
        elif "system.cpu.iew.dispatchedInsts" in key:
            dispatchedInsts = int(value)
        elif "uOpsNotDelivered" in key:
            uOpsNotDelivered = int(value)
        elif "system.cpu.iew.noExecuteCycles" in key:
            noExecuteCycles = int(value)
        elif "system.cpu.iew.oneExecuteCycles" in key:
            oneExecuteCycles = int(value)
        elif "system.cpu.iew.anyLoadCycles" in key:
            anyLoadCycles = int(value)
        elif "system.cpu.iew.anyStoreCycles" in key:
            anyStoreCycles = int(value)
        elif "system.cpu.iew.memStallsL1Miss" in key:
            memStallsL1Miss = int(value)
        elif "system.cpu.iew.memStallsL2Miss" in key:
            memStallsL2Miss = int(value)
        elif "system.cpu.iew.memStallsL3Miss" in key:
            memStallsL3Miss = int(value)


with open(config_file, 'r') as c:
    lines = c.readlines()

    for line in lines:
        if "issueWidth" in line:
            issueWidth = int(line.split('=')[-1])
        if "dispatchWidth" in line:
            dispatchWidth = int(line.split("=")[-1])


numSlots = issueWidth * numCycles
retiring = simOps/numSlots
bad_speculation = (dispatchedInsts - simOps + dispatchWidth*squashCycles)/numSlots
frontend_bound = uOpsNotDelivered/numSlots
backend_bound = 1 - (retiring + bad_speculation + frontend_bound)
if backend_bound < 0:
    backend_bound = 0

print("Retiring\t", retiring)
print("Bad speculation\t", bad_speculation)
print("Frontend bound\t", frontend_bound)
print("Backend bound\t", backend_bound)
print()

execution_stalls = (noExecuteCycles + oneExecuteCycles) / numCycles
memory_bound = (anyLoadCycles + anyStoreCycles) / numCycles
core_bound = execution_stalls - memory_bound

print("Memory bound\t", memory_bound)
print("Core bound\t", core_bound)
print()

store_bound = anyStoreCycles / numCycles
L2_bound = memStallsL1Miss / numCycles
L3_bound = memStallsL2Miss / numCycles
DRAM_bound = memStallsL3Miss / numCycles
L1_bound = (anyLoadCycles / numCycles) - (L2_bound + L3_bound + DRAM_bound)

print("Store bound\t", store_bound)
print("L1 bound\t", L1_bound)
print("L2 bound\t", L2_bound)
print("L3 bound\t", L3_bound)
print("DRAM bound\t", DRAM_bound)
