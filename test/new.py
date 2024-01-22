import os
import base64

# Print key value
key_value = os.environ.get("WHO_TO_TRUST")
actual_val_encoded = base64.b64encode(f"{key_value}".encode("ascii"))
actual_val_decoded = actual_val_encoded.decode("ascii")

if __name__ == "__main__":
  print(type(key_value))
  print(key_value)
  print(actual_val_encoded)
  print(actual_val_decoded)
