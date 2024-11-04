#Yasmine Muraweh 
from cspProblem import Variable, CSP, Constraint        
from operator import lt,ne,eq,gt,le
from cspConsistency import Con_solver, Searcher, Search_with_AC_from_CSP
from cspExamples import ne_
from cspConsistencyGUI import ConsistencyGUI
from cspSearch import Searcher, Search_from_CSP

# Corresponding with the examplea the bottom of page 7.1 (Module 7), consider a problem with
# the varibles A, B, and C - each with the domain {1,2,3,4}.
# We set them up below for the CSP problem.  Note "position" is just an optional parameter to position
# the variables on the screen.

A = Variable('A', {1,2,3,4}, position=(0.5,0.8))
B = Variable('B', {1,2,3,4}, position=(0.2,0.7))  
C = Variable('C', {1,2,3,4}, position=(0.3,0.5)) 


# We will now add the constraints.  We will require A < B, B != 2 and B <C.
# Note the method "lt" should be used for "less than" and "ne_" should be used for "not equal."
# Again, the position arguments are purely optional - for display purposes only.

C0 = Constraint([A,B], lt, "A < B", position=(0.5,0.2))
C1 = Constraint([B], ne_(2), "B != 2", position=(0.7, 0.1))  
C2 = Constraint([B, C], lt, "B < C", position=(0.8, 0.4))


#Next, we create the CSP with a constructor - we will call it "MyCSP".
#You can enable by uncommenting the following line.

MyCSP = CSP("MyCSP", {A, B, C}, [C0, C1, C2])

#We can dereference the variables and constraints - uncomment the two print
#statementes below to see how this works.

print("Variables: "+str(MyCSP.variables))
print("Constraints: "+str(MyCSP.constraints))

# Optional: We can see a visual representation by uncommetning the following. #SKIP
# Visualizing the CSP may help you debug your code when doing the lab.

#MyCSP.show()
# Now we can actually try to solve the CSP.  The first such method we discussed
# was by using a search algorithm.

csp_Search = Searcher(Search_from_CSP(MyCSP))

#We can then display the results by uncommenting this line below.
#Note that this is conducting DFS and it displays some iteresting inforamtion - such as 
#how many pahts were expanded, and how may remain in the frontier before returing a solution.

print(csp_Search.search())

#We can derference these items as follows - note that we first need to dereference the search object itself
#with .search() and then derefernece the solution (.end()) and the cost (.cost).

print(csp_Search.search().end())
#print(searchBasedSolution.search().cost)
#search_result = searchBasedSolution.search()


# We can also use Arc connsitency to reduce the size of the problem (see page 7.3 in ZyBooks Module 7).
# AIPython has some classes that enable this.  First we can set the display setting below (uncomment the line):

Con_solver.max_display_level = 4

# Now we can apply this to our CSP.  Replace the comment with our CSP object name.

ConSolverObject = Con_solver(MyCSP)


#We can run Arc Consistency by uncommenting the follwoing line:

ConSolverObject.make_arc_consistent()

# Note how it iteratively prunces the domains.  We can see the resulting reduced domains
# by dereferencing the object and printing it to the screen.

reducedDomains = ConSolverObject.domains
print(reducedDomains)

#Optional: We can also visualize this result graphically (uncomment the following line) and
#observer how the domain for each variable reduces as you click on the arcs.

#ConsistencyGUI(MyCSP, speed=4, fontsize=15).go()

#Finally, we can run domain splitting, which interleaves search with arc consistency.
#As this is still running search, we can derefernece it in the same manner.

domainSplitSearch = Searcher(Search_with_AC_from_CSP(MyCSP))
domain_split_result = domainSplitSearch.search()

#print(domainSplitSearch.search().end())
if domain_split_result is not None:
    print(domain_split_result.end())
else:
    print("No solution found in domain splitting.")

#AI Python also has a handy method to produce all solutions using domain splitting.
#It is a method .solve_all() in the object that we created for arc consistency, so you can use the same object.
ConSolverObject.solve_all()

# You have completed the ICE.