import sys
import typing

import mido
from mido import MidiTrack

pitchClasses = [
	"C",
	"C#/Db",
	"D",
	"D#/Eb",
	"E",
	"F",
	"F#/Gb",
	"G",
	"G#/Ab",
	"A",
	"A#/Bb",
	"B"
]

protectPercCh = True

def normalizePath(string: str) -> str:
	return string.replace("\\", "/").strip('"')

if __name__ == '__main__':
	# print(sys.argv)
	midiFile: mido.MidiFile = None
	if len(sys.argv) <= 1:
		midiFile = mido.MidiFile(normalizePath(input("Midi File Path: ")))
	else:
		midiFile = mido.MidiFile(normalizePath(sys.argv[1]))
	pitchClass = 0
	if len(sys.argv) <= 2:
		print("0 - C")
		print("1 - C#/Db")
		print("2 - D")
		print("3 - D#/Eb")
		print("4 - E")
		print("5 - F")
		print("6 - F#/Gb (Aka. Marc Evanstein's Pitch Class)")
		print("7 - G")
		print("8 - G#/Ab")
		print("9 - A")
		print("10 - A/B")
		print("11 - B", "Loop at 12 and onwards", sep="\n")
		pitchClass = int(input("Pitch Class ID: ")) % 12
	else:
		pitchClass = int(sys.argv[2]) % 12
	# midiFile.print_tracks()
	midiFileOUT = mido.MidiFile()
	midiFileOUT.ticks_per_beat, midiFileOUT.type = midiFile.ticks_per_beat, midiFile.type
	for trackg in midiFile.tracks:
		track = typing.cast(MidiTrack, trackg)
		trackv2 = mido.MidiTrack()
		# mido.MidiTrack().
		for messageg in track:
			message = typing.cast(mido.Message, messageg)
			if message.type in ['note_on', 'note_off']:
				if protectPercCh and message.channel == 9:
					trackv2.append(message)
					continue
				note = message.note
				note //= 12
				note *= 12
				note += pitchClass
				message.note = note
			else:
				# print(message.type)
				pass
			trackv2.append(message)
		midiFileOUT.tracks.append(trackv2)
	fileName = midiFile.filename.replace(".mid", f"_oneNoteRemap{pitchClasses[pitchClass].replace("/","_")}.mid")
	midiFileOUT.save(fileName)
	print(f"Saved to {fileName}!")
	input("Press enter key to exit...")
