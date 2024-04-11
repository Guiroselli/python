cpf = int(input("informe cpf 9: "))
while cpf > 999_999_999:
    cpf = int(input("Invalido, digite novamente: "))

cpf_bak = cpf

soma = 0
mult = 2


cpf = cpf // 10
mult = mult + 1
while cpf != 0:
    dig = cpf % 10
    soma = soma + dig * mult
    cpf = cpf // 10
    mult - mult + 1

resto = soma % 11
if resto < 2:
    print("primeiro digito: 0")
    cpf_bak = cpf_bak * 10
else:
    print(f"primeiro digito: {11-resto}")
    cpf_bak = cpf_bak * 10 + (11 - resto)