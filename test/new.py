import os

# Print key value
key_value = os.environ.get("WHO_TO_TRUST")

if __name__ == "__main__":
  print(type(key_value))
  print(key_value)
