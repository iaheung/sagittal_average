import numpy as np
from sagittal_brain import run_averages
import subprocess
import os

def test_sagittal_average():
    # Define a test input array with varying values
    input_data = np.array([
        [0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1],
        [2, 2, 2, 2, 2],
        [3, 3, 3, 3, 3],
        [4, 4, 4, 4, 4]
    ])
    
    # Expected output based on the correct averaging along rows
    expected_output = np.array([2.0, 2.0, 2.0, 2.0, 2.0])

    # Save the input data to a CSV file
    np.savetxt("brain_sample.csv", input_data, delimiter=',')

    # Run the code
    run_averages(file_input="brain_sample.csv", file_output="brain_average.csv")

    # Load the output data
    output_data = np.loadtxt("brain_average.csv", delimiter=',')

    # Verify that the output matches the expected output
    assert np.array_equal(output_data, expected_output), "Test failed: Output does not match expected values."
    print("Test 1 passed")

def test_axis_misinterpretation():
    # Define an array that would yield different results if the wrong axis is averaged
    input_data = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])
    
    # Expected output if we average along the correct axis (rows)
    expected_output = np.array([4, 5, 6])

    # Save the input data to a CSV file
    np.savetxt("brain_sample.csv", input_data, fmt='%d', delimiter=',')

    # Run the code
    run_averages(file_input="brain_sample.csv", file_output="brain_average.csv")

    # Load the output data
    output_data = np.loadtxt("brain_average.csv", delimiter=',')

    # Verify that the output matches the expected output
    assert np.array_equal(output_data, expected_output), "Test failed: Output does not match expected values."
    print("Test 2 passed")

# without importing function 
def test_big_data():
    # Step 1: Define a good input array (20x20) and the expected output array
    input_data = np.zeros((20, 20))
    input_data[-1, :] = 1  # Set the last row to 1s to introduce variability

    # The expected output is a row with averages along the rows (sagittal)
    # Since 19 rows are all zero and the last row is all 1s, the average will be 0.05
    expected_output = np.full((1, 20), 0.05)

    # Step 2: Save the input array as brain_sample.csv
    np.savetxt("brain_sample.csv", input_data, fmt='%d', delimiter=',')

    # Step 3: Run Charlene's code from within this script using subprocess
    try:
    # Calling sagittal_average.py with subprocess
        subprocess.run(["python", "sagittal_brain.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running Charlene's code: {e}")
        exit(1)

    # Step 4: Read the output from brain_average.csv into output_data
    output_data = np.loadtxt("brain_average.csv", delimiter=',')

    # Step 5: Test if output_data and expected_output are equal
    if np.array_equal(output_data, expected_output):
        print("Test passed: Output matches expected values.")
    else:
        print("Test failed: Output does not match expected values.")
        print("Expected Output:")
        print(expected_output)
        print("Actual Output:")
        print(output_data)
        exit(1)
    print("Test 3 passed")


if __name__ == "__main__":
    test_sagittal_average()
    test_axis_misinterpretation()
    test_big_data()