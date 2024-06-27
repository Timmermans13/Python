# Author: stan
# Had some issues with procces=subprocess since python = python3 on my local env
import subprocess
import pytest

# moves for draw
test_cases = [
    {
        "moves": [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)],
        "expected_output": "It's a draw!"
    },
]

@pytest.mark.parametrize("test_case", test_cases)
def test_index_game(test_case, capsys):
    input_data = '\n'.join(f'{row}\n{col}' for row, col in test_case["moves"]) + '\n'
    process = subprocess.Popen(['python3', 'index.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, stderr = process.communicate(input_data)
    captured_output = stdout.strip()
    assert test_case["expected_output"] in captured_output

if __name__ == "__main__":
    pytest.main()
