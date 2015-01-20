# decorative-otp

Requires: [python-pil](https://pypi.python.org/pypi/PIL), fonts-liberation

Produces decorative one-time-pad images suitable for your next LARP, ARG or just to leave around the house.

The images produced by the script:

* Incorporate a "faux typewriter" effect by randomly jittering the letters of an old-timey monospace font
* Are sized to fit on a standard index card when printed
* Are produced twice with the same numbers so two copies can be printed
* Have an incrementing index number for synchronisation purposes
* Are probably not suitable for actual cryptographic use

To use, you will also need `LiberationMono-Bold.ttf` and `LiberationMono-Regular.ttf` from the [Liberation Fonts](https://fedorahosted.org/liberation-fonts/) collection placed in to the same directory as the script.

This code was written hastily a long time ago. For publication in 2015 the random number functions have been changed to use Python's [SystemRandom](https://docs.python.org/2/library/random.html#random.SystemRandom), which should make the produced cards slightly more viable in the event someone accidentally uses them for actual cryptography.
