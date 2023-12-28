#!/bin/sh

### MODIFY HERE! ###
CONFIGFILE="config_riscv.cfg"  # Config file
OUTPUTDIR="riscv"
DATE="$(date +%m-%d-%H-%M)"
MP_DEGREE=10  # Number of simulators to run concurrently
###################

run_bench() {
	echo ""
	echo "#### Running $1 ..."
	python3 gem5.py -f ${CONFIGFILE} -o "${DATE}-${OUTPUTDIR}" -b $1
}

benchmarks=(barnes fmm ocean-cont radiosity raytrace \
	water-spatial cholesky fft lu-cont radix)

#benchmarks=(fmm)

for bench in "${benchmarks[@]}"
do
	while [ $(jobs | wc | awk '{print $1}') -ge ${MP_DEGREE} ]; do
		sleep 30
	done
	run_bench $bench &
done
