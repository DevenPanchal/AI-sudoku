#DIAGONAL SUDOKU SOLVER
# TO SWITCH TO NON_DIAGONAL (NORMAL) SUDOKU,
# make the following changes- 1)use old_unitlist in place of unitlist and
# 2)supply correct normal grid instead of diag_sudoku_grid and pass it to display(solve(name_of_new_grid))
assignments = []  # this is needed by the visualizer, the steps/ moves so that it can show them in order
rows = 'ABCDEFGHI'
cols = '123456789'


def cross(A, B):
    "Cross product of elements in A and elements in B."
    return [s + t for s in A for t in B]


boxes = cross(rows, cols)
row_units = [cross(r, cols) for r in rows]
column_units = [cross(rows, c) for c in cols]
square_units = [cross(rs, cs) for rs in ('ABC', 'DEF', 'GHI') for cs in ('123', '456', '789')]
#diag_units = [['A1','B2','C3','D4','E5','F6','G7','H8','I9'],['A9','B8','C7','D6','E5','F4','G3','H2','I1']]#could be intelligently generated. as below
#diagonal1 = [rows[i]+cols[i] for i in range(9)]
#diagonal2 = [rows[i]+cols[8-i] for i in range(9)]
#or
diagonal1 = [a[0]+a[1] for a in zip(rows, cols)]
diagonal2 = [a[0]+a[1] for a in zip(rows, cols[::-1])]
diag_units = [diagonal1,diagonal2]
#print(diag_units)
unitlist = row_units + column_units + square_units + diag_units
old_unitlist = row_units + column_units + square_units
units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s], [])) - set([s])) for s in boxes)
nk_twins=[]


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

def remove_value_from_string(oldstr,value_to_remove,l,x):
    """Handles string removal from a box

        Args:
            oldstr(str)
            value_to_remove(str)
        Returns:
            newstr(str)
        """
    #if len(oldstr)==1:
        #print("Invalid deletion attempted in x", end="")
        #print(x)
        #print("Value of l is", end="")
        #print(l)
    newstr = oldstr.replace(value_to_remove,"")
    return newstr


def naked_twins_eliminator(values):
    """The real elimination handling function for the naked_twins function

    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}
    Returns:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}
    """
    for l in nk_twins:
        if (l[0][0] == l[1][0]): # if both are row peers
            # we affect the row then
            values_to_eliminate = values[l[0]]
            # or values_to_eliminate=values[l[1]]
            # below loop iterates over each box in the row specified by l[0]
            for x in units[l[0]][0]:
                if x != l[0] and x != l[1]:
                    try:
                        if values_to_eliminate[0] in values[x]:
                            values[x] = remove_value_from_string(values[x], values_to_eliminate[0], l, x)

                        if values_to_eliminate[1] in values[x]:
                            values[x] = remove_value_from_string(values[x], values_to_eliminate[1], l, x)
                    except IndexError:
                        # print('From twins',end="" )
                        # print(l)
                        # print('From'+ x )
                        # print('values is', end="")
                        # print(values)
                        pass

        if (l[0][1] == l[1][1]): # if both are column peers
            # we affect the column then
            values_to_eliminate = values[l[0]]
            # or values_to_eliminate=values[l[1]]
            # below loop iterates over each box in the column specified by l[0]
            for x in units[l[0]][1]:
                if x != l[0] and x != l[1]:
                    try:
                        if values_to_eliminate[0] in values[x]:
                            values[x] = remove_value_from_string(values[x], values_to_eliminate[0], l, x)
                        if values_to_eliminate[1] in values[x]:
                            values[x] = remove_value_from_string(values[x], values_to_eliminate[1], l, x)
                    except IndexError:
                        # print('From twins', end="")
                        # print(l)
                        # print('From' + x)
                        # print('values is', end="")
                        # print(values)
                        pass

        if l[0] in units[l[1]][2]:  # if both are square peers
            # we affect the square units boxes  then
            values_to_eliminate = values[l[0]]
            # or values_to_eliminate=values[l[1]]
            # below loop iterates over each box in the square specified by l[0]
            for x in units[l[0]][2]:
                if x != l[0] and x != l[1]:
                    try:
                        if values_to_eliminate[0] in values[x]:
                            values[x] = remove_value_from_string(values[x], values_to_eliminate[0], l, x)
                        if values_to_eliminate[1] in values[x]:
                            values[x] = remove_value_from_string(values[x], values_to_eliminate[1], l, x)
                    except IndexError:
                        # print('From twins', end="")
                        # print(l)
                        # print('From' + x)
                        # print('values is', end="")
                        # print(values)
                        pass

        # will be used only when we encounter diagonal naked pairs. Which can arise when u in naked_twins() iterates over unitlist and not old_unitlist
        if (len(units[l[0]])==4 and len(units[l[1]])==4):
            if l[0] in units[l[1]][3]:# if both are diagonal peers
            # we affect the diagonal units boxes  then

                values_to_eliminate = values[l[0]]
            # or values_to_eliminate=values[l[1]]
            # below loop iterates over each box in the diagonal specified by l[0]
                for x in units[l[0]][3]:
                    if x != l[0] and x != l[1]:
                        try:
                            if values_to_eliminate[0] in values[x]:
                                values[x] = remove_value_from_string(values[x], values_to_eliminate[0], l, x)
                            if values_to_eliminate[1] in values[x]:
                                values[x] = remove_value_from_string(values[x], values_to_eliminate[1], l, x)
                        except IndexError:
                        # print('From twins', end="")
                        # print(l)
                        # print('From' + x)
                        # print('values is', end="")
                        # print(values)
                            pass

            else:pass
    return values




def naked_twins(values):
    """Eliminate values using the naked twins strategy.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}
    Returns:
        the values dictionary with the naked twins eliminated from peers.
    """
    # Find all instances of naked twins
    for u in unitlist:
        for (pos, bx) in enumerate(u):  # FOR LOOP 1
            if len(values[bx]) == 2:
                # print("the next cx's are due to" + bx)
                for cx in u[pos + 1:]:  # FOR LOOP 2
                    if len(values[cx]) == 2:
                        if values[bx] == values[cx] and bx != cx:
                            # print(cx)
                            # we have got the naked twins at this point
                            # now is the time to append them into a variable seen throughout this function
                            # after checking it does not already exist due to these nested for loops
                            nk_tup = (bx, cx)
                            #print(nk_twins)
                            if not (nk_tup in nk_twins):

                                nk_twins.append(nk_tup)
                                    # But be careful to call naked_twins_eliminator go here only when new naked twins are appended to avoid indexing issues.
                                    # So checking length before eliminating and clearing list on every exit from function required
                                    # Also, some grids require calling eliminator as soon as a new new naked twin is
                                    # appended to avoid issues on collecting all naked twins and then eliminating.
                                if len(nk_twins) != 0:
                                    #print(nk_twins)
                                    #print('hi')
                                    values = naked_twins_eliminator(values.copy())
                                    nk_twins.clear()
    return values

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
    """
    See zip function to c
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
    NOTES FOR SELF:

    This function does some work which is not intuitive while solving the sudoku visually.
    At this point, Usually I would pick those boxes for which I see minimum limitations
    and try to fill them up by looking at all its peers.

    But this algorithm (step) traverses through each unit, and tries to 'fill in' digits in that unit,
    if it can be filled in in any box based on values in the same unit's boxes.
    Then it goes to other units, horizontal vertical, square one by one.

    Basically, the thought process this algorithm/ step takes is that each unit whether it is horizontal 
    or vertical or square unit, must have all numbers filled in 1 to 9 in the units

    So, the difference between algorithm, I thought of, and this algorithm at this step is-
    My algorithm wanted to find boxes it could fill up uniquely(surely)based on its peer's values
    and then make multiple subsequent passes after constraint propagation and application.
    (implemented using alternate eliminate step and this step).That is it was trying to go after some unknown stuff.

    On the other hand, this algorithm (at this step) goes after filling up every unit 
    (by uniquely filling its boxes) with numbers 1 to 9, which is a known fact about the solution to sudoku.
    Constraint propagation is not addressed or needed to be addressed in this algorithm at this step at this point of time.
    Infact constraint propagation is nothing but a series of eliminate and only choice steps..which may solve the probem 
    or we may get stuck at some point..

    I have adapted the solution provided but renamed the "dplaces" variable to "places_in_unit_where_current_digit_matches"
    to make it more meaningful.

    On a side note, it is interesting to see how compact Python makes it to specify complex conditions.
    See how the "places_in_unit_where_current_digit_matches" variable is , see how 
    the following variables have been created using list and dctinoary comprehensions.. interesting!! 

    row_units = [cross(r, cols) for r in rows]
    column_units = [cross(rows, c) for c in cols]
    square_units = [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]
    unitlist = row_units + column_units + square_units
    units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
    peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)
    
    Notice the use of zip in the display function.
    
    See how cross is defined to be such that the granularity of the arguments can 
    be chosen to be an entire list ( in case of row_units, cols) or one character of a string (in case of rs square_units).

    See how interesting can be patterns created out of the 1st argument becoming distributed over the second argument (depending on both's granularity).
    """
    for unit in unitlist:
        for digit in '123456789':
            places_in_unit_where_current_digit_matches = [box for box in unit if digit in values[box]]
            if len(places_in_unit_where_current_digit_matches) == 1:
                # values[places_in_unit_where_current_digit_matches[0]] = digit
                values = assign_value(values, places_in_unit_where_current_digit_matches[0], digit)
    return values


def reduce_puzzle(values):
    """
        Iterate eliminate() and only_choice(). If at some point, there is a box with no available values, return False.
        If the sudoku is solved, return the sudoku.
        If after an iteration of both functions, the sudoku remains the same, return the sudoku.
        Input: A sudoku in dictionary form.
        Output: The resulting sudoku in dictionary form.
    """
    solved_values = [box for box in values.keys() if len(values[box]) == 1]
    stalled = False
    while not stalled:
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])
        values = eliminate(values)
        values = naked_twins(values.copy())
        values = only_choice(values)
        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
        stalled = solved_values_before == solved_values_after
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False
    return values


def search(values):
    """
    NOTES FOR SELF
    See the below snippets - how much done with how less code.
    See functions all, min
    values = reduce_puzzle(values)
        if values is False:
            return False ## Failed earlier
        if all(len(values[s]) == 1 for s in boxes):
            return values ## Solved!
        # Choose one of the unfilled squares with the fewest possibilities
        n,s = min((len(values[s]), s) for s in boxes if len(values[s]) > 1)
    Also, see how the need for a global flag variable is avoided by returning the values from the function
    In utils.py, see the calculation and python usage for
    units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
    peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)
    """
    # Using depth-first search and propagation, create a search tree and solve the sudoku."
    # First, reduce the puzzle using the previous function
    values = reduce_puzzle(values)
    if values is False:
        return False
    if all(len(values[s]) == 1 for s in boxes):
        return values
    # Choose one of the unfilled squares with the fewest possibilities
    # done in another function best_unfulfilled_box_selector(values)
    # Now use recursion to solve each one of the resulting sudokus, and if one returns a value (not False), return that answer!
    # If you're stuck, see the solution.py tab!
    ret_tup = best_unfulfilled_box_selector(values)
    box = ret_tup[1]
    for v in values[box]:
        new_dictionary_layer = values.copy()
        # new_dictionary_layer[box] = v
        new_dictionary_layer = assign_value(new_dictionary_layer, box, v)
        result_of_call_to_search = search(new_dictionary_layer)
        if result_of_call_to_search:
            return result_of_call_to_search


# Chooses one of the unfilled squares with the fewest possibilities
def best_unfulfilled_box_selector(values):
    n, s = min((len(values[s]), s) for s in boxes if len(values[s]) > 1)
    return (n, s)


def solve(grid):
    """
    Find the solution to a Sudoku grid.
    Args:
        grid(string): a string representing a sudoku grid.
            Example: '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    Returns:
        The dictionary representation of the final sudoku grid. False if no solution exists.
    """
    """
    values = {"G7": "1234568", "G6": "9", "G5": "35678", "G4": "23678", "G3":
        "245678", "G2": "123568", "G1": "1234678", "G9": "12345678", "G8":
                  "1234567", "C9": "13456", "C8": "13456", "C3": "4678", "C2": "68",
              "C1": "4678", "C7": "13456", "C6": "368", "C5": "2", "A4": "5", "A9":
                  "2346", "A8": "2346", "F1": "123689", "F2": "7", "F3": "25689", "F4":
                  "23468", "F5": "1345689", "F6": "23568", "F7": "1234568", "F8":
                  "1234569", "F9": "1234568", "B4": "46", "B5": "46", "B6": "1", "B7":
                  "7", "E9": "12345678", "B1": "5", "B2": "2", "B3": "3", "C4": "9",
              "B8": "8", "B9": "9", "I9": "1235678", "I8": "123567", "I1": "123678",
              "I3": "25678", "I2": "123568", "I5": "35678", "I4": "23678", "I7":
                  "9", "I6": "4", "A1": "2468", "A3": "1", "A2": "9", "A5": "3468",
              "E8": "12345679", "A7": "2346", "A6": "7", "E5": "13456789", "E4":
                  "234678", "E7": "1234568", "E6": "23568", "E1": "123689", "E3":
                  "25689", "E2": "123568", "H8": "234567", "H9": "2345678", "H2":
                  "23568", "H3": "2456789", "H1": "2346789", "H6": "23568", "H7":
                  "234568", "H4": "1", "H5": "35678", "D8": "1235679", "D9": "1235678",
              "D6": "23568", "D7": "123568", "D4": "23678", "D5": "1356789", "D2":
                  "4", "D3": "25689", "D1": "123689"}
    """
    values = grid_values(grid)
    values = eliminate(values)

    # naked_twins() can also instead also be called ony once here. We have chosen to call it repeatedly
    # from inside reduce_puzzle along with repeated calls to eliminate and only_choice.
    # This is how we achieve constraint propagation using naked twins strategy
    # since naked_twins() function has its own elimination function
    values = only_choice(values)
    values = reduce_puzzle(values)


    values = search(values)
    return values


if __name__ == '__main__':
    """
    NOTES FOR SELF:
    If the python interpreter is running that module (the source file) as the main program, it sets the special __name__ variable to have a value "__main__". If this file is being imported from another module, __name__ will be set to the module's name.
    By doing the main check, you can have that code only execute when you want to run the module as a program and not have it execute when someone just wants to import your module and call your functions themselves.
    https://stackoverflow.com/questions/419163/what-does-if-name-main-do
    """
    #not_diag_sudoku_grid = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'# +> this will work with the other version of unit_list without diag_units
    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    #diag_sudoku_grid = '9.1....8.8.5.7..4.2.4....6...7......5..............83.3..6......9................'
    #diag_sudoku_grid = '...8...1.781..........1....4.......5..8..7.....75.319................6.........3.'
    display(solve(diag_sudoku_grid)) # displays the solution using display function
    #print(assignments)
    try:
        from visualize import visualize_assignments


        visualize_assignments(assignments) #visualizes the solution in a pygame window using the visualize_assignments function
    except SystemExit:
        pass
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')

