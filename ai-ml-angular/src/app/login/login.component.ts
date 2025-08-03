import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { MyServiceService } from '../my-service.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
   errorMessage: string = '';
   loginForm : FormGroup;


   constructor(private formBuilder: FormBuilder,
    private myServise: MyServiceService // Inject your service here
   ) {
      this.loginForm = this.formBuilder.group({
         username: ['', Validators.required],
         password: ['', Validators.required]
      });
     
   }

   onSubmit() {
      let loginData = {
          email: this.loginForm.value.username,
          password: this.loginForm.value.password 
      }

      this.myServise.login(loginData).subscribe({
         next: (response) => {
            console.log("Full response:", response);

            if (response.status === 201) {
               alert("✅ Login successful");
               this.loginForm.reset();
            } else {
               alert("⚠️ Something else happened: " + response.body?.error);
            }
         },
         error: (error) => {
            console.log("Error status:", error.status);
            console.log("Error body:", error.error);
            alert("❌ " + (error.error?.error || "Unknown error"));
         }
      });
  }
}
