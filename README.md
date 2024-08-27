# Integration Using Simpson’s 1/3 Rule Numerical Method Implementation in Python

This repository contains a Python implementation of Simpson's 1/3 Rule for numerical integration. The code estimates the integral of a given function \( f(x) \) within specified limits using Simpson's 1/3 Rule, a method for approximating the definite integral of a function.

## Table of Contents
- [Simpson’s 1/3 Rule Theory](#simpsons-13-rule-theory)
- [Dependencies](#dependencies)
- [Installation](#installation)
- [Usage](#usage)
- [Code Explanation](#code-explanation)
- [Example](#example)
- [Files in the Repository](#files-in-the-repository)
- [Input Parameters](#input-parameters)
- [Troubleshooting](#troubleshooting)
- [Author](#author)

## Simpson’s 1/3 Rule Theory

Simpson’s 1/3 Rule is a method for numerical integration that approximates the integral of a function by fitting parabolas to segments of the function over the specified interval. It is particularly effective when the function is relatively smooth.

### Formula:
The formula for Simpson's 1/3 Rule is as follows:
\[
\int_{a}^{b} f(x) \, dx \approx \frac{h}{3} \left[ f(x_0) + 4f(x_1) + 2f(x_2) + 4f(x_3) + \ldots + 4f(x_{n-1}) + f(x_n) \right]
\]
where:
- \( h = \frac{b - a}{n} \)
- \( n \) is an even number of subintervals.

### Note:
For Simpson's 1/3 Rule to be applicable, the number of segments \( n \) must be even.

## Dependencies
To run this code, you only need the built-in Python libraries. This script does not require any external libraries.

## Installation
Simply clone the repository or copy the script into your desired working directory.

## Usage
1. Clone the repository.
2. Run the script using Python:
    ```sh
    python simpsons_13_rule.py
    ```
3. Provide the required input when prompted:
    - Enter the lower limit.
    - Enter the upper limit.
    - Enter the number of segments (must be even).

## Code Explanation
The code defines a function for \( f(x) \), which is the function we want to integrate. It includes a main function that applies Simpson's 1/3 Rule to calculate the integral over the specified limits.

Here is a breakdown of the code:

```python
def F(x):
    return x*x  # The function to integrate (x^2)

def Simpsons_13_interpolation(a, b, n):
    h = (b - a) / n  # Compute the width of each segment
    integration = 0
    for i in range(n):
        x0 = a + i * h
        x1 = x0 + h / 2
        x2 = a + (i + 1) * h
        val = h * (F(x0) + 4 * F(x1) + F(x2)) / 6  # Calculate the area for this segment
        integration += val  # Sum up the area contributions
    return integration

# User input section
print("____Simpson's 1/3 Rule____")
a = float(input("Enter the lower limit: "))
b = float(input("Enter the upper limit: "))
step_size = int(input("Enter the number of segments (must be even): "))
integration = Simpsons_13_interpolation(a, b, step_size)
print("\nIntegrated value = %.6f" % (integration))
```

## Example
Below is an example of how to use the script:

1. **Run the script**:
    ```sh
    python simpsons_13_rule.py
    ```

2. **Enter the input values**:
    ```
    Enter the lower limit: 0
    Enter the upper limit: 5
    Enter the number of segments (must be even): 4
    ```

3. **Output**:
    ```
    Integrated value = 41.666667
    ```

## Files in the Repository
- `simpsons_13_rule.py`: The main script for performing integration using Simpson's 1/3 Rule.

## Input Parameters
The script prompts for the following input values:
- **Lower Limit (a)**: The lower bound of the definite integral.
- **Upper Limit (b)**: The upper bound of the definite integral.
- **Number of Segments (n)**: The number of segments over which to perform the integration (must be even).

## Troubleshooting
1. **Input Values**: Ensure that the input values are appropriate for the function being integrated and cover the range of interest.
2. **Number of Segments**: Make sure that \( n \) (the number of segments) is an even number.
3. **Python Version**: This script is compatible with Python 3. Ensure you have Python 3 installed.

## Author
Script created by sudipto3331.

---

This documentation should guide you through understanding, installing, and using the Simpson’s 1/3 Rule script for numerical integration. For further issues or feature requests, please open an issue in the repository on GitHub. Feel free to contribute by creating issues and submitting pull requests. Happy coding!
