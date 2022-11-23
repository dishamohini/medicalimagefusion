from matplotlib import pyplot
#横坐标
#pyplot.subplot(3, 3, 1)
pyplot.subplot(3, 3, 1)
Fig=['1','2','3']
#纵坐标
without_DHDCB=[62.1528,55.661,57.7845]
without_DWT =[63.5548,55.9964,58.2589]
without_AAFM =[63.5707,57.2569,59.2386]
without_DHDCB_DWT_AAFM =[61.7304,55.0082,60.9637]
Our_Proposed =[71.6312,58.8622,68.775]
#生成折线图：函数polt
pyplot.plot(Fig,without_DHDCB,label='without_DHDCB',marker='.')
pyplot.plot(Fig,without_DWT,label='without_DWT',marker='1')
pyplot.plot(Fig,without_AAFM,label='without_AAFM',marker='o')
pyplot.plot(Fig,Our_Proposed,label='Our_Proposed',marker='*')
pyplot.plot(Fig,without_DHDCB_DWT_AAFM,label='without_DHDCB_DWT_AAFM',marker='^')
pyplot.title('EI')

pyplot.subplot(3, 3, 2)
Fig=['1','2','3']
#纵坐标
without_DHDCB=[53.103,97.8939,90.2221]
without_DWT =[55.0399,98.9902,90.4622]
without_AAFM =[54.0953,99.1284,91.3994]
without_DHDCB_DWT_AAFM =[52.6605,97.6876,88.4073]
Our_Proposed =[56.1341,99.3715,90.5776]
#生成折线图：函数polt
pyplot.plot(Fig,without_DHDCB,label='without_DHDCB',marker='.')
pyplot.plot(Fig,without_DWT,label='without_DWT',marker='1')
pyplot.plot(Fig,without_AAFM,label='without_AAFM',marker='o')
pyplot.plot(Fig,Our_Proposed,label='Our_Proposed',marker='*')
pyplot.plot(Fig,without_DHDCB_DWT_AAFM,label='without_DHDCB_DWT_AAFM',marker='^')
pyplot.title('SD')

pyplot.subplot(3, 3, 3)
Fig=['1','2','3']
#纵坐标
without_DHDCB=[3.1801,3.4227,3.3495]
without_DWT =[3.1259,3.4468,3.3434]
without_AAFM =[3.1262,3.4006,3.3339]
without_DHDCB_DWT_AAFM =[3.1143,3.4316,3.3198]
Our_Proposed =[3.1931,3.494,3.3486]
#生成折线图：函数polt
pyplot.plot(Fig,without_DHDCB,label='without_DHDCB',marker='.')
pyplot.plot(Fig,without_DWT,label='without_DWT',marker='1')
pyplot.plot(Fig,without_AAFM,label='without_AAFM',marker='o')
pyplot.plot(Fig,Our_Proposed,label='Our_Proposed',marker='*')
pyplot.plot(Fig,without_DHDCB_DWT_AAFM,label='without_DHDCB_DWT_AAFM',marker='^')
pyplot.title('MI')

pyplot.subplot(3, 3, 4)
Fig=['1','2','3']
#纵坐标
without_DHDCB=[0.6596,0.5218,0.425]
without_DWT =[0.6653,0.519,0.4271]
without_AAFM =[0.665,0.5243,0.4283]
without_DHDCB_DWT_AAFM =[0.6494,0.5203,0.4514]
Our_Proposed =[0.7096,0.5934,0.5244]
#生成折线图：函数polt
pyplot.plot(Fig,without_DHDCB,label='without_DHDCB',marker='.')
pyplot.plot(Fig,without_DWT,label='without_DWT',marker='1')
pyplot.plot(Fig,without_AAFM,label='without_AAFM',marker='o')
pyplot.plot(Fig,Our_Proposed,label='Our_Proposed',marker='*')
pyplot.plot(Fig,without_DHDCB_DWT_AAFM,label='without_DHDCB_DWT_AAFM',marker='^')
y=r"${Q}^{F}_{AB}$"
pyplot.title(y)

pyplot.subplot(3, 3, 5)
Fig=['1','2','3']
#纵坐标
without_DHDCB=[0.5594,0.6729,0.742]
without_DWT =[0.5604,0.6736,0.7437]
without_AAFM =[0.5678,0.6652,0.7418]
without_DHDCB_DWT_AAFM =[0.5773,0.6607,0.7433]
Our_Proposed =[0.5833,0.676,0.7475]
#生成折线图：函数polt
pyplot.plot(Fig,without_DHDCB,label='without_DHDCB',marker='.')
pyplot.plot(Fig,without_DWT,label='without_DWT',marker='1')
pyplot.plot(Fig,without_AAFM,label='without_AAFM',marker='o')
pyplot.plot(Fig,Our_Proposed,label='Our_Proposed',marker='*')
pyplot.plot(Fig,without_DHDCB_DWT_AAFM,label='without_DHDCB_DWT_AAFM',marker='^')
pyplot.title('MSSIM')

pyplot.subplot(3, 3, 6)
Fig=['1','2','3']
#纵坐标
without_DHDCB=[0.4356,0.2794,0.2418]
without_DWT =[0.4366,0.2307,0.2532]
without_AAFM =[0.4353,0.2661,0.2408]
without_DHDCB_DWT_AAFM =[0.4319,0.2551,0.2249]
Our_Proposed =[0.4681,0.3404,0.2561]
#生成折线图：函数polt
pyplot.plot(Fig,without_DHDCB,label='without_DHDCB',marker='.')
pyplot.plot(Fig,without_DWT,label='without_DWT',marker='1')
pyplot.plot(Fig,without_AAFM,label='without_AAFM',marker='o')
pyplot.plot(Fig,Our_Proposed,label='Our_Proposed',marker='*')
pyplot.plot(Fig,without_DHDCB_DWT_AAFM,label='without_DHDCB_DWT_AAFM',marker='^')
pyplot.title('PC')

pyplot.subplot(3, 3, 7)
Fig=['1','2','3']
#纵坐标
without_DHDCB=[0.3494,0.2612,0.2208]
without_DWT =[0.3485,0.2576,0.2283]
without_AAFM =[0.3511,0.2623,0.2262]
without_DHDCB_DWT_AAFM =[0.3351,0.2609,0.2192]
Our_Proposed =[0.3794,0.2934,0.2478]
#生成折线图：函数polt
pyplot.plot(Fig,without_DHDCB,label='without_DHDCB',marker='.')
pyplot.plot(Fig,without_DWT,label='without_DWT',marker='1')
pyplot.plot(Fig,without_AAFM,label='without_AAFM',marker='o')
pyplot.plot(Fig,Our_Proposed,label='Our_Proposed',marker='*')
pyplot.plot(Fig,without_DHDCB_DWT_AAFM,label='without_DHDCB_DWT_AAFM',marker='^')
pyplot.title('VIF')

pyplot.subplot(3, 3, 8)
Fig=['1','2','3']
#纵坐标
without_DHDCB=[0.4347,0.3622,0.151]
without_DWT =[0.4764,0.3842,0.1239]
without_AAFM =[0.4504,0.3752,0.1412]
without_DHDCB_DWT_AAFM =[0.447,0.3856,0.126]
Our_Proposed =[0.5118,0.4256,0.1736]
#生成折线图：函数polt
pyplot.plot(Fig,without_DHDCB,label='without_DHDCB',marker='.')
pyplot.plot(Fig,without_DWT,label='without_DWT',marker='1')
pyplot.plot(Fig,without_AAFM,label='without_AAFM',marker='o')
pyplot.plot(Fig,Our_Proposed,label='Our_Proposed',marker='*')
pyplot.plot(Fig,without_DHDCB_DWT_AAFM,label='without_DHDCB_DWT_AAFM',marker='^')
y=r"${Q}_{EP}$"
pyplot.title(y)

pyplot.subplot(3, 3, 9)
Fig=['1','2','3']
#纵坐标
without_DHDCB=[0.2959,0.5153,0.5144]
without_DWT =[0.2996,0.5219,0.5271]
without_AAFM =[0.3199,0.5127,0.5106]
without_DHDCB_DWT_AAFM =[0.3502,0.5238,0.5265]
Our_Proposed =[0.3854,0.522,0.5241]
#生成折线图：函数polt
pyplot.plot(Fig,without_DHDCB,label='without_DHDCB',marker='.')
pyplot.plot(Fig,without_DWT,label='without_DWT',marker='1')
pyplot.plot(Fig,without_AAFM,label='without_AAFM',marker='o')
pyplot.plot(Fig,Our_Proposed,label='Our_Proposed',marker='*')
pyplot.plot(Fig,without_DHDCB_DWT_AAFM,label='without_DHDCB_DWT_AAFM',marker='^')
pyplot.title('UIQI')
pyplot.legend(loc='right', bbox_to_anchor=(0.5,-0.2),borderaxespad = 0.2,fontsize='larger',frameon=False,ncol=3)

pyplot.show()