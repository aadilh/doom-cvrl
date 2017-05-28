# Introduction

In order to use the trained model from DOOMBasic-v0 mission using A3C we first visualize the weights of the Convolution layers. The data flow graph of the Actor-Critic Network used is shown below.

![Data Flow graph of Actor-Critic Network](./images/architecture.png)


## Architecture

### Input Image

Color: Grayscale

Dimension: 84 x 84

### Convolution Layer 1
Activation: ReLU

Kernel Size: 4 x 4

Stride: 2 x 2

Padding: VALID

Input Channels: 16

Output Channels: 32

Output Dimensions: 20 x 20

### Convolution Layer 2
Kernel Size: 8 x 8

Stride: 4 x 4

Padding: VALID

Input Channels: 1

Output Channels: 16

Output Dimensions: 9 x 9

### Dense Layer

Activation: ReLU

Input Dimension: 81

Output Dimension: 256

# Results

For visualization we have sampled around 1500 images from 500 different game instances. The visualization of all images can be found in `images` directory. Here we only show the visualization of 144 images.

For Visualizing the weights of the kernels 2 different methods were used to scale the weights to 0-255 range. In the first method simple extrapolation of Intensity was done by subtracting minimum value and dividing the difference of maximum and minimum. In the second method the first method was applied to scale the positive and negative weights to an RGB space where negative weights were set to be blue and positive weights were set to be red.

## Input
![Input State Images](./images/small_master.png)

## Convolution Layer 1

Kernel | Scaling Method 1 | Scaling Method 2
-------|------------------|-----------------
0 | ![Kernel 1 grayscale](./images/conv1/grayscale_conv1_0.png) | ![Kernel 1 colored](./images/conv1/colored_conv1_0.png)
1 | ![Kernel 1 grayscale](./images/conv1/grayscale_conv1_1.png) | ![Kernel 1 colored](./images/conv1/colored_conv1_1.png)
2 | ![Kernel 1 grayscale](./images/conv1/grayscale_conv1_2.png) | ![Kernel 1 colored](./images/conv1/colored_conv1_2.png)
3 | ![Kernel 1 grayscale](./images/conv1/grayscale_conv1_3.png) | ![Kernel 1 colored](./images/conv1/colored_conv1_3.png)
4 | ![Kernel 1 grayscale](./images/conv1/grayscale_conv1_4.png) | ![Kernel 1 colored](./images/conv1/colored_conv1_4.png)
5 | ![Kernel 1 grayscale](./images/conv1/grayscale_conv1_5.png) | ![Kernel 1 colored](./images/conv1/colored_conv1_5.png)
6 | ![Kernel 1 grayscale](./images/conv1/grayscale_conv1_6.png) | ![Kernel 1 colored](./images/conv1/colored_conv1_6.png)
7 | ![Kernel 1 grayscale](./images/conv1/grayscale_conv1_7.png) | ![Kernel 1 colored](./images/conv1/colored_conv1_7.png)
8 | ![Kernel 1 grayscale](./images/conv1/grayscale_conv1_8.png) | ![Kernel 1 colored](./images/conv1/colored_conv1_8.png)
9 | ![Kernel 1 grayscale](./images/conv1/grayscale_conv1_9.png) | ![Kernel 1 colored](./images/conv1/colored_conv1_9.png)
10 | ![Kernel 1 grayscale](./images/conv1/grayscale_conv1_10.png) | ![Kernel 1 colored](./images/conv1/colored_conv1_10.png)
11 | ![Kernel 1 grayscale](./images/conv1/grayscale_conv1_11.png) | ![Kernel 1 colored](./images/conv1/colored_conv1_11.png)
12 | ![Kernel 1 grayscale](./images/conv1/grayscale_conv1_12.png) | ![Kernel 1 colored](./images/conv1/colored_conv1_12.png)
13 | ![Kernel 1 grayscale](./images/conv1/grayscale_conv1_13.png) | ![Kernel 1 colored](./images/conv1/colored_conv1_13.png)
14 | ![Kernel 1 grayscale](./images/conv1/grayscale_conv1_14.png) | ![Kernel 1 colored](./images/conv1/colored_conv1_14.png)
15 | ![Kernel 1 grayscale](./images/conv1/grayscale_conv1_15.png) | ![Kernel 1 colored](./images/conv1/colored_conv1_15.png)

## Convolutional Layer 2

Kernel | Scaling Method 1 | Scaling Method 2
-------|------------------|-----------------
0 | ![Kernel 1 grayscale](./images/conv2/grayscale_conv2_0.png) | ![Kernel 1 colored](./images/conv2/colored_conv2_0.png)
1 | ![Kernel 1 grayscale](./images/conv2/grayscale_conv2_1.png) | ![Kernel 1 colored](./images/conv2/colored_conv2_1.png)
2 | ![Kernel 1 grayscale](./images/conv2/grayscale_conv2_2.png) | ![Kernel 1 colored](./images/conv2/colored_conv2_2.png)
3 | ![Kernel 1 grayscale](./images/conv2/grayscale_conv2_3.png) | ![Kernel 1 colored](./images/conv2/colored_conv2_3.png)
4 | ![Kernel 1 grayscale](./images/conv2/grayscale_conv2_4.png) | ![Kernel 1 colored](./images/conv2/colored_conv2_4.png)
5 | ![Kernel 1 grayscale](./images/conv2/grayscale_conv2_5.png) | ![Kernel 1 colored](./images/conv2/colored_conv2_5.png)
6 | ![Kernel 1 grayscale](./images/conv2/grayscale_conv2_6.png) | ![Kernel 1 colored](./images/conv2/colored_conv2_6.png)
7 | ![Kernel 1 grayscale](./images/conv2/grayscale_conv2_7.png) | ![Kernel 1 colored](./images/conv2/colored_conv2_7.png)
8 | ![Kernel 1 grayscale](./images/conv2/grayscale_conv2_8.png) | ![Kernel 1 colored](./images/conv2/colored_conv2_8.png)
9 | ![Kernel 1 grayscale](./images/conv2/grayscale_conv2_9.png) | ![Kernel 1 colored](./images/conv2/colored_conv2_9.png)
10 | ![Kernel 1 grayscale](./images/conv2/grayscale_conv2_10.png) | ![Kernel 1 colored](./images/conv2/colored_conv2_10.png)
11 | ![Kernel 1 grayscale](./images/conv2/grayscale_conv2_11.png) | ![Kernel 1 colored](./images/conv2/colored_conv2_11.png)
12 | ![Kernel 1 grayscale](./images/conv2/grayscale_conv2_12.png) | ![Kernel 1 colored](./images/conv2/colored_conv2_12.png)
13 | ![Kernel 1 grayscale](./images/conv2/grayscale_conv2_13.png) | ![Kernel 1 colored](./images/conv2/colored_conv2_13.png)
14 | ![Kernel 1 grayscale](./images/conv2/grayscale_conv2_14.png) | ![Kernel 1 colored](./images/conv2/colored_conv2_14.png)
15 | ![Kernel 1 grayscale](./images/conv2/grayscale_conv2_15.png) | ![Kernel 1 colored](./images/conv2/colored_conv2_15.png)
16 | ![Kernel 1 grayscale](./images/conv2/grayscale_conv2_16.png) | ![Kernel 1 colored](./images/conv2/colored_conv2_16.png)
17 | ![Kernel 1 grayscale](./images/conv2/grayscale_conv2_17.png) | ![Kernel 1 colored](./images/conv2/colored_conv2_17.png)
18 | ![Kernel 1 grayscale](./images/conv2/grayscale_conv2_18.png) | ![Kernel 1 colored](./images/conv2/colored_conv2_18.png)
19 | ![Kernel 1 grayscale](./images/conv2/grayscale_conv2_19.png) | ![Kernel 1 colored](./images/conv2/colored_conv2_19.png)
20 | ![Kernel 1 grayscale](./images/conv2/grayscale_conv2_20.png) | ![Kernel 1 colored](./images/conv2/colored_conv2_20.png)
21 | ![Kernel 1 grayscale](./images/conv2/grayscale_conv2_21.png) | ![Kernel 1 colored](./images/conv2/colored_conv2_21.png)
22 | ![Kernel 1 grayscale](./images/conv2/grayscale_conv2_22.png) | ![Kernel 1 colored](./images/conv2/colored_conv2_22.png)
23 | ![Kernel 1 grayscale](./images/conv2/grayscale_conv2_23.png) | ![Kernel 1 colored](./images/conv2/colored_conv2_23.png)
24 | ![Kernel 1 grayscale](./images/conv2/grayscale_conv2_24.png) | ![Kernel 1 colored](./images/conv2/colored_conv2_24.png)
25 | ![Kernel 1 grayscale](./images/conv2/grayscale_conv2_25.png) | ![Kernel 1 colored](./images/conv2/colored_conv2_25.png)
26 | ![Kernel 1 grayscale](./images/conv2/grayscale_conv2_26.png) | ![Kernel 1 colored](./images/conv2/colored_conv2_26.png)
27 | ![Kernel 1 grayscale](./images/conv2/grayscale_conv2_27.png) | ![Kernel 1 colored](./images/conv2/colored_conv2_27.png)
28 | ![Kernel 1 grayscale](./images/conv2/grayscale_conv2_28.png) | ![Kernel 1 colored](./images/conv2/colored_conv2_28.png)
29 | ![Kernel 1 grayscale](./images/conv2/grayscale_conv2_29.png) | ![Kernel 1 colored](./images/conv2/colored_conv2_29.png)
30 | ![Kernel 1 grayscale](./images/conv2/grayscale_conv2_30.png) | ![Kernel 1 colored](./images/conv2/colored_conv2_30.png)
31 | ![Kernel 1 grayscale](./images/conv2/grayscale_conv2_31.png) | ![Kernel 1 colored](./images/conv2/colored_conv2_31.png)
