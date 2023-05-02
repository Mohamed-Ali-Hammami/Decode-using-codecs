import base64
import codecs

# Encoded string
encoded_string = "SGVsbG8gV29trhrybGQh"

# Try decoding as base64
try:
    print("Trying base64 decode")
    decoded = base64.b64decode(encoded_string).decode('utf-8')
    print("Decoded as base64: ", decoded)

    
# If it's not base64, try decoding as hex
except:
    try:
        print("Trying hex decode")
        decoded = codecs.decode(encoded_string, 'hex').decode('utf-8')
        print("Decoded as hex: ", decoded)
        
        
    # If it's not hex, try decoding as UTF-8
    except:
        try:
            print("Trying UTF-8 decode")
            decoded = encoded_string.decode('utf-8')
            print("Decoded as UTF-8: ", decoded)
        
        # If it's not UTF-8, try decoding as UTF-16
        except:
            try:
                print("Trying UTF-16 decode")
                decoded = encoded_string.decode('utf-16')
                print("Decoded as UTF-16: ", decoded)
                
            # If it's not UTF-16, try decoding as ISO-8859
            except:
                try:
                    print("Trying ISO-8859 decode")
                    decoded = encoded_string.decode('iso-8859-1')
                    print("Decoded as ISO-8859: ", decoded)
                    
                # If it's not ISO-8859, try decoding as Windows-1252
                except:
                    try:
                        print("Trying Windows-1252 decode")
                        decoded = encoded_string.decode('windows-1252')
                        print("Decoded as Windows-1252: ", decoded)
                        
                    # If it's not Windows-1252, try decoding as binary
                    except:
                        try:
                            print("Trying binary decode")
                            decoded = ''.join(chr(int(encoded_string[i:i+8], 2)) for i in range(0, len(encoded_string), 8))
                            print("Decoded as binary: ", decoded)
                            
                        # If it's not binary, assume it's ASCII
                        except:
                            try:
                                print("Trying ascii decode")
                                decoded = encoded_string.decode('ascii')
                                print("Decoded as ASCII: ", decoded)
                            
                            # If it's not ASCII, print an error message
                            except:
                                print("Error: could not decode the encoded string in any format")
