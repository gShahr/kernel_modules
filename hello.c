// SPDX-License-Identifier: GPL-2.0
#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/init.h>

MODULE_LICENSE("GPL");
MODULE_AUTHOR("Gabriel Shahrouzi");
MODULE_DESCRIPTION("Says hello on load and bye when removed");

static int __init hello_init(void)
{
	pr_info("Hello\n");
	return 0;
}

static void __exit hello_exit(void)
{
	pr_info("Bye\n");
}

module_init(hello_init);
module_exit(hello_exit);
