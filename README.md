# 🚨 Error Translator

A powerful CLI tool that translates programming errors into clear, human-readable explanations.

Built to help beginners understand what actually went wrong — without decoding cryptic messages.

---

## 📌 What It Does

The program:

- Reads a local `errors.json` database
- Accepts an error name via terminal input (e.g., `TypeError`)
- Searches for the error
- Returns a simplified explanation
- Shows a fallback message if the error is not found

---

## 🧠 Why This Project Exists

Programming error messages can be confusing, especially for beginners.

Example:

```python
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

What that usually means:

> You tried to perform an operation between incompatible data types.

This tool translates technical errors into understandable explanations.

---

## 🌍 Future Vision

Error Translator is designed to grow beyond just Python.

Planned expansions:

- 🌐 Support for multiple programming languages  
- 🧩 Community-contributed error database  
- 🖥 GUI version  
- 🤖 Possible AI-assisted explanation system  

---

## 📂 Project Structure

```
error-translator/
│
├── main.py
├── errors.json
└── README.md
```

---

## ▶️ How To Run

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/error-translator.git
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the program

```bash
python main.py
```

---

## 🖥 Example Usage

```
Hello! Describe your error so we can help you!
Put the init (ex: TypeError, SyntaxError)

> TypeError
```

Output:

```
You tried to use incompatible data types in an operation.
```

---

## 📦 Requirements

- Python 3.x
- pandas

---

## 🚀 Roadmap

- [ ] Add support for more languages (JavaScript, Java, C++, etc.)
- [ ] Implement GUI version
- [ ] Create structured contribution system for new errors
- [ ] Improve database structure
- [ ] Explore AI integration for dynamic explanations
