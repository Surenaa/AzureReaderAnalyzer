In this script, we define the url variable with the Azure URL you provided. The send_random_number function generates a random number between 1 and 100, creates a JSON payload with the number, and sends a POST request to the specified URL.

The script then loops num_numbers times (in this case, 10) and calls the send_random_number function for each iteration, sending a random number to the Azure URL.

Make sure you have the requests library installed before running this script. You can install it by running pip install requests in your terminal.

Note that this script assumes the Azure endpoint expects a JSON payload with a "number" field to receive the random number. Adjust the code as per the specific requirements of your Azure endpoint.