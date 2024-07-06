import re
import datetime
import random
import math
import statistics
import calendar
import webbrowser
import os
import sys
import operator
import streamlit as st

def chatbot_response(user_input):
    user_input = user_input.lower().strip()
    
    # Safe eval for arithmetic expressions
    def safe_eval(expr):
        allowed_chars = "0123456789+-*/(). "
        if all(char in allowed_chars for char in expr):
            try:
                return eval(expr, {"__builtins__": {}})
            except:
                return None
        return None

    # Try to evaluate direct arithmetic expressions
    result = safe_eval(user_input)
    if result is not None:
        return f"The result is {result}."

    # Define basic arithmetic operations with additional patterns
    operations = {
        'add': operator.add,
        'plus': operator.add,
        'subtract': operator.sub,
        'minus': operator.sub,
        'multiply': operator.mul,
        'times': operator.mul,
        'product': operator.mul,
        'divide': operator.truediv,
        'divided by': operator.truediv
    }

    # Recognize and evaluate arithmetic expressions with words and symbols
    for op, func in operations.items():
        patterns = [
            f'(\d+)\s*{op}\s*(\d+)',
            f'{op}\s*(\d+)\s*\*\s*(\d+)',
            f'{op}\s*(\d+)\s*{op}\s*(\d+)',
            f'(\d+)\s*\*\s*(\d+)',
        ]
        for pattern in patterns:
            match = re.search(pattern, user_input)
            if match:
                num1, num2 = int(match.group(1)), int(match.group(2))
                result = func(num1, num2)
                return f"The result of {num1} {op} {num2} is {result}."

    # Recognize date and time queries
    if "date" in user_input:
        return f"Today's date is {datetime.date.today()}."
    if "time" in user_input:
        return f"The current time is {datetime.datetime.now().strftime('%H:%M:%S')}."

    # Recognize random number request
    if "random number" in user_input:
        return f"Here is a random number: {random.randint(1, 100)}."

    # Recognize mathematical calculations
    if "square root" in user_input:
        number = float(re.search(r'square root of (\d+)', user_input).group(1))
        return f"The square root of {number} is {math.sqrt(number)}."
    if "factorial" in user_input:
        number = int(re.search(r'factorial of (\d+)', user_input).group(1))
        return f"The factorial of {number} is {math.factorial(number)}."
    
    # Recognize trigonometric calculations
    if "sine of" in user_input:
        angle = float(re.search(r'sine of (\d+)', user_input).group(1))
        return f"The sine of {angle} degrees is {math.sin(math.radians(angle))}."
    
    # Recognize logarithmic calculations
    if "logarithm of" in user_input:
        number = float(re.search(r'logarithm of (\d+)', user_input).group(1))
        return f"The natural logarithm of {number} is {math.log(number)}."
    
    # Recognize exponential calculations
    if "exponential of" in user_input:
        number = float(re.search(r'exponential of (\d+)', user_input).group(1))
        return f"The exponential of {number} is {math.exp(number)}."
    
    # Recognize power calculations
    if "power of" in user_input:
        numbers = list(map(int, re.findall(r'\d+', user_input)))
        return f"The result of {numbers[0]} raised to the power of {numbers[1]} is {math.pow(numbers[0], numbers[1])}."
    
    # Recognize rounding calculations
    if "round" in user_input:
        number = float(re.search(r'round (\d+)', user_input).group(1))
        return f"The rounded value of {number} is {round(number)}."
    
    # Recognize absolute value calculations
    if "absolute value of" in user_input:
        number = float(re.search(r'absolute value of (\d+)', user_input).group(1))
        return f"The absolute value of {number} is {abs(number)}."
    
    # Recognize comparison operations
    if "greater than" in user_input:
        numbers = list(map(int, re.findall(r'\d+', user_input)))
        return f"{numbers[0]} is greater than {numbers[1]}: {numbers[0] > numbers[1]}."
    
    # Recognize statistical calculations
    if "mean of" in user_input:
        numbers = list(map(int, re.findall(r'\d+', user_input)))
        return f"The mean of {numbers} is {statistics.mean(numbers)}."
    if "median of" in user_input:
        numbers = list(map(int, re.findall(r'\d+', user_input)))
        return f"The median of {numbers} is {statistics.median(numbers)}."
    if "mode of" in user_input:
        numbers = list(map(int, re.findall(r'\d+', user_input)))
        return f"The mode of {numbers} is {statistics.mode(numbers)}."

    # Recognize calendar queries
    if "calendar for" in user_input:
        year = int(re.search(r'calendar for (\d+)', user_input).group(1))
        return f"Here is the calendar for {year}:\n{calendar.TextCalendar().formatyear(year)}"

    # Recognize opening URLs
    if "open website" in user_input:
        url = re.search(r'open website (.+)', user_input).group(1)
        webbrowser.open(url)
        return f"Opening website: {url}"

    # Recognize file operations
    if "create file" in user_input:
        filename = re.search(r'create file (.+)', user_input).group(1)
        with open(filename, 'w') as f:
            f.write('')
        return f"File {filename} created."
    if "delete file" in user_input:
        filename = re.search(r'delete file (.+)', user_input).group(1)
        os.remove(filename)
        return f"File {filename} deleted."
    
    # Recognize directory operations
    if "create directory" in user_input:
        dirname = re.search(r'create directory (.+)', user_input).group(1)
        os.makedirs(dirname)
        return f"Directory {dirname} created."
    
    # Recognize system operations
    if "system info" in user_input:
        return f"System info: {sys.version}"
    
    # Recognize help
    if "help" in user_input:
        return "I can perform arithmetic calculations, date and time queries, random number generation, mathematical, trigonometric, logarithmic, exponential, power, rounding, absolute value, comparison, and statistical calculations, calendar queries, open URLs, and file, directory, and system operations. How can I assist you today?"    

    # Recognize greeting
    if any(greeting in user_input for greeting in ["hello", "hi", "hey"]):
        return "Hello! How can I assist you today?"

    # Recognize farewell
    if any(farewell in user_input for farewell in ["bye", "goodbye", "see you"]):
        return "Goodbye! Have a great day!"

    # Recognize thanks
    if any(thanks in user_input for thanks in ["thank you", "thanks"]):
        return "You're welcome!"
    
    # Default response
    return "I'm sorry, I didn't understand that. Can you please rephrase?"

# Streamlit UI
st.title("Python rule based Chatbot")

# Create two tabs
tab1, tab2 = st.tabs(["**Chatbot**", "**Sample Queries**"])

with tab1:
    st.write("Welcome to my Rule-based Chatbot! Type 'exit' to end the conversation. Type 'help' to see what the chatbot can do")

    # Initialize session state for conversation history
    if 'history' not in st.session_state:
        st.session_state.history = []

    # Get user input
    user_input = st.text_input("You:", "")

    # Display conversation history
    if st.session_state.history:
        for i, (query, response) in enumerate(st.session_state.history):
            st.markdown(f"""
                <div style="text-align: right; color: #4CAF50; padding: 10px; border-radius: 10px;">
                    <strong>User:</strong> {query}
                </div>
                <div style="text-align: left; color: #2196F3; padding: 10px; border-radius: 10px;">
                    <strong>Chatbot:</strong> {response}
                </div>
            """, unsafe_allow_html=True)

    if user_input:
        if user_input.lower() == 'exit':
            st.write("Chatbot: Goodbye!")
        else:
            response = chatbot_response(user_input)
            st.session_state.history.append((user_input, response))
            st.markdown(f"""
                <div style="text-align: right; color: #4CAF50; padding: 10px; border-radius: 10px;">
                    <strong>User:</strong> {user_input}
                </div>
                <div style="text-align: left; color: #2196F3; padding: 10px; border-radius: 10px;">
                    <strong>Chatbot:</strong> {response}
                </div>
            """, unsafe_allow_html=True)

with tab2:
    st.write("Here are some sample queries you can try with the chatbot:")
    sample_queries = [
        "Hello! How are you?",
        "Can you tell me today's date?",
        "What's the current time?",
        "Generate a random number for me.",
        "What is the square root of 25?",
        "Calculate the factorial of 5.",
        "What is the sine of 30 degrees?",
        "What is the natural logarithm of 10?",
        "Find the exponential of 2.",
        "What is 2 raised to the power of 3?",
        "Round 3.14159 to the nearest whole number.",
        "What is the absolute value of -15?",
        "Is 5 greater than 3?",
        "What is the mean of 1, 2, 3, 4, 5?",
        "Find the median of 4, 2, 7, 3, 8.",
        "What is the mode of 1, 1, 2, 3, 3, 3?",
        "Show me the calendar for 2024.",
        "Open website https://www.google.com.",
        "Create a file named 'example.txt'.",
        "Give me some help on what you can do."
    ]
    for query in sample_queries:
        st.write(f"- {query}")
