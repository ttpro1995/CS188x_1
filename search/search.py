# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):# not working yet
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    #start = problem.getStartState()
    #print 'start ', start
   # start_succ = problem.getSuccessors(start)
   # print  'start succ', start_succ
    #b = start_succ[0]
    #print  'b ',b
   # print 'b position ' ,b[0]
   # b = b[0]
    #b_succ = problem.getSuccessors(b)
   # print 'b succ ',b_succ
    #c = b_succ[0]
    #print 'c ',c
    
    "*** My code here ***"
    
   # procedure DFS-iterative(G,v):
   #   let S be a stack
    #  S.push(v)
     # while S is not empty
      #      v = S.pop()
       #     if v is not labeled as discovered:
        #        label v as discovered
         #       for all edges from v to w in G.adjacentEdges(v) do
          #          S.push(w)
    
    m_counter = 0
    visited = []
    v = problem.getStartState()      
    S = util.Stack()
    v = (v,'start',0)
    v = [v] # make it an array
    S.push(v)
    while (S.isEmpty()==False):
        v = S.pop()
        #print v 
        m_counter = m_counter +1
        #print m_counter
        cur_state = v[-1]
        cur_position = cur_state[0]
        #print cur_position
        if (problem.isGoalState(cur_position)):
            break 
        if (cur_position in visited):
            continue # skip node already expanded
        v_succ= problem.getSuccessors(cur_position) #expanded a node
        visited.append(cur_position)
        for edge in v_succ:
            if edge in v:
                continue # avoid loop  
            if edge in visited:
                continue # not expand state already visit
            tmp_arr = list(v)  # a tmp array clone from v
            tmp_arr.append(edge) # push edge into array
            edge = tmp_arr # new plan (the path + new edge)
            S.push(edge)    
        
    from game import Directions
            
    result = []
    del v[0] # start dummy
    for state in v:
        directon = state[1]
        result.append(directon)
    return result                     
    
    #util.raiseNotDefined()

def breadthFirstSearch(problem):#done
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    m_counter = 0
    visited = []
    v = problem.getStartState()      
    S = util.Queue()
    v = (v,'start',0)
    v = [v] # make it an array
    S.push(v)
    while (S.isEmpty()==False):
        v = S.pop()
        #print v 
        m_counter = m_counter +1
        #print m_counter
        cur_state = v[-1]
        cur_position = cur_state[0]
        #print cur_position
        if (problem.isGoalState(cur_position)):
            break         
        if cur_position in visited:
            continue # skip if node already expanded
        v_succ= problem.getSuccessors(cur_position)  # expand a node
        visited.append(cur_position) # mark already visited (expanded) node        
        for edge in v_succ: 
            tmp_arr = list(v)  # a tmp array clone from v
            tmp_arr.append(edge) # push edge into array
            edge = tmp_arr # new plan (the path + new edge)
            S.push(edge)    
            
    
    from game import Directions
    
    del v[0] # start dummy
    result = []
    for state in v:
        directon = state[1]
        result.append(directon)
    return result         

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    m_counter = 0
    visited = []
    v = problem.getStartState()      
    S = util.PriorityQueue()
    v = (v,'start',0)
    v = [v] # make it an array
    S.push(v,0)
    while (S.isEmpty()==False):
        v = S.pop()
        #print v 
        m_counter = m_counter +1
        #print m_counter
        cur_state = v[-1]
        cur_position = cur_state[0]
        #print cur_position
        if (problem.isGoalState(cur_position)):
            break         
        if cur_position in visited:
            continue # skip if node already expanded
        v_succ= problem.getSuccessors(cur_position)  # expand a node
        visited.append(cur_position) # mark already visited (expanded) node        
        for edge in v_succ: 
            new_cost = edge[2] # the cost to new node
            cur_cost = (v[-1])[2] # old cost so far, write at index 2 in last tuple of array
            sum_cost = cur_cost + new_cost
            # create new state from edge with sum cost
            new_edge = (edge[0],edge[1],sum_cost)
            tmp_arr = list(v)  # a tmp array clone from v
            tmp_arr.append(new_edge) # push edge into array
            new_edge = tmp_arr # new plan (the path + new edge)
            S.push(new_edge,sum_cost)    
            
    
    from game import Directions
    
    del v[0] # start dummy
    result = []
    for state in v:
        directon = state[1]
        result.append(directon)
    return result    

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
