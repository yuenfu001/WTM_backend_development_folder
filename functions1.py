# birhane = 56
# glory = 90

# multiply = birhane*glory

# print(multiply)

def process_student(name,score):

    def calculate_score(s):
        if s>=70:
            return "A"
        elif s>=50:
            return "B"
        return "F"

    grade = calculate_score(score)
    return f'Student: {name} | grad: {grade}'

# print(process_student("Sarah",85))

def format_currency(amount):
    return f"{amount:.1f}"

def generate_receipt(item_name, price,tax_rate):
    taxed = (price*tax_rate)
    total = price + taxed
    formatted_total = format_currency(total)

    return f"Item:{item_name}| Total Due: {formatted_total} with a taxed amount of: {format_currency(taxed)}"

print(generate_receipt("Laptop",600,.07))

def function_name(birhane, glory):  # parameter
    return f"Multiplication of {birhane} and {glory} is {birhane*glory}"
    # print(f"Multiplication of {birhane} and {glory} is {birhane*glory}")


# if condition:
#     execute if true
# else:
#     execute if false
# print(function_name(98,50))# 98 and 50 are arguments
# print(function_name(2,5))
# print(function_name(10,25))
# function_name(98,50)
# function_name(2,5)
# function_name(10,25)

# def student_info(name,course,country):
#     print(f"fullname: {name}\ncourse: {course}\ncountry: {country}")

# student_info("Birhane Tekayneh","backend development","Ethopia")
# student_info("Abigiya Daniel","Frontend development","Eritrea")
# student_info("Ridwanullah Abdurrasheed","UI/UX","Ghana")

# def student_info(name,course,country="Cameroon"):
#     print(f"fullname: {name}\ncourse: {course}\ncountry: {country}")


# student_info("backend development","Birhane Tekayneh")
# student_info("Abigiya Daniel","Frontend development","Eritrea")
# student_info("Ridwanullah Abdurrasheed","UI/UX","Ghana")

# Arbitrary Argument *args
# def unknown_parameter(*abrt):
#     print(type(abrt))
#     print(
#         f"firstname: {abrt[0]}\nlastname: {abrt[1]}\nage: {abrt[2]}"
#     )

# unknown_parameter("Staphanie","Simon",50)

# Arbitrary Keyword Argument **kwargs


# def unknown_kwargs(**glory):
#     print(type(glory))
#     print(
#         f"firstname: {glory['fname']}\nlastname: {glory['lname']}\ncourse: {glory['course']}\nage: {glory['age']}\n"
#     )

# unknown_kwargs(fname="Asakhe",lname="Sotyato",course="UI/UX",age=90)

# def abs_position(arg1,arg2,/):
#     print(f"testing positional argument using {arg1} and {arg2}")

# abs_position("position1","position2")
# abs_position(arg2="position1",arg1="position2")

# def abs_kwargs(*,arg1,arg2):
#     print(f"testing positional argument using {arg1} and {arg2}")

# abs_kwargs("position1","position2")
# abs_kwargs(arg2="position1",arg1="position2")

# def product_info(item,amount):

#     def caculate_taxed_amount():
#         taxed_amount = amount * ta

# def process_student(name,score):
#     # helper function
#     def calculate_grade(s):
#         if s>=80:
#             return "A"
#         elif s >=60:
#             return "B"
#         elif s >=50:
#             return "C"
#         else:
#             return "F"
#     grade = calculate_grade(score)
#     return f"Student: {name} | Grade: {grade}"

# print(process_student("Stephanie Simon",90))
# print(process_student("Abigiya Daniel",70))
# print(process_student("Merlin Lebese",49))
# print(process_student("Chiko Liu",55))


# def format_number(amount):
#     return f"{amount: .1f}"

# def generate_receipt(item,amount, tax_rate):
#     taxed_amount = amount * tax_rate
#     formatted_amount = format_number(taxed_amount)
#     print(f"Item bought: {item}\nItem Cost: {amount}\nTaxed Amount:{formatted_amount}")


# print("="*27)
# generate_receipt("Laptop",980,.12)
# print("="*27)
# generate_receipt("Electric Bike",4322,.16)
# print("="*27)
# generate_receipt("Grocceries",1095,.02)
# print("==========================")

from libraries.module import calculator
# import module

# print(module.calculator("+",10,5))
# print(module.calculator("-",10,5))
# print(module.calculator("/",10,2))
# print(module.calculator("/",10,0))
# print(module.calculator("*",10,43))
print(calculator("+",10,5))
print(calculator("-",10,5))
print(calculator("/",10,2))
print(calculator("/",10,0))
print(calculator("*",10,43))


