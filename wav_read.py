import sys
from pprint import pprint

def printFeader(file):
    wavfile = open(file,'rb')

    wav_header = {}

    wav_header['riff_chunk_id'] = wavfile.read(4).decode('ascii')
    wav_header['riff_chunk_size'] = int.from_bytes(wavfile.read(4), 'little')
    wav_header['riff_form_type'] = wavfile.read(4).decode('ascii')
    wav_header['fmt_chunk_id'] = wavfile.read(4).decode('ascii')
    wav_header['fmt_chunk_size'] = int.from_bytes(wavfile.read(4), 'little')
    wav_header['fmt_wave_format_type'] = int.from_bytes(wavfile.read(2), 'little')
    wav_header['fmt_channel'] = int.from_bytes(wavfile.read(2), 'little')
    wav_header['fmt_samples_per_sec'] = int.from_bytes(wavfile.read(4), 'little')
    wav_header['fmt_bytes_per_sec'] = int.from_bytes(wavfile.read(4), 'little')
    wav_header['fmt_block_size'] = int.from_bytes(wavfile.read(2), 'little')
    wav_header['fmt_bits_per_sample'] = int.from_bytes(wavfile.read(2), 'little')
    wav_header['data_chunk_id'] = wavfile.read(4).decode('ascii')
    wav_header['data_chunk_size'] = int.from_bytes(wavfile.read(4), 'little')

    pprint(wav_header)

if __name__ == '__main__':
    
    file = sys.argv[1]
    printFeader(file)