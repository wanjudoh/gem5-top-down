#!/bin/python3

import sys
import os
import time
import argparse
import configparser
import datetime
import subprocess

def AddOption(config, tag) :
    parm=""
    options=config.options(tag)
    for option_name in options:
        option_value = config.get(tag, option_name)
        if option_value == "" :
            parm = parm + " " + option_name
        else :
            parm = parm + " " + option_name + "=" + option_value
    return parm

def MakeDir(path, rmf):
    is_exist = os.path.exists(path)
    rm_bool = is_exist and rmf

    if rm_bool :
        os.system("rm -rf " + path)
 
    if not os.path.exists(path):
        os.mkdir(path)
        os.system("chmod g+w " + path)

def RunBench(config, root_dir, output_dir, workload, iterations, size):
    gem5_config_option  = AddOption(config, "CONFIGOPT")

    GEM5_BUILD_FILE     = config.get("TRACE", "BUILDFILE").split('\n')[0]

    GEM5_CONFIG_FILE    = config.get("TRACE", "CONFIGFILE").split('\n')[0]

    GEM5_BENCH_DIR      = config.get("TRACE", "BENCHDIR").split('\n')[0]

    if "random_" in workload :
        output_dir = output_dir + "/control"
    elif "chain" in workload :
        output_dir = output_dir + "/dependency"
    elif "int" in workload or "fp" in workload :
        output_dir = output_dir + "/execution"
    else :
        output_dir = output_dir + "/memory"

    MakeDir(output_dir, False)
    output_dir = output_dir + "/" + workload
    MakeDir(output_dir, False)

    gem5_build_option = " --outdir=" + output_dir \
            + " --stats-file=" + workload + ".result"
 
    stdout_file = workload + ".out"
    stderr_file = workload + ".err"
    
    if size == None:
        cmd = GEM5_BUILD_FILE + " " \
            + gem5_build_option + " " \
            + GEM5_CONFIG_FILE + " " \
            + gem5_config_option + " " \
            + "--cmd='" + workload + ";" + iterations + "' "\
            + "--benchdir " + GEM5_BENCH_DIR\
            + " > " + output_dir + "/"+ stdout_file \
            + " 2> " + output_dir + "/" + stderr_file
    else:
        cmd = GEM5_BUILD_FILE + " " \
            + gem5_build_option + " " \
            + GEM5_CONFIG_FILE + " " \
            + gem5_config_option + " " \
            + "--cmd='" + workload + ";" + iterations + ";" + size + "' "\
            + "--benchdir " + GEM5_BENCH_DIR\
            + " > " + output_dir + "/"+ stdout_file \
            + " 2> " + output_dir + "/" + stderr_file

    print("GEM5_BUILD_FILE:", GEM5_BUILD_FILE)
    print("gem5 build_option:", gem5_build_option)
    print("GEM5 CONFIG FILE:", GEM5_CONFIG_FILE)
    print("gem5 config option:", gem5_config_option)
    print("CMD:", cmd)
    subprocess.run(cmd, shell=True)

    time.sleep(1)

################### argparser #######################
parser = argparse.ArgumentParser(description='GEM5 script')

parser.add_argument('-f', '--configfile', action='store', dest='configfile',
        help='.cfg config file')
parser.add_argument('-o', '--outputdir', action='store', dest='outputdir',
        help='output directory name')
parser.add_argument('-b', '--bench', default="",
        help="The benchmark to run in syscall emulation mode")

parser.add_argument('-i', '--iterations', action='store', dest='iterations',
        help='number of iteartions')
parser.add_argument('-s', '--size', action='store', dest='size',
        help='memory size (512: 16KB, 1024: 32KB, 2048: 64KB ...')

args = parser.parse_args()

config = configparser.ConfigParser()
config.optionxform = str
config.read(args.configfile, encoding="UTF-8")

if args.bench:
    workload=args.bench
else:
    print("No workload specified.\nPlease write option --bench or -b \nExiting!\n", file=sys.stderr)
    sys.exit(1)

PWD=os.getcwd()
ROOT_DIR=PWD+"/.."
OUTPUT_DIR=PWD+"/results"

if not os.path.exists(OUTPUT_DIR):
    MakeDir(OUTPUT_DIR, False)

if args.outputdir == None:
    date=datetime.datetime.now().strftime("%m-%d")
    time_h_m=datetime.datetime.now().strftime("%H-%M")
    OUTPUT_DIR=OUTPUT_DIR+'/'+date+'-'+time_h_m
else:
    OUTPUT_DIR=OUTPUT_DIR+'/'+args.outputdir
MakeDir(OUTPUT_DIR, False)

if args.iterations == None:
    print("Please provide the number of iterations: option -i")
    sys.exit(1)

if "random_" in workload or "chain" in workload or "int" in workload or "fp" in workload:
    if args.size != None:
        print("erase the -s option for this microbenchmark")
        sys.exit(1)

if "load" in workload or "store" in workload:
    if args.size == None:
        print("Please provide the size of memory(512: 16KB, 1024: 32KB, 2048: 64KB ...): option -s")
        sys.exit(1)

################## Print Dir Infos  ######################
print("Root directory: ", ROOT_DIR)
print("Output directory: ", OUTPUT_DIR)

################## Run Benchmarks  ######################
RunBench(config, ROOT_DIR, OUTPUT_DIR, workload, args.iterations, args.size)

