# GIF-Generator

This repository contains code for generating a GIF from a sequence of images using Python.

# Installation
To run the code in this repository, follow these steps:

Clone the repository to your local machine.
Make sure you have Python 3 installed.

# Install the necessary dependencies using pip:

pip install imageio
pip install pillow

# Usage
To generate a GIF, place the sequence of images in the images/ directory and run the following command:
python generate_gif.py
This will create a file called output.gif in the output/ directory.

By default, the code assumes that the images are named frame1.png, frame2.png, and so on. If your images are named differently, you can change the filenames in the generate_gif.py file.

You can also customize the duration of each frame in the generated GIF by changing the duration variable in the generate_gif.py file. By default, each frame is displayed for 0.2 seconds.

# Example
As an example, this repository contains a sequence of images in the images/ directory that show a ball bouncing. Running the generate_gif.py script with these images generates the following GIF:

Example GIF

# Contributing
If you would like to contribute to this repository, feel free to fork the repository and submit a pull request.
