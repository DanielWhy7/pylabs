# Laboratory Work No. 3
# Working with multidimensional arrays

- [Theory](#theory)
  - [Images](#images)
  - [Audio files](#audio-files)
  - [NumPy](#numpy)
  - [OpenCV](#opencv)
  - [SoundFile](#soundfile)
  - [Matplotlib](#matplotlib)
  - [Useful links](#useful-links)
- [Task](#task)
  - [General task](#general-task)
  - [Transformations](#transformations)
  - [Variants](#variants)

# Theory

## Images
Images are multidimensional arrays (matrices) of pixels. Each pixel contains a brightness value that affects the color of the image.

Main components:
- Size - the length and width of the image, measured in the number of pixels.
- Channels - the third dimension after length and width. The number of channels affects the color of the image. Color images usually have 3 channels - red, green, and blue (r, g, b); grayscale and binary images have one channel (brightness value). Images with transparency have 4 channels (r, g, b, a), where the fourth channel is responsible for transparency.
- Pixel - the smallest indivisible unit of an image. A pixel has a brightness from 0 to 255 (uint) or from 0 to 1 (float). A pixel can contain from 1 to 4 values depending on the number of image channels. For example, a green pixel will have the value (0, 255, 0).

## Audio files
Audio files are one-dimensional (mono) or two-dimensional (stereo) arrays consisting of samples.

Main components:
- Size - the length of the array, the number of samples.
- Sample - an instantaneous value of the amplitude of the sound wave.
- Amplitude - the value of each sample. Has a value from -1.0 to 1.0.
- Sampling rate - the number of samples per second, measured in hertz (Hz, Hz). Affects the audio quality. Standard CD quality is 44100 Hz.
- Duration - the size divided by the sampling rate (gives the length of the audio in seconds).

## NumPy
NumPy is a library for working with multidimensional arrays and matrix operations. It provides high performance due to its implementation in C/C++.

Installation: 
```
pip install numpy
```

Key features:

- N-dimensional arrays (ndarray)
- Mathematical functions (linear algebra, Fourier transform)
- Tools for integration with C/C++


## OpenCV

OpenCV is an open-source library for computer vision and image processing. It was developed to solve problems related to the processing and analysis of images and video.

Installation:
```
pip install opencv-python
```

Example of use:
```py
import cv2  # import
# The following import variant is also possible:
# from cv2 import cv2

img = cv2.imread('image.jpg')  # load image

cv2.imshow('girl', img)  # display
cv2.waitKey(0)

cv2.imwrite('image2.jpg', img)  # save image
```

Since an image is a multidimensional array, operations from the `numpy` library can be applied to it, for example:

```py
img[0, 0, :] = 255  # replace pixel value
shape = img.shape  # get size
img2 = img.astype(np.uint8)  # convert types
```

## SoundFile

SoundFile is a library for reading and writing audio files. Data is loaded in the format of numpy arrays.

Installation: 
```py
pip install soundfile
```

Example of use:
```py
import soundfile as sf

# Load audio
data, samplerate = sf.read('audio.mp3')

print(f"Array of samples: {data}")
print(f"Sampling rate: {samplerate}")

# Save audio  
sf.write('new_audio.mp3', data, samplerate)
```


## Matplotlib

Matplotlib is a data visualization library in Python that allows you to create static, animated, and interactive plots.

Installation:
```
pip install matplotlib
```

Example of displaying an image:
```py
import matplotlib.pyplot as plt  # import
plt.imshow(img)  # load image
plt.show()  # display
```

Example of plotting a sine graph:
```py
import matplotlib.pyplot as plt
import numpy as np

# create data
x = np.linspace(0, 10, 100)  # 100 points from 0 to 10
y = np.sin(x)  # find sine

# create plot
plt.figure(figsize=(10, 5))  # plot size

plt.plot(x, y, label='sin(x)', color='blue')  # linear sine graph
plt.title('Sine Graph')  # plot title
plt.xlabel('x')  # x-axis label
plt.ylabel('sin(x)')  # y-axis label
plt.axhline(0, color='black',linewidth=0.5, ls='--')  # line on x-axis
plt.axvline(0, color='black',linewidth=0.5, ls='--')  # line on y-axis
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)  # grid
plt.legend()  # legend

# display plot
plt.show()
```

## Useful links

- [numpy (doc)](https://numpy.org/doc/stable/index.html)
- [OpenCV (doc)](https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html)
- [scikit-image](https://scikit-image.org/docs/stable/)
- [SoundFile (doc)](https://python-soundfile.readthedocs.io/en/latest/)
- [matplotlib](https://matplotlib.org/stable/index.html)


# Task
## General task

1. Using the data from the second laboratory work, read an image or audio from a file.
2. Print the size of the image or audio.
3. Perform the transformations from your variant on the image or audio file. 
4. Use matplotlib to demonstrate the original image or audio and the result.
5. Save the result to a new file.

The path to the source file, the path for saving, and the parameters according to the variant (if any) must be passed through command-line arguments.


## Transformations
These are not the variants themselves! The variants are below.

1. Crop the image to the specified dimensions, starting from the top-left corner.
2. Resize the image to the specified dimensions.
3. Combine (splice) two images.
4. Rotate the image by a specified angle.
5. Invert the colors in the image.
6. Make the image grayscale.
7. Make the image binary.
8. Swap the image channels.
9. Flip (mirror) the image.
10. Overlay one image on another, making the overlaid image semi-transparent.
11. Make a puzzle out of the image (divide into n equal parts and reassemble them randomly into an image of the same size).
12. Add white noise to the image.
13. Add a frame to the image (draw it yourself or use an image).
14. Make the image round (the area outside the circle must be black, white, or transparent).
15. Add a gradient effect (the image gradually becomes lighter from one side).


16. Decrease the amplitude of the audio file samples by a given amount.
17. Increase the amplitude of the audio file samples by a given amount.
18. Trim the audio length in a specified range.
19. Concatenate (glue) two audio files.
20. Reverse the audio.
21. Make a silence filter (remove sections quieter than a given threshold).
22. Mix two audio files.
23. Make an echo effect (by overlaying with a delay).
24. Increase the audio playback speed by a given factor.
25. Decrease the audio playback speed by a given factor.
26. Add white noise to the audio.
27. Decrease the amplitude above a given value to a threshold value.
28. Make a smoothing (averaging of values) of the audio using numpy.convolve.
29. Amplify high frequencies (to highlight high frequencies, you need to subtract the smoothed version from the normal version of the audio).

## Variants

The variants indicate the numbers of the transformations that you need to perform. The transformations themselves are above.

1. (1, 4, 10)
2. (2, 6, 9)
3. (3, 5, 6)
4. (4, 7, 9)
5. (5, 11, 12)
6. (6, 14, 15)
7. (7, 2, 13)
8. (8, 3, 12)
9. (9, 13, 8)
10. (3, 7, 11)


11. (16, 23, 26)
12. (17, 18, 20)
13. (18, 21, 25)
14. (19, 26, 28)
15. (20, 21, 22)
16. (21, 24, 28)
17. (22, 23, 29)
18. (23, 25, 27)
19. (24, 19, 29)
20. (25, 26, 28)
