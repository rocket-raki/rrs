from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render, redirect
from .models import ContactFormSubmission
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def home(request):
    css= '''
/* Reset and Universal Styles */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}
body {
  font-family: Arial, sans-serif;
  line-height: 1.6;
  margin: 0;
  padding: 0;
  background-color: #f4f4f9;
  color: #333;
}   


/* Header Styling */
header {
    background-color: #333;
    color: #fff;
    padding: 2rem 0;
    text-align: center;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    margin-bottom: 2rem;
}

header h1 {
    font-size: 2rem;
    margin-bottom: 0.5rem;
}

header p {
    font-size: 1.1rem;
    font-weight: 300;
}

/* Main Content Area */
main {
    width: 90%;
    max-width: 800px;
    margin: 2rem auto;
    display: flex;
    flex-direction: column;
    gap: 1.5rem; /* Consistent spacing between posts */
}

/* Post Styling */
.post {
    background: #fff;
    padding: 2rem;
    border-radius: 8px;
    box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s ease, box-shadow 0.3s ease; /* Add smooth hover effect */
}

.post:hover {
    transform: translateY(-5px);
    box-shadow: 0 0 25px rgba(0, 0, 0, 0.2);
}

.post h2 {
    color: #333;
    font-size: 1.5rem;
    margin-bottom: 0.5rem;
}

.post .date {
    color: #777;
    font-size: 0.9rem;
    margin-bottom: 1rem;
}

.post p {
    font-size: 1rem;
    line-height: 1.7;
    margin-bottom: 1rem;
}

/* Read More Link */
.read-more {
    color: #007bff;
    font-weight: bold;
    text-decoration: none;
    transition: color 0.3s ease;
}

.read-more:hover {
    color: #0056b3;
    text-decoration: underline;
}

/* Footer Styling */
footer {
    text-align: center;
    padding: 1rem 0;
    color: #777;
    font-size: 0.9rem;
    margin-top: 2rem;
}

/* Responsive Media Queries */
@media (max-width: 600px) {
    header h1 {
        font-size: 1.8rem;
    }
    
    .post {
        padding: 1.5rem;
    }

    .post h2 {
        font-size: 1.3rem;
    }

    .post p {
        font-size: 0.95rem;
    }
}
'''
    
    context = {
        'css':css,
        'blogname':'Rare Syntax',
        'tagline':'Thoughts, Stories, and Ideas',
        'posts' : [
        {'blogtitle': 'Python', 'date': 'November 14, 2024', 'description': 'An introductory guide to Python programming and its applications.'},
        {'blogtitle': 'Java', 'date': 'November 13, 2024', 'description': 'Explore Java and its versatility in building cross-platform applications.'},
        {'blogtitle': 'JavaScript', 'date': 'November 12, 2024', 'description': 'Learn about JavaScript, the backbone of web development.'},
        {'blogtitle': 'Django', 'date': 'November 11, 2024', 'description': 'Django makes web development easy and efficient. Here’s how!'},
        {'blogtitle': 'Machine Learning', 'date': 'November 10, 2024', 'description': 'Introduction to machine learning concepts and algorithms.'},
        {'blogtitle': 'Data Science', 'date': 'November 9, 2024', 'description': 'Dive into data science, from data analysis to visualization.'},
        {'blogtitle': 'React', 'date': 'November 8, 2024', 'description': 'Build interactive UIs with React, a popular JavaScript library.'},
        {'blogtitle': 'Flask', 'date': 'November 7, 2024', 'description': 'Learn Flask, a lightweight web framework for Python developers.'},
        {'blogtitle': 'SQL', 'date': 'November 6, 2024', 'description': 'Understand the basics of SQL for database management.'}
    ]
    }
    html_content = '''
        <style>{{css}}</style>
        <header>
        <h1>Welcome to {{blogname}}</h1>
        <p>{{tagline}}</p>
    </header>
    
    <main>
    {% for post in posts %}
        <article class="post">
            <h2>{{post.blogtitle}}</h2>
            <p class="date">{{post.date}}</p>
            <p>{{post.description}}</p>
            <a href="#" class="read-more">Read More</a>
        </article>
    {% endfor %}

        
        
       
    </main>
    
    '''

   
    code = Template(html_content).render(Context(context))
    return render(request, "index.html", {"code": code})




def about(request):
    css = '''/* Global Styles */
body {
  font-family: 'Inter', Arial, sans-serif; /* Sleek and modern font */
  background-color: #fafafa; /* Light background */
  color: #333; /* Dark text for readability */
  margin: 0;
  padding: 0;
  line-height: 1.8;
  font-size: 16px;
}

/* About Section */
.about {
  background-color: #ffffff;
  padding: 5rem 2rem;
  text-align: center;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.1); /* Soft shadow for depth */
  border-radius: 18px; /* Rounded corners */
  margin: 2rem auto;
  max-width: 1100px;
  transition: box-shadow 0.3s ease;
}

.about:hover {
  box-shadow: 0 12px 48px rgba(0, 0, 0, 0.12);
}

/* Heading Styles */
.about h1 {
  font-size: 3.8rem;
  font-weight: 800;
  margin-bottom: 1rem;
  color: #222;
  text-transform: uppercase;
  letter-spacing: 2px;
  padding-bottom: 0.8rem;
  border-bottom: 3px solid #00c3ff; /* Bright modern color */
  display: inline-block;
}

.about h2 {
  font-size: 2.4rem;
  margin-top: 4rem;
  font-weight: 700;
  color: #444;
  margin-bottom: 1.5rem;
  text-transform: capitalize;
  letter-spacing: 1.2px;
  border-bottom: 2px solid #f0f0f0;
  padding-bottom: 0.5rem;
  display: inline-block;
}

/* Paragraph Styling */
.about p {
  font-size: 1.2rem;
  line-height: 1.9;
  color: #666;
  margin-bottom: 3rem;
  max-width: 900px;
  margin-left: auto;
  margin-right: auto;
  letter-spacing: 0.8px;
  opacity: 0.9;
  transition: opacity 0.3s ease;
}

.about p:hover {
  opacity: 1;
}

/* List Styling */
.about ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.about ul li {
  font-size: 1.2rem;
  color: #444;
  margin-bottom: 1.8rem;
  line-height: 1.9;
  padding-left: 2.5rem;
  position: relative;
  font-weight: 600;
}

.about ul li::before {
  content: '✓';
  position: absolute;
  left: 0;
  color: #00c3ff; /* Modern cyan accent */
  font-size: 1.8rem;
  top: 50%;
  transform: translateY(-50%);
}

.about ul li strong {
  color: #333;
  font-weight: 700;
  letter-spacing: 0.5px;
}

/* Link Styling */
.about a {
  color: #00c3ff; /* Bright link color */
  text-decoration: none;
  font-weight: 600;
  transition: color 0.3s ease, transform 0.3s ease;
}

.about a:hover {
  color: #ff6347; /* Bright red for hover */
  text-decoration: underline;
  transform: translateY(-2px); /* Slight move for interaction */
}

/* Card Style for "Our Team" Section */
.card {
  background-color: #ffffff;
  color: #333;
  padding: 3rem;
  border-radius: 18px;
  margin-bottom: 4rem;
  box-shadow: 0 10px 36px rgba(0, 0, 0, 0.08);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  cursor: pointer;
  max-width: 500px;
  margin-left: auto;
  margin-right: auto;
}

.card:hover {
  transform: translateY(-8px);
  box-shadow: 0 12px 48px rgba(0, 0, 0, 0.12);
}

.card h3 {
  font-size: 1.8rem;
  margin-bottom: 1.5rem;
  color: #212121;
  font-weight: 700;
}

.card p {
  font-size: 1.1rem;
  color: #777;
  line-height: 1.8;
}

/* Dark Mode Footer */
.footer {
  background-color: #1e1e1e; /* Dark footer */
  color: #e0e0e0; /* Light gray text for contrast */
  padding: 3rem 0;
  text-align: center;
  margin-top: 5rem;
  box-shadow: 0 -6px 18px rgba(0, 0, 0, 0.1);
}

.footer .footer-credit {
  font-size: 1rem;
  color: #e0e0e0;
  margin-top: 1.5rem;
}

.footer .footer-credit a {
  color: #1eff7c; /* Neon green accent */
  text-decoration: none;
  font-weight: 600;
  transition: color 0.3s ease, transform 0.3s ease;
}

.footer .footer-credit a:hover {
  color: #ffcc00; /* Vibrant yellow on hover */
  text-decoration: underline;
  transform: translateY(-1px); /* Interactive hover effect */
}

/* Responsive Design */
@media (max-width: 768px) {
  .about h1 {
    font-size: 2.8rem;
  }

  .about p {
    font-size: 1rem;
  }

  .about ul li {
    font-size: 1rem;
  }

  .card {
    padding: 2rem;
  }

  .about {
    padding: 4rem 1.5rem;
  }
}

'''
    html_content = '''<style>{{ css|safe }}</style>

<!-- About Section -->
<section class="about">
  <div class="container">
    <h1>About RARE SYNTAX</h1>
    <p>RARE SYNTAX is a platform dedicated to providing high-quality tech education in various programming languages. We focus on empowering learners with the skills they need to succeed in the ever-evolving world of software development.</p>

    <h2>Our Mission</h2>
    <p>Our mission is to bridge the knowledge gap in the tech industry by providing affordable and accessible education. Whether you're just starting your coding journey or looking to expand your skills, we offer comprehensive courses that cater to all levels of learners.</p>

    <h2>What We Offer</h2>
    <p>We specialize in offering courses in:</p>
    <ul>
      <li><strong>Python</strong> – Learn one of the most versatile programming languages used in data science, web development, and automation.</li>
      <li><strong>JavaScript</strong> – Master the language of the web, from front-end development to back-end frameworks like Node.js.</li>
      <li><strong>Django</strong> – Dive into web development with one of the most popular Python frameworks for building robust applications.</li>
    </ul>

    <h2>Why Choose Us?</h2>
    <p>At RARE SYNTAX, we offer a unique approach to learning that combines theory with practical, real-world projects. Our courses are designed to make learning engaging and interactive, helping you retain knowledge and build confidence in your coding skills.</p>

    <h2>Our Team</h2>
    <p>RARE SYNTAX was founded by passionate tech enthusiasts with years of experience in the software industry. Our team is committed to providing the best learning experience, tailored to meet the needs of both beginners and advanced learners.</p>

    <h2>Contact Us</h2>
    <p>If you have any questions or need further information about our courses, feel free to reach out to us:</p>
    <ul>
      <li>Email: <a href="mailto:raresyntax@gmail.com">raresyntax@gmail.com</a></li>
      <li>Phone: +91 9731383927</li>
      <li>Website: <a href="http://www.raresyntax.in">www.raresyntax.in</a></li>
    </ul>
  </div>
</section>

'''
    context={
        'title':'about',
        'css':css
    }
    code = Template(html_content).render(Context(context))
    return render(request, "index.html", {"code": code})





@csrf_exempt
def contact(request):
    # Define CSS content
    css = '''/* Global Styles */
* {
  box-sizing: border-box;
}

body {
  font-family: 'Helvetica Neue', sans-serif;
  background-color: #e9ecef;
  margin: 0;
  padding: 0;
  color: #495057;
}

h1, h2 {
  margin: 0;
  padding: 0;
}

/* Contact Section */
.contact {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background-color: #f8f9fa;
  padding: 30px;
}

.container {
  max-width: 850px;
  width: 100%;
  background-color: #ffffff;
  box-shadow: 0 6px 30px rgba(0, 0, 0, 0.1);
  border-radius: 12px;
  padding: 40px;
}

/* Title */
.contact h1 {
  font-size: 2.2rem;
  color: #007b5e;
  margin-bottom: 20px;
  font-weight: 700;
  text-align: center;
}

/* Contact Form */
.contact-form {
  display: grid;
  gap: 20px;
}

.contact-form h2 {
  font-size: 1.8rem;
  color: #007b5e;
  font-weight: 700;
  margin-bottom: 20px;
  text-align: center;
  border-bottom: 2px solid #007b5e;
  padding-bottom: 10px;
}

/* Form Fields */
.form-group {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.form-group label {
  font-weight: 600;
  color: #333;
}

.form-group input,
.form-group textarea,
.form-group select {
  width: 100%;
  padding: 14px;
  border-radius: 8px;
  border: 2px solid #ced4da;
  background-color: #f8f9fa;
  font-size: 1rem;
  transition: border-color 0.3s ease, box-shadow 0.3s ease;
}

.form-group input:focus,
.form-group textarea:focus,
.form-group select:focus {
  border-color: #007b5e;
  outline: none;
  box-shadow: 0 0 8px rgba(0, 123, 94, 0.3);
}

/* Textarea */
.form-group textarea {
  resize: vertical;
  min-height: 120px;
}

/* Checkbox Group */
.checkbox-group {
  display: flex;
  flex-wrap: wrap;
  gap: 15px;
  font-size: 1rem;
  color: #495057;
}

.checkbox-group label {
  font-weight: normal;
  margin: 0;
  padding: 0;
}

.checkbox-group input {
  margin-right: 10px;
}

/* Submit Button */
.submit-btn {
  padding: 14px 20px;
  font-size: 1.1rem;
  color: #fff;
  background-color: #007b5e;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: background-color 0.3s ease, transform 0.3s ease;
  width: 100%;
  margin-top: 20px;
}

.submit-btn:hover {
  background-color: #006c4e;
  transform: scale(1.05);
}

.submit-btn:active {
  background-color: #005742;
}

/* Success/Error Message */
.message {
  font-size: 1rem;
  color: #28a745;
  margin-top: 20px;
}

.message.error {
  color: #dc3545;
}

/* Responsive Design */
@media (max-width: 768px) {
  .contact-form {
    gap: 15px;
  }

  .submit-btn {
    width: 100%;
  }
}

@media (max-width: 480px) {
  .container {
    padding: 20px;
  }

  .contact h1 {
    font-size: 1.8rem;
  }

  .contact-form h2 {
    font-size: 1.5rem;
  }
}

    '''
    html_content = '''
<div class="contact">
  <div class="container">
    <h1>Contact Us</h1>
    <form class="contact-form" action="{% url 'contact' %}" method="POST">
      {% csrf_token %}
      <h2>Send Us a Message</h2>

      <!-- Name Field -->
      <div class="form-group">
        <label for="full-name">Full Name</label>
        <input type="text" id="full-name" name="full-name" placeholder="Enter your full name" required>
      </div>

      <!-- Email Field -->
      <div class="form-group">
        <label for="email">Email Address</label>
        <input type="email" id="email" name="email" placeholder="you@example.com" required>
      </div>

      <!-- Phone Field -->
      <div class="form-group">
        <label for="phone">Phone Number</label>
        <input type="tel" id="phone" name="phone" placeholder="+91 123 456 7890" required>
      </div>

      <!-- Subject Field -->
      <div class="form-group">
        <label for="subject">Subject</label>
        <input type="text" id="subject" name="subject" placeholder="Subject of your message" required>
      </div>

      <!-- Inquiry Type -->
      <div class="form-group">
        <label for="inquiry-type">Inquiry Type</label>
        <select id="inquiry-type" name="inquiry-type" required>
          <option value="">Select a category</option>
          <option value="general">General Inquiry</option>
          <option value="support">Support</option>
          <option value="course-info">Course Information</option>
          <option value="feedback">Feedback</option>
          <option value="other">Other</option>
        </select>
      </div>

      <!-- Message Field -->
      <div class="form-group">
        <label for="message">Message</label>
        <textarea id="message" name="message" rows="5" placeholder="Write your message here..." required></textarea>
      </div>

      <!-- Preferred Contact Method -->
      <div class="form-group">
        <label>Preferred Contact Method:</label>
        <div class="checkbox-group">
          <label><input type="checkbox" name="contact-method" value="email"> Email</label>
          <label><input type="checkbox" name="contact-method" value="phone"> Phone</label>
          <label><input type="checkbox" name="contact-method" value="sms"> SMS</label>
        </div>
      </div>

      <!-- Preferred Contact Time -->
      <div class="form-group">
        <label for="contact-time">Preferred Contact Time</label>
        <input type="time" id="contact-time" name="contact-time">
      </div>

      <!-- Submit Button -->
      <button type="submit" class="submit-btn">Send Message</button>
    </form>
  </div>
</div>


'''
    if request.method == 'POST':
    # CSRF token will be verified automatically here
        full_name = request.POST.get('full-name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        inquiry_type = request.POST.get('inquiry-type')
        message = request.POST.get('message')
        preferred_contact_method = request.POST.getlist('contact-method')
        preferred_contact_time = request.POST.get('contact-time')

    # Save form data
        contact_submission = ContactFormSubmission(
           full_name=full_name,
           email=   email,
           phone=phone,
           subject=subject,
           inquiry_type=inquiry_type,
           message=message,
           preferred_contact_method=", ".join(preferred_contact_method),
           preferred_contact_time=preferred_contact_time
           )
        contact_submission.save()

    # Redirect after saving
        return redirect('contact') 

    # Passing the context to the template
    context = {
        'title': 'Contact Us',
        'css': css
    }


    context={
        'title':'contact',
        'css':css
    }
    code = Template(html_content).render(Context(context))
    return render(request, "index.html", {"code": code})





  
def gallery(request):
    css = ''' 
    /* Gallery Section */
.gallery {
  padding: 3rem 2rem;
  background-color: #f0f0f0;  /* Light gray background */
  text-align: center;
}

.gallery .container {
  max-width: 1200px;
  margin: 0 auto;
}

.gallery h1 {
  font-size: 2.4rem;
  margin-bottom: 1rem;
  color: #4caf50;  /* Green for headings */
}

.gallery p {
  font-size: 1.2rem;
  margin-bottom: 2rem;
  color: #555;
}

.gallery-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 1.5rem;
}

.gallery-item {
  position: relative;
  overflow: hidden;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

.gallery-item img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.3s ease;
}

.gallery-item:hover img {
  transform: scale(1.1); /* Zoom in on hover */
}

.overlay {
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  background-color: rgba(0, 0, 0, 0.6); /* Dark overlay */
  opacity: 0;
  transition: opacity 0.3s ease;
  display: flex;
  justify-content: center;
  align-items: center;
}

.overlay .text {
  font-size: 1.5rem;
  color: white;
  text-transform: uppercase;
  font-weight: bold;
}

.gallery-item:hover .overlay {
  opacity: 1;
}

/* Responsive Design */
@media (max-width: 768px) {
  .gallery h1 {
    font-size: 2rem;
  }

  .gallery p {
    font-size: 1rem;
  }

  .gallery-grid {
    grid-template-columns: 1fr 1fr;
  }
}

  '''

    html_content = '''

    <style>{{css}}</style>
            <section class="gallery">
  <div class="container">
    <h1>Our Gallery</h1>
    <p>Explore our gallery to see the projects, events, and achievements that showcase the work we've done and the community we've built.</p>

    <div class="gallery-grid">
      <!-- Image 1 -->
      <div class="gallery-item">
        <img src="https://img.freepik.com/premium-photo/people-working-office_1048944-29352029.jpg" alt="Image 1">
        <div class="overlay">
          <div class="text">Office</div>
        </div>
      </div>

      <!-- Image 2 -->
      <div class="gallery-item">
        <img src="https://img.freepik.com/free-photo/modern-equipped-computer-lab_23-2149241219.jpg?semt=ais_hybrid" alt="Image 2">
        <div class="overlay">
          <div class="text">Christene Phalmer - Software Developer</div>
        </div>
      </div>

      <!-- Image 3 -->
      <div class="gallery-item">
        <img src="https://nxtide.com/wp-content/uploads/2022/02/Offshore-Development-Center-Services-Poland-2-scaled.jpg" alt="Image 3">
        <div class="overlay">
          <div class="text">Jane Foster - Team Manager</div>
        </div>
      </div>

      <!-- Add more gallery items as needed -->
    </div>
  </div>
</section>

   '''
    context={
        'title':'gallery',
        'css':css
    }
    code = Template(html_content).render(Context(context))
    return render(request, "index.html", {"code": code})
    


def reviews(request):
    css = ''' 
/* Reviews Section */
.reviews {
  padding: 3rem 2rem;
  background-color: #f8f8f8;  /* Light gray background */
  text-align: center;
}

.reviews .container {
  max-width: 1200px;
  margin: 0 auto;
}

.reviews h1 {
  font-size: 2.5rem;
  margin-bottom: 1rem;
  color: #4caf50;  /* Green for headings */
}

.reviews p {
  font-size: 1.2rem;
  margin-bottom: 2rem;
  color: #555;
}

.reviews-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 1.5rem;
}

.review-item {
  background-color: #fff;
  padding: 2rem;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  text-align: left;
  transition: transform 0.3s ease;
}

.review-item:hover {
  transform: translateY(-10px); /* Lift effect on hover */
}

.review-img {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  object-fit: cover;
  margin-bottom: 1rem;
}

.review-content h3 {
  font-size: 1.4rem;
  font-weight: bold;
  color: #333;
  margin-bottom: 0.5rem;
}

.review-content p {
  font-size: 1rem;
  color: #777;
  margin-bottom: 1rem;
}

.rating span {
  color: #ff9800; /* Gold color for stars */
  font-size: 1.2rem;
}

/* Responsive Design */
@media (max-width: 768px) {
  .reviews h1 {
    font-size: 2rem;
  }

  .reviews p {
    font-size: 1rem;
  }

  .reviews-grid {
    grid-template-columns: 1fr 1fr;
  }

  .review-item {
    padding: 1.5rem;
  }
}


'''
    html_content = '''
    <style>{{css}}</style>
<section class="reviews">
  <div class="container">
    <h1>What Our Students Say</h1>
    <p>We believe in the power of feedback to help us grow and improve. Here are some reviews from our students who have benefited from our courses.</p>

    <div class="reviews-grid">
      <!-- Review 1 -->
      <div class="review-item">
        <img src="https://img.freepik.com/premium-photo/montenegro-stylish-high-school-student-classroom-8k-realistic-photo-modern-youth-culture_1161356-76693.jpg" alt="Student 1" class="review-img">
        <div class="review-content">
          <h3>John Doe</h3>
          <p>"RARE SYNTAX has transformed my coding skills. The Python course helped me land my first job as a software developer!"</p>
          <div class="rating">
            <span>&#9733;&#9733;&#9733;&#9733;&#9733;</span> <!-- 5 stars -->
          </div>
        </div>
      </div>

      <!-- Review 2 -->
      <div class="review-item">
        <img src="https://img.freepik.com/premium-photo/young-smiling-student-woman-holds-books-while-looking-camera-white-background-education_136403-15774.jpg" alt="Student 2" class="review-img">
        <div class="review-content">
          <h3>Jane Smith</h3>
          <p>"The JavaScript course was incredibly detailed and practical. I now feel confident building full-stack applications."</p>
          <div class="rating">
            <span>&#9733;&#9733;&#9733;&#9733;&#9734;</span> <!-- 4 stars -->
          </div>
        </div>
      </div>

      <!-- Review 3 -->
      <div class="review-item">
        <img src="https://www.shutterstock.com/image-photo/image-happy-beautiful-student-girl-600nw-1824708863.jpg" alt="Student 3" class="review-img">
        <div class="review-content">
          <h3>Emily Johnson</h3>
          <p>"I loved the Django course! The hands-on projects were extremely helpful in applying the concepts learned in real-world scenarios."</p>
          <div class="rating">
            <span>&#9733;&#9733;&#9733;&#9733;&#9733;</span> <!-- 5 stars -->
          </div>
        </div>
      </div>

      <!-- More reviews can be added as needed -->
    </div>
  </div>
</section>

 '''
    
    
    
    context={
        'title':'about',
        'css':css
    }
    code = Template(html_content).render(Context(context))
    return render(request, "index.html", {"code": code})











def courses(request):
    css ='''
/* Courses Section */
.courses {
  padding: 3rem 2rem;
  background-color: #f4f4f9;
  color: #333;
}

.courses .container {
  max-width: 1000px;
  margin: 0 auto;
  padding: 0 2rem;
}

.courses h1 {
  font-size: 2.4rem;
  text-align: center;
  margin-bottom: 1rem;
  color: #4caf50; /* Bright color for headings */
}

.courses p {
  font-size: 1.2rem;
  text-align: center;
  margin-bottom: 3rem;
  color: #555;
}

.course-list {
  display: flex;
  flex-wrap: wrap;
  gap: 2rem;
  justify-content: center;
}

.course {
  background-color: #fff;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  width: 30%;
  transition: all 0.3s ease;
  overflow: hidden;
}

.course:hover {
  transform: translateY(-5px);
}

.course-image img {
  width: 100%;
  height: auto;
}

.course-content {
  padding: 1.5rem;
  text-align: center;
}

.course-content h2 {
  font-size: 1.6rem;
  margin-bottom: 1rem;
  color: #333;
}

.course-content p {
  font-size: 1.1rem;
  margin-bottom: 1.5rem;
  color: #666;
}

.btn {
  background-color: #d23c77;
  color: #fff;
  padding: 0.8rem 1.5rem;
  text-decoration: none;
  font-weight: bold;
  border-radius: 4px;
  transition: background-color 0.3s ease;
}

.btn:hover {
  background-color: #b42f6e;
}

/* Responsive Design */
@media (max-width: 768px) {
  .course {
    width: 100%;
  }

  .courses h1 {
    font-size: 2rem;
  }

  .courses p {
    font-size: 1rem;
  }
}
'''
    html_content='''
    <style>{{css}}</style>
    
    <section class="courses">
  <div class="container">
    <h1>Our Courses</h1>
    <p>Explore our range of comprehensive courses designed to help you succeed in the tech industry. Whether you're a beginner or an advanced learner, we have something for everyone.</p>

    <div class="course-list">
      <!-- Course 1: Python -->
      <div class="course">
        <div class="course-image">
          <img src="https://bigblue.academy/images/image/blog/python-courses/204.jpg" alt="Python Course">
        </div>
        <div class="course-content">
          <h2>Python for Beginners</h2>
          <p>Learn the basics of Python programming. From syntax to libraries, this course covers everything you need to get started with Python.</p>
          <a href="/courses/python/" class="btn">Learn More</a>
        </div>
      </div>
      <!-- Course 2: JavaScript -->
      <div class="course">
        <div class="course-image">
          <img src="https://img-c.udemycdn.com/course/480x270/5422984_16fc_2.jpg" alt="JavaScript Course">
        </div>
        <div class="course-content">
          <h2>JavaScript for Web Development</h2>
          <p>Master JavaScript and learn how to build dynamic websites. This course covers everything from basics to advanced JavaScript techniques.</p>
          <a href="/courses/javascript/" class="btn">Learn More</a>
        </div>
      </div>

      <!-- Course 3: Django -->
      <div class="course">
        <div class="course-image">
          <img src="https://www.creative-tim.com/blog/content/images/2021/09/cover-ct-django-cheat-sheet.png" alt="Django Course">
        </div>
        <div class="course-content">
          <h2>Django for Web Development</h2>
          <p>Learn Django, one of the most popular web frameworks for Python. This course teaches you how to build powerful, secure web applications.</p>
          <a href="/courses/django" class="btn">Learn More</a>
        </div>
      </div>

      <!-- Add more courses as needed -->
    </div>
  </div>
</section>
''' 
    context={
        'title':'courses',
        'css':css
    }
    code = Template(html_content).render(Context(context))
    return render(request, "index.html", {"code": code})

  



def course(request, course):
    css = ''' 
    /* General Reset */
    *,
    *::before,
    *::after {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }

    body {
        font-family: Arial, sans-serif;
        background-color: #f4f4f9;
        color: #333;
    }

    /* Header Styles */
    header {
        background-color: #306998;  /* Python Blue */
        color: #fff;
        padding: 2rem 0;
        text-align: center;
    }

    header h1 {
        font-size: 2.5rem;
        margin-bottom: 0.5rem;
    }

    header p {
        font-size: 1.1rem;
        font-weight: 300;
    }

    /* Main Content */
    main {
        width: 90%;
        max-width: 1200px;
        margin: 3rem auto;
        display: flex;
        flex-direction: column;
        gap: 2rem;
    }

    /* Course Container */
    .course-container {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
        gap: 2rem;
        margin-top: 2rem;
    }

    /* Individual Course Card */
    .course-card {
        background-color: #fff;
        padding: 1.5rem;
        border-radius: 8px;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }

    .course-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
    }

    .course-card img {
        width: 100%;
        border-radius: 8px;
        object-fit: cover;
        height: 200px;
        margin-bottom: 1rem;
    }

    .course-info h2 {
        font-size: 1.5rem;
        color: #333;
        margin-bottom: 0.5rem;
    }

    .course-info p {
        font-size: 1rem;
        color: #666;
        margin-bottom: 1rem;
        line-height: 1.5;
    }

    .btn {
        padding: 0.55rem 0.75rem;
        font-size: 1.1rem;
        background-color: #306998; /* Python Blue */
        color: #fff;
        text-decoration: none;
        border-radius: 5px;
        text-align: center;
        display: inline-block;
        transition: background-color 0.3s ease;
    }

    .btn:hover {
        background-color: #27627d; /* Darker Python Blue */
    }

    /* Footer Styles */
    footer {
        text-align: center;
        padding: 1rem;
        background-color: #333;
        color: #fff;
        font-size: 0.9rem;
        margin-top: 3rem;
    }

    /* Media Queries for Responsiveness */
    @media (max-width: 768px) {
        header h1 {
            font-size: 2rem;
        }

        .course-container {
            grid-template-columns: 1fr 1fr;
        }

        .course-card img {
            height: 180px;
        }
    }

    @media (max-width: 480px) {
        header h1 {
            font-size: 1.5rem;
        }

        .course-container {
            grid-template-columns: 1fr;
        }

        .course-card img {
            height: 160px;
        }
    }
    '''

    # Dummy course data (to be replaced with database in a real app)
    courses = {
        "python": {
            "title": "Python Programming",
            "description": "Learn the basics and advanced concepts of Python programming. This course will take you from beginner to expert, covering everything from syntax to building real-world applications.",
            "image": "https://bigblue.academy/images/image/blog/python-courses/204.jpg ",
        },
        "javascript": {
            "title": "JavaScript for Web Development",
            "description": "Master JavaScript and create interactive websites. This course covers both the fundamentals and advanced techniques for modern web development.",
            "image": "https://img-c.udemycdn.com/course/480x270/5422984_16fc_2.jpg ",
        },
        "django": {
            "title": "Django for Web Development",
            "description": "Learn how to build dynamic, secure, and scalable web applications using Django. This course teaches you the power of Python-based web development.",
            "image": "https://www.creative-tim.com/blog/content/images/2021/09/cover-ct-django-cheat-sheet.png",
        },
    }

    # Check if the course exists
   


    html_content = '''
    <style>{{css}}</style>

    <header>
        <div class="container">
            <h1>{{ course.title }}</h1>
            <p>{{ course.description }}</p>
        </div>
    </header>

    <main>
        <section class="course-container">
            <div class="course-card">
                <img src="{{ course.image }}" alt="{{ course.title }}">
                <div class="course-info">
                    <h2>{{ course.title }}</h2>
                    <p>{{ course.description }}</p>
                    <a href="beginner/" class="btn">Beginner</a>
                    <a href="intermediate/" class="btn">Intermediate</a>
                    <a href="advanced/" class="btn">Advanced</a>
                </div>
            </div>
        </section>
    </main>
    '''

    # Context to pass to the template
    
    context={
        'title':'gallery',
        'css':css,
        'course':courses[course]
    }
    code = Template(html_content).render(Context(context))
    return render(request, "index.html", {"code": code})
    




def course_learn(request, course_name, course_level):
    css = ''' 
    /* General Reset */
    *,
    *::before,
    *::after {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }

    body {
        font-family: Arial, sans-serif;
        background-color: #f4f4f9;
        color: #333;
    }

    /* Header Styles */
    header {
        background-color: #306998;  /* Python Blue */
        color: #fff;
        padding: 2rem 0;
        text-align: center;
    }

    header h1 {
        font-size: 2.5rem;
        margin-bottom: 0.5rem;
    }

    header p {
        font-size: 1.1rem;
        font-weight: 300;
    }

    /* Main Content */
    main {
        width: 90%;
        max-width: 1200px;
        margin: 3rem auto;
        display: flex;
        flex-direction: column;
        gap: 2rem;
    }

    /* Course Container */
    .course-container {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
        gap: 2rem;
        margin-top: 2rem;
    }

    /* Individual Course Card */
    .course-card {
        background-color: #fff;
        padding: 1.5rem;
        border-radius: 8px;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }

    .course-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
    }

    .course-card img {
        width: 100%;
        border-radius: 8px;
        object-fit: cover;
        height: 200px;
        margin-bottom: 1rem;
    }

    .course-info h2 {
        font-size: 1.5rem;
        color: #333;
        margin-bottom: 0.5rem;
    }

    .course-info p {
        font-size: 1rem;
        color: #666;
        margin-bottom: 1rem;
        line-height: 1.5;
    }

    .btn {
        padding: 0.75rem 1.5rem;
        font-size: 1.1rem;
        background-color: #306998; /* Python Blue */
        color: #fff;
        text-decoration: none;
        border-radius: 5px;
        text-align: center;
        display: inline-block;
        transition: background-color 0.3s ease;
    }

    .btn:hover {
        background-color: #27627d; /* Darker Python Blue */
    }

    /* Footer Styles */
    footer {
        text-align: center;
        padding: 1rem;
        background-color: #333;
        color: #fff;
        font-size: 0.9rem;
        margin-top: 3rem;
    }

    /* Media Queries for Responsiveness */
    @media (max-width: 768px) {
        header h1 {
            font-size: 2rem;
        }

        .course-container {
            grid-template-columns: 1fr 1fr;
        }

        .course-card img {
            height: 180px;
        }
    }

    @media (max-width: 480px) {
        header h1 {
            font-size: 1.5rem;
        }

        .course-container {
            grid-template-columns: 1fr;
        }

        .course-card img {
            height: 160px;
        }
    }
    '''

    # Course data for different levels and courses (Python, JavaScript, Django)
    courses = {
        "python": {
            "beginner": {
                "title": "Python for Beginners",
                "description": "Learn the basics of Python programming. This course will cover syntax, basic libraries, and getting started with programming.",
                "image": "https://goedu.ac/wp-content/uploads/2021/11/Python-for-beginners.png",
            },
            "intermediate": {
                "title": "Intermediate Python",
                "description": "Take your Python skills to the next level with topics like object-oriented programming (OOP), file handling, and more advanced libraries.",
                "image": "https://blob.sololearn.com/assets/python-intermediate-web-og-v1.png",
            },
            "advanced": {
                "title": "Advanced Python",
                "description": "Dive deep into Python's advanced features like decorators, generators, multi-threading, and building efficient algorithms.",
                "image": "https://purpletutor.com/wp-content/uploads/2023/02/advance-python.jpeg",
            },
        },
        "javascript": {
            "beginner": {
                "title": "JavaScript for Beginners",
                "description": "Learn the fundamentals of JavaScript, one of the most popular programming languages for web development.",
                "image": "https://static.skillshare.com/uploads/video/thumbnails/0ab63be061d2a2051fc5a20337d2bc7f/original",
            },
            "intermediate": {
                "title": "Intermediate JavaScript",
                "description": "Deepen your understanding of JavaScript with topics like async programming, DOM manipulation, and modern JavaScript frameworks.",
                "image": "https://static-assets.codecademy.com/assets/course-landing-page/meta/4x3/learn-intermediate-javascript.jpg",
            },
            "advanced": {
                "title": "Advanced JavaScript",
                "description": "Master advanced concepts like closures, the event loop, and building complex applications with JavaScript.",
                "image": "https://cdn0.knowledgecity.com/opencontent/courses/previews/CMP1282/800--v112252.jpg",
            },
        },
        "django": {
            "beginner": {
                "title": "Django for Beginners",
                "description": "Learn how to build web applications using Django, one of the most popular web frameworks in Python.",
                "image": "https://codewithstein.com/media/media/uploads/course_images/Cws_-_premium.006.jpeg",
            },
            "intermediate": {
                "title": "Intermediate Django",
                "description": "Take your Django skills to the next level by learning advanced techniques like creating APIs, using Django Rest Framework, and working with databases.",
                "image": "https://justdjango.com/_next/image?url=https%3A%2F%2Fjustdjango-static.sfo2.digitaloceanspaces.com%2Fmedia%2Fcourse_thumbnails%2Fintermediate.png&w=1920&q=75",
            },
            "advanced": {
                "title": "Advanced Django",
                "description": "Master Django with advanced concepts such as optimization, security, and deployment strategies.",
                "image": "https://d3s1xydsbc15sr.cloudfront.net/media/elearning/skill/Django_Advanced.jpg",
            },
        },
    }

  
    html_content = '''
    <style>{{ css }}</style>
    

    <header>
        <div class="container">
            <h1>{{ course.title }}</h1>
            <p>{{ course.description }}</p>
        </div>
    </header>

    <main>
        <section class="course-container">
            <div class="course-card">
                <img src="{{ course.image }}" alt="{{ course.title }}">
                <div class="course-info">
                    <h2>{{ course.title }}</h2>
                    <p>{{ course.description }}</p>
                    <a href="#" class="btn">Start Learning</a>
                </div>
            </div>
        </section>
    </main>
    '''

  
    context={
        'course':courses[course_name][course_level],
        'title':course_name,
        'css':css
    }
    code = Template(html_content).render(Context(context))
    return render(request, "index.html", {"code": code})
    
