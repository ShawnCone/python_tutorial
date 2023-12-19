# Go to individual problems and run this main.py file to check answers

if __name__ == '__main__':
    from problems import problem_set_0
    res_0 = problem_set_0.check()
    if res_0:
        from problems import problem_set_1
        res_1 = problem_set_1.check()
    
    if res_1:
        from problems import problem_set_2
        res_2 = problem_set_2.check()

    
