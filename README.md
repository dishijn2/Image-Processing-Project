# Image-Processing-Project
## An early fire detection system using image processing for waste stations

#### ABSTRACT
The framework proposed in this project utilizes Image Processing systems that examine a picture and a signal is used which gives a caution when the mishap will happen, mainly for open environments like waste stations. The system uses a camera to detect fires so there is no requirement for any sensors. The heat signatures and fire patterns in images are recognized to discover that it is a fire or not. The fundamental aim of the proposed model is to avoid false alerts and to detect fire as early as possible.

##### Architecture
![architecture](https://raw.githubusercontent.com/dishijn2/Image-Processing-Project/master/architecture.jpg)


##### MODULE DESCRIPTION
The framework is structured into four modules. First module is Video recording and moving to controller. The camera catches consistent edges from the region of its inclusion. The caught pictures or casings are should be move to the controller for applying picture preparing capacity. Shading based division is the second module of the framework. In this module in the wake of isolating the edges as single picture it is exposed to standard shading based division. The fragments are then partitioned into steady estimated squares. In the third module, fire design acknowledgment happens. The squares of the fragmented picture will be breaking down for the nearness of warmth mark or fire designs. Also, the last or fourth module is crisis trigger where if any unconventional example is distinguished in any of the squares for a specific timeframe, it will turn on the crisis mode and will give a caution.

