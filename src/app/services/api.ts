import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private baseUrl = 'http://127.0.0.1:5000';

  constructor(private http: HttpClient) {}

  // Método para obtener un mensaje de bienvenida
  getMessage(): Observable<any> {
    return this.http.get(`${this.baseUrl}/`);
  }

  // Registro
  register(data: any): Observable<any> {
    return this.http.post(`${this.baseUrl}/api/auth/register`, data);
  }

  // Login
  login(data: any): Observable<any> {
    return this.http.post(`${this.baseUrl}/api/auth/login`, data);
  }

  // Perfil (requiere token)
  getProfile(token: string): Observable<any> {
    const headers = new HttpHeaders(). set('Authorization', `Bearer ${token}`);
    return this.http.get(`${this.baseUrl}/api/auth/profile`, { headers });
  }

  // Lista productos
  getProducts(): Observable<any> {
    return this.http.get(`${this.baseUrl}/products`);
  }

  // Crear producto (opcional, si no está protegido)
  createProduct(data: any): Observable<any> {
    return this.http.post(`${this.baseUrl}/products`, data);
  }
}
