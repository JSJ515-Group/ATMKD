from __future__ import print_function

import torch.nn as nn
import torch.nn.functional as F


class DistillKL(nn.Module):
    """Distilling the Knowledge in a Neural Network"""
    def __init__(self, T):
        super(DistillKL, self).__init__()
        self.T = T

    def forward(self, y_s, y_t, is_ca=False):
        p_s = F.log_softmax(y_s/self.T, dim=1)
        p_t = F.softmax(y_t/self.T, dim=1)
        if is_ca: 
            loss = (nn.KLDivLoss(reduction='none')(p_s, p_t) * (self.T**2)).sum(-1)
        else:
            loss = nn.KLDivLoss(reduction='batchmean')(p_s, p_t) * (self.T**2)
        return loss


class DIST(nn.Module):
    def __init__(self, beta=1.0, gamma=1.0,tau=4):
        super(DIST, self).__init__()
        self.beta = beta
        self.gamma = gamma
        self.tau = tau


    # def forward(self, z_s, z_t):
    #     y_s = (z_s / self.tau).softmax(dim=1)
    #     y_t = (z_t / self.tau).softmax(dim=1)
    #     inter_loss = self.tau**2 * inter_class_relation(y_s, y_t)
    #     intra_loss = self.tau**2 * intra_class_relation(y_s, y_t)
    #     kd_loss = self.beta * inter_loss + self.gamma * intra_loss
    #     return kd_loss
    def forward(self, z_s, z_t,is_ca=False):
        # y_s = (z_s / self.tau).softmax(dim=1)
        # y_t = (z_t / self.tau).softmax(dim=1)
        # z_s/t:(64,100)
        y_s = F.softmax(z_s / self.tau, dim=1)
        y_t = F.softmax(z_t / self.tau, dim=1)

        if is_ca:
            inter_loss = (self.tau ** 2 * inter_class_relation(y_s, y_t))
            # loss = (nn.KLDivLoss(reduction='none')(p_s, p_t) * (self.T ** 2)).sum(-1)

            intra_loss = (self.tau ** 2 * intra_class_relation(y_s, y_t))
        else:
            inter_loss = self.tau**2 * inter_class_relation(y_s, y_t)
            intra_loss = self.tau**2 * intra_class_relation(y_s, y_t)
        loss = self.beta * inter_loss + self.gamma * intra_loss
        return loss


def cosine_similarity(a, b, eps=1e-8):

    return (a * b).sum(1) / (a.norm(dim=1) * b.norm(dim=1) + eps)

# a,b:(64,100)
# (a * b).sum(1) / (a.norm(dim=1) * b.norm(dim=1) + eps):torch.Size([100])

def pearson_correlation(a, b, eps=1e-8):
    # a,b:(64,100)

    return cosine_similarity(a - a.mean(1).unsqueeze(1),
                             b - b.mean(1).unsqueeze(1), eps)
# a - a.mean(1).unsqueeze(1):torch.Size([100, 64])

def inter_class_relation(y_s, y_t):
    return 1 - pearson_correlation(y_s, y_t)
# 1 - pearson_correlation(y_s, y_t).mean():torch.Size([])

def intra_class_relation(y_s, y_t):
    return inter_class_relation(y_s, y_t)


# 余弦相似度计算：如果希望尝试其他相似度度量方式，你可以替换cosine_similarity函数中的计算方法。例如，你可以使用欧几里得距离或曼哈顿距离来计算相似度。
#
# 皮尔逊相关系数计算：如果你希望采用其他相关系数来衡量两个矩阵之间的相关程度，你可以替换pearson_correlation函数中的计算方法。例如，你可以使用Spearman等其他相关系数。
#
# 类间关系计算：如果你希望尝试其他类间关系的计算方法，你可以替换inter_class_relation函数中的计算方法。例如，你可以尝试使用协方差或其他距离度量来衡量两个矩阵的类间关系。
#
# 类内关系计算：如果你希望尝试其他类内关系的计算方法，你可以替换intra_class_relation函数中的计算方法。例如，你可以尝试使用类内方差或其他距离度量来衡量两个矩阵的类内关系。
#
# 这些替换可以根据任务和需求而定，选择合适的计算方法可以更好地适应具体的问题。需要注意的是，替换函数时要确保新的函数符合任务需求，并保持与源代码的输入输出兼容性。