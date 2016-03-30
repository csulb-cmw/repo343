from commit import ignore 

def main():
    test_cases = [
            ['user/documents/test', False ],
            ['user/documents/.test', True ],
            ['user/documents/repo343/test.py', False],
            ['user/repo343/test/another/test.py', False],
            ['user/test/program.o', False],
            ]
    for test in test_cases:
        print 'testing "' + test[0] +'"...'
        if ignore(test[0]) == test[1]:
            print 'passed!'
        else:
            print 'FAILED!!!!'

main()
