# Australian-Bush-Fire-Analysis

The following project was inspired from analyzing bush fire data collected from NASA's MODIS AND VIIRS fire detection algorithms.
The technologies and dataset can be viewed here -> https://www.kaggle.com/carlosparadis/fires-from-space-australia-and-new-zeland/code

The tree directory can be viewed below:

    /project
        app.py
        model.py
        model.pkl
        /template
            index.html
        /static
            /img
              #image is stored here
              
The following analysis can be concluded:

Overall:
NRT data has been in constant use more frequently and recently compared to ARC, providing more signals of confidence intensities overtime.

Nominal fires occur more frequently and detected for both NRT and ARC quality datasets. 

For NRT (Near Real Time) image data:
- Nominal fires occure more frequently, followed by High then Low confidence fires.
- High confidence Fires generally take more place in latitudes between -35 to -30 Latitude and 150 to 153 longitude.
- Low fire confidences can occur in most locations, between -20 to -10 latitude and 143 to 154 longitude.
- Nominal fires took more place in -35 to -30  latitude and 150 to 155 longitude. 

For ARC (Standard Quality Image) image data:
- Most high confidence fires took place in -30 (or between -20 to 10) latitude and 150 to 153 longitude.
- Most low confidence fires took place more in latitudes between -20 to -10 longitude.
- Nominal fires took place generally in -30 latitude and 151 longitude. 

The final product should be as follows:


![image](https://user-images.githubusercontent.com/69723555/133626605-e1a058d0-1ea8-48f0-b371-2e8d01196f66.png)

And...

![image](https://user-images.githubusercontent.com/69723555/133626725-ad0d8f7a-68a9-41af-be3e-230e6357978c.png)

