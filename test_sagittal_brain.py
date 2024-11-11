import numpy as np
from sagittal_brain import run_averages

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

if __name__ == "__main__":
    test_sagittal_average()
    test_axis_misinterpretation()
    print("All tests passed.")