---

# ASCII Banner Generator

---

## Table of Contents

* [Features](#features)
* [Installation](#installation)
* [Usage](#usage)
* [Tech Stack](#tech-stack)
* [Tests](#tests)
* [Contributing](#contributing)
* [License](#license)
* [Credits](#credits)

---

## Features

Key functionalities of the project:

* Convert any input text into ASCII art
* Uses styled font rendering (`ansi_shadow`)
* Automatically saves output to `banner.txt`
* Simple CLI workflow
* Lightweight with minimal dependencies

---

## Installation

Follow these steps to run the project locally.

### 1. Clone the repository

```bash
git clone https://github.com/SiddhathShah30/ascii-banner-generator.git
cd ascii-banner-generator
```

### 2. Install dependencies

```bash
pip install pyfiglet
```

### 3. Run the script

```bash
python banner.py
```

---

## Usage

The program prompts you to enter text and generates an ASCII banner.

### Example

```text
Enter the text to convert to ASCII art: Hello
```

### Output

```text
Copy This:

██╗  ██╗███████╗██╗     ██╗      ██████╗
██║  ██║██╔════╝██║     ██║     ██╔═══██╗
███████║█████╗  ██║     ██║     ██║   ██║
██╔══██║██╔══╝  ██║     ██║     ██║   ██║
██║  ██║███████╗███████╗███████╗╚██████╔╝
╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝ ╚═════╝
```

The ASCII output is also saved automatically to:

```
banner.txt
```

---

## Tech Stack

Technologies used in this project:

* Python 3
* pyfiglet – ASCII text rendering library

---

## Tests

No automated tests are included yet.

You can manually test by running:

```bash
python banner.py
```

Then verify:

* Console output appears correctly
* `banner.txt` file is generated

---

## Contributing

Contributions are welcome.

If you'd like to improve this project:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a pull request

For major changes, please open an issue first to discuss what you'd like to add.

---

## License
MIT License

Copyright (c) 2026 SiddharthShah30

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


---

## Credits

* Built using the pyfiglet library
* Inspired by classic terminal banner generators

---
