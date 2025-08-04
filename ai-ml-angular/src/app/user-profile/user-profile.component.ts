import { Component } from '@angular/core';
import { MyServiceService } from '../my-service.service';

@Component({
  selector: 'app-user-profile',
  templateUrl: './user-profile.component.html',
  styleUrls: ['./user-profile.component.css']
})
export class UserProfileComponent {
  details: any;
   constructor(
    private myService: MyServiceService // Inject your service here
   ){}

   ngOnInit() {
      this.getProfile();
   }

   getProfile() {
    
    this.myService.userProfile().subscribe({
      next: (response) => {
         console.log(response);
         this.details = response.body.data;
      }
    })
   }
}
