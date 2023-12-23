In this i am directly using x, y, z values of the livestock sensor to train and test the model. Here the acceleration x, y, z are the respective acceleration in x, y, z direction.
 
So input features to the model will be `x_0` to `z_269` (accelerometer data)and it will learn from its corresponding behaviours (sitting, standing, walking, grazing) during model training.

**dataset structure:**

| time_stamp          | sitting | standing | walking | grazing | x_0    | x_29   | ... | z_239  | z_269  |
|---------------------|---------|----------|---------|---------|--------|--------|-----|--------|--------|
| 2019-02-04T18:03:13 | 0       | 1        | 0       | 0       | -0.094 | -0.109 | ... | 0.598  | 0.594  |
| 2019-02-04T18:03:23 | 0       | 1        | 0       | 0       | -0.109 | -0.105 | ... | 0.586  | 0.582  |
| ...                 | ...     | ...      | ...     | ...     | ...    | ...    | ... | ...    | ...    |


