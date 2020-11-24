from dataSource import *
from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import date

conMysql = dataSource("127.0.0.1", "root", "", "piezas_pc_inventario", "3306", "mysql")
conSqLite = dataSource("", "", "", "piezas_pc_proveedores", "", "sqlite")

app = Flask(__name__)

#settings
app.secret_key = 'mysecretkey'#Llave de sesion

#PIEZAS PC
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
  return render_template('edit_producto.html', producto = data[0], proveedor = data2)

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

#PROVEEDORES
@app.route('/proveedores/<string:prov>')
def proveedore(prov): 
  data = conSqLite.getData("select * from proveedores")
  return render_template('proveedor.html', provee = data, prov = 1)

@app.route('/proveedores/')
def proveedore2(): 
  prov = 1
  data = conSqLite.getData("select * from proveedores")
  return render_template('proveedor.html', provee = data, prov = 1)

@app.route('/add_proveedor', methods=['POST'])
def add_proveedor():
  if request.method=='POST':
    nit = request.form['nit']
    nombre_provedor = request.form['nombre-p']
    empresa = request.form['nombre-e']
    conSqLite.query("INSERT INTO `proveedores` ( `nit`, `nombre_provedor`, `empresa`) VALUES ("+nit+", '"+nombre_provedor+"', '"+empresa+"')")
    
    flash('Proveedor creado con satisfactoriamente')
    return redirect(url_for('proveedore2'))

@app.route('/edit_proveedor/<string:id>')
def edit_proveedor(id):
  data = conSqLite.getData("select * from proveedores WHERE id_proveedores= "+id+"")
  return render_template('edit_proveedor.html', proveedor = data[0])

@app.route('/update_proveedor/<string:id>', methods = ['POST'])
def update_proveedor(id):
  nit = request.form['nit']
  nombre_provedor = request.form['nombre-p']
  empresa = request.form['nombre-e']
  conSqLite.query("UPDATE proveedores SET nit = "+nit+", nombre_provedor = '"+nombre_provedor+"', empresa = '"+empresa+"' WHERE id_proveedores = "+id+"")
  flash('Proveedor editado con satisfactoriamente')
  return redirect(url_for('proveedore2'))

@app.route('/delete_proveedor/<string:id>')
def delete_proveedor(id):
  conSqLite.query('DELETE FROM proveedores WHERE id_proveedores='+id+'')
  flash('Producto eliminado')
  return redirect(url_for('proveedore2'))

if __name__ == '__main__':
  app.run(port = 8080, debug = True)