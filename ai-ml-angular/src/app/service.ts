import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class Service {
  private _PATH = 'http://127.0.0.1:5000/predict'; 

  constructor(private http: HttpClient) {
    // Initialization logic can go here
  }

  getPrediction(data: any) :Observable<any> {
    return this.http.post(this._PATH, {message: data});
  }
}
