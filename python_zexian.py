from matplotlib import pyplot
from IPython.display import Latex
x=(r"${Q}^F_{AB}$")
#横坐标
pyplot.subplot(4, 2, 1)
Fig=['1','2','3','4','5']
#纵坐标
IFCNN=[40.3732,	28.1722, 32.9355, 33.7129, 38.1346]
FusionGAN=[27.6598,18.4008,24.8373,15.1599,16.4154]
densefuse=[41.9973,20.456,35.1211,29.3797,27.6991]
rfn_nest=[36.2331,16.5431,36.5083,19.6614,23.346]
DLF=[28.265, 21.1656,22.361,22.1034,25.8369]
ResNet=[28.1452, 21.4747,22.5443,22.2407,26.5942]
GTF=[35.674, 25.9217,34.1382,22.2485,31.8566]
mdlatlrr=[29.431, 23.7696,25.1551,23.2219,28.3545]
ADF=[35.0289, 27.8273,34.3495,29.3904,32.7816]
Proposed=[46.2273, 36.4294,38.1513, 34.5242,41.6889]
#生成折线图：函数polt
pyplot.plot(Fig,IFCNN,label='IFCNN:39.26',marker='.')
pyplot.plot(Fig,FusionGAN,label='FusionGAN:20.50',marker='1')
pyplot.plot(Fig,densefuse,label='DenseFuse:30.93',marker='o')
pyplot.plot(Fig,rfn_nest,label='RFN-Nest:26.46',marker='v',color='y')
pyplot.plot(Fig,DLF,label='DLF:23.95',marker='^')
pyplot.plot(Fig,ResNet,label='ResNet:24.20',marker='<')
pyplot.plot(Fig,GTF,label='GTF:29.97',marker='>')
pyplot.plot(Fig,mdlatlrr,label='MDLatLRR:25.99',marker='s')
pyplot.plot(Fig,ADF,label='ADF:31.88',marker='*')
pyplot.plot(Fig,Proposed,label='Our:39.40',marker='D',color='r')
pyplot.title('EI')
pyplot.xticks([0,1,2,3,4])
pyplot.yticks([10,15,20,25,30,35,40,45,50])
pyplot.legend(loc='right', bbox_to_anchor=(1.6,0.5),borderaxespad = 0.2,fontsize='small',frameon=False,ncol=1)


pyplot.subplot(4, 2, 2)
Fig=['1','2','3','4','5']
#纵坐标

IFCNN=[5.3754,3.8198,4.6163,4.8625,5.6602]
FusionGAN=[3.3216,1.9594,3.2305,1.5863,1.8233]
densefuse=[4.9058,2.4304,4.5062,3.8404,3.5974]
rfn_nest=[3.5732, 1.6258,4.082,2.0173,2.3935]
DLF=[3.3059, 2.551,2.8909,2.8764,3.3498]
ResNet=[3.2868,2.5582,2.9056,2.8836,3.4186]
GTF=[4.1439, 2.8856,4.5644,3.1798,4.7325]
mdlatlrr=[3.4205,2.8466,3.239,2.9888,3.6504]
ADF=[4.1082,3.8363,4.6329,3.8547,4.9041]
Proposed=[5.3512,4.2477,4.8543,4.0806,4.7926]
#生成折线图：函数polt
pyplot.plot(Fig,IFCNN,label='IFCNN:4.87',marker='.')
pyplot.plot(Fig,FusionGAN,label='FusionGAN:2.38',marker='1')
pyplot.plot(Fig,densefuse,label='DenseFuse:3.86',marker='o')
pyplot.plot(Fig,rfn_nest,label='RFN-Nest:2.74',marker='v',color='y')
pyplot.plot(Fig,DLF,label='DLF:2.99',marker='^')
pyplot.plot(Fig,ResNet,label='ResNet:3.01',marker='<')
pyplot.plot(Fig,GTF,label='GTF:3.90124',marker='>')
pyplot.plot(Fig,mdlatlrr,label='MDLatLRR:3.23',marker='s')
pyplot.plot(Fig,ADF,label='ADF:4.27',marker='*')
pyplot.plot(Fig,Proposed,label='Our:4.67',marker='D',color='r')
pyplot.title('AG')
pyplot.xticks([0,1,2,3,4])
pyplot.yticks([1,2,3,4,5,6])
pyplot.legend(loc='right', bbox_to_anchor=(1.6,0.5),borderaxespad = 0.2,fontsize='small',frameon=False,ncol=1)


pyplot.subplot(4, 2, 3)
Fig=['1','2','3','4','5']
#纵坐标
Proposed=[34.8677,35.6754,38.0559,48.8088,40.178]
IFCNN=[23.3928,23.344,26.5999,32.4196,27.6523]
FusionGAN=[25.449,20.6366,24.2888,34.9712,22.7217]
densefuse=[34.2876,21.0969,43.8823,43.1357,29.6715]
rfn_nest=[35.3629,20.0359,50.5568,44.1193,31.4631]
DLF=[22.8,21.4261,26.1905,31.6482,27.2386]
ResNet=[22.758,22.8534,27.9243,33.7855,29.9267]
GTF=[26.8622,29.7764,24.3397,38.1739,28.7653]
mdlatlrr=[23.2551,22.6913,26.745,32.0246,28.1578]
ADF=[23.2271,21.9811,26.875,31.6915,27.7295]
#生成折线图：函数polt
pyplot.plot(Fig,IFCNN,label='IFCNN:26.68',marker='.')
pyplot.plot(Fig,FusionGAN,label='FusionGAN:25.61',marker='1')
pyplot.plot(Fig,densefuse,label='DenseFuse:34.41',marker='o')
pyplot.plot(Fig,rfn_nest,label='RFN-Nest:36.31',marker='v',color='y')
pyplot.plot(Fig,DLF,label='DLF:25.86',marker='^')
pyplot.plot(Fig,ResNet,label='ResNet:27.45',marker='<')
pyplot.plot(Fig,GTF,label='GTF:29.58',marker='>')
pyplot.plot(Fig,mdlatlrr,label='MDLatLRR:26.57',marker='s')
pyplot.plot(Fig,ADF,label='ADF:26.30',marker='*')
pyplot.plot(Fig,Proposed,label='Our:39.52',marker='D',color='r')
pyplot.title('SD')
pyplot.xticks([0,1,2,3,4])
pyplot.yticks([20,25,30,35,40,45,50,55])
pyplot.legend(loc='right', bbox_to_anchor=(1.6,0.5),borderaxespad = 0.2,fontsize='small',frameon=False,ncol=1)

pyplot.subplot(4, 2, 4)
Fig=['1','2','3','4','5']
#纵坐标
Proposed=[6.9081, 6.7363, 6.8341,7.1248,6.8059]
IFCNN=[6.3524, 6.1233, 6.2395,6.6184,6.3688]
FusionGAN=[6.584, 6.0131,6.3567,6.7167,6.0056]
densefuse=[6.7653, 5.9399,6.8976,6.9074,6.4134]
rfn_nest=[6.8501, 5.8416,7.1935,6.9988,6.5438]
DLF=[6.2427, 5.9387,6.219,6.5366,6.3172]
ResNet=[6.2505, 5.982,6.302,6.6266,6.4107]
GTF=[6.6779, 6.6204,6.4802,6.9582,6.5244]
mdlatlrr=[6.2671, 6.0188,6.2629,6.5591,6.3284]
ADF=[6.2865, 6.0398,6.3417,6.6047,6.3385]
#生成折线图：函数polt
pyplot.plot(Fig,IFCNN,label='IFCNN:6.34',marker='.')
pyplot.plot(Fig,FusionGAN,label='FusionGAN:6.34',marker='1')
pyplot.plot(Fig,densefuse,label='DenseFuse:6.58',marker='o')
pyplot.plot(Fig,rfn_nest,label='RFN-Nest:6.69',marker='v',color='y')
pyplot.plot(Fig,DLF,label='DLF:6.25',marker='^')
pyplot.plot(Fig,ResNet,label='ResNet:6.31',marker='<')
pyplot.plot(Fig,GTF,label='GTF:6.65',marker='>')
pyplot.plot(Fig,mdlatlrr,label='MDLatLRR:6.29',marker='s')
pyplot.plot(Fig,ADF,label='ADF:6.32',marker='*')
pyplot.plot(Fig,Proposed,label='Our:6.88',marker='D',color='r')
pyplot.title('EN')
pyplot.xticks([0,1,2,3,4])
pyplot.yticks([5.5,6,6.5,7,7.5])
pyplot.legend(loc='right', bbox_to_anchor=(1.6,0.5),borderaxespad = 0.2,fontsize='small',frameon=False,ncol=1)


pyplot.subplot(4, 2, 5)
Fig=['1','2','3','4','5']
#纵坐标
Proposed=[0.5331,0.6655,0.6554,0.4328,0.4871]
IFCNN=[0.4235, 0.5185,0.5694,0.4359,0.4284]
FusionGAN=[0.2577,0.2307,0.2974,0.1521,0.1332]
densefuse=[0.4396, 0.3781,0.6187,0.4213,0.3723]
rfn_nest=[0.4164, 0.2142,0.6016,0.2645,0.2971]
DLF=[0.367,0.4205,0.4633,0.3499,0.3465]
ResNet=[0.3646,0.4349,0.4762,0.358,0.3739]
GTF=[0.4358, 0.3979,0.5458,0.3145,0.4042]
mdlatlrr=[0.4006, 0.5296,0.5711,0.3955,0.4336]
ADF=[0.4719, 0.4282,0.6499,0.4975,0.4588]
#生成折线图：函数polt
pyplot.plot(Fig,IFCNN,label='IFCNN:0.48',marker='.')
pyplot.plot(Fig,FusionGAN,label='FusionGAN:0.21',marker='1')
pyplot.plot(Fig,densefuse,label='DenseFuse:0.45',marker='o')
pyplot.plot(Fig,rfn_nest,label='RFN-Nest:0.36',marker='v',color='y')
pyplot.plot(Fig,DLF,label='DLF:0.39',marker='^')
pyplot.plot(Fig,ResNet,label='ResNet:0.40',marker='<')
pyplot.plot(Fig,GTF,label='GTF:0.42',marker='>')
pyplot.plot(Fig,mdlatlrr,label='MDLatLRR:0.47',marker='s')
pyplot.plot(Fig,ADF,label='ADF:0.50',marker='*')
pyplot.plot(Fig,Proposed,label='Our:0.55',marker='D',color='r')
pyplot.title(x)
pyplot.xticks([0,1,2,3,4])
pyplot.yticks([0.1,0.2,0.3,0.4,0.5,0.6,0.7])
pyplot.legend(loc='right', bbox_to_anchor=(1.6,0.5),borderaxespad = 0.2,fontsize='small',frameon=False,ncol=1)


#pyplot.legend(loc='0', bbox_to_anchor=(1.02,1.0),borderaxespad = 0.,fontsize='x-small')
pyplot.subplot(4, 2, 6)
Fig=['1','2','3','4','5']
#纵坐标
Proposed=[0.3246,0.4572,0.3498,0.2291,0.3611]
IFCNN=[0.2397,0.3633,0.2867,0.2648,0.3442]
FusionGAN=[0.0777,0.1131,0.0639,0.0613,0.1128]
densefuse=[0.2562,0.374,0.311,0.2663,0.374]
rfn_nest=[0.2602,0.2202,0.3128,0.2729,0.3343]
DLF=[0.2578,0.3859,0.3131,0.2675,0.3807]
ResNet=[0.2559,0.3844,0.3257,0.2756,0.3903]
GTF=[0.2124,0.1714,0.1822,0.2434,0.2504]
mdlatlrr=[0.2855,0.4223,0.3425,0.2945,0.4294]
ADF=[0.3188,0.3719,0.348,0.2095,0.3741]
#生成折线图：函数polt
pyplot.plot(Fig,IFCNN,label='IFCNN:0.30',marker='.')
pyplot.plot(Fig,FusionGAN,label='FusionGAN:0.09',marker='1')
pyplot.plot(Fig,densefuse,label='DenseFuse:0.32',marker='o')
pyplot.plot(Fig,rfn_nest,label='RFN-Nest:0.28',marker='v',color='y')
pyplot.plot(Fig,DLF,label='DLF:0.32',marker='^')
pyplot.plot(Fig,ResNet,label='ResNet:0.33',marker='<')
pyplot.plot(Fig,GTF,label='GTF:0.21',marker='>')
pyplot.plot(Fig,mdlatlrr,label='MDLatLRR:0.34',marker='s')
pyplot.plot(Fig,ADF,label='ADF:0.32',marker='*')
pyplot.plot(Fig,Proposed,label='Our:0.35',marker='D',color='r')
pyplot.title('PC')
pyplot.xticks([0,1,2,3,4])
pyplot.yticks([0,0.1,0.2,0.3,0.4,0.5])
pyplot.legend(loc='right', bbox_to_anchor=(1.6,0.5),borderaxespad = 0.2,fontsize='small',frameon=False,ncol=1)


pyplot.subplot(4, 2, 7)
Fig=['1','2','3','4','5']
#纵坐标
Proposed=[0.3209, 0.4792, 0.4228,0.38,0.3743]
IFCNN=[0.3055, 0.4233,0.3969,0.4229,0.3843]
FusionGAN=[0.1978, 0.2227,0.2766,0.1511,0.1642]
densefuse=[0.3172, 0.3681,0.4519,0.4115,0.3488]
rfn_nest=[0.3006, 0.2816,0.4259,0.331,0.2993]
DLF=[0.2808, 0.3722,0.3424,0.3583,0.3382]
ResNet=[0.28, 0.3819,0.3492,0.3635,0.3458]
GTF=[0.3194, 0.3411,0.3731,0.3519,0.3279]
mdlatlrr=[0.2908, 0.4071,0.3696,0.3707,0.3601]
ADF=[0.3393, 0.3888,0.383,0.4096,0.3629]

#生成折线图：函数polt
pyplot.plot(Fig,IFCNN,label='IFCNN:0.39',marker='.')
pyplot.plot(Fig,FusionGAN,label='FusionGAN:0.20',marker='1')
pyplot.plot(Fig,densefuse,label='DenseFuse:0.38',marker='o')
pyplot.plot(Fig,rfn_nest,label='RFN-Nest:0.33',marker='v',color='y')
pyplot.plot(Fig,DLF,label='DLF:0.34',marker='^')
pyplot.plot(Fig,ResNet,label='ResNet:0.34',marker='<')
pyplot.plot(Fig,GTF,label='GTF:0.34',marker='>')
pyplot.plot(Fig,mdlatlrr,label='MDLatLRR:0.36',marker='s')
pyplot.plot(Fig,ADF,label='ADF:0.38',marker='*')
pyplot.plot(Fig,Proposed,label='Our:0.40',marker='D',color='r')
pyplot.title('VIFF')
pyplot.xticks([0,1,2,3,4])
pyplot.yticks([0.1,0.2,0.3,0.4,0.5])
pyplot.legend(loc='right', bbox_to_anchor=(1.6,0.5),borderaxespad = 0.2,fontsize='small',frameon=False,ncol=1)


pyplot.subplot(4, 2, 8)
Fig=['1','2','3','4','5']
#纵坐标
Proposed=[0.8554, 0.819,0.8001,0.5418,0.4771]
IFCNN=[0.5418, 0.4723,0.5359,0.5402,0.4866]
FusionGAN=[0.4412, 0.3099,0.3127,0.3676,0.2985]
densefuse=[0.5834, 0.3723,0.6136,0.5534,0.4341]
rfn_nest=[0.5276, 0.3147,0.4639,0.4475,0.3628]
DLF=[0.5103, 0.3932,0.3671,0.509,0.4272]
ResNet=[0.5044, 0.3943,0.3644,0.529,0.4407]
GTF=[0.7645, 0.5305,0.8982,0.6134,0.7007]
mdlatlrr=[0.5301, 0.4392,0.4159,0.5324,0.4716]
ADF=[0.72, 0.3868,0.7978,0.734,0.7352]
#生成折线图：函数polt
pyplot.plot(Fig,IFCNN,label='IFCNN:0.52',marker='.')
pyplot.plot(Fig,FusionGAN,label='FusionGAN:0.35',marker='1')
pyplot.plot(Fig,densefuse,label='DenseFuse:0.51',marker='o')
pyplot.plot(Fig,rfn_nest,label='RFN-Nest:0.42',marker='v',color='y')
pyplot.plot(Fig,DLF,label='DLF:0.44',marker='^')
pyplot.plot(Fig,ResNet,label='ResNet:0.45',marker='<')
pyplot.plot(Fig,GTF,label='GTF:0.70',marker='>')
pyplot.plot(Fig,mdlatlrr,label='MDLatLRR:0.48',marker='s')
pyplot.plot(Fig,ADF,label='ADF:0.67',marker='*')
pyplot.plot(Fig,Proposed,label='Our:0.70',marker='D',color='r')
y=r"${Q}_EP$"
pyplot.title(y)
pyplot.xticks([0,1,2,3,4])
pyplot.yticks([0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9])
pyplot.legend(loc='right', bbox_to_anchor=(1.6,0.5),borderaxespad = 0.2,fontsize='small',frameon=False,ncol=1)


pyplot.show()
#pyplot.savefig('G:/dzs/CBAM_CNN_paper/图/EN.png',dpi=500,bbox_inches = 'tight')