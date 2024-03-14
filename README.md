
# Subscrypt

Subscrypt is a Python class designed to facilitate file fragmentation and defragmentation using subpart salting and the Fernet encryption scheme from the `cryptography` library.

## Features

- Fragmentation of files into multiple encrypted segments
- Defragmentation to reconstruct the original file from the encrypted segments
- Support for customizable number of divisions and salt lengths
- Automatic generation and management of encryption keys

## Installation

To use Subscrypt, ensure you have Python installed and install the required dependencies:

```bash
pip install cryptography
```

## Usage

```python
from subscrypt import Subscrypt

# Initialize Subscrypt object with optional parameters
subscrypt = Subscrypt(divs=4, salt_length=4)

# Fragment a file
subscrypt.frag("sample.jpg")

# Defragment a file
subscrypt.defrag("sample.jpg", divs=4, licenseFile="license.enc")
```

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Make sure to replace `sample.jpg` with the actual filename and extension you want to fragment or defragment. This template assumes that you've organized your code into a Python module named `subscrypt`. You may need to adjust the import statement in the usage section according to your project structure.
