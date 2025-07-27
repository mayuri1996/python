import { Component } from '@angular/core';
import { Service } from './service';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [FormsModule,CommonModule],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App {
  message: string = '';
  prediction: string = '';
  isLoading: boolean = false;
  error: boolean = false;

  constructor(private _service:Service) {}

  getPrediction() {
    this.isLoading = true;
    this.error = false;

    this._service.getPrediction(this.message).subscribe(
      (response) => {
        this.isLoading = false;
        this.prediction = response.prediction;
      },
      (err) => {
        this.isLoading = false;
        this.error = true;
        console.error('Prediction error:', err);
      }
    );
  }
}
