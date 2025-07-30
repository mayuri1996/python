import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { MyServiceService } from '../my-service.service';

@Component({
  selector: 'app-registration',
  templateUrl: './registration.component.html',
  styleUrls: ['./registration.component.css']
})
export class RegistrationComponent {
  registrationForm: FormGroup; // Define your form group here

  constructor(
    private formBuilder: FormBuilder,
    private myServise: MyServiceService // Inject your service here
  ) {
    // Initialize your form group here
    this.registrationForm = this.formBuilder.group({
      username: ['', Validators.required],
      email: ['', [Validators.required, Validators.email]],
      password: ['', [Validators.required, Validators.minLength(6)]],
    });
  }

  get f() {
    return this.registrationForm.controls;
  }

  onSubmit() {
    if (this.registrationForm.valid) {
      let registrationData = {
        name: this.registrationForm.value.username,
        email: this.registrationForm.value.email,
        password: this.registrationForm.value.password
      };
      this.myServise.registration(registrationData).subscribe({
        next: (response) => {
          console.log("Full response:", response);

          if (response.status === 201) {
            alert("✅ Registered successfully");
            this.registrationForm.reset();
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
    } else {
      // Handle form errors
      console.error('Form is invalid');
    }
  }
}
