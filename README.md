# Funny Midi Alterations

A set of self-made Python (`.py`) script files that alter MIDI (`.mid`) files in different ways

## Exceptions

- If pitch is altered, Channel 10, the percussion/drum channel, gets to keep its notes in tact to avoid remapping percussion sounds

## Alterators Include: 

- Pitch Class Limiter `pitchClassLimiter.py`: Modifies notes by limiting their pitch to on pitch class, making all intervals be parallel octaves
