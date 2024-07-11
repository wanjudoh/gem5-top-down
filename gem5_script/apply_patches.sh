#!/bin/bash

cd ../gem5
patch -p1 < ../patches/0001-Add-L3-and-DRAM-device-size-options.patch
patch -p1 < ../patches/0002-Add-cpu-options.patch
patch -p1 < ../patches/0003-Add-top-level-analysis.patch
patch -p1 < ../patches/0004-Add-backend-bound-analysis.patch
patch -p1 < ../patches/0005-Add-cache-bound-analysis.patch
