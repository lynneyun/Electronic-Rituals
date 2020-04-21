## What do my actions tell me about myself? ##

Maybe we should think about data machine learning but in an unexpected, conventionally 'useless' way. What happens when we get a bunch of datapoints that are not related? 

![Randomness feels like looking up at the night sky sometimes.](https://cdn.pixabay.com/photo/2017/08/30/01/05/milky-way-2695569__340.jpg)

A lot of  methods of predicting come out of wanting to make sense of the random — one thing that sticks out in my mind is my habit of trying to make sense of shapes in my retina before going to bed. It took me a while to realize that when you close your eyes, you see patterns and swirls from a phenomenon called [phosphenes](https://scienceline.org/2014/12/why-do-we-see-colors-with-our-eyes-closed/). What's really cool about this is that these patterns of light come from _inside your eyes_— just like how fireflies emit glow!

![An artist's attempt to illustrate phosophenes](https://feross.org/images/phosphene-artistic-depiction.gif)

 Maybe I could try to find the digital equivalent for my digital life, which is all the more significant since most of my interaction happens online these days. Where do I leave daily ‘footprints’ in my digital day? What can those footprints tell me about the past, present, and future? What could be their method of ‘communicating’ to me?

## Potential Data Collection Points ##

The first step in this process is collecting the data of my digital ‘footprints’ Some things that come to mind, with initial preferences in order:

- Things I’m typing on my computer every day. 
- data on browsers (cookies and history data)
- my downloads folders
- desktop (littered with screenshots)
- Instagram posts and ‘likes’
- Phone photos
- Email in/outbox

Fortunately (unfortunately?) I've discovered that there are free key logger programs for at least half of these activities. They claim that this is to monitor activity for children and potentially employees (yikes!). I've downloaded and installed one that's named [Elite Keylogger](https://www.elitekeyloggers.com/elite-keylogger-mac).

## How to transform them to a generative format ##

Largely, these data points end up being either text-based or image based. This gives me a few choices: 

- convert them into a self-generating text format:
	- via a Markov chain
	- Using GPT-2 (Q: will I have enough data in two weeks?)

- convert them into a self-generating image format:
	- via GANs

- convert them into another medium
	-  such as using text to generate an image format 
		-  I could use it to create my own ‘Star map’
		-  I could also use OCR on it (Running OCR via Python [Medium Post](https://medium.com/@bhadreshpsavani/how-to-use-tesseract-library-for-ocr-in-google-colab-notebook-5da5470e4fe0))

## Major Q: What do I want to predict? ##

I could make this into a random generator that produces an opaque-style oracle, something that needs to be interpreted for the meaning. Alternatively, I could just use data in a somewhat legible way to predict what I will be doing. 