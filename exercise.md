# Scenario: Text Analysis

## What is text analysis?
Text analysis, also known as text mining or text analytics, refers to the process of extracting meaningful information and insights from textual data.

### Objectives
After completing this lab, you will be able to:

Use Python commands to perform text analysis.
Convert the text to lowercase and then find and count the frequency of all unique words, as well as a specified word.

## Setup
For this lab, you will be using the following data types:

 - List
 - Strings
 - Classes and objects

Let's consider a real-life scenario where you are analyzing customer feedback for a product. You have a large data set of customer reviews in the form of strings, and you want to extract useful information from them using the three identified tasks:

# Task 1. String in lowercase #: You want to pre-process the customer feedback by converting all the text to lowercase. This step helps standardize the text. Lower casing the text allows you to focus on the content rather than the specific letter casing.


Task 2. Frequency of all words in a given string: After converting the text to lowercase, you want to determine the frequency of each word in the customer feedback. This information will help you identify which words are used more frequently, indicating the key aspects or topics that customers are mentioning in their reviews. By analyzing the word frequencies, you can gain insights into the most common issues raised by customers.

Task 3. Frequency of a specific word: In addition to analyzing the overall word frequencies, you want to specifically track the frequency of a particular word that is relevant to your analysis. For example, you might be interested in monitoring how often the word "reliable" appears in customer reviews to gauge customer sentiment about the product's reliability. By focusing on the frequency of a specific word, you can gain a deeper understanding of customer opinions or preferences related to that particular aspect.

By performing these tasks on the customer feedback dataset, you can gain valuable insights into customer sentiment

## Part-A
Note: In Part-A, you would not be getting any output as you are just storing the string and creating a class.

Step 1: Define a string
"Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet."

### Hint: Use a variable and store the above string.

`givenstring="Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet."`

To achieve the tasks mentioned in the scenario, you need to create a class with three different methods.
### Step 2: Define the class and its attributes

- 1. Create a class named TextAnalyzer.
- 2. Define the constructor __init__ method that takes a text argument.

### Step 3: Implement a code to format the text in lowercase

- 1. Inside the constructor, convert the text argument to lowercase using the `lower()` method.
- 2. Then, remove punctuation marks (periods, exclamation marks, commas, and question marks) from the text using the `replace()` method.
- 3. Finally, assign the formatted text to a new attribute called fmtText.
Here you will be updating the above TextAnalyzer class with the points mentioned above.

## Step 4: Implement a code to count the frequency of all unique words
  - In this step, you will implement the freqAll() method with the below parameters:
  - 1. Split the fmtText attribute into individual words using the split() method.
- 2. Create an empty dictionary to store the word frequency.
- 3. Iterate over the list of words and update the frequency dictionary accordingly.
- 4. Use count method for counting the occurence.
- 5. Return the frequency dictionary.
Update the above TextAnalyzer class with points mentioned above.

## Step 5: Implement a code to count the frequency of a specific word
In step-5, you have to implement the freqOf(word) method that takes a word argument:

- 1. Create a method and pass the word that needs to be found.
- 2. Get the freqAll method to look for count and check if that word is in the list.
- 3. Return the count. If the word is not found, the count returned is 0.
Update the above TextAnalyzer class with the points mentioned above.

art-B
In Part B, you will call the functions created in Part A, allowing the functions to execute and generate output.

Step 1: Create an instance of TextAnalyzer class
Instantiate the TextAnalyzer class by passing the given string as an argument.

Step 2: Call the function that converts the data into lowercase

Step 3: Call the function that counts the frequency of all unique words from the data

ou have successfully calculated the frequency of all unique words in the string.

Step 4: Call the function that counts the frequency of a specific word
Here, you will call the function that counts the frequency of the word "lorem".

Print the output.**
