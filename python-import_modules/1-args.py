def main():
    import sys

    # print('\n')
    # print(sys.argv)
    # print('\n')

    # print(len(sys.argv))

    # print('\n')

    no_of_arguments = len(sys.argv)

    if (no_of_arguments == 1):
        print('{} argument: {}'.format(len(sys.argv), sys.argv))
        
    elif (no_of_arguments >1):
        print('{} arguments: {}'.format(len(sys.argv), sys.argv))
        
    elif (no_of_arguments == 0):
        print('{} argument.'.format(len(sys.argv)))
        
if __name__ == "__main__":
    main()