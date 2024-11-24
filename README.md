# Spotify-Animation

If you're looking to just use this and don't really care about what else this README has to say, just...

- Run `pip install -r requirements.txt`
- Change `fill_color` and `back_color` in `main.py` to whatever RGB colors you desire (they are defaulted to Black and Spotify Green)
- Change `link` in `main.py` to the link you want your QR Code to redirect to (e.g., your Spotify Jam link)
- Run `python main.py`

If you're looking to read more, thanks for your interest! Here's some more info...

## What?

This is a program that creates an animation of a QR Code bouncing around a screen, with the Spotify logo in the background. The QR Code is intended to link to a _Spotify Jam_, where fellow listeners can add their own songs to a collaborative queue; ideally, the animation is played on a big public display (e.g., a TV) for all function attendees to access.

## Why?

Whenever I hosted a function, I used Spotify on my Amazon Fire Stick (which was hooked up to a TV), but I wasn't too much of a fan for two reasons:

- It just uses Spotify's own UI, which is variable depending on the song. I thought this was a slight issue because, in a darker setting, sometimes my TV would just have a really bright screen and shift the mood a bit. I think that a simplistic box-bouncing-around UI is much more ideal.
- It doesn't have a convenient way for attendees to queue their own music. Sometimes people want to play what they like, and I think it's much easier to just have the Spoyify Jam information publicly displayed.

I admittedly drew a lot of inspiration from that one [Coinbase Super Bowl ad](https://www.youtube.com/watch?v=uJ9pNQrz0fA&ab_channel=AnthonyKalamut%28SouthsideAdGuy%29).

## How?

As you can probably tell from the code, I use `pygame` for the animation and `qrcode` and `PIL` for the QR Code generation and logo altering, respectively.

I've actually never used `pygame` before, and I used ChatGPT/LLaMa to help me a lot with this.

## Who?

This is intended for everyone to use (hence it's a public repo)! Feel free to also contribute to this project by making it more computationally efficient, adding new animation styles, etc...

## When?

I made this in October 2024, and a friend of mine saw it and said I should make it public. So here we are.

## Where?

I'm only adding this section to complete the "5W's + How" theme. I don't really think I have much to say about a "where" for this project.
