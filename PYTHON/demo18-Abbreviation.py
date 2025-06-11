def generate_abbreviation(company_name):
    words = company_name.split()
    abbreviation = ''.join(word[0].upper() for word in words)
    return abbreviation
company_name = input("Enter the company name: ")
abbreviation = generate_abbreviation(company_name)
print("The abbreviation is:", abbreviation) 