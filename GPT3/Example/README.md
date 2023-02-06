# GPT3 Example

You need to copy `.env.example` to be `.env` and fill-in the Azure API key of the OpenAI service.

```powershell
$ python .\language_model.py -h

$ python .\language_model.py -t "Will the Microsoft stock price increase?" -n 100

# Translate
python .\translation.py -t "There is a white cat in a box." -s few-shot
python .\translation.py -t "There is a white cat in a box." -s one-shot
python .\translation.py -t "There is a white cat in a box." -s zero-shot

# Code generation
$ python .\language_model.py -t "Write HelloWorld() in .NET:" -n 200
$ python .\language_model.py -t "Write HelloWorld() in Python:" -n 200

# Relevance
$ python .\language_model.py -t "A: I like to eat ice cream `n B: Apple is delicious `n These two sentence is relevant or not?"
$ python .\language_model.py -t "A: I like to eat ice cream `n B: Ice cream is delicious `n These two sentence is relevant or not?"
$ python .\relevance.py
Doc 1: I love to drive car
Doc 2: Truck is my favorite

# Generate article
$ python .\article_generation.py
Title: How to apologize to the boss?
Subtitle: The correct reaction when making mistakes at work.

# Math calculation
$ python .\math_calculation.py -t "8 * 7 * 2"
```
