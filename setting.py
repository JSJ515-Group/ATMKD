# cifar100_teacher_model_name = [
#     # 'cifar100-resnet110-0',
#     'cifar100-resnet110-0','cifar100-resnet110-1', 'cifar100-resnet110-2',
#     # 'cifar100-resnet32x4-0'
# ]
#
# # ------------- teacher net --------------------#
# teacher_model_path_dict = {
#
#     'cifar100-resnet110-0': 'save/CAMKD/teachers/models/resnet110_cifar100_lr_0.05_decay_0.0005_trial_0/resnet110_best.pth',
#     'cifar100-resnet110-1': 'save/CAMKD/teachers/models/resnet110_cifar100_lr_0.05_decay_0.0005_trial_0/resnet110_best.pth',
#     'cifar100-resnet110-2': 'save/CAMKD/teachers/models/resnet110_cifar100_lr_0.05_decay_0.0005_trial_0/resnet110_best.pth',
#     # 'cifar100-resnet110-0': 'save/CAMKD/teachers/models/resnet110_cifar100_lr_0.05_decay_0.0005_trial_0/resnet110_best.pth',
#
#
# }
# ------------- teacher net --------------------#
teacher_model_path_dict = {

    'cifar100-resnet32x4-0': 'save/CAMKD/teachers/models/resnet32x4_cifar100_lr_0.05_decay_0.0005_trial_0/resnet32x4_best.pth',
    'cifar100-resnet32x4-1': 'save/CAMKD/teachers/models/resnet32x4_cifar100_lr_0.05_decay_0.0005_trial_1/resnet32x4_best.pth',
    'cifar100-resnet32x4-2': 'save/CAMKD/teachers/models/resnet32x4_cifar100_lr_0.05_decay_0.0005_trial_2/resnet32x4_best.pth',
    'cifar100-resnet32x4-3': 'save/CAMKD/teachers/models/resnet32x4_cifar100_lr_0.05_decay_0.0005_trial_3/resnet32x4_best.pth',

    # 'cifar100-resnet110-0': 'save/CAMKD/teachers/models/resnet110_cifar100_lr_0.05_decay_0.0005_trial_0/resnet110_best.pth',


}
cifar100_teacher_model_name = [
    # 'cifar100-resnet110-0',
    'cifar100-resnet32x4-0','cifar100-resnet32x4-1', 'cifar100-resnet32x4-2','cifar100-resnet32x4-3',
    # 'cifar100-resnet32x4-0'
]





# 意欲使用多个（大于三个）教师，在多个教师里根据置信度再舍弃一个，由于resnet32×4性能最好，所以使用了两个resnet32×4
# cifar100_teacher_model_name = [
#     # 'cifar100-resnet110-0',
#     'cifar100-resnet32x4-0','cifar100-resnet32x4-1','cifar100-resnet20x4', 'cifar100-resnet8x4',
#     # 'cifar100-resnet32x4-0'
# ]
#
#
# # ------------- teacher net --------------------#
# teacher_model_path_dict = {
#
#     'cifar100-resnet32x4-0': 'save/CAMKD/teachers/models/resnet32x4_cifar100_lr_0.05_decay_0.0005_trial_0/resnet32x4_best.pth',
#     'cifar100-resnet32x4-1': 'save/CAMKD/teachers/models/resnet32x4_cifar100_lr_0.05_decay_0.0005_trial_0/resnet32x4_best.pth',
#     'cifar100-resnet20x4': 'save/CAMKD/teachers/models/resnet20x4_cifar100_lr_0.05_decay_0.0005_trial_0/resnet20x4_best.pth',
#     'cifar100-resnet8x4': 'save/CAMKD/teachers/models/resnet8x4_cifar100_lr_0.05_decay_0.0005_trial_0/resnet8x4_best.pth',
#     # 'cifar100-resnet110-0': 'save/CAMKD/teachers/models/resnet110_cifar100_lr_0.05_decay_0.0005_trial_0/resnet110_best.pth',
#
#
# }


# 意欲使用三个强大的教师网络WRN40-2
# cifar100_teacher_model_name = [
#     # 'cifar100-resnet110-0',
#     'cifar100-wrn_40_2-0','cifar100-wrn_40_2-1','cifar100-wrn_40_2-2',
#     # 'cifar100-resnet32x4-0'
# ]
#
#
# # ------------- teacher net --------------------#
# teacher_model_path_dict = {
#
#     'cifar100-wrn_40_2-0': 'save/CAMKD/teachers/models/wrn_40_2_cifar100_lr_0.05_decay_0.0005_trial_0/wrn_40_2_best.pth',
#     'cifar100-wrn_40_2-1': 'save/CAMKD/teachers/models/wrn_40_2_cifar100_lr_0.05_decay_0.0005_trial_0/wrn_40_2_best.pth',
#     'cifar100-wrn_40_2-2': 'save/CAMKD/teachers/models/wrn_40_2_cifar100_lr_0.05_decay_0.0005_trial_0/wrn_40_2_best.pth',
#
#     # 'cifar100-resnet110-0': 'save/CAMKD/teachers/models/resnet110_cifar100_lr_0.05_decay_0.0005_trial_0/resnet110_best.pth',
#
#
# }

# 意欲使用多个（大于三个）教师，在多个教师里根据置信度再舍弃一个，由于resnet32×4性能最好，所以使用了两个resnet32×4
# cifar100_teacher_model_name = [
#     # 'cifar100-resnet110-0',
#     'cifar100-resnet32x4','cifar100-resnet20x4', 'cifar100-resnet8x4',
#     # 'cifar100-resnet32x4-0'
# ]
#
#
# # ------------- teacher net --------------------#
# teacher_model_path_dict = {
#
#     'cifar100-resnet32x4': 'save/CAMKD/teachers/models/resnet32x4_cifar100_lr_0.05_decay_0.0005_trial_0/resnet32x4_best.pth',
#     'cifar100-resnet20x4': 'save/CAMKD/teachers/models/resnet20x4_cifar100_lr_0.05_decay_0.0005_trial_0/resnet20x4_best.pth',
#     'cifar100-resnet8x4': 'save/CAMKD/teachers/models/resnet8x4_cifar100_lr_0.05_decay_0.0005_trial_0/resnet8x4_best.pth',
#     # 'cifar100-resnet110-0': 'save/CAMKD/teachers/models/resnet110_cifar100_lr_0.05_decay_0.0005_trial_0/resnet110_best.pth',
#
#
# }
# cifar100_teacher_model_name = [
#     'cifar100-resnet32x4-0', 'cifar100-resnet32x4-1', 'cifar100-resnet32x4-2','cifar100-resnet32x4-3',
#
# ]
#
#
# # ------------- teacher net --------------------#
# teacher_model_path_dict = {
#     'cifar100-resnet32x4-0': 'save/CAMKD/teachers/models/resnet32x4_cifar100_lr_0.05_decay_0.0005_trial_0/resnet32x4_best.pth',
#     'cifar100-resnet32x4-1': 'save/CAMKD/teachers/models/resnet32x4_cifar100_lr_0.05_decay_0.0005_trial_1/resnet32x4_best.pth',
#     'cifar100-resnet32x4-2': 'save/CAMKD/teachers/models/resnet32x4_cifar100_lr_0.05_decay_0.0005_trial_2/resnet32x4_best.pth',
#     'cifar100-resnet32x4-3': 'save/CAMKD/teachers/models/resnet32x4_cifar100_lr_0.05_decay_0.0005_trial_3/resnet32x4_best.pth',
# }



cifar100_teacher_model_name = [
    'cifar100-vgg13-0', 'cifar100-vgg13-1', 'cifar100-vgg13-2',

]


# ------------- teacher net --------------------#
teacher_model_path_dict = {
    'cifar100-vgg13-0': 'save/CAMKD/teachers/models/vgg13_cifar100_lr_0.05_decay_0.0005_trial_0/vgg13_best.pth',
    'cifar100-vgg13-1': 'save/CAMKD/teachers/models/vgg13_cifar100_lr_0.05_decay_0.0005_trial_1/vgg13_best.pth',
    'cifar100-vgg13-2': 'save/CAMKD/teachers/models/vgg13_cifar100_lr_0.05_decay_0.0005_trial_2/vgg13_best.pth',
    # 'cifar100-resnet20x4-3': 'save/CAMKD/teachers/models/resnet20x4_cifar100_lr_0.05_decay_0.0005_trial_3/resnet20x4_best.pth',
}


# cifar100_teacher_model_name = [
#     'cifar100-resnet8x4','cifar100-resnet20x4', 'cifar100-resnet32x4',
#     # 'cifar100-resnet32x4-0'
# ]
# # ------------- teacher net --------------------#
# teacher_model_path_dict = {
#
#     'cifar100-resnet8x4': 'save/CAMKD/teachers/models/resnet32x4_cifar100_lr_0.05_decay_0.0005_trial_0/resnet32x4_best.pth',
#     'cifar100-resnet20x4': 'save/CAMKD/teachers/models/resnet32x4_cifar100_lr_0.05_decay_0.0005_trial_1/resnet32x4_best.pth',
#     'cifar100-resnet32x4': 'save/CAMKD/teachers/models/resnet32x4_cifar100_lr_0.05_decay_0.0005_trial_2/resnet32x4_best.pth',
#     # 'cifar100-resnet32x4-3': 'save/CAMKD/teachers/models/resnet32x4_cifar100_lr_0.05_decay_0.0005_trial_3/resnet32x4_best.pth',
#
#     # 'cifar100-resnet110-0': 'save/CAMKD/teachers/models/resnet110_cifar100_lr_0.05_decay_0.0005_trial_0/resnet110_best.pth',
#
#
# }
