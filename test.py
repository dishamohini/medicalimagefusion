import argparse
import torch
import torch.nn as nn
import torchvision.transforms as transforms
import os
from models import fusion_model
from tqdm import tqdm
from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
from torchvision.datasets import ImageFolder
from input_data import ImageDataset
from pytorch_ssim import ssim
import time
from torchvision.utils import save_image,make_grid

os.environ["CUDA_VISIBLE_DEVICES"] = "0"
torch.cuda.set_device(0)

parser = argparse.ArgumentParser()
parser.add_argument("--infrared_dataroot", default="F:\dzs\shujuji\TNO\IV__images\Infrared/1/", type=str)
parser.add_argument("--visible_dataroot", default="F:\dzs\shujuji\TNO\IV__images\Visible/1/", type=str)
parser.add_argument("--batch_size", type=int, default=1)
parser.add_argument("--output_root", default="./outputs/feature/ct_mri_fusion_results/", type=str)
parser.add_argument("--image_size", type=int, default=[224, 224])
parser.add_argument("--epoch", type=int, default=1)
parser.add_argument("--lr", type=float, default=0.0001)
parser.add_argument("--checkpoint_dir", type=str, default="checkpoints/")


def feature_imshow(inp, title=None):
    """Imshow for Tensor."""
    inp = inp.detach().numpy().transpose((1, 2, 0))
    mean = np.array([0.5, 0.5, 0.5])
    std = np.array([0.5, 0.5, 0.5])
    inp = std * inp + mean
    inp = np.clip(inp, 0, 1)
    plt.imshow(inp)
    if title is not None:
        plt.title(title)
    plt.pause(0.001)  # pause a bit so that plots are updated


if __name__ == "__main__":
    opt = parser.parse_args()
    if not os.path.exists(opt.checkpoint_dir):
        os.makedirs(opt.checkpoint_dir)
    device = torch.device('cuda:0')
    if not os.path.exists(opt.output_root):
        os.makedirs(opt.output_root)
    net = fusion_model.Fusion_swin_transformer_net().to(device)
    net.load_state_dict(torch.load("F:/dzs/image fusion and color transfer/checkpoints/fusion_last_mustd_ssim_tv_flgcshare2_1.pth"))
    net.eval()
    print(net)
    transform = transforms.Compose([
        transforms.Resize(opt.image_size, interpolation=2),
        transforms.ToTensor()])
    with torch.no_grad():
        for i in range(20):
            start = time.time()
            index = i + 1
            infrared = Image.open(opt.infrared_dataroot + 'IR'+ str(index) + '.png').convert('L')
            infrared = transform(infrared).unsqueeze(0)
            visible = Image.open(opt.visible_dataroot + 'VIS'+str(index) + '.png').convert('L')
            visible = transform(visible).unsqueeze(0)
            infrared = infrared.to(device)
            visible = visible.to(device)
            fused_img = net(infrared,visible)
            feature_output1 = net.featuremap1.transpose(1, 0).cpu()
            feature_output2 = net.featuremap2.transpose(1, 0).cpu()
            out1 = make_grid(feature_output1,nrow=12)
            feature_imshow(out1)
            out2 = make_grid(feature_output2,nrow=12)
            feature_imshow(out2)
            save_image(out1, os.path.join(opt.output_root, 'out1' + ".jpg"))
            save_image(out2, os.path.join(opt.output_root, 'out2' + ".jpg"))
            save_image(fused_img.cpu(), os.path.join(opt.output_root, str(index) + ".jpg"))
            end = time.time()
            print('consume time:',end-start)


