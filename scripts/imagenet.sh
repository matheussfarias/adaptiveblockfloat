# 4 bits, man 1, exp 3
#sh end_to_end.sh resnet50 IMAGENET 128 adaptive_block_fp 4 1 0
#sh end_to_end.sh resnet50 IMAGENET 128 adaptive_fp 4 1 0
#sh end_to_end.sh resnet50 IMAGENET 128 block_fp 4 1 0
#sh end_to_end.sh resnet50 IMAGENET 128 fp_n 4 1 0

# 6 bits, man 3, exp 2
#sh end_to_end.sh resnet50 IMAGENET 128 adaptive_block_fp 6 3 0
#sh end_to_end.sh resnet50 IMAGENET 128 adaptive_fp 6 3 0
#sh end_to_end.sh resnet50 IMAGENET 128 block_fp 6 3 0
#sh end_to_end.sh resnet50 IMAGENET 128 fp_n 6 3 0

# 8 bits, man 4, exp 3
#resnet50
#sh end_to_end.sh resnet50 IMAGENET 128 adaptive_block_fp 8 4 0
#sh end_to_end.sh resnet50 IMAGENET 128 adaptive_fp 8 4 0
#sh end_to_end.sh resnet50 IMAGENET 128 block_fp 8 4 0
#sh end_to_end.sh resnet50 IMAGENET 128 fp_n 8 4 0

#deit_base
sh end_to_end.sh deit_base IMAGENET 128 adaptive_block_fp 8 4 0
#sh end_to_end.sh deit_base IMAGENET 128 adaptive_fp 8 4 0
#sh end_to_end.sh deit_base IMAGENET 128 block_fp 8 4 0
#sh end_to_end.sh deit_base IMAGENET 128 fp_n 8 4 0

#vit_base
sh end_to_end.sh vit_base IMAGENET 128 adaptive_block_fp 8 4 0
#sh end_to_end.sh vit_base IMAGENET 128 adaptive_fp 8 4 0
#sh end_to_end.sh vit_base IMAGENET 128 block_fp 8 4 0
#sh end_to_end.sh vit_base IMAGENET 128 fp_n 8 4 0

#vgg19_bn
sh end_to_end.sh vgg19_bn IMAGENET 128 adaptive_block_fp 8 4 0
#sh end_to_end.sh vgg19_bn IMAGENET 128 adaptive_fp 8 4 0
#sh end_to_end.sh vgg19_bn IMAGENET 128 block_fp 8 4 0
#sh end_to_end.sh vgg19_bn IMAGENET 128 fp_n 8 4 0

#mobilenet
sh end_to_end.sh mobilenet IMAGENET 128 adaptive_block_fp 8 4 0
#sh end_to_end.sh mobilenet IMAGENET 128 adaptive_fp 8 4 0
#sh end_to_end.sh mobilenet IMAGENET 128 block_fp 8 4 0
#sh end_to_end.sh mobilenet IMAGENET 128 fp_n 8 4 0

# 10 bits, man 5, exp 4
#resnet50
sh end_to_end.sh resnet50 IMAGENET 128 adaptive_block_fp 10 5 0
#sh end_to_end.sh resnet50 IMAGENET 128 adaptive_fp 10 5 0
#sh end_to_end.sh resnet50 IMAGENET 128 block_fp 10 5 0
#sh end_to_end.sh resnet50 IMAGENET 128 fp_n 10 5 0

#deit_base
sh end_to_end.sh deit_base IMAGENET 128 adaptive_block_fp 10 5 0
#sh end_to_end.sh deit_base IMAGENET 128 adaptive_fp 10 5 0
#sh end_to_end.sh deit_base IMAGENET 128 block_fp 10 5 0
#sh end_to_end.sh deit_base IMAGENET 128 fp_n 10 5 0

#vit_base
sh end_to_end.sh vit_base IMAGENET 128 adaptive_block_fp 10 5 0
#sh end_to_end.sh vit_base IMAGENET 128 adaptive_fp 10 5 0
#sh end_to_end.sh vit_base IMAGENET 128 block_fp 10 5 0
#sh end_to_end.sh vit_base IMAGENET 128 fp_n 10 5 0

#vgg19_bn
sh end_to_end.sh vgg19_bn IMAGENET 128 adaptive_block_fp 10 5 0
#sh end_to_end.sh vgg19_bn IMAGENET 128 adaptive_fp 10 5 0
#sh end_to_end.sh vgg19_bn IMAGENET 128 block_fp 10 5 0
#sh end_to_end.sh vgg19_bn IMAGENET 128 fp_n 10 5 0

#mobilenet
sh end_to_end.sh mobilenet IMAGENET 128 adaptive_block_fp 10 5 0
#sh end_to_end.sh mobilenet IMAGENET 128 adaptive_fp 10 5 0
#sh end_to_end.sh mobilenet IMAGENET 128 block_fp 10 5 0
#sh end_to_end.sh mobilenet IMAGENET 128 fp_n 10 5 0

# 12 bits, man 6, exp 5
#resnet50
sh end_to_end.sh resnet50 IMAGENET 128 adaptive_block_fp 12 6 0
#sh end_to_end.sh resnet50 IMAGENET 128 adaptive_fp 12 6 0
#sh end_to_end.sh resnet50 IMAGENET 128 block_fp 12 6 0
#sh end_to_end.sh resnet50 IMAGENET 128 fp_n 12 6 0

#deit_base
sh end_to_end.sh deit_base IMAGENET 128 adaptive_block_fp 12 6 0
#sh end_to_end.sh deit_base IMAGENET 128 adaptive_fp 12 6 0
#sh end_to_end.sh deit_base IMAGENET 128 block_fp 12 6 0
#sh end_to_end.sh deit_base IMAGENET 128 fp_n 12 6 0

#vit_base
sh end_to_end.sh vit_base IMAGENET 128 adaptive_block_fp 12 6 0
#sh end_to_end.sh vit_base IMAGENET 128 adaptive_fp 12 6 0
#sh end_to_end.sh vit_base IMAGENET 128 block_fp 12 6 0
#sh end_to_end.sh vit_base IMAGENET 128 fp_n 12 6 0

#vgg19_bn
sh end_to_end.sh vgg19_bn IMAGENET 128 adaptive_block_fp 12 6 0
#sh end_to_end.sh vgg19_bn IMAGENET 128 adaptive_fp 12 6 0
#sh end_to_end.sh vgg19_bn IMAGENET 128 block_fp 12 6 0
#sh end_to_end.sh vgg19_bn IMAGENET 128 fp_n 12 6 0

#mobilenet
sh end_to_end.sh mobilenet IMAGENET 128 adaptive_block_fp 12 6 0
#sh end_to_end.sh mobilenet IMAGENET 128 adaptive_fp 12 6 0
#sh end_to_end.sh mobilenet IMAGENET 128 block_fp 12 6 0
#sh end_to_end.sh mobilenet IMAGENET 128 fp_n 12 6 0

# 16 bits, man 10, exp 5
#resnet50
#sh end_to_end.sh resnet50 IMAGENET 128 adaptive_block_fp 16 10 0
#sh end_to_end.sh resnet50 IMAGENET 128 adaptive_fp 16 10 0
#sh end_to_end.sh resnet50 IMAGENET 128 block_fp 16 10 0
#sh end_to_end.sh resnet50 IMAGENET 128 fp_n 16 10 0

#deit_base
sh end_to_end.sh deit_base IMAGENET 128 adaptive_block_fp 16 10 0
#sh end_to_end.sh deit_base IMAGENET 128 adaptive_fp 16 10 0
#sh end_to_end.sh deit_base IMAGENET 128 block_fp 16 10 0
#sh end_to_end.sh deit_base IMAGENET 128 fp_n 16 10 0

#vit_base
sh end_to_end.sh vit_base IMAGENET 128 adaptive_block_fp 16 10 0
#sh end_to_end.sh vit_base IMAGENET 128 adaptive_fp 16 10 0
#sh end_to_end.sh vit_base IMAGENET 128 block_fp 16 10 0
#sh end_to_end.sh vit_base IMAGENET 128 fp_n 16 10 0

#vgg19_bn
sh end_to_end.sh vgg19_bn IMAGENET 128 adaptive_block_fp 16 10 0
#sh end_to_end.sh vgg19_bn IMAGENET 128 adaptive_fp 16 10 0
#sh end_to_end.sh vgg19_bn IMAGENET 128 block_fp 16 10 0
#sh end_to_end.sh vgg19_bn IMAGENET 128 fp_n 16 10 0

#mobilenet
sh end_to_end.sh mobilenet IMAGENET 128 adaptive_block_fp 16 10 0
#sh end_to_end.sh mobilenet IMAGENET 128 adaptive_fp 16 10 0
#sh end_to_end.sh mobilenet IMAGENET 128 block_fp 16 10 0
#sh end_to_end.sh mobilenet IMAGENET 128 fp_n 16 10 0

# 32 bits, man 23, exp 8
#sh end_to_end.sh resnet50 IMAGENET 128 adaptive_block_fp 32 23 0
#$sh end_to_end.sh resnet50 IMAGENET 128 adaptive_fp 32 23 0
#sh end_to_end.sh resnet50 IMAGENET 128 block_fp 32 23 0
#sh end_to_end.sh resnet50 IMAGENET 128 fp_n 32 23 0

