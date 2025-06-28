## Creating an animation with Matplotlib

Essentially, this project creates many pie charts in a folder using the `makedynamicpiecharts()` function.
Then it opens them simultaneously with a delay with `animate()`.

I've posted videos I've made from this project at -insert link-.

This project was a huge learning experience. With challenge after challenge, making me realize I needed more specific code. Learned lamda alot better to sort the list of images so they would open in order.
I also created a map degrees function that would simulate going around a circle with `rotateval` of incrementation and `count` of amount of times.

The pythonanimations.py file contains the bulk of the code. The deleteimages_inimagesfolder.py simply resets the images folder by deleting all images for a new animation. And 360 mapping is where I developed the code to track degree intervals. Its more fleshed out with print statements in that file, versus in pythonanimations.py in simply appends to a list. 
