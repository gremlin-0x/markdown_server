# markdown_server
A Python local web server that serves markdown files locally and supports interlinking.

## Origin
I noticed I was getting very comfortable with writing in markdown in `vim` and I like the idea of it very much as well. So pretty soon I started taking notes of what I'm learning in `vim` and I realized, it's very difficult to read these without UI, so I added the following to my `.zshrc`:

```
function md() {
	css_url="/var/local/markdown.css"
	pandoc $1 -s -c $css_url -o /tmp/md.html 2>/dev/null
	xdg-open /tmp/md.html
}
```

But, then I thought it would be infinitely cooler if I could build a structured and interlinked group of markdown files and read and browse them, follow links between them, whenever I want.

## The code
I had a bunch of help from ChatGPT, I particularly struggled with the problem of serving `/index.md` upon execution and also automatic conversion to html whenever markdown files are called on the server.

## How it works
Just include this `server.py` script, `markdown.css` file of your choice (__I also got this one from somewhere, sorry about this, will credit author if they show up__) and all `.md` files you want to serve and then run:

```
python server.py
```
Assuming, one of the files will be named `index.md`, a browser will open with that file as the homepage. 

_Hope you too will find it useful._
