# Voice-Controlled Calculator

## Description
The Voice-Controlled Calculator is a simple Python script that allows users to perform basic arithmetic operations through voice commands. Using the `speech_recognition` library, the script captures spoken input, interprets arithmetic expressions, and calculates the result. It is designed with comprehensive error handling for scenarios like speech recognition errors, invalid inputs, and connectivity issues.

---

## Features
- Perform basic arithmetic operations using voice commands:
  - Addition (`+`)
  - Subtraction (`-`)
  - Multiplication (`x` or `*`)
  - Division (`divided by`)
  - Modulus (`mod`)
  - Exponentiation (`^`)
- Real-time voice-to-text processing.
- Handles multiple error scenarios:
  - Recognition issues (e.g., unclear speech).
  - Invalid input formats.
  - Missing internet connection.

---

## Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/AZaUk/voice-controlled-calculator.git
   ```
2. Navigate to the project directory:
   ```bash
   cd voice-controlled-calculator
   ```
3. Run the script:
   ```bash
   python voice_calculator.py
   ```
4. Speak an arithmetic expression when prompted (e.g., "5 + 5" or "9 - 3").
5. Review the calculated result displayed in the console.

---

## Example
**Input:** (Spoken)
```
5 + 5
```
**Output:**
```
10
```

---

## Requirements
- Python 3.6 or higher
- `speech_recognition` library

Install the library using pip:
```bash
pip install SpeechRecognition
```

---

## Contributing
1. Fork the repository.
2. Create a new branch for your feature:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature description"
   ```
4. Push your branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

---

## TODO's
- Add functionality to synthesize the answer using text-to-speech, enabling seamless interaction for visually impaired users
- Add support for an infinite number of operands, allowing calculations with any quantity of values and accommodating various data types

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

## Acknowledgments
Special thanks to the developers of the `speech_recognition` library for enabling seamless voice-to-text integration and to all contributors for enhancing this project.

