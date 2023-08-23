#precio con descuentos de un objeto aplicando programacion funcional

def descuento(price, descont):#funcion que descuenta el porcentaje del precio
    return price - (price * descont) / 100


def canasta(dic, function):
    total = 0
    for i, discount in dic.items():#usando la llave y el valor
        total += function(i,discount) #acumulando el valor retornado de la funcion
    return total


print(
    "El precio de la compra tras aplicar los descuentos es: ",
    canasta({1000: 20, 500: 10, 100: 1}, descuento),
)
