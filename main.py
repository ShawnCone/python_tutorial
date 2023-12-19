from problems import problem_set_0
# from problems import problem_set_1
# from problems import problem_set_2

# Go to individual problems 

if __name__ == '__main__':
    res_0 = problem_set_0.check()
    if res_0:
        from problems import problem_set_1
        res_1 = problem_set_1.check()
    
    if res_1:
        from problems import problem_set_2
        res_2 = problem_set_2.check()

    
