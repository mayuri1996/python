import { Component } from '@angular/core';
import { MyServiceService } from './my-service.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'ai-ml-angular';

  message: string = '';
  prediction: string = '';

  constructor(private myService: MyServiceService) { }

  sendMessage() {
    this.myService.sendMessage(this.message).subscribe({
      next: (response) => {
        this.prediction = response.prediction; // Assuming the response has a 'prediction' field
      },
      error: (error) => {
        console.error('Error occurred:', error);
        this.prediction = 'Error occurred while fetching prediction.';  
      }
  })
}
}
