from matplotlib import pyplot
#横坐标
pyplot.subplot(3, 3, 1)
Fig=['1','2','3','4','5','6','7','8','9','10','11','12']
#纵坐标
DDcGAN=[32.337,22.659,29.402,25.273,34.623,40.776,35.839,25.804,35.254,34.001,30.302,30.152]
IFCNN=[39.334,46.012,44.126,32.879,54.547,54.186,52.118,26.839,75.174,71.007,62.812,59.052]
PMGI=[86.707,78.488,62.976,55.505,85.641,83.974,84.333,45.54,101.024,85.807,81.072,71.515]
our_method=[50.963,56.757,59.697,44.447,71.783,77.366,67.907,33.564,94.582,83.908,78.229,68.136]
SDNet=[39.4285,36.6193,44.034,32.4803,46.4373,50.3342,51.9616,30.4609,57.5257,50.5629,48.1231,42.6502]
U2Fusion=[31.096,37.501,48.591,33.896,56.067,57.573,62.882,33.631,66.03,62.011,57.041,55.624]
FusionDN=[78.492,62.99,50.99,44.583,68.722,71.031,70.128,35.915,83.205,67.319,66.183,60.431]

#生成折线图：函数polt
pyplot.plot(Fig,DDcGAN,label='DDcGAN',marker='.',c='b')
pyplot.plot(Fig,IFCNN,label='IFCNN',marker='1',c='lime')
pyplot.plot(Fig,PMGI,label='PMGI',marker='o',c='teal')
pyplot.plot(Fig,our_method,label='our_method',marker='D',c='r')
pyplot.plot(Fig,SDNet,label='SDNet',marker='s',c='y')
pyplot.plot(Fig,U2Fusion,label='U2Fusion',marker='v',c='bisque')
pyplot.plot(Fig,FusionDN,label='FusionDN',marker='^',c='cornflowerblue')
pyplot.title('EI')

pyplot.subplot(3, 3, 2)
Fig=['1','2','3','4','5','6','7','8','9','10','11','12']
#纵坐标
DDcGAN=[15.791,19.811,45.754,44.221,39.348,54.195,43.826,53.051,33.125,37.06,33.795,28.323]
IFCNN=[27.842,40.838,63.59,58.77,57.782,55.537,53.476,64.384,56.761,66.043,59.778,60.451]
PMGI=[56.549,63.975,71.407,69.322,71.899,70.116,73.149,77.872,63.643,64.199,60.968,58.666]
our_method=[38.555,56.421,90.962,83.417,79.937,81.088,72.758,91.452,81.792,94.313,86.742,83.211]
SDNet=[16.408,25.0059,56.6754,55.8031,45.7388,52.4359,50.7396,75.9022,40.1716,45.1622,43.104,42.4633]
U2Fusion=[19.548,30.925,61.474,53.936,57.391,53.902,64.62,74.329,46.513,53.587,49.721,51.169]
FusionDN=[48.405,55.096,57.795,54.71,55.386,56.839,58.827,56.52,54.412,52.308,52.978,47.788]

#生成折线图：函数polt
pyplot.plot(Fig,DDcGAN,label='DDcGAN',marker='.',c='b')
pyplot.plot(Fig,IFCNN,label='IFCNN',marker='1',c='lime')
pyplot.plot(Fig,PMGI,label='PMGI',marker='o',c='teal')
pyplot.plot(Fig,our_method,label='our_method',marker='D',c='r')
pyplot.plot(Fig,SDNet,label='SDNet',marker='s',c='y')
pyplot.plot(Fig,U2Fusion,label='U2Fusion',marker='v',c='bisque')
pyplot.plot(Fig,FusionDN,label='FusionDN',marker='^',c='cornflowerblue')
pyplot.title('SD')

pyplot.subplot(3, 3, 3)
Fig=['1','2','3','4','5','6','7','8','9','10','11','12']
#纵坐标
DDcGAN=[1.046,1.642,3.299,3.071,3.192,3.293,2.949,2.879,2.487,2.698,2.572,2.491]
IFCNN=[1.731,2.326,3.186,3.203,3.383,3.207,3.057,3.058,2.558,2.805,2.709,2.869]
PMGI=[1.697,2.285,3.221,3.011,3.301,3.175,2.959,2.954,2.63,2.845,2.691,2.738]
our_method=[1.76,2.309,3.391,3.369,3.605,3.566,3.362,3.184,2.826,2.877,2.804,2.905]
SDNet=[1.226,1.8275,3.1939,3.1835,3.1935,3.3028,3.0053,3.054,2.5281,2.7595,2.6371,2.6748]
U2Fusion=[1.566,2.173,3.183,3.123,3.295,3.082,3.114,3.011,2.546,2.763,2.658,2.822]
FusionDN=[1.607,2.261,3.165,2.997,3.195,3.126,2.904,2.794,2.565,2.733,2.653,2.707]

#生成折线图：函数polt
pyplot.plot(Fig,DDcGAN,label='DDcGAN',marker='.',c='b')
pyplot.plot(Fig,IFCNN,label='IFCNN',marker='1',c='lime')
pyplot.plot(Fig,PMGI,label='PMGI',marker='o',c='teal')
pyplot.plot(Fig,our_method,label='our_method',marker='D',c='r')
pyplot.plot(Fig,SDNet,label='SDNet',marker='s',c='y')
pyplot.plot(Fig,U2Fusion,label='U2Fusion',marker='v',c='bisque')
pyplot.plot(Fig,FusionDN,label='FusionDN',marker='^',c='cornflowerblue')
pyplot.title('MI')

pyplot.subplot(3, 3, 4)
Fig=['1','2','3','4','5','6','7','8','9','10','11','12']
#纵坐标
DDcGAN=[0.291,0.099,0.184,0.212,0.155,0.248,0.256,0.275,0.103,0.106,0.094,0.107]
IFCNN=[0.788,0.67,0.482,0.471,0.559,0.516,0.616,0.5,0.58,0.539,0.525,0.476]
PMGI=[0.607,0.572,0.465,0.397,0.545,0.457,0.565,0.391,0.552,0.479,0.458,0.429]
our_method=[0.819,0.685,0.553,0.532,0.594,0.64,0.697,0.553,0.624,0.534,0.549,0.478]
SDNet=[0.5111,0.3402,0.3828,0.3795,0.3553,0.3597,0.4453,0.4121,0.2974,0.2539,0.2744,0.2386]
U2Fusion=[0.415,0.388,0.447,0.407,0.459,0.434,0.511,0.42,0.387,0.359,0.363,0.382]
FusionDN=[0.608,0.569,0.439,0.392,0.466,0.451,0.512,0.33,0.476,0.383,0.409,0.333]

#生成折线图：函数polt
pyplot.plot(Fig,DDcGAN,label='DDcGAN',marker='.',c='b')
pyplot.plot(Fig,IFCNN,label='IFCNN',marker='1',c='lime')
pyplot.plot(Fig,PMGI,label='PMGI',marker='o',c='teal')
pyplot.plot(Fig,our_method,label='our_method',marker='D',c='r')
pyplot.plot(Fig,SDNet,label='SDNet',marker='s',c='y')
pyplot.plot(Fig,U2Fusion,label='U2Fusion',marker='v',c='bisque')
pyplot.plot(Fig,FusionDN,label='FusionDN',marker='^',c='cornflowerblue')
y=r"${Q}^{F}_{AB}$"
pyplot.title(y)

pyplot.subplot(3, 3, 5)
Fig=['1','2','3','4','5','6','7','8','9','10','11','12']
#纵坐标
DDcGAN=[0.12,0.127,0.224,0.201,0.226,0.276,0.276,0.193,0.148,0.147,0.136,0.116]
IFCNN=[0.758,0.714,0.789,0.84,0.755,0.748,0.758,0.857,0.713,0.718,0.732,0.78]
PMGI=[0.125,0.19,0.232,0.196,0.254,0.245,0.279,0.232,0.206,0.198,0.18,0.155]
our_method=[0.775,0.729,0.769,0.813,0.732,0.733,0.751,0.835,0.72,0.712,0.731,0.769]
SDNet=[0.1513,0.1743,0.2385,0.2382,0.244,0.2609,0.2858,0.2995,0.1792,0.1698,0.1624,0.1529]
U2Fusion=[0.394,0.404,0.526,0.55,0.577,0.53,0.454,0.605,0.413,0.415,0.438,0.483]
FusionDN=[0.123,0.21,0.238,0.2,0.251,0.268,0.283,0.21,0.208,0.189,0.183,0.154]

#生成折线图：函数polt
pyplot.plot(Fig,DDcGAN,label='DDcGAN',marker='.',c='b')
pyplot.plot(Fig,IFCNN,label='IFCNN',marker='1',c='lime')
pyplot.plot(Fig,PMGI,label='PMGI',marker='o',c='teal')
pyplot.plot(Fig,our_method,label='our_method',marker='D',c='r')
pyplot.plot(Fig,SDNet,label='SDNet',marker='s',c='y')
pyplot.plot(Fig,U2Fusion,label='U2Fusion',marker='v',c='bisque')
pyplot.plot(Fig,FusionDN,label='FusionDN',marker='^',c='cornflowerblue')
pyplot.title('MSSIM')

pyplot.subplot(3, 3, 6)
Fig=['1','2','3','4','5','6','7','8','9','10','11','12']
#纵坐标
DDcGAN=[0.096,0.08,0.079,0.063,0.106,0.128,0.191,0.053,0.119,0.097,0.086,0.063]
IFCNN=[0.759,0.501,0.319,0.341,0.414,0.356,0.49,0.306,0.412,0.314,0.336,0.295]
PMGI=[0.604,0.491,0.297,0.26,0.4,0.32,0.422,0.295,0.372,0.318,0.274,0.29]
our_method=[0.656,0.434,0.281,0.276,0.375,0.378,0.537,0.244,0.407,0.235,0.299,0.252]
SDNet=[0.4118,0.1902,0.169,0.1812,0.209,0.2101,0.283,0.1474,0.1918,0.1575,0.1793,0.1148]
U2Fusion=[0.432,0.264,0.24,0.22,0.335,0.257,0.362,0.19,0.303,0.239,0.242,0.215]
FusionDN=[0.463,0.349,0.195,0.138,0.224,0.234,0.294,0.133,0.233,0.2,0.194,0.118]

#生成折线图：函数polt
pyplot.plot(Fig,DDcGAN,label='DDcGAN',marker='.',c='b')
pyplot.plot(Fig,IFCNN,label='IFCNN',marker='1',c='lime')
pyplot.plot(Fig,PMGI,label='PMGI',marker='o',c='teal')
pyplot.plot(Fig,our_method,label='our_method',marker='D',c='r')
pyplot.plot(Fig,SDNet,label='SDNet',marker='s',c='y')
pyplot.plot(Fig,U2Fusion,label='U2Fusion',marker='v',c='bisque')
pyplot.plot(Fig,FusionDN,label='FusionDN',marker='^',c='cornflowerblue')
pyplot.title('PC')

pyplot.subplot(3, 3, 7)
Fig=['1','2','3','4','5','6','7','8','9','10','11','12']
#纵坐标
DDcGAN=[0.193,0.167,0.171,0.157,0.16,0.176,0.188,0.158,0.142,0.127,0.13,0.112]
IFCNN=[0.423,0.346,0.263,0.298,0.299,0.292,0.345,0.334,0.247,0.216,0.234,0.199]
PMGI=[0.307,0.322,0.253,0.265,0.283,0.29,0.345,0.358,0.225,0.209,0.208,0.195]
our_method=[0.462,0.36,0.258,0.291,0.306,0.314,0.39,0.304,0.272,0.208,0.234,0.199]
SDNet=[0.3097,0.2528,0.2184,0.2434,0.2246,0.2268,0.2593,0.2765,0.1851,0.1715,0.1812,0.1647]
U2Fusion=[0.3,0.252,0.233,0.262,0.245,0.239,0.28,0.28,0.192,0.179,0.187,0.171]
FusionDN=[0.272,0.285,0.212,0.211,0.228,0.221,0.261,0.226,0.183,0.169,0.179,0.15]

#生成折线图：函数polt
pyplot.plot(Fig,DDcGAN,label='DDcGAN',marker='.',c='b')
pyplot.plot(Fig,IFCNN,label='IFCNN',marker='1',c='lime')
pyplot.plot(Fig,PMGI,label='PMGI',marker='o',c='teal')
pyplot.plot(Fig,our_method,label='our_method',marker='D',c='r')
pyplot.plot(Fig,SDNet,label='SDNet',marker='s',c='y')
pyplot.plot(Fig,U2Fusion,label='U2Fusion',marker='v',c='bisque')
pyplot.plot(Fig,FusionDN,label='FusionDN',marker='^',c='cornflowerblue')
pyplot.title('VIF')

pyplot.subplot(3, 3, 8)
Fig=['1','2','3','4','5','6','7','8','9','10','11','12']
#纵坐标
DDcGAN=[0.159,0.132,0.137,0.177,0.144,0.603,0.179,0.315,0.08,0.085,0.09,0.096]
IFCNN=[0.362,0.347,0.332,0.367,0.363,0.711,0.377,0.491,0.172,0.173,0.173,0.177]
PMGI=[0.123,0.17,0.23,0.154,0.202,0.595,0.204,0.241,0.151,0.14,0.129,0.119]
our_method=[0.389,0.341,0.33,0.364,0.346,0.79,0.429,0.566,0.201,0.191,0.203,0.174]
SDNet=[0.2123,0.1748,0.2176,0.2308,0.1978,0.6227,0.2512,0.388,0.0992,0.0914,0.1063,0.1109]
U2Fusion=[0.177,0.187,0.209,0.229,0.221,0.637,0.244,0.379,0.096,0.095,0.101,0.117]
FusionDN=[0.176,0.227,0.226,0.241,0.237,0.602,0.262,0.313,0.118,0.097,0.122,0.114]

#生成折线图：函数polt
pyplot.plot(Fig,DDcGAN,label='DDcGAN',marker='.',c='b')
pyplot.plot(Fig,IFCNN,label='IFCNN',marker='1',c='lime')
pyplot.plot(Fig,PMGI,label='PMGI',marker='o',c='teal')
pyplot.plot(Fig,our_method,label='our_method',marker='D',c='r')
pyplot.plot(Fig,SDNet,label='SDNet',marker='s',c='y')
pyplot.plot(Fig,U2Fusion,label='U2Fusion',marker='v',c='bisque')
pyplot.plot(Fig,FusionDN,label='FusionDN',marker='^',c='cornflowerblue')
y=r"${Q}_{EP}$"
pyplot.title(y)

pyplot.subplot(3, 3, 9)
Fig=['1','2','3','4','5','6','7','8','9','10','11','12']
#纵坐标
DDcGAN=[0.096,0.089,0.172,0.146,0.165,0.212,0.211,0.137,0.12,0.114,0.106,0.092]
IFCNN=[0.667,0.649,0.704,0.755,0.625,0.587,0.642,0.737,0.643,0.654,0.667,0.724]
PMGI=[0.114,0.171,0.186,0.152,0.212,0.202,0.234,0.151,0.185,0.17,0.153,0.136]
our_method=[0.683,0.651,0.682,0.729,0.602,0.553,0.644,0.699,0.656,0.648,0.668,0.712]
SDNet=[0.1305,0.1476,0.1856,0.1805,0.1949,0.2107,0.2408,0.1974,0.1569,0.1386,0.1351,0.1304]
U2Fusion=[0.135,0.156,0.233,0.223,0.272,0.268,0.277,0.204,0.202,0.193,0.183,0.176]
FusionDN=[0.112,0.187,0.19,0.15,0.21,0.22,0.241,0.147,0.187,0.162,0.157,0.135]

#生成折线图：函数polt
pyplot.plot(Fig,DDcGAN,label='DDcGAN',marker='.',c='b')
pyplot.plot(Fig,IFCNN,label='IFCNN',marker='1',c='lime')
pyplot.plot(Fig,PMGI,label='PMGI',marker='o',c='teal')
pyplot.plot(Fig,our_method,label='our_method',marker='D',c='r')
pyplot.plot(Fig,SDNet,label='SDNet',marker='s',c='y')
pyplot.plot(Fig,U2Fusion,label='U2Fusion',marker='v',c='bisque')
pyplot.plot(Fig,FusionDN,label='FusionDN',marker='^',c='cornflowerblue')
pyplot.title('UIQI')
pyplot.legend(loc='right', bbox_to_anchor=(0.5,-0.2),borderaxespad = 0.2,fontsize='larger',frameon=False,ncol=4)

pyplot.show()
#pyplot.savefig('G:/dzs/CBAM_CNN_paper/图/EN.png',dpi=500,bbox_inches = 'tight')