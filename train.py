import argparse
import torch
import torch.nn as nn
import torchvision.transforms as transforms
import os
from models import fusion_model
from tqdm import tqdm
from PIL import Image
from torchvision.datasets import ImageFolder
import time
import torch.nn.functional as F
from input_data import ImageDataset
from pytorch_ssim import ssim,gradient
os.environ["CUDA_VISIBLE_DEVICES"] = "0"
torch.cuda.set_device(0)
torch.set_num_threads(6)

parser = argparse.ArgumentParser()
parser.add_argument("--infrared_dataroot", default="F:\dzs\shujuji\CT_MRI\crop_images/train_ct/", type=str)
parser.add_argument("--visible_dataroot", default="F:\dzs\shujuji\CT_MRI\crop_images/train_mri/", type=str)
parser.add_argument("--batch_size", type=int, default=10)
parser.add_argument("--image_size", type=int, default=[64, 64])
parser.add_argument("--epoch", type=int, default=5)
parser.add_argument("--lr", type=float, default=0.0001)
parser.add_argument("--checkpoint_dir", type=str, default="checkpoints/")


def tv_loss(x, batch_size=1):
    batch_size = x.shape[0]
    c_x = x.shape[1]
    h_x = x.shape[2]
    w_x = x.shape[3]
    count_h = x[:, :, 1:, :].size(1) * x[:, :, 1:, :].size(2) * x[:, :, 1:, :].size(3)
    count_w = x[:, :, :, 1:].size(1) * x[:, :, :, 1:].size(2) * x[:, :, :, 1:].size(3)
    h_tv = torch.pow((x[:, :, 1:, :] - x[:, :, :h_x - 1, :]), 2).sum()
    w_tv = torch.pow((x[:, :, :, 1:] - x[:, :, :, :w_x - 1]), 2).sum()
    return h_tv / count_h + w_tv / count_w

if __name__ == "__main__":
    opt = parser.parse_args()
    if not os.path.exists(opt.checkpoint_dir):
        os.makedirs(opt.checkpoint_dir)
    #device = torch.device('cuda:0')
    net = fusion_model.Fusion_NOHDC_NODWT_NOSCNet().cuda()
    optim = torch.optim.Adam(filter(lambda p: p.requires_grad,net.parameters()),lr=opt.lr)
    train_datasets = ImageDataset(opt.infrared_dataroot, opt.visible_dataroot, opt.image_size)
    lens = len(train_datasets)
    log_file = './log_dir'
    dataloader = torch.utils.data.DataLoader(train_datasets,batch_size=opt.batch_size,num_workers = 4, shuffle=False, pin_memory=True)
    runloss = 0.
    total_params = sum(p.numel() for p in net.parameters())
    print('total parameters:', total_params)
    for epoch in range(opt.epoch):
        #if （epoch+1） % 5==1:
          #  opt.lr=0.1*opt.lr
        for index, data in enumerate(dataloader):
            infrared = data[0].cuda()
            visible = data[1].cuda()
            fused_img = net(infrared,visible)
            LOSS_SSIM = 1-ssim(fused_img, infrared, visible)
            #LOSS_L1 = nn.L1Loss()
            #LOSS_L1_NORM = LOSS_L1(fused_img, visible)
            #LOSS_TV_l = nn.MSELoss()
            #LOSS_TV = LOSS_TV_l(fused_img,visible)
            #100*tv_loss(fused_img-visible)
            loss = LOSS_SSIM #+ LOSS_TV LOSS_L1_NORM +
            runloss += loss.item()
            print('epoch [{}/{}], images [{}/{}], SSIM loss is {:.5}, total loss is  {:.5}, lr: {}'.
                  format(epoch + 1, opt.epoch, (index + 1) * opt.batch_size, lens+1, LOSS_SSIM.item(), loss.item(), opt.lr))
            runloss = 0.
            optim.zero_grad()
            loss.backward()
            optim.step()
    torch.save(net.state_dict(), './ablation/fusion_ctmri_std_ssim_nohdc_nodwt_noscnet_idwt.pth'.format(opt.lr, log_file[2:]))