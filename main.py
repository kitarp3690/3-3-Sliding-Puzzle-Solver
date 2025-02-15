# making a 3*3 sliding number puzzle solver using A* algorithm
import numpy as np
import heapq

class Puzzle:
    def __init__(self, state):
        self.state = np.array(state)
        self.goal_state = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])

    def check_solved(self)->bool:
        """This function checks whether the given state is matched with the goal state"""
        return np.array_equal(self.state, self.goal_state)

    def calculate_heuristic_value(self, given_state:np)->int:
        """This calculates the heuristic value(also known as Manhattan distance)"""
        goal_state=np.array(([1,2,3],[4,5,6],[7,8,0]))
        heuristic = 0
        for i in range(3):
            for j in range(3):
                value = given_state[i,j]
                if value != 0: # =0 because we dont need to calculate for empty tile(i.e 0)
                    goal_i, goal_j = divmod(value-1, 3)
                    heuristic += abs(i-goal_i) + abs(j-goal_j)
        return heuristic

    def find_empty_tile(self)->int:
        """This function finds the position of empty tile and returns it"""
        i, j = np.where(self.state == 0)
        return i[0],j[0] # [0] is used because where function return tuple

    def generate_possible_moves(self)->list:
        """This function generates new states by moving the empty tile and returns possible moves list"""
        moves = []
        x, y = self.find_empty_tile()
        directions = [(-1,0), (1,0), (0,-1), (0,1)]  # Up, Down, Left, Right
        
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy # calculating the new position of new tile

            if 0 <= new_x < 3 and 0 <= new_y< 3: # making sure the new position is within the bound
                new_state = self.state.copy() # we use copy function instead of using new_state=self.state because in numpy when we change new_state it also changes self.state automatically
                new_state[x,y], new_state[new_x, new_y] = new_state[new_x, new_y], new_state[x, y] # swapping empty tile with neighbour tile  
                moves.append(new_state)
        # print(moves)
        return moves

    def solving(self):
        """Solving the problem using A* algorithm"""
        priority_queue = []
        came_from = {}
        heapq.heappush(priority_queue, (self.calculate_heuristic_value(self.state), 0, self.state.tolist()))
        # print(f'\n\npriority_queue= {priority_queue}\n\n')
        visited = set()  # To keep track of visited states
        current_state = None
        
        while priority_queue:
            _, g, current_state = heapq.heappop(priority_queue)
            current_state = np.array(current_state)
            
            # If this state has already been visited, skip it
            current_state_tuple = tuple(map(tuple, current_state))
            if current_state_tuple in visited:
                continue
            
            # Mark the current state as visited
            visited.add(current_state_tuple)
            # print(f'visited={visited}')

            # If this state is the goal, reconstruct the solution path
            if np.array_equal(current_state, self.goal_state):
                # print(f'completed_s={current_state}')
                # for key, value in came_from.items():
                #     print(f"dictionary{key}:{value}\n")
                print("Solved!")
                self.print_solution(came_from, current_state)
                return
            
            # Explore the neighbors (possible moves)
            for move in Puzzle(current_state).generate_possible_moves():
                move_tuple = tuple(map(tuple, move))
                if move_tuple not in visited:  # Only consider unvisited moves
                    h = self.calculate_heuristic_value(move)
                    heapq.heappush(priority_queue, (g + 1 + h, g + 1, move.tolist()))
                    # print(f'pq={priority_queue}')
                    
                    # Record the current state as the previous state of the move
                    came_from[move_tuple] = current_state_tuple
            
        print("No solution found")

    def print_solution(self, came_from, current_state):
        """This function backtracks and prints the solution path."""
        path = []

        while current_state is not None:
        # for i in range(5):
            path.append(current_state)
            
            # Convert to tuple (if that's how the dictionary stores keys)
            current_state_tuple = tuple(map(tuple, current_state))
            # print(f'Checking for key: {current_state_tuple}')
            
            # Retrieve the previous state
            previous_state = came_from.get(current_state_tuple, None)
            # print(f'Retrieved value: {previous_state}')
            
            # If previous_state is None, stop looping
            if previous_state is None:
                break
            
            current_state = previous_state  # Move to the previous state
        
        if not path:
            print("No solution path exists.")
            return
        # print(path)
        path.reverse()  # Reverse to show path from start to goal

        count_step = 0
        print("Steps::-----\n")
        for step in path:
            count_step += 1
            print(f'step {count_step}: \n{np.array(step)}\n')  # Print as a 2D array

def intialization():
    """Initialize"""
    goal_state = np.array([[1,2,3],[4,5,6],[7,8,0]])
    initial_state = np.zeros((3,3),dtype=int)
    print("Write '0' for empty block ")
    for i in range(3):
        for j in range(3):
            initial_state[i,j]= int(input(f"Enter number for [{i}][{j}] block: "))
    print(f'Initial State of Puzzle::\n{initial_state}\n')
    puzzle = Puzzle(initial_state)
    puzzle.solving()


intialization()
