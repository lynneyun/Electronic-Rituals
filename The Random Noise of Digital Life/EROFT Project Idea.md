## EROFT Final Project Idea ##

## What do my actions tell me about myself? ##

Maybe we should think about data machine learning but in an unexpected, conventionally 'useless' way. What happens when we get a bunch of datapoints that are not related? A lot of  methods of predicting come out of wanting to make sense of the random — one thing that sticks out in my mind is my habit of trying to make sense of shapes in my retina before going to bed. It took me a while to realize that when you close your eyes, you see patterns and swirls from a phenomenon called [phosphenes](https://www.huffpost.com/entry/why-do-i-see-patterns-when-i-close-my-eyes_b_7597438). Some people think the images that you see might originate from 'flashes of things you've seen', or ‘things you have experienced throughout your day’. Maybe I could try to find the digital equivalent for my digital life, which is all the more significant since most of my interaction happens online these days. Where do I leave daily ‘footprints’ in my digital day? What can those footprints tell me about the past, present, and future? What could be their method of ‘communicating’ to me?

## Potential Data Collection Points ##

The first step in this process is collecting the data of my digital ‘footprints’ Some things that come to mind, with initial preferences in order:

- Things I’m typing on my computer every day. (Q: Maybe trying to install a keylogger is not a great idea from a security standpoint though?)
- data on browsers (cookies and history data)
- my downloads folders
- desktop (littered with screenshots)
- Instagram posts and ‘likes’
- Phone photos
- Email in/outbox

## How to transform them to oracle format ##

Largely, these data points end up being text-based. This gives me a few choices: 

- convert them into a self-generating text format:
	- via a Markov chain
	- Using GPT-2 (Q: will I have enough data in two weeks?)
- convert them into another medium
	-  such as using text to generate an image format 
		-  I could use it to create my own ‘Star map’
		-  I could also use OCR on it (Running OCR via Python [Medium Post](https://medium.com/@bhadreshpsavani/how-to-use-tesseract-library-for-ocr-in-google-colab-notebook-5da5470e4fe0))