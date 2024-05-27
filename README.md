# Sound-Classification
## Important Notice
Using wsl to run may fail to access the microphone via pyaudio package!
(I'm not sure about linux, the code will work as long as pyaudio works.)
## Setup Environment
### CLAP
```
$ git clone https://github.com/LAION-AI/CLAP.git
$ cd CLAP
$ pip install .
$ pip install torch torchvision torchaudio -f https://download.pytorch.org/whl/torch_stable.html
$ pip install -r requirements.txt
```
### record audio
```
$ pip install pyaudio
```
### serial
```
S pip install pyserial
```
### play audio
```
$ pip install --upgrade wheel
$ pip install playsound
```
## Setup code
In main.py:
* you may need to change the serial port and baud_rate at line 10, 11 and set serial_on to True in line 12
* you may need to change the microphone format in line 16~18
    * Microphone format in Windows: Sound settings -> Input -> Microphone array -> Format
    * Using wsl or linux to run may fail to access the microphone
## Run
### PC side
./src/main.py
### Arduino side
## Reference
Wu*, Y. *et al.* (2023) ‘Large-scale Contrastive Language-Audio Pretraining with Feature Fusion and Keyword-to-Caption Augmentation’, in *IEEE International Conference on Acoustics, Speech and Signal Processing, ICASSP*.

Chen, K. *et al.* (2022) ‘HTS-AT: A Hierarchical Token-Semantic Audio Transformer for Sound Classification and Detection’, in *IEEE International Conference on Acoustics, Speech and Signal Processing, ICASSP*.