# Sound-Classification
## Important Notice
Using wsl or linux to run may fail to access the microphone!
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
## Settings
In main.py:
* you may need to change the serial port and baud_rate at line 10, 11 and set serial_on to True in line 12
* you may need to change the microphone format in line 16~18
    * Microphone format in Windows: Sound settings -> Input -> Microphone array -> Format
    * Using wsl or linux to run may fail to access the microphone
## Run
./src/main.py