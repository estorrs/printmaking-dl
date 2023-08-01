conda create -n printmaking-dl -c pytorch -c nvidia pytorch torchvision torchaudio pytorch-cuda=11.7 python==3.10 -y
conda activate printmaking-dl
conda install -c conda-forge cmake>=3.12 gcc_linux-64 libstdcxx-ng ffmpeg numpy scikit-image jupyter tornado==6.1 -y
pip install svgwrite svgpathtools cssutils numba torch-tools visdom
python setup.py install
