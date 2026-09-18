def resolver_tablero(n, hueco_x, hueco_y):
   
    tablero = [[0 for _ in range(n)] for _ in range(n)]
    numero_tesela = 1 

    
    def teselar(x_inicio, y_inicio, tamano, hx, hy):
        nonlocal numero_tesela
        
        
        if tamano == 2:
            for i in range(x_inicio, x_inicio + 2):
                for j in range(y_inicio, y_inicio + 2):
                 
                    if not (i == hx and j == hy):
                        tablero[i][j] = numero_tesela
            numero_tesela += 1
            return

      
        mitad = tamano // 2
        centro_x = x_inicio + mitad
        centro_y = y_inicio + mitad

        
        cuadrante_hueco = 0
        if hx >= centro_x: cuadrante_hueco += 2
        if hy >= centro_y: cuadrante_hueco += 1

       
        tesela_actual = numero_tesela
        numero_tesela += 1

        huecos_nuevos = []
        
        if cuadrante_hueco == 0:
            huecos_nuevos.append((hx, hy)) 
        else:
            tablero[centro_x - 1][centro_y - 1] = tesela_actual
            huecos_nuevos.append((centro_x - 1, centro_y - 1)) 

        
        if cuadrante_hueco == 1:
            huecos_nuevos.append((hx, hy))
        else:
            tablero[centro_x - 1][centro_y] = tesela_actual
            huecos_nuevos.append((centro_x - 1, centro_y))

       
        if cuadrante_hueco == 2:
            huecos_nuevos.append((hx, hy))
        else:
            tablero[centro_x][centro_y - 1] = tesela_actual
            huecos_nuevos.append((centro_x, centro_y - 1))

      
        if cuadrante_hueco == 3:
            huecos_nuevos.append((hx, hy))
        else:
            tablero[centro_x][centro_y] = tesela_actual
            huecos_nuevos.append((centro_x, centro_y))

       
        teselar(x_inicio, y_inicio, mitad, huecos_nuevos[0][0], huecos_nuevos[0][1])
        teselar(x_inicio, y_inicio + mitad, mitad, huecos_nuevos[1][0], huecos_nuevos[1][1])
        teselar(x_inicio + mitad, y_inicio, mitad, huecos_nuevos[2][0], huecos_nuevos[2][1])
        teselar(x_inicio + mitad, y_inicio + mitad, mitad, huecos_nuevos[3][0], huecos_nuevos[3][1])

    
    tablero[hueco_x][hueco_y] = 0 
    teselar(0, 0, n, hueco_x, hueco_y)

  
    print(f"Tablero de {n}x{n} con hueco en ({hueco_x}, {hueco_y}):\n")
    for fila in tablero:
       
        print(" ".join(f"{celda:2}" if celda != 0 else "XX" for celda in fila))

resolver_tablero(8, 0, 2)