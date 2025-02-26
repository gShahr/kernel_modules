#!/bin/bash

cd /opt/linux_work/kernel_modules/generate-panic
make clean
make
sudo rmmod panic.c
sudo insmod panic.ko
sudo dmesg | tail