# Quantunn_Gate 🌌
  Status: Actively in development 🛠️

# Developed by: Invisible Label (Cesar School - Recife/PE)

Quantunn Gate is a text-based sci-fi RPG that explores the intersection between immersive narrative, 70's stylized Text-RPG and computer vision technologies. The project was born from a collaboration of students (Invisible Label) from CESAR School to create an indie experience that revives retro-futuristic aesthetics with a modern implementation.
Currently, the OpenCV feature is passing by technical difficulties. Work in progress

# How to Play the Game:
  ## To run the game (if using Windows/MacOS/Linux):
  ### (If Linux)
      sudo apt update && sudo apt install -y libgl1-mesa-glx libglib2.0-0 libsm6 libxext6 libxrender1
  ## clone this repository:
      git clone https://github.com/Renato-Augusto0-68/Quantunn_Gate.git
  ### (if Linux, also do)
      cd Quantunn_Gate     
  ## Then, create an virtual enviroment( Venv), in the project's file:
      python3 -m venv venv
  ### (if Linux/MacOS, also do)
      source venv/bin/activate
  ## Then, install all the requirements listed:
      pip install -r requirements.txt
  ## Last, run the game:
      python main.py
  ### (If Linux, do)
      cd Quantunn_Gate/game_components/python_game && python3 main.py 
# 🚀  The Project
The game places the player in a sci-fi universe where decisions shape destiny. Developed to pay a homage to 70's text RPG's, but also using elements from modern games, with a soundtrack composed of synthesizers, and OpenCV as head-gesture control, for the choice selection.
The history is being finished.

# 🛠️ Technologies Used

## Python 3.13.2: 
  Base language due to its versatility and speed of prototyping.

## Pygame:
  Engine for interface rendering, state control, and audio.

## OpenCV: 
  Used for gesture control by webcam of the player (can be turned off, if there's no webcam to be used).

# 🧠 Technical Differentiators
    Unlike simple text-based RPGs, Quantum Gate focuses on:

## Modular Architecture: 
  Clear separation between the event engine and visual components (game_components);

## Computer Vision: 
  Camera integration via OpenCV for control replacement;

## Non-Linear Narrative:
  Decision tree system implemented via graph/state logic;

## Synth-based Soundtrack

## Cross-Platform Engineering: 
  Developed and optimized to run seamlessly on both Windows and Linux/WSL.
=
