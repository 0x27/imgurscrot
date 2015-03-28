# imgurscrot
imgur/scrot screengrabber/uploader

## What?
Simple utility that takes a screenshot of your entire screen and pushes it to Imgur using the Imgur API.

## API
Get an API key from [api.imgur.com][api.imgur.com] and set the client_id variable to the client_id you get. Just pick one of the anonymous tokens as I was not arsed linking screenshots 
to accounts.

## Requirements
Its all stdlib except [pyscreenshot][pyscreenshot] and [requests][requests] which you can easily install.  

```
pip install pyscreenshot requests
```

## Use
Put it somewhere in $PATH as an executable (chmod +x) file named "imgurscrot" and just do "imgurscrot" to screeenshot your full screen and automatically upload it.

## Licence
[Licenced under the WTFPL][wtfpl]

## Beer
Beer can be sent to 16MtQtgCVgZvqXoYFzi1L85cKDQAxLGY4A :)

## Bugs
If it fucks up leave an issue in the tracker please.

## Notes
I had meant to use the actual imgur library but it kept fucking up so I just used requests instead. 

[api.imgur.com]: https://api.imgur.com
[pyscreenshot]: https://pypi.python.org/pypi/pyscreenshot
[requests]: https://pypi.python.org/pypi/requests
[wtfpl]: http://wtfpl.net

