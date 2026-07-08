# Quantunn_Gate 🌌
  Status: Actively in development 🛠️

## Developed by: Invisible Label (Cesar School - Recife/PE)

 For WSL compilation, there has to be made clear that, due to the conversion for the Linux Kernel be compatible with Windows ecosystem, it (WSL) doesn't has direct acess to the GPU.

## Step 1:
  To create your .wslconfig file:

  Press Win+R, then type:

    %USERPROFILE% 
  Create a file named wsl.config (DO `NOT` save as .txt)

  ## Step 1.5
  Open the file

  According to your RAM memory, it has to be ajusted, so that WSL isn't using all the RAM avaliable
  (The best practise is to put the memory value as equal to half of the RAM )
  #### example with 8GB of RAM:
    memory=4GB 
    pageReporting=true
    guiApplications=true
  #### example with 16GB of RAM:
    memory=8GB 
    pageReporting=true
    guiApplications=true

 ## Step2:
  Update your GPU's driver, by installing the latest version, on the web, according to the maker:
  ### [Intel's drivers](https://www.google.com/search?q=https://www.intel.com/content/www/us/en/download-center.html)

  ### [Nvidia's drivers](https://www.nvidia.com/Download/index.aspx)

  ### [AMD's drivers](https://www.amd.com/en/support)

## Step3:
  run this command to install the dependencies:

    sudo apt install build-essential cmake git \
    libx11-dev libxrandr-dev libxinerama-dev libxcursor-dev libxi-dev \
    libgl1-mesa-dev libglu1-mesa-dev libegl1-mesa-dev libgles2-mesa-dev


## To run the game:
      sudo apt update && sudo apt install -y libgl1-mesa-glx libglib2.0-0 libsm6 libxext6 libxrender1
  ### create a folder for the game && clone this repository:
      git clone https://github.com/Renato-Augusto0-68/Quantunn_Gate.git
      
  ## Then, create a Venv in the project's file:
      python3 -m venv venv
  ### Activate the Venv    
      source venv/bin/activate
  ## Then, install all the requirements listed:
      pip install -r requirements.txt
      sudo apt update && sudo apt install python3-pip
      python.exe -m pip install opencv-python
  ## Lastly, to run the game:
   ### first, enter in the correct folder:
        cd Quantunn_Gate/game_components/python_game
   ### run the main:
         python.exe main.py 
  