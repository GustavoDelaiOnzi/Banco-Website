from django import template

register = template.Library()

def ultimos4Digitos(string):
    string = string[-4:]
    return string

def subtract(value, arg):
    return value - arg

register.filter('ultimos4Digitos', ultimos4Digitos)
register.filter('subtract', subtract)