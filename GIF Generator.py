import imageio
filenames = ["Image-Slideshow/Piyush.jpg","Image-Slideshow/Kaira.png"]
images = []
for filename in filenames:
    images.append(imageio.imread(filename))
imageio.mimsave('Image-Slideshow/movie.gif', images,'GIF',duration=1)