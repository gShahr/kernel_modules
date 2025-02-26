#!/bin/bash
# Taken from https://nixyogi.github.io/wiki/kernel/debugging/Solving-syzkaller-bugs.html#process-for-solving-a-syzkaller-bug

KERNEL_IMG_PATH=$1
RFS_IMG_PATH=$2

qemu-system-x86_64 \
    -m 2G \
    -smp 2 \
    -kernel ${KERNEL_IMG_PATH} \
    -append "console=ttyS0 root=/dev/sda1 earlyprintk=serial net.ifnames=0 nokaslr" \
    -drive file=${RFS_IMG_PATH},format=raw \
    -net user,host=10.0.2.10,hostfwd=tcp:127.0.0.1:10021-:22 \
    -net nic,model=e1000 \
    -enable-kvm \
    -nographic \
    -pidfile vm.pid \
    2>&1 | tee vm.log
