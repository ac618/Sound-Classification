# Sound-Classification
## Setup Environment
### CLAP
git clone https://github.com/LAION-AI/CLAP.git
cd CLAP
pip install .
pip install torch torchvision torchaudio -f https://download.pytorch.org/whl/torch_stable.html
pip install -r requirements.txt
### record audio
pip install pyaudio
### serial
pip install pyserial
### play audio
pip install --upgrade wheel
pip install playsound
## Run
./src/main.py