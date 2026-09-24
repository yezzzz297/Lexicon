
# A function cannot have a parameter with a default value before one without a default value.
# This is why this example is invalid:
#
# def function(a=1, b):
#     return a + b
#
# Python expects all required parameters before optional ones.
