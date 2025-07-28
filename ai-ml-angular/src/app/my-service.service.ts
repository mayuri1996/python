import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class MyServiceService {

  private apiUrl = 'http://localhost:5000/predict'; // Adjust the URL as needed

  constructor(
    private http: HttpClient
  ) { }

  sendMessage(message: string) :Observable<any> {
    return this.http.post<any>(this.apiUrl, { message:message });
  }
}
