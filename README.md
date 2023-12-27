# Top-down analysis with Gem5 simulator

### Clone this repository
```
$ git clone --recursive git@github.com:wanjudoh/gem5-top-down.git
$ cd gem5-top-down
```

### Apply the patches.
```
$ cd gem5
$ patch -p1 < ../001-L3-cache.patch
$ patch -p1 < ../002-DRAM-device-option.patch
$ patch -p1 < ../003-Top-level.patch
```

### Build Gem5 simulator.
```
$ scons ./build/ARM/gem5.opt -j16
$ scons ./build/RISCV/gem5.opt -j16
```

### Build Splash-4
```
$ cd Splash-4
$ vim Makefile.config

# EDIT HERE
CC := PATH/TO/riscv64-gcc

$ make
```
#### Troubleshooting
* volrend*
    * 
* water*
    * 