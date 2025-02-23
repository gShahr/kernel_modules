// SPDX-License-Identifier: GPL-2.0
#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/init.h>
#include <linux/moduleparam.h>

MODULE_LICENSE("GPL");
MODULE_AUTHOR("Gabriel Shahrouzi");
MODULE_DESCRIPTION("Generate panic");

static int __init init_panic(void)
{
	pr_info("Invoking panic");
	panic("Panic called\n");
	return 0;
}

static void __exit exit_panic(void)
{
	pr_info("Bye\n");
}

module_init(init_panic);
module_exit(exit_panic);
