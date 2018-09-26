n=int(input('Enter two numbers'))
if(n==i*i):
print('Perfect square')
else:
print('Not perfect square')
 
//Derived Class
class B : A
{
 public void fooB()
 {
 //TO DO:
 }
}
 
//Derived Class
class C : A
{
 public void fooC()
 {
 //TO DO:
 }
}
 
//Derived Class
class D : B, A, C
{
 public void fooD()
 {
 //TO DO:
 }
}
Hierarchical inheritance
In this inheritance, more than one derived classes are created from a single base.

￼
//Base Class
class A
{
 public void fooA()
 
 {
 //TO DO:
 }
}
 
//Derived Class
class B : A
{
 public void fooB()
 {
 //TO DO:
 }
}
 
//Derived Class
class C : A
{
 public void fooC()
 {
 //TO DO:
 }
}
 
//Derived Class
class D : C
{
 public void fooD()
 {
 //TO DO:
 }
}
 
//Derived Class
class E : C
{
 public void fooE()
 {
 //TO DO:
 }
}
 
//Derived Class
class F : B
{
 public void fooF()
 {
 //TO DO:
 }
}
 
//Derived Class
class G :B
{
 public void fooG()
 {
 //TO DO:
 }
}
Hybrid inheritance
This is combination of more than one inheritance. Hence, it may be a combination of Multilevel and Multiple inheritance or Hierarchical and Multilevel inheritance or Hierarchical and Multipath inheritance or Hierarchical, Multilevel and Multiple inheritance.

Since .NET Languages like C#, F# etc. does not support multiple and multipath inheritance. Hence hybrid inheritance with a combination of multiple or multipath inheritance is not supported by .NET Languages.

￼
//Base Class
class A
{
 public void fooA()
 {
 //TO DO:
 }
}
 
//Base Class
class F
{
 public void fooF()
 {
 //TO DO:
 }
}
 
//Derived Class
class B : A, F
{
 public void fooB()
 {
 //TO DO:
 }
}
 
//Derived Class
class C : A
{
 public void fooC()
 {
 //TO DO:
 }
}
 
//Derived Class
class D : C
{
 public void fooD()
 {
 //TO DO:
 }
}
 
//Derived Class
class E : C
{
 public void fooE()
 {
 //TO DO:
 }
}
Advantages of Inheritance
Reduce code redundancy.

Provides code reusability.

Reduces source code size and improves code readability.

Code is easy to manage and divided into parent and child classes.

Supports code extensibility by overriding the base class functionality within child classes.

Disadvantages of Inheritance
In Inheritance base class and child classes are tightly coupled. Hence If you change the code of parent class, it will get affects to the all the child classes.

In class hierarchy many data members remain unused and the memory allocated to them is not utilized. Hence affect performance of your program if you have not implemented inheritance correctly.

What do you think?
I hope you will enjoy the tips while programming with .NET Languages like C#. I would like to have feedback from my blog readers. Your valuable feedback, question, or comments about this article are always welcome.

❮ Prev    Next ❯ 
Hands-on Learning
￼
C# Essentials
63
Lectures
05+
Hours
￼
The Complete ASP.NET MVC5 with AngularJS
78
Lectures
11+
Hours
￼
Project - ASP.NET MVC with Angular
33
Lectures
03+
Hours
Free Interview Books
￼￼￼￼￼
 
Our Popular Courses
The Complete MVC5 with AngularJS 99 49
The Complete AngularJS with WebAPI 99 49
Project - ASP.NET MVC with Angular 99 49
The Complete AWS Solution Architect 99 49
The Complete Xamarin Forms 99 49 Our YouTube Channel
 
￼
 
 
￼
 
￼
Learn. Build. Empower.
Master in-demand job skills with linear and project-based courses. Get access to world class Learning Platform to LEARN the tools and tricks to BUILD industry grade applications under our expert guidance. Our innovative hands-on training approach, will EMPOWER you to take any future assignment with confidence.
PLATFORM
Events
Free eBooks
Skill Challenge
Professional Reviews
Corporate Training
Software Consulting
Technical Recruiting
SUPPORT
Contact Us
Student Scholarship
Become An Instructor
Become An Author
Refer And Earn
Job Openings
Verify Certificate
COMPANY
About Us
Founder
Terms and Conditions
Privacy Policy
Refund Policy
Disclaimer
Sitemap
© 2018 Dot Net Tricks Innovation Pvt. Ltd. All rights Reserved. The course names and logos are the trademarks of their respective owners.

Made with  in India.

