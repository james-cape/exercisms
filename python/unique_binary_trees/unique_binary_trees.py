class UniqueBinaryTrees:
    def __init__(self):
        self.known_results = {
            0: 1,
            1: 1,
            2: 2
        }


    def numTrees(self, quantity):
        # Run recursively until the tree is broken down into a previously-known quantity
        # If the quantity already has a known number of possibilities stored, return it
        if quantity in self.known_results:
            return self.known_results[quantity]
        
        # If the quantity result is not stored, 
        # Reset the results_int to 0
        results_int = 0
        for i in range(1, quantity+1):

            # Get combinations of the range to the left
            # If i == 1, argument should be 0
            # If i == 2, argument should be 1, regardles of quantity
            # If i == 3, argument should be 2, regardles of quantity
            left_node = self.numTrees(i-1)

            # Get combinations of the range to the right
            # If i == 1 and quantity == 3, argument should be 2
            # If i == 2 and quantity == 3, argument should be 1
            right_node = self.numTrees(quantity - i)

            # Total combinations for i equal left multiplied by right (not the sum of left and right)
            # If one side quantity is <0, that means 
            # If one side quantity is 0, return 1 so the product with the other side is not also 0
            # The exception to this rule is quantity=0, accounted for in get_all_results()
            results_int += left_node * right_node

        # Store result for that quantity
        self.known_results[quantity] = results_int

        return results_int
