# conundrum
A minor mocking of the enigma machine, set in the 2020s

Something I slapped together to try to keep my sanity during some weird times. I tried to update the enigma machine to 256 characters instead of 26, 256 rotors instead of the handful available, and the possibility of a character to encode to itself.

I designed it to take input data from stdin and write the resulting data directly to stdout. 

In main.py there's a comment on exactly how to put in settings --
# ./main.py 0x000b2e1affff 39 164 41 157 60 226 0x0123

The first argument is a big number in hex, compirising of six bytes, stating all of the positions on the six wheels. So in the example, the first wheel position is 0x00. the second 0x0b, the third 0x2e, and so on.

The next six arguments are (in order) the six wheels from precon.py. There are 256 of such wheels defined in precon.py.

The last argument is a two-byte hexadecimal number instructing which position on the "big wheel" it should start with. The big wheel has 65,536 positions, or 0x0000 through 0xFFFF.

Now, as far as which settings to use, well, that's up to you.

All of the other code is just purpose-built code that probably could have been skipped if I really wanted to learn the more esoteric options of moving data around with common bash utilities.
