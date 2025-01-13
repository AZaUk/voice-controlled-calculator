import speech_recognition as sr
import operator

while True:
    r = sr.Recognizer()
    print("Say something like '5 + 5' or '9 - 3'")
    with sr.Microphone() as source:
        audio = r.listen(source)
        voice = ''

        try:
            voice = r.recognize_google(audio, language="en-EN")
            print(f"You said: {voice}")
        except sr.UnknownValueError as e:
            print("Could not understand the audio.")
            print(e)
        except sr.RequestError as e:
            print("No internet connection.")
            print(e)
        except TypeError as e:
            print("An error occurred with the input.")
            print(e)
        except ValueError as e:
            print("Only numerical expressions are accepted.")
            print(e)
        except KeyError as e:
            print("Only numerical expressions are accepted.")
            print(e)

        def signs(op):
            try:
                return {
                    '+' : operator.add,
                    '-' : operator.sub,
                    'x' : operator.mul,
                    '*' : operator.mul,
                    'divided' : operator.truediv,
                    'mod' : operator.mod,
                    '^' : operator.xor,
                }[op]
            except KeyError as e:
                print("Invalid operator. Please use a valid one.")
                print(e)

        def calculation(op1, oper, op2):
            try:
                op1, op2 = int(op1), int(op2)
            except ValueError as e:
                print("Operands must be integers.")
                print(e)
                return None
            try:
                return signs(oper)(op1, op2)
            except KeyError as e:
                print("Calculation failed due to an invalid operator.")
                print(e)
                return None

        try:
            result = calculation(*(voice.split()))
            if result is not None:
                print(f"Result: {result}")
        except TypeError as e:
            print("An error occurred during calculation.")
            print(e)
