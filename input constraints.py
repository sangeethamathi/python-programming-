from constrainst input*
problem=problem()
problem.addVariable('a',range(5))
problem.addVariable('b',range(5))
problem.addConstraint(lambda a,b:a+b==5)
problem.addCanstraint(lambda a,b:a*b==6)
problem.get Solution()
