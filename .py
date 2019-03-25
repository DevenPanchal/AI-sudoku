assignments = []

def assign_value(values, box, value):
    """
    Please use this function to update your values dictionary!
    Assigns a value to a given box. If it updates the board record it.
    """

    # Don't waste memory appending actions that don't actually change any values
    if values[box] == value:
        return values

    values[box] = value
    if len(value) == 1:
        assignments.append(values.copy())
    return values

def naked_twins(values):
    """Eliminate values using the naked twins strategy.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the values dictionary with the naked twins eliminated from peers.
    """

    # Find all instances of naked twins
    # Eliminate the naked twins as possibilities for their peers

def cross(A, B):
    "Cross product of elements in A and elements in B."
    return [s + t for s in a for t in b]

def grid_values(grid):
    """
    Convert grid into a dict of {square: char} with '123456789' for empties.
    Args:
        grid(string) - A grid in string form.
    Returns:
        A grid in dictionary form
            Keys: The boxes, e.g., 'A1'
            Values: The value in each box, e.g., '8'. If the box has no value, then the value will be '123456789'.
    """
    chars = []
    digits = '123456789'
    for c in grid:
        if c in digits:
            chars.append(c)
        if c == '.':
            chars.append(digits)
    assert len(chars) == 81
    return dict(zip(boxes, chars))

def display(values):
    """
    Display the values as a 2-D grid.
    Args:
        values(dict): The sudoku in dictionary form
    """

    width = 1 + max(len(values[s]) for s in boxes)
    line = '+'.join(['-' * (width * 3)] * 3)
    for r in rows:
        print(''.join(values[r + c].center(width) + ('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF': print(line)
    return

def eliminate(values):
    """
        Go through all the boxes, and whenever there is a box with a value, eliminate this value from the values of all its peers.
        Input: A sudoku in dictionary form.
        Output: The resulting sudoku in dictionary form.
    """
    solved_values = [box for box in values.keys() if len(values[box]) == 1]
    for box in solved_values:
        digit = values[box]
        for peer in peers[box]:
            values[peer] = values[peer].replace(digit, '')
    return values

def only_choice(values):
    """
        Go through all the units, and whenever there is a unit with a value that only fits in one box, assign the value to this box.
        Input: A sudoku in dictionary form.
        Output: The resulting sudoku in dictionary form.
    """
    """
    """
    NOTES BY DEVEN: """
        for unit in unitlist:
    This function does some work which is not intuitive while solving the sudoku 
visually.  for digit in '123456789':
    At this point, Usually I would pick those boxes for which I see minimum limitations 
dplaces = [box for box in unit if digit in values[box]]
    and try to fill them up by looking at all its peers.  if len(dplaces) == 1:
                    values[dplaces[0]] = digit
    But this algorithm (step) traverses through each unit, and tries to 'fill in' digits 
in that unit, return values
    if it can be filled in in any box based on values in the same unit's boxes.
    Then it goes to other units, horizontal vertical, square one by one. def 
reduce_puzzle(values):
        """
    Basically, the thought process this algorithm/ step takes is that each unit whether 
it is horizontal Iterate eliminate() and only_choice(). If at some point, there is a box 
with no available values, return False.
    or vertical or square unit, must have all numbers filled in 1 to 9 in the units If 
the sudoku is solved, return the sudoku.
            If after an iteration of both functions, the sudoku remains the same, return 
the sudoku.
    So, the difference between algorithm, I thought of, and this algorithm at this step 
is- Input: A sudoku in dictionary form.
    My algorithm wanted to find boxes it could fill up uniquely(surely)based on its 
peer's values Output: The resulting sudoku in dictionary form.
    and then make multiple subsequent passes after constraint propagation and 
application.  """
    (implemented using alternate eliminate step and this step).That is it was trying to 
go after some unknown stuff.  solved_values = [box for box in values.keys() if 
len(values[box]) == 1]
        stalled = False
    On the other hand, this algorithm (at this step) goes after filling up every unit 
while not stalled:
    (by uniquely filling its boxes) with numbers 1 to 9, which is a known fact about the 
solution to sudoku.  solved_values_before = len([box for box in values.keys() if 
len(values[box]) == 1])
    Constraint propagation is not addressed or needed to be addressed in this algorithm 
at this step at this point of time.  values = eliminate(values)
    Infact constraint propagation is nothing but a series of eliminate and only choice 
steps..which may solve the probem values = only_choice(values)
    or we may get stuck at some point..  solved_values_after = len([box for box in 
values.keys() if len(values[box]) == 1])
            stalled = solved_values_before == solved_values_after
    I have adapted the solution provided but renamed the "dplaces" variable to 
"places_in_unit_where_current_digit_matches" if len([box for box in values.keys() if 
len(values[box]) == 0]):
    to make it more meaningful.  return False
    
def search(values):
    On a side note, it is interesting to see how compact Python makes it to specify 
complext conditions.
    See how the "places_in_unit_where_current_digit_matches" variable is , see how def 
solve(grid):
    the following variables have been created.. interesting!!  """
        Find the solution to a Sudoku grid.
    row_units = [cross(r, cols) for r in rows] Args:
    column_units = [cross(rows, c) for c in cols] grid(string): a string representing a 
sudoku grid.
    square_units = [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in 
('123','456','789')] Example: 
'2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    unitlist = row_units + column_units + square_units Returns:
    units = dict((s, [u for u in unitlist if s in u]) for s in boxes) The dictionary 
representation of the final sudoku grid. False if no solution exists.
    peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes) """
    	from utils import *
    See how cross is defined to be such that the granularity of the arguments can """
    be chosen to be an entire list ( in case of row_units, cols) or one character of a 
string (in case of rs square_units). NOTES BY DEVEN
    
See the below snippets - how much done with how less code. See functions all, min
    See how interesting can be patterns created out of the 1st argument bcoming 
distributed over the second argument (depending on both's granularity). values = 
reduce_puzzle(values)
    """   
     if values is False:
        return False ## Failed earlier
    if all(len(values[s]) == 1 for s in boxes): 
        return values ## Solved!
    # Choose one of the unfilled squares with the fewest possibilities
    n,s = min((len(values[s]), s) for s in boxes if len(values[s]) > 1)
    
Also, see how the need for a global flag variable is avoided by returning the values from te function

In utils.py, see the calculation and python usage for
units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)
    
"""
# Choose one of the unfilled squares with the fewest possibilities
def best_unfulfilled_box_selector(values):
    n,s = min((len(values[s]), s) for s in boxes if len(values[s]) > 1)
    return (n,s)
    
def search(values):
    
    # Using depth-first search and propagation, create a search tree and solve the sudoku."
    # First, reduce the puzzle using the previous function
    values = reduce_puzzle(values)
    if values is False:
        return False
    
  
    if all(len(values[s]) == 1 for s in boxes):
        return values
    # Now use recursion to solve each one of the resulting sudokus, and if one returns a value (not False), return that answer!
    # If you're stuck, see the solution.py tab!
    
    ret_tup = best_unfulfilled_box_selector(values)
    box = ret_tup[1]
    
    for v in values[box]:
        new_dictionary_layer = values.copy()
        new_dictionary_layer[box] = v
        result_of_call_to_search = search(new_dictionary_layer)
        if result_of_call_to_search:
            return result_of_call_to_search

if __name__ == '__main__':
    """
    If the python interpreter is running that module (the source file) as the main program, it sets the special __name__ variable to have a value "__main__". If this file is being imported from another module, __name__ will be set to the module's name.
    By doing the main check, you can have that code only execute when you want to run the module as a program and not have it execute when someone just wants to import your module and call your functions themselves.
    https://stackoverflow.com/questions/419163/what-does-if-name-main-do
    """
    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    display(solve(diag_sudoku_grid))

    try:
        from visualize import visualize_assignments
        visualize_assignments(assignments)

    except SystemExit:
        pass
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')
