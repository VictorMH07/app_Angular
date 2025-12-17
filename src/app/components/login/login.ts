import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { RouterLink } from '@angular/router';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [FormsModule, CommonModule, RouterLink],
  templateUrl: './login.html',
  styleUrls: ['./login.css']
})
export class Login {
  mostrarLogin = true; // Alterna entre login y registro

  // Campos del login
  emailLogin = '';
  passwordLogin = '';

  // Campos del registro
  nombre = '';
  emailRegistro = '';
  passwordRegistro = '';
  confirmarPassword = '';

  toggleForms(): void {
    this.mostrarLogin = !this.mostrarLogin;
  }

  iniciarSesion(): void {
    console.log('Iniciando sesión con:', this.emailLogin, this.passwordLogin);
    alert(`Inicio de sesión con ${this.emailLogin}`);
  }

  registrarse(): void {
    if (this.passwordRegistro !== this.confirmarPassword) {
      alert('Las contraseñas no coinciden');
      return;
    }
    console.log('Registrando usuario:', this.nombre, this.emailRegistro);
    alert(`Usuario registrado: ${this.nombre}`);
  }
}

