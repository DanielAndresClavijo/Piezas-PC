from dataSource import *
from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import date

conMysql = dataSource("127.0.0.1", "root", "", "piezas_pc_inventario", "3306", "mysql")
conSqLite = dataSource("", "", "", "piezas_pc_proveedores", "", "sqlite")

app = Flask(__name__)

#settings
app.secret_key = 'mysecretkey'#Llave de sesion

@app.route('/')
def Index(): 
  data = conMysql.getData("select * from inventario")
  data2 = conSqLite.getData("select * from proveedores")
  return render_template('index.html', productos = data, proveedores = data2)

@app.route('/add_product', methods=['POST'])
def add_product():
  if request.method=='POST':
    codigo_barras = request.form['codigo_barras']
    nombre = request.form['nombre']
    especificaciones = request.form['especificaciones']
    marca = request.form['marca']
    precio = request.form['precio']
    id_proveedor = request.form['proveedor']
    fecha = date.today()
    fecha_inventario = fecha.strftime('%Y-%m-%d')
    conMysql.query("INSERT INTO `inventario` ( `codigo_barras`, `nombre`, `especificaciones`, `marca`, `precio`, `fecha_inventario`, `id_proveedor`) VALUES ("+codigo_barras+", '"+nombre+"', '"+especificaciones+"', '"+marca+"', "+precio+", '"+fecha_inventario+"', "+id_proveedor+")")
    
    flash('Pieza Guardada en el inventario Satisfactoriamente')
    return redirect(url_for('Index'))

@app.route('/edit_product/<string:id>')
def get_product(id):
  data = conMysql.getData("select * from inventario WHERE id_inventario="+id+"")
  data2 = conSqLite.getData("select * from proveedores ")
  return render_template('edit_producto.html', producto = data[0], proveedores = data2)

@app.route('/update_producto/<string:id>', methods = ['POST'])
def update_producto(id):
  codigo_barras = request.form['codigo_barras']
  nombre = request.form['nombre']
  especificaciones = request.form['especificaciones']
  marca = request.form['marca']
  precio = request.form['precio']
  id_proveedor = request.form['proveedor']
  fecha_inventario = request.form['fecha_inventario']
  conMysql.query("UPDATE inventario SET codigo_barras = "+codigo_barras+", nombre = '"+nombre+"', especificaciones = '"+especificaciones+"', marca = '"+marca+"', precio = "+precio+", fecha_inventario = '"+fecha_inventario+"', id_proveedor = "+id_proveedor+" WHERE id_inventario = "+id+"")
  flash('Pieza Editada en el inventario Satisfactoriamente')
  return redirect(url_for('Index'))

@app.route('/delete_product/<string:id>')
def delete_product(id):
  conMysql.query('DELETE FROM inventario WHERE id_inventario='+id+'')
  flash('Producto eliminado')
  return redirect(url_for('Index'))

if __name__ == '__main__':
  app.run(port = 8080, debug = True)