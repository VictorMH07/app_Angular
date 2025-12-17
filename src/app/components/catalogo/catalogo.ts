import { Component } from '@angular/core';
import { NgFor, DecimalPipe } from '@angular/common';

interface Producto {
  nombre: string;
  descripcion: string;
  precio: number;
  unidad: string;
  imagen: string;
}

@Component({
  selector: 'app-catalogo',
  standalone: true,
  imports: [NgFor, DecimalPipe],
  templateUrl: './catalogo.html',
  styleUrl: './catalogo.css'
})
export class Catalogo {
  productos: Producto[] = [
    {
      nombre: 'Aguacae Hass Orgánico',
      descripcion: 'Eje cafetero (Risaraldas, Caldas) y Tolima.',
      precio: 9500,
      unidad: 'kg',
      imagen:'/images/aguacate.jpg'
    }, 
    {
      nombre: 'Lulo (Naranjilla) Orgánico',
      descripcion: 'Departamnto de Cundinamarca.',
      precio: 8500,
      unidad: 'kg',
      imagen:'/images/lulo.jpg'
    }, 
    {
      nombre: 'Mango Tommy Orgánico',
      descripcion: 'Tolima',
      precio: 6500,
      unidad: 'kg',
      imagen:'/images/Mango.jpg'
    }, 
  ];

  agregarAlCarrito(producto: Producto) {
    alert('${producto.nombre} agregado al carrito.');
  }
}
