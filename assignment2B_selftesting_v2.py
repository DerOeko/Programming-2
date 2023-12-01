# import the file with your solutions
import assignment2B as asgmt
import numpy as np

def test_sum_even_rec_odd():
    if asgmt.sum_even_rec(13) == 42 : 
        print("Passed test_sum_even_rec_odd")
    else:
        print("Failed test_sum_even_rec_odd")
        print("Expected: 42")
        print("Received: ", asgmt.sum_even_rec(13))

def test_sum_even_rec_even():
    if asgmt.sum_even_rec(20) == 110 : 
        print("Passed test_sum_even_rec_even")
    else:
        print("Failed test_sum_even_rec_even")
        print("Expected: 110")
        print("Received: ", asgmt.sum_even_rec(20))

def test_array_product_rec():
    if asgmt.array_product_rec(np.array([30, 2, 4, 18, 3])) == 12960 : 
        print("Passed test_array_product_rec")
    else:
        print("Failed test_array_product_rec")
        print("Expected: 12960")
        print("Received: ", asgmt.array_product_rec(np.array([30, 2, 4, 18, 3])))

def test_array_product_rec_zero():
    if asgmt.array_product_rec(np.array([30, 2, 0, 9, 11, 34])) == 0 : 
        print("Passed test_array_product_rec_zero")
    else:
        print("Failed test_array_product_rec_zero")
        print("Expected: 0")
        print("Received: ", asgmt.array_product_rec(np.array([30, 2, 0, 9, 11, 34])))

def test_concat_rec():
    if asgmt.concat_rec(["I", "love", "programming"]) == "I love programming" :
        print("Passed test_concat_rec")
    else:
        print("Failed test_concat_rec")
        print("Expected: \"I love programming\"")
        print("Received: \"" + asgmt.concat_rec(["I", "love", "programming"])+"\"")

def test_concat_rec_signle():
    if asgmt.concat_rec(["Hey"]) == "Hey" :
        print("Passed test_concat_rec_empty")
    else:
        print("Failed test_concat_rec_empty")
        print("Expected: \"Hey\"")
        print("Received: \""+ asgmt.concat_rec(["Hey"])+"\"")

def test_half_christmas_tree_rec():
    if asgmt.half_christmas_tree_rec(4) == "*\n**\n***\n****" : 
        print("Passed test_half_christmas_tree_rec")
    else:
        print("Failed test_half_christmas_tree_rec")
        print("Expected: \n *\n**\n***\n****")
        print("Received: \n asgmt.half_christmas_tree_rec(4)")

def test_find_max_rec():
    list_of_numbers = [1,4,2,5,7,3,6,8,2]
    result = asgmt.find_max_rec(list_of_numbers)
    if result == 8:
        print("Passed test_find_max_rec")
    else:
        print("Failed test_find_max_rec")
        print("Expected: 8 ")
        print("Received: ", result)


# Define different testing functions
def main():
    """
    Main function
    """
    print("Testing sum_even_rec() function")
    test_sum_even_rec_odd()
    test_sum_even_rec_even()
    print(".................................")
    
    print("Testing array_product_rec() function")
    test_array_product_rec()
    test_array_product_rec_zero()
    print(".................................")
    
    print("Testing concat_rec() function")
    test_concat_rec()
    test_concat_rec_signle()    
    print(".................................")
    
    print("Testing half_christmas_tree_rec() function")
    test_half_christmas_tree_rec()
    print(".................................")
    
    print("Testing find_max_rec() function")
    test_find_max_rec()
    print(".................................")
    
if __name__=="__main__":    
    main()