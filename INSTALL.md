
## Table of Contents
- [Installation](#installation)
	- [Ubuntu 16.04](#ubuntu-1604)
	- [Ubuntu 18.04](#ubuntu-1804)

## Installation


### Ubuntu 16.04
Basic requirements:
- ROS Kinetic (`/rosversion: 1.12.7`)
- Gazebo 8.1.1
- Python 3.5.2
- OpenCV3, installed from sources for Python 3 (`git clone https://github.com/Itseez/opencv.git`)
- OpenAI gym

#### ROS Kinetic dependencies
```
sudo apt install python3-pip python3-pyqt4
sudo pip3 install rospkg catkin_pkg opencv-python netifaces scikit-image matplotlib



sudo apt-get install \
cmake gcc g++ qt4-qmake libqt4-dev \
libusb-dev libftdi-dev \
python3-defusedxml python3-vcstool \
ros-kinetic-octomap-msgs        \
ros-kinetic-joy                 \
ros-kinetic-geodesy             \
ros-kinetic-octomap-ros         \
ros-kinetic-control-toolbox     \
ros-kinetic-pluginlib	       \
ros-kinetic-trajectory-msgs     \
ros-kinetic-control-msgs	       \
ros-kinetic-std-srvs 	       \
ros-kinetic-nodelet	       \
ros-kinetic-urdf		       \
ros-kinetic-rviz		       \
ros-kinetic-kdl-conversions     \
ros-kinetic-eigen-conversions   \
ros-kinetic-tf2-sensor-msgs     \
ros-kinetic-pcl-ros \
ros-kinetic-navigation
```



#### Gazebo gym
go to your ros working space and install the application

```bash
cd ros_folder/src
git clone https://github.com/nguyensmai/tp-rl.git
cd tp-rl
pip3 install -e .
```

If successful, expect something like [this](https://gist.github.com/vmayoral/4a1e5999811ac8bfbf7875670c430d27).

#### Dependencies and libraries
```
sudo pip3 install h5py
sudo apt-get install python3-skimage
```

!!!WARNING!!! The commands above must be undone when you finish this project
Remove the library opencv2 of python2.7 

``` bash
cd /opt/ros/kinetic/lib/python2.7/dist-packages/
sudo mv cv2.so cv2Bkp.so
```

!!!WARNING!!! At the end of this project, to restore your initial opencv2 library for python2.7,remember to:

``` bash
cd /opt/ros/kinetic/lib/python2.7/dist-packages/
sudo mv cv2Bkp.so cv2.so
```

#### Try it out (turtlebot simple env)


Agent dependencies:
```bash
cd gym_gazebo/envs/installation
bash setup_kinetic.bash	
bash turtlebot_setup.bash 
```

Ignore error messages such as 
```bash 
bash: /home/mai/catkin_ws/src/tp-rl/gym_gazebo/envs/installation/catkin_ws/devel/setup.bash: No such file or directory
```

Open a new terminal. Run the environment with a sarsa agent:
```bash
cd working_space_path/tp-rl/examples/turtlebot
python3 circuit2_turtlebot_lidar_sarsa.py
```

**Known Issues**:
- `spacenav_node` not compiling. `CATKIN_IGNORE`d.
- `wiimote` not compiling. `CATKIN_IGNORE`d.
- `kobuki_qtestsuite` not compiling. `CATKIN_IGNORE`d.

-  If you get the message error ```bash
Invalid <arg> tag: environment variable 'GYM_GAZEBO_WORLD_CIRCUIT2' is not set. 

Arg xml is <arg default="$(env GYM_GAZEBO_WORLD_CIRCUIT2)" name="world_file"/>
The traceback for the exception was written to the log file
``` You will need to go to folder  gym_gazebo/envs/installation and execute bash turtlebot_setup.bash 

-  If you get the message error ```bash
ImportError: /opt/ros/kinetic/lib/python2.7/dist-packages/cv2.so: undefined symbol: PyCObject_Type
```
you will need to remove the library opencv2 of python2.7 

### Ubuntu 18.04 (not supported, only  indicative)

#### Basic requirements
- ROS Melodic: Desktop-Full Install recommended, includes Gazebo 9.0.0 (http://wiki.ros.org/melodic/Installation/Ubuntu).
- Gazebo 9.0.0

#### ROS Melodic related dependencies
```
sudo apt-get install \
python-pip python3-vcstool python3-pyqt4 \
pyqt5-dev-tools \
libbluetooth-dev libspnav-dev \
pyqt4-dev-tools libcwiid-dev \
cmake gcc g++ qt4-qmake libqt4-dev \
libusb-dev libftdi-dev \
python3-defusedxml python3-vcstool \
ros-melodic-octomap-msgs        \
ros-melodic-joy                 \
ros-melodic-geodesy             \
ros-melodic-octomap-ros         \
ros-melodic-control-toolbox     \
ros-melodic-pluginlib	       \
ros-melodic-trajectory-msgs     \
ros-melodic-control-msgs	       \
ros-melodic-std-srvs 	       \
ros-melodic-nodelet	       \
ros-melodic-urdf		       \
ros-melodic-rviz		       \
ros-melodic-kdl-conversions     \
ros-melodic-eigen-conversions   \
ros-melodic-tf2-sensor-msgs     \
ros-melodic-pcl-ros \
ros-melodic-navigation
```

#### Install Python Packages:
```
sudo pip install gym
sudo pip install h5py scikit-image
pip install tensorflow-gpu (if you have a gpu if not then just pip install tensorflow)
sudo pip install keras
```

#### Install Sophus:
```
cd ~
git clone https://github.com/stonier/sophus -b release/0.9.1-kinetic
cd sophus
mkdir build
cd build
cmake ..
make
sudo make install
```

#### Install gym-gazebo
```
cd ~
git clone https://github.com/erlerobot/gym-gazebo
cd gym-gazebo
sudo pip install -e .
```

#### Run bash files, build the ros workspace:
```
cd gym-gazebo/gym_gazebo/envs/installation
bash setup_melodic.bash
```

#### Execution examples
##### Run example for qlearn:
terminal 1
```
cd gym-gazebo/gym_gazebo/envs/installation/
bash turtlebot_setup.bash
```
terminal 2
```
cd gym-gazebo/examples/turtlebot
python circuit_turtlebot_lidar_qlearn.py
```

##### Run example for dqn:
terminal 1
```
cd gym-gazebo/gym_gazebo/envs/installation/
bash turtlebot_nn_setup.bash
```
terminal 2
```
cd gym-gazebo/examples/turtlebot
python circuit_turtlebot_lidar_qlearn.py
```


##### Using Neural Networks
This part of the installation is required only for the environments using DeepQLearning.

###### Keras and Theano installation
```bash
# install dependencies

sudo apt-get install gfortran

# install sript specific dependencies (temporal)
sudo apt-get install python-skimage

# install Theano
git clone git://github.com/Theano/Theano.git
cd Theano/
sudo python setup.py develop

#isntall Keras
sudo pip install keras
```
dot_parser error fix:
```bash
sudo pip install --upgrade pydot
sudo pip install --upgrade pyparsing
```
###### Enablig GPU for Theano

Follow the instructions [here](http://deeplearning.net/software/theano/install.html#gpu-linux) and change $PATH instead of $CUDA_ROOT.

Working on a clean installation of Ubuntu 18.04 using CUDA 10.0.

The following flags are needed in order to execute in GPU mode, using an alias is recommended.
```bash
THEANO_FLAGS=mode=FAST_RUN,device=gpu,floatX=float32
```

---

