# Image-Processing-Project
## An early fire detection system using image processing for waste stations

#### PROPOSED MODEL
The framework proposed in this project utilizes Image Processing systems that examine a picture and a signal is used which gives a caution when the mishap will happen, mainly for open environments like waste stations. The system uses a camera to detect fires so there is no requirement for any sensors. The heat signatures and fire patterns in images are recognized to discover that it is a fire or not. The fundamental aim of the proposed model is to avoid false alerts and to detect fire as early as possible.

##### Architecture
![architecture](https://raw.githubusercontent.com/dishijn2/Image-Processing-Project/master/architecture.jpg)


#### MODULE DESCRIPTION
The framework is structured into four modules. First module is Video recording and moving to controller. The camera catches consistent edges from the region of its inclusion. The caught pictures or casings are should be move to the controller for applying picture preparing capacity. Shading based division is the second module of the framework. In this module in the wake of isolating the edges as single picture it is exposed to standard shading based division. The fragments are then partitioned into steady estimated squares. In the third module, fire design acknowledgment happens. The squares of the fragmented picture will be breaking down for the nearness of warmth mark or fire designs. Also, the last or fourth module is crisis trigger where if any unconventional example is distinguished in any of the squares for a specific timeframe, it will turn on the crisis mode and will give a caution.

##### Process Outline
![processflow](https://raw.githubusercontent.com/dishijn2/Image-Processing-Project/master/flow%20diagram.png)


#### METHODOLOGY
Fire is distinguished utilizing fire designs with warmth Signature. Warmth mark is shading examples to speak to the fire. There are three channels are utilized to discover the warmth signature. They are:
•	RGB filter
RGB channel is used to Extract Red (R) Green (G) and Blue (B) segment of every pixel. And after that in each pixel two conditions are checked. They are: 
	If R >G>B 
	If R> Rt (Rt is the red edge an incentive between (0,255). This depends on light in the picture. 

•	CieLAB filter
cieLAB shading model are Highlights red, yellow and related hues like orange. For all pixels in the edge the mean estimation of L, A and B parts are distinguished. For each pixel four channels are utilized.
	If L>L mean
	If A>A mean  
	If B>B mean 
	If B>A mean

•	RGB filter 2
It functions admirably around evening time mode. In this technique the R, G, and B segments are contrasted and edge esteems. (rt=140, gt=100, bt=100) Three conditions are verified: 
	R>rt
	G>gt
	B<b 

[Python code for fire detection](https://raw.githubusercontent.com/dishijn2/Image-Processing-Project/master/fire_detection.py)

[Experimentation and Results](https://github.com/dishijn2/Image-Processing-Project/blob/master/Experimentations%20and%20Result.pdf)
