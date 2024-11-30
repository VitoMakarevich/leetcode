class Solution(object):
    def lowestCommonAncestor(self, root, nodes):
	
		# Convert to set to do constant time lookup, which saves ~2s on runtime
        nodes = set(nodes)
		
		# This is where we're storing the final answer
        self.found = None
        
        def traverse(root):
		
		    # Return if it's not a tree node
            if root == None:
                return 0
            
			# This finds the number of tree nodes that are in the nodes set
            foundAncestors = traverse(root.left) + traverse(root.right)
			
			# A node is a descendant of itself, so if the root is in the nodes set we add 1
            if root in nodes:
                foundAncestors += 1
			
			# This means that every node in the nodes set is an ancestor
            if foundAncestors == len(nodes):
			    # set the value of self.found to root if self.found != None
                self.found = self.found or root
				
            return foundAncestors
        
        traverse(root)
        return self.found