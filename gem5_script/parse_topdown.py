
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
decodedInsts = 0
uOpsNotDelivered = 0
decodeWidth = 0

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
        elif "decode.squashCycles" in key:
            squashCycles = int(value)
        elif "decodedInsts" in key:
            decodedInsts = int(value)
        elif "uOpsNotDelivered" in key:
            uOpsNotDelivered = int(value)

with open(config_file, 'r') as c:
    lines = c.readlines()

    for line in lines:
        if "decodeWidth" in line:
            decodeWidth = int(line.split('=')[-1])
            break

numSlots = decodeWidth * numCycles
retiring = simOps/numSlots
bad_speculation = (decodedInsts - simOps + decodeWidth*squashCycles)/numSlots
frontend_bound = uOpsNotDelivered/numSlots
backend_bound = 1 - (retiring + bad_speculation + frontend_bound)

print("Retiring:", retiring)
print("Bad speculation:", bad_speculation)
print("Frontend bound:", frontend_bound)
print("Backend bound:", backend_bound)
