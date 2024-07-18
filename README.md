# Top-down analysis with Gem5 simulator

### Build Gem5 simulator
* Clone this repository
```
$ git clone --recursive git@github.com:wanjudoh/gem5-top-down.git
$ cd gem5-top-down
```

* Patch를 적용합니다.
    * 0001-Add-L3-and-DRAM-device-size-options.patch
        * L3 cache와 DRAM device size를 설정할 수 있도록 한 patch입니다.
    * 0002-Add-cpu-options.patch
        * CPU의 pipeline width와 buffer들의 크기를 설정할 수 있도록 한 patch입니다.
    * 0003-Add-top-level-analysis.patch
        * Top-level 분석을 위한 patch입니다.
    * 0004-Add-backend-bound-analysis.patch
        * Backend bound breakdown을 위한 patch입니다.
    * 0005-Add-cache-bound-analysis.patch
        * Memory bound breakdown을 위한 patch입니다.
```
$ cd gem5_script
$ ./apply_patches.sh
```

* Build Gem5 simulator
    * RISC-V ISA를 사용하도록 하여 gem5를 build합니다.
```
$ scons ./build/RISCV/gem5.opt -j`nproc`
```

## Splash-4

### Build Splash-4
* Splash-4를 clone한 뒤 risc-v cross-compiler를 사용하여 build합니다.
* volrend*는 build하는 방법이 까다롭기 때문에 제외하였습니다.
* 만약 risc-v cross-compiler가 설치되어있지 않다면 [설치](https://github.com/riscv-collab/riscv-gnu-toolchain/tree/master)해주세요.

```
$ cd Splash-4
$ rm -r Splash-4/volrend*
$ vim Makefile.config

#### EDIT HERE ####
CC := PATH/TO/riscv/bin/riscv64-unknown-linux-gnu-gcc
CFLAGS :=  ... -static  # add -static flag
###################

$ make
```

### Run Splash-4
* gem5_script 디렉토리 아래에 시뮬레이션 실행을 위한 스크립트들이 포함되어있습니다.
    * config_riscv.cfg: 시뮬레이션할 system의 옵션들을 지정해주는 config file
    * gem5.py: gem5를 실행시키는 python script
        * Usage: `$ python3 gem5.py -f <.cfg file> -o <result directory name> -b <benchmark name>`
    * run_gem5_riscv.sh: 여러 벤치마크를 동시에 실행시킬 수 있도록 작성한 wrapper script
        * `MP_DEGREE`: 동시에 실행할 프로세스 수
        * `benchmarks`: 실행시킬 벤치마크 목록
    * se_splash.py: 기존 gem5에서 제공하는 se.py 파일을 수정한 python script
        * Splash-4 벤치마크를 실행시키기 위한 옵션들이 정의되어있습니다.
```
$ cd gem5_script

# single program
$ python3 ./gem5.py -f config_riscv.cfg -o test -b fft

# multi-program
$ ./run_gem5_riscv.sh
```
* 시뮬레이션을 실행하고 나면 gem5_script/results 디렉토리 아래에 시뮬레이션 결과 파일들이 저장됩니다.

## Microbenchmark

* microbenchmarks 디렉토리 아래에 코드와 binary들이 포함되어있습니다.
    * control: random_#.cc라는 이름의 파일들이 포함되어있으며 #은 branch문의 randomness를 나타냅니다.
    * dependency: chain_#.cc라는 이름의 파일들이 포함되어있으며 #은 read-after-write dependency간의 거리를 나타냅니다.
    * execution: int/fp, add/div/mul을 수행하는 microbenchmark들이 포함되어있습니다.
    * memory: load/store, dependent/independent/random을 수행하는 microbenchmark들이 포함되어있습니다.
* micro_script 디렉토리 아래에 microbenchmark들을 실행시킬 수 있는 스크립트들이 포함되어있습니다.
```
$ cd micro_script

# gem5, microbenchmark.py, microbenchmarks/ 경로 수정
$ vim micro_config.cfg

# run microbenchmark
$ python3 ./gem5_microbenchmark.py -f micro_config.cfg -o <output path> -b <microbenchmark name> -i <iter> [-s <size>]

# example: Randomly load 16KB of data
$ python3 ./gem5_microbenchmark.py -f micro_config.cfg -o <OUTDIR> -b load_random -i 100000 -s 512
```

## Top-down analysis
* gem5_script 디렉토리 아래에 top-level 분석을 수행해주는 python 스크립트가 포함되어있습니다.
* python 스크립트에서는 인자로 넣어주는 디렉토리 경로에 위치한 config 파일과 result 파일을 parsing하여 top-down 분석 결과를 출력해줍니다.
```
$ cd gem5_script
$ python3 ./parse_topdown.py <result directory>

# Ex) python3 ./parse_topdown.py ../micro_script/results/dep_6/dependency/chain_6/
Retiring         0.18844549832499766
Bad speculation  0.0008710425458097292
Frontend bound   0.37639162243244656
Backend bound    0.4342918366967461

Memory bound     0.1466118576056442
Core bound       0.40294662321065733

Store bound      0.022279821834374613
L1 bound         0.11545322754428365
L2 bound         0.0004792079482686507
L3 bound         0.0001608710328532471
DRAM bound       0.008238729245864043
```
