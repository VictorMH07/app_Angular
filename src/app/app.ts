import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterOutlet } from '@angular/router';
import { ApiService } from './services/api';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, RouterOutlet],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class AppComponent implements OnInit {
  message = 'Cargando...';

  constructor(private api: ApiService) {}

  ngOnInit(){
    this.loadMessage(); // Llama al cargar la pagina
  }

  loadMessage() {
    this.api.getMessage().subscribe({
      next: (data) => {
        this.message = data.message;
      }, 
      error: (err) => {
        console.error('Error', err);
        this.message = 'Error al conectar con Flask' + err.message;
      }
    });
  }
}
