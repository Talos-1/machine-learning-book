# install pytorch with CUDA

#pip3 install torch==1.9.1+cu111 torchvision==0.10.1+cu111 torchaudio==0.9.1 -f https://download.pytorch.org/whl/torch_stable.html
#pip3 install torchtext==0.10.1

# check if GPU is being used

import torch

print(f'torch version: {torch.__version__}')
print(f'CUDA is available: {torch.cuda.is_available()}')
print(f'device count: {torch.cuda.device_count()}')
print(f'current device: {torch.cuda.current_device()}')
print(f'device 0 is: {torch.cuda.get_device_name(0)}')