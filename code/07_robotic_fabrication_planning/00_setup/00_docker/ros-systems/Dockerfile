# Build:
#  docker build --rm -f Dockerfile -t augmentedfabricationlab/ros-abb-fabtory-planner .
#
# Usage:
#  docker pull augmentedfabricationlab/ros-abb-fabtory-planner

FROM gramaziokohler/ros-noetic-moveit
LABEL maintainer "Gonzalo Casas <casas@arch.ethz.ch>"

SHELL ["/bin/bash","-c"]
ENV CATKIN_WS=/root/catkin_ws
RUN mkdir -p $CATKIN_WS/src

COPY . /root/catkin_ws/src

# Add robot packages to local catkin workspace
RUN echo "Building tools for ROS" \
    && source /opt/ros/${ROS_DISTRO}/setup.bash \
    # Update apt-get because its cache is always cleared after installs to keep image size down
    && apt-get update \
    # && apt-get update && apt-get -y upgrade \
    # RRC packages
    && git clone https://github.com/compas-rrc/compas_rrc_ros.git \
    # && git clone https://github.com/gramaziokohler/abb_crb15000_5_95_moveit_config \
    # && git clone https://github.com/augmentedfabricationlab/robotic_setups_description.git \
    # Install dependencies
    && cd $CATKIN_WS \
    && rosdep install -y --from-paths . --ignore-src --rosdistro ${ROS_DISTRO}\
    # Build catkin workspace
    && catkin_make \
    # Clear apt-cache to reduce image size
    && rm -rf /var/lib/apt/lists/*
