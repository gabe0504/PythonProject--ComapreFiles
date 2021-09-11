#main function creates the dictionary 'd' and sets the parameters 'params.'
#main function then passes dictionary and parameters as arguments into the function p3_dictionary_manipualtions
def main():
    d={'Canada': 'ca', 'United States':'us', 'Mexico':'mx'} #dictionary created with key-value elements
    params=['Canada', 'France', 'sw', 'se'] #list of parameters
    p3_dictionary_manipulations(d, params) #function which

def p3_dictionary_manipulations(d, params):
#for-loop checks for Canada and France in dictionary and prints the result
    for items in params[:2]:
        if items in d:
            print('a.', items, 'in dict\n' + 'True\n')
        else:
            print('b.', items, 'in dict\n' + 'False\n')
#for-loop uses x variable to print keys and their associated values in a table
    print('c. Keys and values in dict (key in field width 20)')
    for x in d:
        print(format(x, '20'), d.get(x))
#key Sweden added to dictionary with its incorrect country abbreviation added from parameters list as value
    d['Sweden']=params[2]
    print('\nd. Dict with Sweden set to \'sw\':')
    print(d)
#lines 24-27 deletes they key-value pair for Sweden then adds it again with the correct country abbreviation
    del d['Sweden']
    d['Sweden']=params[3]
    print('\ne. Dict with Sweden set to \'se\':')
    print(d)
#lines 30-32 rearranges the order of the key-value elements and stores them in the variable d2.
#abbr:name sets new key-value arrangment. For loop iterates to variables over the items method
    d2 = {abbr: name for name, abbr in d.items()} #'abbr:name' sets the new key-valu arrangement
    print("\nf. Reverse mapping using dictionary comprehension:")
    print(d2)
#lines 33-35 performs the above operation again but uses the upper() method to capitalize the country names
    print('\ng. Reverse mapping uppercase using dictionary comprehension: ')
    d2 = {abbr: name.upper() for name, abbr in d.items()}
    print(d2)
main()
