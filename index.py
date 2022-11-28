from bottle import route, run, Bottle, request, template
from pyswip import Prolog
from variable import inicializar


ini = inicializar()

prolog = Prolog()
prolog.consult("ProyectoV5.pl")

p_page = '''
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<link rel="icon" href="logo.jpeg">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Inicio</title>
</head>
<body>
	<center><article><big><h1 class="titulo" style="color: white;">Sistema Inteligente</h1></big></article></center>
	<center><a href="/start" style="color: white; "><button><h2>Comenzar</h2</button></a></center>
	<aside class="Desc"><h1 class="titulo1" style="color: white;">Descripción del Proyecto</h1>
		<p style="color: white;">Un sistema experto que pueda asesorar
mediante varias preguntas y que determine
que computadora es más conveniente
comprar tomando en cuenta el presupuesto
seleccionado y las necesidades del
usuario.</p>
	</aside>
	<center><aside class="Obj"><h1 class="titulo1" style="color: white;">Objetivo del Proyecto</h1>
		<p align=left style="color: white;">El objetivo principal es lograr que el
proceso de selección de una
computadora sea más fácil y que la
computadora elegida se adecue a sus
necesidades, tomando en cuenta el
presupuesto que tiene cada usuario.
Como segundo objetivo, le permitirá al usuario comparar las computadoras que
entran dentro de sus necesidades y elegir la que más convenga.</p>
	</aside></center>
	<aside class="Eq"><center><h1 class="titulo1" style="color: white;">Equipo</h1></center>
		<p style="color: white;">Guzman Ruvalcaba Krystal<br>
		Rodriguez Martines Rafael Alejandro</p>
	</aside>
</body>
<style>
body {
  background-color: #27708B ;
}
h1.titulo{
	margin: 5%;
	padding: 5%;
	size: 20%;
}
h1.titulo1{
	margin: 5%;
	padding: 5%;
	size: 10%;
}
article{
	width:30%;
	height:95%;
	background-color:Black;
	margin: 5%;
	border-radius: 10%;
	border-top: 4px double white;
   	border-right: 4px double white;  
   	border-bottom: 4px double white;
   	border-left: 4px double white;
}
button{
	width:10%;
	height:15%;
	background-color:#5499C7;
	margin: 5%;
	border-radius: 10%;
	border-top: 4px double white;
   	border-right: 4px double white;  
   	border-bottom: 4px double white;
   	border-left: 4px double white;
}
aside.Desc{
	width:30%;
	height:80%;
	background-color:#17202A;
	margin: 0.5%;
	padding: 1%;
	border-radius: 10%;
	border-top: 4px double white;
   	border-right: 4px double white;  
   	border-bottom: 4px double white;
   	border-left: 4px double white;
}
aside.Obj{
	width:30%;
	height:80%;
	background-color:#212F3C;
	margin: -18%;
	padding: 1%;
	border-radius: 10%;
	border-top: 4px double white;
   	border-right: 4px double white;  
   	border-bottom: 4px double white;
   	border-left: 4px double white;
}
aside.Eq{
	width:30%;
	height:80%;
	background-color:#273746;
	margin: 0%;
	padding: 1%;
	border-radius: 10%;
	border-top: 4px double white;
   	border-right: 4px double white;  
   	border-bottom: 4px double white;
   	border-left: 4px double white;
   	float: right;
}
}
</style>
</html>
'''

formulario1 = '''
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<link rel="icon" href="logo.jpeg">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title></title>
	<script type="text/javascript">
		mobiscroll.select('#multiple-select', {
    	<!DOCTYPE html>
    	<html>
    	<head>
    		<meta charset="utf-8">
    		<meta name="viewport" content="width=device-width, initial-scale=1">
    		<title></title>
    	</head>
    	<body>
    	
    	</body>
    	</html>inputElement: document.getElementById('my-input'),
    	touchUi: false
		});
	</script>
</head>
<body>
	<center><article><big><h1 class="titulo" style="color: white;">Preguntas - Sistema Inteligente</h1></big></article>
	<form align=left method="post" action="/start2" style="color: white;"><br>
		<br><label for="presupuesto">¿Cual es tu presupuesto maximo?</label>
		<input type="number" name="presupuesto" id="presupuesto" required>
		<br>
		<br><label for="prioridad">¿Que priorizas en tu busqueda?</label>
		<select name="prioridad", id="prioridad" required>
			<option value="1">Economia</option>
			<option value="2">Calidad</option>
		</select>
		<br>
		<br><label for="estudiar">¿Usaras la computadora para estudiar?</label>
		<select name="estudiar" id="estudiar">
			<option value="y">SI</option>
			<option value="n">NO</option>
		</select>
		<br>
		<br><label for="trabajar">¿Usaras la computadora para trabajar?</label>
		<select name="trabajar" id="trabajar">
			<option value="y">SI</option>
			<option value="n">NO</option>
		</select>
		<br>
		<br><label for="jugar">¿Usaras la computadora para jugar</label>
		<select name="jugar" id="jugar">
			<option value="y">SI</option>
			<option value="n">NO</option>
		</select>
		<br>

		<button type="submit">Continuar</button>
	</form><br><a href="/" ><button><h2>Regresar al inicio</h2</button></a></center>
</body>
<style>
body {
  background-color: #27708B ;
}
h1.titulo{
	margin: 5%;
	padding: 5%;
	size: 20%;
}
h1.titulo1{
	margin: 5%;
	padding: 5%;
	size: 10%;
}
article{
	width:30%;
	height:95%;
	background-color:Black;
	margin: 5%;
	border-radius: 10%;
	border-top: 4px double white;
   	border-right: 4px double white;  
   	border-bottom: 4px double white;
   	border-left: 4px double white;
}
button{
	width:20%;
	height:20%;
	background-color:#5499C7;
	margin: 10%;
	border-radius: 10%;
	border-top: 4px double white;
   	border-right: 4px double white;  
   	border-bottom: 4px double white;
   	border-left: 4px double white;
}
form{
	width:30%;
	height:80%;
	background-color:#212F3C;
	margin: 5%;
	padding: 2%;
	border-radius: 10%;
	border-top: 4px double white;
   	border-right: 4px double white;  
   	border-bottom: 4px double white;
   	border-left: 4px double white;
   	float: center;
}
}
</style>
</html>
'''

formulario2 = '''
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<link rel="icon" href="logo.jpeg">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title></title>
</head>
<body>
	<center><form align=left style="color: white;" method="post" action="/start3">
		<br><label for="area_est">¿Que area es mas cecana a lo que estudias?</label><br>
		<select name="area_est" id="area_est">
			<option value="1">Educacion basica</option>
			<option value="2">Preparatoria</option>
			<option value="3">Administracion</option>
			<option value="4">Finanzas</option>
			<option value="5">Salud</option>
			<option value="6">Quimica</option>
			<option value="7">Tecnologias de la informacion</option>
			<option value="8">Telecomunicaciones</option>
			<option value="9">Arquitectura</option>
			<option value="10">Diseño y multimedia</option>
			<option value="11">Ingenierias</option>
			<option value="12">Otra carrera</option>
		</select>
		<br>
		<br><label for="tem_est">¿Cuanto tiempo a la semana usas la computadora para estudiar?</label><br>
		<select name="tem_est" id="tem_est">
			<option value="1">1 a 20 horas</option>
			<option value="2">21 a 35 horas</option>
			<option value="3">36 a 50 horas</option>
			<option value="4">51 o mas horas</option>
		</select>
		<br>
		<br><label for="uso_est">¿Como consideras el uso de la computadora para tus estudios?</label><br>
		<select name="uso_est", id="uso_est">
			<option value="1">Poco necesario para mis estudios</option>
			<option value="2">Necesidad regular para mis estudios</option>
			<option value="3">Indispensable para mis estudios</option>
		</select>
		<br>
		<button type="submit" >Continuar</button>
	</form><br><a href="/" ><button><h2>Regresar al inicio</h2</button></a></center>
</body>
<style>
body {
  background-color: #27708B ;
}
h1.titulo{
	margin: 5%;
	padding: 5%;
	size: 20%;
}
h1.titulo1{
	margin: 5%;
	padding: 5%;
	size: 10%;
}
button{
	width:20%;
	height:20%;
	background-color:#5499C7;
	margin: 10%;
	border-radius: 10%;
	border-top: 4px double white;
   	border-right: 4px double white;  
   	border-bottom: 4px double white;
   	border-left: 4px double white;
}
form{
	width:30%;
	height:80%;
	background-color:#212F3C;
	margin: 5%;
	padding: 2%;
	border-radius: 10%;
	border-top: 4px double white;
   	border-right: 4px double white;  
   	border-bottom: 4px double white;
   	border-left: 4px double white;
   	float: center;
}
}
</style>
</html>
'''

formulario3 = '''
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<link rel="icon" href="logo.jpeg">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title></title>
</head>
<body>
	<center><form align=left style="color: white;" method="post" action="/start4">
		<br><label for="area_trab">¿Que area es mas cecana a lo que trabajar?</label><br>
		<select name="area_trab" id="area_trab">
			<option value="1">Educacion</option>
			<option value="2">Turismo</option>
			<option value="3">Administracion</option>
			<option value="4">Finanzas</option>
			<option value="5">Salud</option>
			<option value="6">Quimica</option>
			<option value="7">Tecnologias de l ainformacion</option>
			<option value="8">Telecomunicaciones</option>
			<option value="9">Arquitectura</option>
			<option value="10">Diseño y multimedia</option>
			<option value="11">Comercio</option>
			<option value="12">Transporte</option>
			<option value="13">Mecanica</option>
			<option value="14">Otro sector</option>
		</select>
		<br>
		<br><label for="tem_trab">¿Cuanto tiempo a la semana usas la computadora para trabajar?</label><br>
		<select name="tem_trab" id="tem_trab">
			<option value="1">1 a 20 horas</option>
			<option value="2">21 a 35 horas</option>
			<option value="3">36 a 50 horas</option>
			<option value="4">51 o mas horas</option>
		</select>
		<br>
		<br><label for="uso_trab">¿Como consideras el uso de la computadora para tus trabajar?</label><br>
		<select name="uso_trab" id="uso_trab">
			<option value="1">Poco necesario para mis estudios</option>
			<option value="2">Necesidad regular para mis estudios</option>
			<option value="3">Indispensable para mis estudios</option>
		</select>
		<br>
		<button type="submit" >Continuar</button>
	</form><br><a href="/" ><button><h2>Regresar al inicio</h2</button></a></center>
</body>
<style>
body {
  background-color: #27708B ;
}
h1.titulo{
	margin: 5%;
	padding: 5%;
	size: 20%;
}
h1.titulo1{
	margin: 5%;
	padding: 5%;
	size: 10%;
}
button{
	width:20%;
	height:20%;
	background-color:#5499C7;
	margin: 10%;
	border-radius: 10%;
	border-top: 4px double white;
   	border-right: 4px double white;  
   	border-bottom: 4px double white;
   	border-left: 4px double white;
}
form{
	width:30%;
	height:80%;
	background-color:#212F3C;
	margin: 5%;
	padding: 2%;
	border-radius: 10%;
	border-top: 4px double white;
   	border-right: 4px double white;  
   	border-bottom: 4px double white;
   	border-left: 4px double white;
   	float: center;
}
}
</style>
</html>
'''

formulario4 = '''
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<link rel="icon" href="logo.jpeg">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title></title>
</head>
<body>
	<center><form align=left style="color: white;" method="post" action="/start5">
		<br><label>Selecciona los juegos que juegas o jugarias</label><br>
		<label><input type="checkbox" name="ju1" id="ju1" value="1">Fortnite</label><br>
		<label><input type="checkbox" name="ju1" id="ju1" value="2">Grand Theft Auto V</label><br>
		<label><input type="checkbox" name="ju1" id="ju1" value="3">Overwach</label><br>
		<label><input type="checkbox" name="ju1" id="ju1" value="4">Minecraft</label><br>
		<label><input type="checkbox" name="ju1" id="ju1" value="5">Valorant</label><br>
		<label><input type="checkbox" name="ju1" id="ju1" value="6">Call of Duty Warzone</label><br>
		<label><input type="checkbox" name="ju1" id="ju1" value="7">Elden Ring</label><br>
		<label><input type="checkbox" name="ju1" id="ju1" value="8">Sims</label><br>
		<label><input type="checkbox" name="ju1" id="ju1" value="9">League of Legends</label><br>
		<label><input type="checkbox" name="ju1" id="ju1" value="10">Ninguno de los anteriores</label><br>

		<br>
		<br><label for="tem_jug">¿Cuanto tiempo a la semana usas la computadora para jugar?</label>
		<select name="tem_jug" id="tem_jug">
			<option value="1">1 a 10 horas</option>
			<option value="2">11 a 20 horas</option>
			<option value="3">21 a 30 horas</option>
			<option value="4">31 a 40 horas</option>
			<option value="5">41 a 50 horas</option>
			<option value="6">51 o mas horas</option>
		</select>
		<br>
		<button type="submit" >Continuar</button>
	</form><br><a href="/" ><button><h2>Regresar al inicio</h2</button></a></center>
</body>
<style>
body {
  background-color: #27708B ;
}
h1.titulo{
	margin: 5%;
	padding: 5%;
	size: 20%;
}
h1.titulo1{
	margin: 5%;
	padding: 5%;
	size: 10%;
}
button{
	width:20%;
	height:20%;
	background-color:#5499C7;
	margin: 10%;
	border-radius: 10%;
	border-top: 4px double white;
   	border-right: 4px double white;  
   	border-bottom: 4px double white;
   	border-left: 4px double white;
}
form{
	width:30%;
	height:80%;
	background-color:#212F3C;
	margin: 5%;
	padding: 2%;
	border-radius: 10%;
	border-top: 4px double white;
   	border-right: 4px double white;  
   	border-bottom: 4px double white;
   	border-left: 4px double white;
   	float: center;
}
}
</style>
</html>
'''
final_i = '''
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<link rel="icon" href="logo.jpeg">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title></title>
</head>
<body>
	<center>
	<table style="color: white;">

'''

final_f = '''
</table><br><a href="/" ><button><h2>Regresar al inicio</h2</button></a></center>
</body>
<style>
body {
  background-color: #27708B ;
}
h1.titulo{
	margin: 5%;
	padding: 5%;
	size: 20%;
}
h1.titulo1{
	margin: 5%;
	padding: 5%;
	size: 10%;
}
table{
	width:80%;
	height:80%;
	background-color:#212F3C;
	margin: 10%;
	padding: 2%;
	border-top: 4px groove; white;
   	border-right: 4px groove; white;  
   	border-bottom: 4px groove; white;
   	border-left: 4px groove; white;
   	border-collapse: collapse;
}
td{
	border-bottom: 1px solid #ddd;
	height: 50px;
}
}
</style>
</html>
'''

@route('/')
def inicio():
	ini.presupuesto = ""
	ini.eco_cal = ""

	ini.estudiar = ""
	ini.trabajar = ""
	ini.jugar = ""

	ini.area_estudios = ""
	ini.tiempo_estudios = ""
	ini.uso_estudios = ""

	ini.area_trabajo = ""
	ini.tiempo_trabajo = ""
	ini.uso_trbajo = ""

	ini.juegos.clear()
	ini.tiempo_juego = ""

	return p_page

@route('/start')
def start():
	return formulario1

@route('/start2', method='POST')
def do_start2():
	ini.presupuesto = request.forms.get('presupuesto')
	ini.eco_cal = request.forms.get('prioridad')
	ini.estudiar = request.forms.get('estudiar')
	ini.trabajar = request.forms.get('trabajar')
	ini.jugar = request.forms.get('jugar')

	if ini.estudiar == 'y':
		return formulario2
	else:
		ini.area_estudios = '1'
		ini.tiempo_estudios = '1'
		ini.uso_estudios = '1'
		if ini.trabajar == 'y':
			return formulario3
		else:
			ini.area_trabajo = '1'
			ini.tiempo_trabajo = '1'
			ini.uso_trabajo = '1'
			if ini.jugar == 'y':
				return formulario4
			else:
				ini.juegos.append(8)
				ini.tiempo_juego = '1'
				int_list = [int(i) for i in ini.juegos]
				print('inicio_respuesta('+ini.presupuesto+', '+ini.area_estudios+',' +ini.tiempo_estudios+',' +ini.uso_estudios+',' +ini.area_trabajo+',' +ini.tiempo_trabajo+',' +ini.uso_trabajo+',' +str(int_list)+',' +ini.tiempo_juego+',' +ini.eco_cal+',' +ini.estudiar+',' +ini.trabajar+',' +ini.jugar+', A1, A2, A3, A4, A5, A6)')

				consulta = prolog.query('inicio_respuesta('+ini.presupuesto+', '+ini.area_estudios+',' +ini.tiempo_estudios+',' +ini.uso_estudios+',' +ini.area_trabajo+',' +ini.tiempo_trabajo+',' +ini.uso_trabajo+',' +str(int_list)+',' +ini.tiempo_juego+',' +ini.eco_cal+',' +ini.estudiar+',' +ini.trabajar+',' +ini.jugar+', A1, A2, A3, A4, A5, A6)')

				cadena = ""

				for x in consulta:
					cadenita = '<tr><td>'+str(x["A1"])+'</td><td>'+str(x["A2"])+'</td><td>'+str(x["A3"])+'</td></tr><tr><td>'+str(x["A4"])+'</td><td>'+str(x["A5"])+'</td><td>'+str(x["A6"])+'</td></tr><tr><td colspan="3" style="background-color: gray;"></td><tr>'
					cadena = cadena + cadenita

				return final_i + cadena + final_f


@route('/start3', method='POST')
def do_start3():
	ini.area_estudios = request.forms.get('area_est')
	ini.tiempo_estudios = request.forms.get('tem_est')
	ini.uso_estudios = request.forms.get('uso_est')
	if ini.trabajar == 'y':
		return formulario3
	else:
		ini.area_trabajo = '1'
		ini.tiempo_trabajo = '1'
		ini.uso_trabajo = '1'
		if ini.jugar == 'y':
			return formulario4
		else:
			ini.juegos.append(8)
			ini.tiempo_juego = '1'
			int_list = [int(i) for i in ini.juegos]
			print('inicio_respuesta('+ini.presupuesto+', '+ini.area_estudios+',' +ini.tiempo_estudios+',' +ini.uso_estudios+',' +ini.area_trabajo+',' +ini.tiempo_trabajo+',' +ini.uso_trabajo+',' +str(int_list)+',' +ini.tiempo_juego+',' +ini.eco_cal+',' +ini.estudiar+',' +ini.trabajar+',' +ini.jugar+', A1, A2, A3, A4, A5, A6)')
			consulta = prolog.query('inicio_respuesta('+ini.presupuesto+', '+ini.area_estudios+',' +ini.tiempo_estudios+',' +ini.uso_estudios+',' +ini.area_trabajo+',' +ini.tiempo_trabajo+',' +ini.uso_trabajo+',' +str(int_list)+',' +ini.tiempo_juego+',' +ini.eco_cal+',' +ini.estudiar+',' +ini.trabajar+',' +ini.jugar+', A1, A2, A3, A4, A5, A6)')
			cadena = ""

			for x in consulta:
				cadenita = '<tr><td>'+str(x["A1"])+'</td><td>'+str(x["A2"])+'</td><td>'+str(x["A3"])+'</td></tr><tr><td>'+str(x["A4"])+'</td><td>'+str(x["A5"])+'</td><td>'+str(x["A6"])+'</td></tr><tr><td colspan="3" style="background-color: gray;"></td><tr>'
				cadena = cadena + cadenita
			return final_i + cadena + final_f

@route('/start4', method='POST')
def do_start4():
	ini.area_trabajo = request.forms.get('area_trab')
	ini.tiempo_trabajo = request.forms.get('tem_trab')
	ini.uso_trabajo = request.forms.get('uso_trab')
	if ini.jugar == 'y':
		return formulario4
	else:
		ini.juegos.append(8)
		ini.tiempo_juego = '1'
		int_list = [int(i) for i in ini.juegos]
		print('inicio_respuesta('+ini.presupuesto+', '+ini.area_estudios+',' +ini.tiempo_estudios+',' +ini.uso_estudios+',' +ini.area_trabajo+',' +ini.tiempo_trabajo+',' +ini.uso_trabajo+',' +str(int_list)+',' +ini.tiempo_juego+',' +ini.eco_cal+',' +ini.estudiar+',' +ini.trabajar+',' +ini.jugar+', A1, A2, A3, A4, A5, A6)')

		consulta = prolog.query('inicio_respuesta('+ini.presupuesto+', '+ini.area_estudios+',' +ini.tiempo_estudios+',' +ini.uso_estudios+',' +ini.area_trabajo+',' +ini.tiempo_trabajo+',' +ini.uso_trabajo+',' +str(int_list)+',' +ini.tiempo_juego+',' +ini.eco_cal+',' +ini.estudiar+',' +ini.trabajar+',' +ini.jugar+', A1, A2, A3, A4, A5, A6)')
		cadena = ""

		for x in consulta:
			cadenita = '<tr><td>'+str(x["A1"])+'</td><td>'+str(x["A2"])+'</td><td>'+str(x["A3"])+'</td></tr><tr><td>'+str(x["A4"])+'</td><td>'+str(x["A5"])+'</td><td>'+str(x["A6"])+'</td></tr><tr><td colspan="3" style="background-color: gray;"></td><tr>'
			cadena = cadena + cadenita
		return final_i + cadena + final_f

@route('/start5', method='POST')
def do_start5():

	ini.juegos = request.forms.getall('ju1')
	ini.tiempo_juego = request.forms.get('tem_jug')
	int_list = [int(i) for i in ini.juegos]
	print(str(int_list))
	print('inicio_respuesta('+ini.presupuesto+', '+ini.area_estudios+',' +ini.tiempo_estudios+',' +ini.uso_estudios+',' +ini.area_trabajo+',' +ini.tiempo_trabajo+',' +ini.uso_trabajo+',' +str(int_list)+',' +ini.tiempo_juego+',' +ini.eco_cal+',' +ini.estudiar+',' +ini.trabajar+',' +ini.jugar+', A1, A2, A3, A4, A5, A6)')

	consulta = prolog.query('inicio_respuesta('+ini.presupuesto+', '+ini.area_estudios+',' +ini.tiempo_estudios+',' +ini.uso_estudios+',' +ini.area_trabajo+',' +ini.tiempo_trabajo+',' +ini.uso_trabajo+',' +str(int_list)+',' +ini.tiempo_juego+',' +ini.eco_cal+',' +ini.estudiar+',' +ini.trabajar+',' +ini.jugar+', A1, A2, A3, A4, A5, A6)')
	cadena = ""

	for x in consulta:
		cadenita = '<tr><td>'+str(x["A1"])+'</td><td>'+str(x["A2"])+'</td><td>'+str(x["A3"])+'</td></tr><tr><td>'+str(x["A4"])+'</td><td>'+str(x["A5"])+'</td><td>'+str(x["A6"])+'</td></tr><tr><td colspan="3" style="background-color: gray;"></td><tr>'
		cadena = cadena + cadenita
	return final_i + cadena + final_f

run(host='localhost', port=8080, debug=True)