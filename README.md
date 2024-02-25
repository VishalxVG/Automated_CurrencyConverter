## Currency Converter using Free Currency API

This repository contains a simple currency converter that utilizes the Free Currency API to fetch the latest exchange rates. The converter allows users to input a base currency along with an amount to convert. Upon input, the program calculates and displays the converted values for other currencies specified in the `CURRENCIES` list.

### How to Use:

1. **Import Necessary Libraries:** Ensure you have the `requests` library installed.
   
2. **API Configuration:** Define your API key and set the base URL for the Free Currency API.

3. **Specify Conversion Currencies:** Create a list of currencies to convert to.

4. **Define Conversion Function:** Implement a function `convert_currency(base)` that takes the base currency as input.

5. **Construct API Request:** Inside the conversion function, build the API request URL with the API key, base currency, and desired currencies to convert to.

6. **Send API Request:** Utilize the `requests.get()` method to send a GET request to the API.

7. **Handle API Response:** Parse the JSON response from the API. If successful, return the data; otherwise, handle errors gracefully.

8. **User Interaction:** In a loop, prompt the user to input the base currency. Terminate the loop by entering "Q".

9. **Convert Currency:** Call the `convert_currency(base)` function with the user's input. If the function returns None, continue to the next iteration.

10. **Input Conversion Amount:** Prompt the user to enter the amount they want to convert.

11. **Display Conversion Results:** Iterate over the currencies to convert to, calculate the converted value, and print it.

### Getting Started:

To use the currency converter:

1. Clone this repository to your local machine.
2. Ensure you have Python installed.
3. Install the `requests` library if you haven't already (`pip install requests`).
4. Run the code and follow the prompts. Enter the base currency, the amount to convert, and the program will display the converted values for the other currencies.

Enjoy converting currencies effortlessly!
