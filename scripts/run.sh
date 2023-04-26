# 4 bits, man 1, exp 3
sh end_to_end.sh resnet18 CIFAR10 128 adaptive_block_float 4 1 0
sh end_to_end.sh resnet18 CIFAR10 128 adaptive_fp 4 1 0
sh end_to_end.sh resnet18 CIFAR10 128 block_fp 4 1 0
sh end_to_end.sh resnet18 CIFAR10 128 fp_n 4 1 0

# 6 bits, man 3, exp 2
sh end_to_end.sh resnet18 CIFAR10 128 adaptive_block_float 6 3 0
sh end_to_end.sh resnet18 CIFAR10 128 adaptive_fp 6 3 0
sh end_to_end.sh resnet18 CIFAR10 128 block_fp 6 3 0
sh end_to_end.sh resnet18 CIFAR10 128 fp_n 6 3 0

# 8 bits, man 4, exp 3
sh end_to_end.sh resnet18 CIFAR10 128 adaptive_block_float 8 4 0
sh end_to_end.sh resnet18 CIFAR10 128 adaptive_fp 8 4 0
sh end_to_end.sh resnet18 CIFAR10 128 block_fp 8 4 0
sh end_to_end.sh resnet18 CIFAR10 128 fp_n 8 4 0

# 16 bits, man 10, exp 5
sh end_to_end.sh resnet18 CIFAR10 128 adaptive_block_float 16 10 0
sh end_to_end.sh resnet18 CIFAR10 128 adaptive_fp 16 10 0
sh end_to_end.sh resnet18 CIFAR10 128 block_fp 16 10 0
sh end_to_end.sh resnet18 CIFAR10 128 fp_n 16 10 0

# 32 bits, man 23, exp 8
sh end_to_end.sh resnet18 CIFAR10 128 adaptive_block_float 32 23 0
sh end_to_end.sh resnet18 CIFAR10 128 adaptive_fp 32 23 0
sh end_to_end.sh resnet18 CIFAR10 128 block_fp 32 23 0
sh end_to_end.sh resnet18 CIFAR10 128 fp_n 32 23 0