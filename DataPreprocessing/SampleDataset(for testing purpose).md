The dataset is a time series collection of accelerometer data with corresponding behavior labels, aiming to classify cattle activities into four categories: sitting, standing, walking, and grazing. The dataset is organized in 10-second intervals, capturing accelerometer readings along three axes (x, y, z) sampled at 1 Hz. Each timestamped entry includes binary indicators for the observed behaviors, providing a structured representation of cattle actions over time. The goal is to leverage this dataset for normal behavior prediction.

1. `time_stamp`: Represents the timestamp when the data was recorded.
2. `sitting`: Binary label indicating whether the observed behavior is sitting (1) or not (0).
3. `standing`: Binary label indicating whether the observed behavior is standing (1) or not (0).
4. `walking`: Binary label indicating whether the observed behavior is walking (1) or not (0).
5. `grazing`: Binary label indicating whether the observed behavior is grazing (1) or not (0).
6. `x_0` to `z_269`: Accelerometer readings along the x, y, and z axes at different time points. The suffixes (0, 29, 59, ..., 269) represent specific time intervals within a 10-second window.

**dataset structure:**

| time_stamp          | sitting | standing | walking | grazing | x_0    | x_29   | ... | z_239  | z_269  |
|---------------------|---------|----------|---------|---------|--------|--------|-----|--------|--------|
| 2019-02-04T18:03:13 | 0       | 1        | 0       | 0       | -0.094 | -0.109 | ... | 0.598  | 0.594  |
| 2019-02-04T18:03:23 | 0       | 1        | 0       | 0       | -0.109 | -0.105 | ... | 0.586  | 0.582  |
| ...                 | ...     | ...      | ...     | ...     | ...    | ...    | ... | ...    | ...    |

this dataset is converted into:

**dataset structure:**

|     x    |     y    |     z    | sitting | standing | walking | grazing |
|----------|----------|----------|---------|----------|---------|---------|
|  0.438   |  0.844   |  0.309   |    0    |     0    |    1    |    0    |
| -0.184   | -0.82    | -0.68    |    0    |     0    |    1    |    0    |
|  0.652   |  0.711   |  0.148   |    0    |     0    |    1    |    0    |
|  1.031   |  0.703   |  0.395   |    0    |     0    |    1    |    0    |
|  0.711   |  0.48    |  0.473   |    0    |     0    |    1    |    0    |
|  0.641   |  0.547   |  0.504   |    0    |     0    |    1    |    0    |


