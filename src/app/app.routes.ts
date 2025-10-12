import { Routes } from '@angular/router';
import { Inicio } from './components/inicio/inicio';
import { Login } from './components/login/login';

export const routes: Routes = [
    { path: '', component: Inicio },
    { path: 'login', component: Login }
];
