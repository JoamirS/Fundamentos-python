"""
    Mariana montou o seguinte código python para controlar se sua barraca de frutas possui determinadas frutas
    solicitadas pelos seus clientes.
"""

fruits_for_sale = ['Banana', 'Maca', 'Pera', 'Uva', 'Melancia', 'Jamelao']
requested_fruit = str(input('Qual é a fruta que deseja consultar? '))

if requested_fruit in fruits_for_sale:
    print('Sim, temos a fruta pedida.')
else:
    print('Não, a fruta requisitada não está em estoque.')
