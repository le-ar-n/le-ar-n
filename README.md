# L.earning E.nvironment for A.rchitectural R.obotics for N.ewbies

## Welcome

Welcome to [**L.E.A.R.N.**](https://le-ar-n.github.io/le-ar-n/), a platform dedicated to beginner-friendly creative coding tutorials and exercises for building architecture with robots.

In these tutorials, we will introduce computational methods for architecture, fabrication & construction, incentivising computational literacy. Students will learn the theoretical background and basic implementation details of fundamental datastructures and algorithms, and to plan and control robot tasks in CAD environments using the **[COMPAS](https://compas-dev.github.io/)** and **[COMPAS FAB](https://gramaziokohler.github.io/compas_fab/latest/)** framework, and other open-source libraries.


## Session Blocks

Title | Description | Slides  
----- | ----------- | ------
**Python Basics** | Quick start on Python | [Python Basics](https://docs.google.com/presentation/d/1WHFK_gnQg8jOp2D4GcX2HFWUhVAizvreffQBoUX3fVA/edit?usp=sharing)
**Geometry** | COMPAS geometry  | [Geometry](https://docs.google.com/presentation/d/1B_O2qr_oV_Olf64CaTKgPp1fjy4Z61LwsM8OHDhlvyQ/edit?usp=sharing)
**Frames and Transformations** | Frames and transformations  | [Frames and Transformations](https://docs.google.com/presentation/d/1eXnclwxPe9wMHOsk25_IeLtQKK4OSs0BAjjTEWq7eF0/edit?usp=sharing)
**Data Structures** | COMPAS data structures  | [Data Structures](https://docs.google.com/presentation/d/1ZhYimM0iN6Z2A4RCKiuKsYBqPTwIptLr44-D3ilJjXc/edit?usp=sharing)
**Assembly Information Model** | Assembly and Element data structures  | [Assembly Information Model](https://docs.google.com/presentation/d/1J1jkmQLJ98wGwzvmwt8uPxFqBe0STTynKg6Yyv8J2nE/edit?usp=sharing)
**AM Information Model** | Additive Manufacturing data structures  | [AM Information Model](https://docs.google.com/presentation/d/1gLgQDtK69PGTvqRwn9LETbHu659OO8nmUyur00MQUM0/edit?usp=sharing)
**XR Assembly** | Visualize Assembly data in XR  | [XR Assembly](https://docs.google.com/presentation/d/1DdDuJAUb5US7SeI-M_4wPy6XgSvLWnsWIEJiyZtz0XI/edit?usp=sharing)
**Robotic Fabrication Planning** | Planning of a robotic assembly process | [Robotic Fabrication Planning](https://docs.google.com/presentation/d/1qSVU1neaKMGB9G6ZXQtxqF8JLM43VixEK1s12HQNV-g/edit?usp=sharing)
**Robotic Fabrication Control** | Control of a robotic assembly process | [Robotic Fabrication Control](https://docs.google.com/presentation/d/1vHCZJLlue4ypWv8aqYPhdepQ9mzrjY1xkL59vnXltqw/edit?usp=sharing)
**Design Algorithms** | Simple generative design algorithms | 
**Utilities** | Helpful utilities |  


## Requirements

* Windows 10 Professional
* Rhino 6 / Grasshopper
* [Anaconda Python](https://www.anaconda.com/distribution/?gclid=CjwKCAjwo9rtBRAdEiwA_WXcFoyH8v3m-gVC55J6YzR0HpgB8R-PwM-FClIIR1bIPYZXsBtbPRfJ8xoC6HsQAvD_BwE)
* [Visual Studio Code](https://code.visualstudio.com/)
* [Github Desktop](https://desktop.github.com/)

## Dependencies

* [COMPAS](https://compas-dev.github.io/)
* [COMPAS FAB](https://gramaziokohler.github.io/compas_fab/latest/)
* [Assembly Information Model](https://github.com/augmentedfabricationlab/assembly_information_model)
* [AM Information Model](https://github.com/augmentedfabricationlab/am_information_model)
* [UR Fabrication Control](https://github.com/augmentedfabricationlab/ur_fabrication_control)


## Getting started

Please set up your Python environment following these instructions:

### 1. Setting up the Anaconda environment with COMPAS

Execute the commands below in Anaconda Prompt:
	
    (base) conda config --add channels conda-forge

#### Windows
    (base) conda create -n learn compas_fab --yes
    (base) conda activate learn

#### Mac
    (base) conda create -n learn compas_fab python.app --yes
    (base) conda activate learn
    

#### Verify Installation

    (learn) pip show compas_fab
####
    Name: compas-fab
    Version: 0.19.1
    Summary: Robotic fabrication package for the COMPAS Framework
    ...

#### Install on Rhino

    (learn) python -m compas_rhino.install

NOTE: This installs default to Rhino 6.0, if you are using a different Rhino version add `-v 5.0` or `-v 7.0` after the above statement.


### 2. Installation of Dependencies

    (learn) conda install git

#### Assembly Information Model
    
    (learn) python -m pip install git+https://github.com/augmentedfabricationlab/assembly_information_model@master#egg=assembly_information_model
    (learn) python -m compas_rhino.install -p assembly_information_model
    
NOTE: If you are not using Rhino 6.0, after the above statement, add `-v` followed by the version of your Rhino software (i.e `-v 5.0` or `-v 7.0`)

#### AM Information Model
    
    (learn) python -m pip install git+https://github.com/augmentedfabricationlab/am_information_model@master#egg=am_information_model
    (learn) python -m compas_rhino.install -p am_information_model

NOTE: If you are not using Rhino 6.0, after the above statement, add `-v` followed by the version of your Rhino software (i.e `-v 5.0` or `-v 7.0`)

#### UR Fabrication Control
    
    (learn) python -m pip install git+https://github.com/augmentedfabricationlab/ur_fabrication_control@master#egg=ur_fabrication_control
    (learn) python -m compas_rhino.install -p ur_fabrication_control

NOTE: If you are not using Rhino 6.0, after the above statement, add `-v` followed by the version of your Rhino software (i.e `-v 5.0` or `-v 7.0`)


### 3. Cloning the Course Repository

Create a workspace directory:

C:\Users\YOUR_USERNAME\workspace

Then open Github Desktop and clone the [L.E.A.R.N. repository](https://github.com/le-ar-n/le-ar-n) into you workspace folder.

**Voilà!**
**You can now go to VS Code, Rhino or Grasshopper to run the example files!**
