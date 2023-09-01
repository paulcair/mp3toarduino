import librosa
import numpy as np

# Declaring the variables we will be using 
FRAME_SIZE = 2048 #4096 # 2048 # Number of sample per frame
HOP_SIZE = 512 # 512 #Number of samples per fourier transform
SAMPLING_RATE = 22050 #Hz
FREQUENCY_DURATION_MS = 1000/SAMPLING_RATE*HOP_SIZE # This is the amount of times in ms that a frame lasts
N_CHROMA = 12 #number of chroma
N_OCTAVES = 2
MIDDLE_C = 277 # Hz value for middle C#


# File name and file path (do not include the extension in the file name)
filename = "abc" #Be sure it is one word
filepath = r"C:\Users\paulc\OneDrive\Documents\fab-academy\2023\wav-to-header-project\v2-harmonic"

# Input the path to the wav file here
input_wav_file = str(filepath)+ '\\' + str(filename)+'.wav' 
# Define the output path and txt file name here
output_header_file = str(filepath)+ '\\' + str(filename)+'.h'

# Load the audio file
audio, sr = librosa.load(input_wav_file)

# Compute chromagram
chromagram = librosa.feature.chroma_cqt(y=audio, sr=sr, hop_length=HOP_SIZE, n_chroma=N_CHROMA, n_octaves=N_OCTAVES)

# Determine the numnber of columns (frames) in the spectrogram
column_count = len(chromagram[0])

# Create an empty string array that will be appended to the header file
frequency_array = "const int " + filename + "[] = {"

# Iterate through the spectrogram one frame at a time and find the frequency bin with the highest value and add it to the frequency array.
for col_index in range(column_count):
    max_value = float('-inf')  # Initialize with negative infinity
    max_row_index = None

    for row_index, row in enumerate(chromagram):
        if row[col_index] > max_value:
            max_value = row[col_index]
            max_row_index = row_index   
    print(max_row_index)
    frequency = int(round(MIDDLE_C*2**((max_row_index+1)/12)))
    frequency_array += str(frequency) + ","

# Strip the last comma from the frequency array
frequency_array = frequency_array.rstrip(",")+"};"

# Create the header file
header_file = "#ifndef HEADER_FILE_H\n"
header_file += "#define HEADER_FILE_H\n"
header_file += "#define NUMBER_OF_NOTES " + str(column_count) + "\n"
header_file += "#define FREQUENCY_DURATION_MS " + str(int(round(FREQUENCY_DURATION_MS))) + "\n\n" 
header_file += frequency_array
header_file += "\n\n#endif // HEADER_FILE_H"

with open(output_header_file, 'w') as file:
    file.write(header_file)