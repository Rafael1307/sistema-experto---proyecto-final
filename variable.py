from pyswip import Prolog
prolog = Prolog()
prolog.consult("ProyectoV5.pl")

class inicializar():
	presupuesto = ""
	eco_cal = ""

	estudiar = ""
	trabajar = ""
	jugar = ""

	area_estudios = ""
	tiempo_estudios = ""
	uso_estudios = ""

	area_trabajo = ""
	tiempo_trabajo = ""
	uso_trbajo = ""

	juegos = list()
	tiempo_juego = ""

	consulta = prolog.query(' tcal_requisitos_minimos(A1, A2, A3, A4, A5, A6)')