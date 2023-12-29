# Top-down analysis with Gem5 simulator

### Build Gem5 simulator
* Clone this repository
```
$ git clone --recursive git@github.com:wanjudoh/gem5-top-down.git
$ cd gem5-top-down
```

* Patch를 적용합니다.
    * 001: L3 cache와 DRAM device size를 설정할 수 있도록 한 patch입니다.
    * 002: CPU의 pipeline width와 buffer들의 크기를 설정할 수 있도록 한 patch입니다.
    * 003: Top-down 분석을 위한 patch입니다.
```
$ cd gem5
$ patch -p1 < ../patches/001-Add-L3-and-DRAM-device-size-options.patch
$ patch -p1 < ../patches/002-Add-cpu-options.patch
$ patch -p1 < ../patches/003-Top-level.patch
```

* Build Gem5 simulator
    * RISC-V ISA를 사용하도록 하여 gem5를 build합니다.
```
$ scons ./build/RISCV/gem5.opt -j`nproc`
```

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

### Run
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

## Top-level analysis
* gem5_script 디렉토리 아래에 top-level 분석을 수행해주는 python 스크립트가 포함되어있습니다.
```
$ cd gem5_script
$ python3 ./parse_topdown.py <result directory>

# Ex) python3 ./parse_topdown.py ./results/12-28-19-01-riscv/fft
Retiring: 0.3057830063700331
Bad speculation: 0.0070259509263605685
Frontend bound: 0.22879423265227428
Backend bound: 0.45839681005133204
```
