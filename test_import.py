#!/usr/bin/env python3

# Test script to import mymath package
try:
    import mymath
    print("Import successful!")
    
    # Test basic functions
    result1 = mymath.basic.add(5, 3)
    print(f"mymath.basic.add(5, 3) = {result1}")
    
    # Test stats functions
    result2 = mymath.stats.mean([1, 2, 3, 4, 5])
    print(f"mymath.stats.mean([1, 2, 3, 4, 5]) = {result2}")
    
except Exception as e:
    print(f"Error: {e}")