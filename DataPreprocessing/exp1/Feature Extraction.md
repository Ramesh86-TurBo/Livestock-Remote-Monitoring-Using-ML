In this i am directly using x, y, z values of the livestock sensor to train and test the model. Here the acceleration x, y, z are the respective acceleration in x, y, z direction.
 
So input features to the model will be x, y, z (accelerometer data)and it will learn from its corresponding behaviours (sitting, standing, walking, grazing) during model training.

**dataset structure:**


|     x    |     y    |     z    | sitting | standing | walking | grazing |
|----------|----------|----------|---------|----------|---------|---------|
|  0.438   |  0.844   |  0.309   |    0    |     0    |    1    |    0    |
| -0.184   | -0.82    | -0.68    |    0    |     0    |    1    |    0    |
|  0.652   |  0.711   |  0.148   |    0    |     0    |    1    |    0    |
|  1.031   |  0.703   |  0.395   |    0    |     0    |    1    |    0    |
|  0.711   |  0.48    |  0.473   |    0    |     0    |    1    |    0    |
|  0.641   |  0.547   |  0.504   |    0    |     0    |    1    |    0    |


