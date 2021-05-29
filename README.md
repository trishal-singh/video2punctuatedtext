# video2punctuatedtext
It is used to trancribe vdeos to punctuated text.

# How to run:
# Step 1:
Create a virtual environment with python 3.7.10 installed. If using anaconda then use the below command:</br>

conda create --name env_name python=3.7.10</br>
Install the following packages:</br>
torch</br>
torchaudio</br>
omegaconf</br>
If using anaconda then the following commands should work:</br>
conda install pytorch torchvision torchaudio cpuonly -c pytorch</br>
conda install -c conda-forge omegaconf</br>


# Step 2:
Clone this repository

# Step 3:
Move inside the video2punctuatedtext folder

# Step 4:
Install the required libraries by using  the command:</br>

pip install -r requirements.txt</br>
pip install git+https://github.com/NVIDIA/NeMo.git@$'main'

# Step 5:
Change the filepath in main.py to reflect your video path.

# Step 6:
Run the program using:</br>
python main.py

# Output:

![Output](Output.png)
