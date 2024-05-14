import struct
import numpy as np

def load_audio(file_path):
    with open(file_path,'rb') as audio_file:
        # Getting the audio file parameters
        # Read the header to get audio file information
        
        header = audio_file.read(44) # In WAV files, first 44 bytes are reserved for the header
        print(f"The header is {header}")
        
        if header[:4] != b'RIFF' or header[8:12] != b'WAVE' or header[12:16] != b'fmt ':
            raise ValueError("Invalid WAV file")
            
        # Extract relevant information from the header
        header_chunk_id = struct.unpack('4s', header[0:4])[0]
        header_chunk_size = struct.unpack('<I', header[4:8])[0]
        header_chunk_format = struct.unpack('4s', header[8:12])[0]
        format_chunk_id = struct.unpack('4s', header[12:16])[0]
        format_chunk_size = struct.unpack('<I', header[16:20])[0]
        format_code = struct.unpack('<H', header[20:22])[0]
        channels = struct.unpack('<H', header[22:24])[0]
        sample_rate = struct.unpack('<I', header[24:28])[0]
        byte_rate = struct.unpack('<I', header[28:32])[0]
        block_align = struct.unpack('<H', header[32:34])[0]
        sample_width = struct.unpack('<H', header[34:36])[0]
        data_chunk_id = struct.unpack('4s', header[36:40])[0]
        data_chunk_size = struct.unpack('<I', header[40:44])[0]
        
        # Read the data from the file
        audio_file.seek(44);
        data = audio_file.read(data_chunk_size)
    
    # Converting the raw binary data to a list of integers : 
    data_array = np.frombuffer(data, dtype=np.uint16)
    # Convert to float32
    data_array = data_array.astype(np.float32)
    
    return header_chunk_id, header_chunk_size, header_chunk_format, format_chunk_id, format_chunk_size, data_array, format_code, channels, sample_width, sample_rate, byte_rate, block_align, data_chunk_id, data_chunk_size
