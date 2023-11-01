import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AuthServiceLogin } from '../../services/auth.service.login';
import { MatSnackBar } from '@angular/material/snack-bar';
import { User } from '../../models/user';


@Component({
  selector: 'app-forget-password',
  templateUrl: './forget-password.component.html',
  styleUrls: ['./forget-password.component.css']
})
export class ForgetPasswordComponent implements OnInit {
  userModal = new User();
  isLoading: boolean = false;
  mailStatus: string = '';
  mailSent: boolean = false;

  constructor(
    private router: Router,
    private authService: AuthServiceLogin,
    private snackBar: MatSnackBar,
  ) { }

  ngOnInit() {
    this.isLoading = false;
  }

  onForgotPasswordSubmit() {
    this.isLoading = true;
    this.authService.forgotPassword(this.userModal['email']).subscribe(data => {
      this.isLoading = false;
      if (data == 'success') {
        this.mailStatus = 'We have sent the new password to your registered email';
        this.mailSent = true;
      }
      else {
        this.mailStatus = "Email doesn't exist.Please enter the registered email";
        this.mailSent = false;
      }

      setTimeout(() => {
          this.mailStatus = '';
          if (data == 'success')
            this.showLoginPage();
      }, 8000);
    })
  }

  showLoginPage() {
    this.router.navigate(['']);
  }
}
