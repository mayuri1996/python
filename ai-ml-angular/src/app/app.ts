import { Component, signal } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { Service } from './service';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet,FormsModule],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App {
  message:any;
  prediction:any;

  constructor(private service: Service) {
    // Initialization logic can go here
  }

  getPrediction() {
    this.service.getPrediction(this.message).subscribe((response) => {
      console.log(response);
      this.prediction = response.prediction;
    });
  }
}
