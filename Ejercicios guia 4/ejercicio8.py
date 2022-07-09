import unittest
"""
Crear la clase Fecha que contiene:
3 atributos (números enteros) que representan el día, mes y año de la fecha
El constructor de Fecha que recibe 3 parámetros para dia, mes y año
Sobrecarga del constructor que no tiene parámetros que setea los atributos en la fecha 1/1/2000
Los métodos getter y setter de los atributos
El método toString()
El método diaSiguiente() que devuelve la fecha del día siguiente
El método diaAnterior() que devuelve la fecha del día anterior
El método cantDiasEntre2Fechas()
"""
class ComprobarFecha(unittest.TestCase):      
    def test_dia_siguiente(self):
        fecha = Fecha(1,2,2020)
        self.assertTrue(fecha.dia_siguiente(),2/2/2020)

    def test_dia_anterior(self):
        fecha = Fecha(1,3,2020)
        self.assertTrue(fecha.dia_anterior(),29/2/2020)
        
    def test_cantidad_dias_entre_dos_fechas(self):
        fecha1 = Fecha(1,2,2020)
        fecha2 = Fecha(13,6,1985)
        self.assertTrue(fecha1.cantidad_dias_entre_dos_fechas,12651)
        

class Fecha:
    def __init__(self,dia,mes,year):
        self.dia = dia
        self.mes = mes
        self.year = year

    @classmethod
    def get_dia_mes_year(cls):
        return cls(1,1,2000)
    
    def dia_siguiente(self): 
        meses_30dias = [4,6,9,11]
        meses_31dias = [1,3,5,7,8,10,12]
        bisiesto = self.year % 4 == 0 and self.year % 100 != 0 or self.year % 400 == 0
        

        if (self.dia > 28 and self.mes==2 and not bisiesto) or (self.dia > 29 and self.mes==2) or (self.dia == 31 and self.mes not in meses_31dias) or (self.dia > 31):
            return "El mes ingresado no tiene esa cantidad de días"
        elif self.dia==28 and self.mes==2 and bisiesto:
            return "Fecha: 29/2/{}".format(self.year)
        elif (self.dia==31 and self.mes!=12) or (self.dia==30 and self.mes in meses_30dias) or (self.dia >= 28 and self.mes==2):
            self.mes+=1
            return "Fecha: 1/{}/{}".format(self.mes,self.year)
        elif self.dia == 31 and self.mes==12:
            self.year+=1
            return "Fecha: 1/1/{}".format(self.year)
        else:
            self.dia+=1 
            return "Fecha: {}/{}/{}".format(self.dia,self.mes,self.year)

    def dia_anterior(self):  
        meses_30dias = [4,6,9,11]
        bisiesto = self.year % 4 == 0 and self.year % 100 != 0 or self.year % 400 == 0
        
        if self.dia > 31 or self.dia > 29 and self.mes == 2 or self.dia == 29 and not bisiesto:
            return "El mes ingresado no tiene esa cantidad de días"
        elif (self.dia==1 and self.mes!=1 and self.mes in meses_30dias) or (self.dia==1 and self.mes not in meses_30dias and self.mes==2) or self.dia==1 and self.mes==8:
            self.mes-=1
            return "Fecha: 31/{}/{}".format(self.mes,self.year)
        elif self.dia==1 and self.mes==1:
            self.year-=1
            return "Fecha: 31/12/{}".format(self.year)
        elif self.dia==1 and self.mes not in meses_30dias and self.mes!= 3 and self.mes!=8:
            self.mes-=1
            return "Fecha: 30/{}/{}".format(self.mes,self.year)
        elif self.dia==1 and self.mes==3:
            if bisiesto:
                return "Fecha: 29/2/{}".format(self.year)
            else:
                return "Fecha: 28/2/{}".format(self.year)
        else:
            self.dia-=1
            return "Fecha: {}/{}/{}".format(self.dia,self.mes,self.year)
            

    def cantidad_dias_entre_dos_fechas(self,fecha2):
        meses_31dias = [1,3,5,7,8,11]
        meses_30dias = [4,6,9,10,12]
        dias_transcurridos_year1= self.dia
        bisiesto = self.year % 4 == 0 and self.year % 100 != 0 or self.year % 400 == 0
        
        for i in range(1,self.mes):  
            if i in meses_31dias:
                dias_transcurridos_year1+=31
            elif i in meses_30dias:
                dias_transcurridos_year1+=30
            elif i == 2 and bisiesto:
                dias_transcurridos_year1+=29
            else:
                dias_transcurridos_year1+=28
                
               
        if bisiesto:
            dias_restantes_year1 = 366 - dias_transcurridos_year1
        else:
            dias_restantes_year1 = 365 - dias_transcurridos_year1
            
        dias_transcurridos_year2 = fecha2.dia
        bisiesto = fecha2.year % 4 == 0 and fecha2.year % 100 != 0 or fecha2.year % 400 == 0
        
        for i in range(1,fecha2.mes):  
            if i in meses_31dias:
                dias_transcurridos_year2+=31
            elif i in meses_30dias:
                dias_transcurridos_year2+=30
            elif i == 2 and bisiesto:
                dias_transcurridos_year2+=29
            else:
                dias_transcurridos_year2+=28
                
               
        if bisiesto:
            dias_restantes_year2 = 366 - dias_transcurridos_year2 
        else:
            dias_restantes_year2 = 365 - dias_transcurridos_year2 
            
        if self.year < fecha2.year:
            year_menor = self.year
            year_mayor = fecha2.year
        else: 
            year_menor = fecha2.year
            year_mayor = self.year
                    
        dias_years_intermedios = 0    
        for i in range(year_menor+1,year_mayor):
            bisiesto = i % 4 == 0 and i % 100 != 0 or i % 400 == 0
            if bisiesto:
                dias_years_intermedios+= 366
            else:
                dias_years_intermedios+= 365
                
        if dias_restantes_year1 < dias_restantes_year2:
            dias_entre_fechas = dias_restantes_year1 + dias_years_intermedios + dias_transcurridos_year2
        else:
            dias_entre_fechas = dias_restantes_year2 + dias_years_intermedios + dias_transcurridos_year1  
            
        return "Han pasado {} días entre ambas fechas".format(dias_entre_fechas)
                  
    def get_dia(self):
        return self.dia

    def get_mes(self):
        return self.mes

    def get_year(self):
        return self.year

    def set_dia(self,dia):
        self.dia = dia

    def set_mes(self,mes):
        self.mes = mes

    def set_year(self,year):
        self.year = year

    def __str__(self):
        return "Fecha: {}/{}/{}".format(self.dia,self.mes,self.year)

if __name__ == "__main__":
    unittest.main()


