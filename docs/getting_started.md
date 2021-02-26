---
layout: page
title: Getting Started
---

<iframe src="https://player.vimeo.com/video/496027774" width="640" height="360" frameborder="0" allow="autoplay; fullscreen" allowfullscreen></iframe>
<p><a href="https://vimeo.com/496027774">Welcome to our Video Tutorial Series of L.E.A.R.N.</a></p>


### 1. Setting up the Anaconda environment with COMPAS

Execute the commands below in Anaconda Prompt:
	
    (base) conda config --add channels conda-forge

#### Windows
    (base) conda create -n afab_course python=3.8 compas_fab=0.13 --yes
    (base) conda activate afab_course

#### Mac
    (base) conda create -n afab_course python=3.8 compas_fab=0.13 python.app --yes
    (base) conda activate afab_course
    

#### Verify Installation

    (afab_course) pip show compas_fab
####
    Name: compas-fab
    Version: 0.13.1
    Summary: Robotic fabrication package for the COMPAS Framework
    ...

<iframe src="https://player.vimeo.com/video/496027774" width="640" height="360" frameborder="0" allow="autoplay; fullscreen" allowfullscreen></iframe>
<p><a href="https://vimeo.com/500532145">Welcome to our Video Tutorial Series of L.E.A.R.N.</a></p>

### Install on Rhino

    (afab_course) python -m compas_rhino.install

NOTE: This installs to Rhino 6.0, use `-v 5.0` if needed.


### 2. Installation of Dependencies

    (afab_course) conda install git

#### Assembly Information Model
    
    (afab_course) python -m pip install git+https://github.com/augmentedfabricationlab/assembly_information_model@master#egg=assembly_information_model
    (afab_course) python -m compas_rhino.install -p assembly_information_model

#### UR Fabrication Control
    
    (afab_course) python -m pip install git+https://github.com/augmentedfabricationlab/ur_fabrication_control@master#egg=ur_fabrication_control
    (afab_course) python -m compas_rhino.install -p ur_fabrication_control


### 3. Cloning the Course Repository

Create a workspace directory:

C:\Users\YOUR_USERNAME\workspace

Then open Github Desktop and clone the following repository into you workspace folder:

* [L.E.A.R.N. repository](https://github.com/le-ar-n/le-ar-n)


**Voilà! You can now go to VS Code, Rhino or Grasshopper to run the example files!**

### Slides
[How to run Python in Anaconda prompt, VS Code, Rhino & Grasshopper](https://docs.google.com/presentation/d/1TQNj92qhDZBSEtYajfmCCKaSDm2lwxsIdcFl3V1vE7Q/edit?usp=sharing)

