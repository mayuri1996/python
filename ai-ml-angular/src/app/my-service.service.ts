import { HttpClient, HttpResponse } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class MyServiceService {

  private apiUrl = 'http://localhost:5000/predict'; // Adjust the URL as needed
  private registrationUrl = 'http://localhost:5000/auth/register'; // Adjust the URL as needed
  private loginUrl = 'http://localhost:5000/auth/login'; // Adjust the URL as needed

  constructor(
    private http: HttpClient
  ) { }

  sendMessage(message: string) :Observable<any> {
    return this.http.post<any>(this.apiUrl, { message:message ,user_name:'Mayuri Jadhav'});
  }

  registration(registrationData: any): Observable<HttpResponse<any>> {
    const registrationUrl = this.registrationUrl; // Adjust the URL as needed
    return this.http.post<any>(registrationUrl, registrationData, {
    observe: 'response'  // for full response status code and all
  });
  }

  login(loginData: any): Observable<HttpResponse<any>> {
    const loginUrl = this.loginUrl; // Adjust the URL as needed
    return this.http.post<any>(loginUrl, loginData, {
    observe: 'response'  // // for full response status code and all
  });
  }
}
