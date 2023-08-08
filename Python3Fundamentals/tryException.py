acronyms = {
    'LOL' : 'Laugh Out Loud',
    'IDK' : 'I Dont Know'
}

try:
    definition = acronyms['LOL']
    print(definition)
except:
    print("Key Not Found")
finally:
    for acronym in acronyms:
        print(acronym)

print("Program Continues")

def division(num1,num2):
    if num2 == 0:
        # raise ZeroDivisionError
        raise Exception('Division by Zero')
    result = num1 / num2
    print(result)

division(22,0)