# Write your solution here

def row_correct(sudoku: list, row_no: int) -> bool:
    """
    takes a 2D array representing a Sudoku grid, and an integer referring to a single row,
    as its arguments. Rows are indexed from 0. Evaluate if whether the row is filled in correctly i.e.,
    whether it contains each of the numbers 1 to 9 at most once

    Args:
        sudoku (list): 2D array
        row_no (int): row number to evaluate

    Returns:
        bool: True if filled correctly else False
    """
    num_list = []
               
    
    for element in sudoku[row_no]:
        if element !=0 and element in num_list:
            return False
        elif element!=0:
            num_list.append(element)
                
    return True
                           
                
                

if __name__ == "__main__":
    sudoku = [
    [9, 0, 0, 0, 8, 0, 3, 0, 0],
    [2, 0, 0, 2, 5, 0, 7, 0, 0],
    [0, 2, 0, 3, 0, 0, 0, 0, 4],
    [2, 9, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 3, 0, 5, 6, 0],
    [7, 0, 5, 0, 6, 0, 4, 0, 0],
    [0, 0, 7, 8, 0, 3, 9, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

    print(row_correct(sudoku, 0))
    print(row_correct(sudoku, 1))
    