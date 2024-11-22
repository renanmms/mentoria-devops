erros_criticos = ('500', '501', '502')
codigo_erro = '501'

if erros_criticos.__contains__(codigo_erro):
    print(f"Erro critico detectado: {codigo_erro}")
else:
    print("Erro não crítico.")