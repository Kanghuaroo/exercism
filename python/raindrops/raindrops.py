def convert(number):
    output=''
    #add output
    if number % 3 == 0:
        output += 'Pling'
    if number % 5 == 0:
        output += 'Plang'
    if number % 7 == 0:
        output += 'Plong'
    #check if output changed
    if output == '':
        return str(number)
    else:
        return output
