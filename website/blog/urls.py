from django.urls import path
from .views import*

urlpatterns =[
    path('',home,name='home'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    path('gallery/',gallery,name='gallery'),
    path('reviews/',reviews,name='reviews'),
    path('courses/',courses,name='courses'),
    
    path('courses/<str:course>/', course, name='course'),
    path('courses/<str:course_name>/<str:course_level>/', course_learn, name='course_detail'),
]
   
    
#  css = '''
#        /* Global Styles */
# body {
#   font-family: Arial, sans-serif;
#   line-height: 1.6;
#   margin: 0;
#   padding: 0;
#   background-color: #f4f4f9;
#   color: #333;
# }

# /* About Section */
# .about {
#   background-color: #fff;
#   padding: 4rem 2rem;
#   color: #333;
# }

# .about .container {
#   max-width: 900px;
#   margin: 0 auto;
#   padding: 0 2rem;
# }

# .about h1, .about h2 {
#   font-size: 2rem;
#   color: #1eff7c;
#   text-align: center;
#   margin-bottom: 1rem;
# }

# .about p {
#   font-size: 1.1rem;
#   color: #666;
#   line-height: 1.8;
#   text-align: center;
#   margin-bottom: 1.5rem;
# }

# /* List styling */
# .about ul {
#   list-style: none;
#   padding-left: 0;
# }

# .about ul li {
#   font-size: 1.1rem;
#   color: #333;
#   margin-bottom: 1rem;
#   line-height: 1.6;
# }

# .about ul li strong {
#   color: #1eff7c;
# }

# .about a {
#   color: #1eff7c;
#   text-decoration: none;
# }

# .about a:hover {
#   text-decoration: underline;
#   color: #0056b3;
# }

# /* Section Spacing */
# .about h2 {
#   margin-top: 2rem;
# }

# /* Mobile Responsive Design */
# @media (max-width: 768px) {
#   .about h1, .about h2 {
#     font-size: 1.6rem;
#   }

#   .about p {
#     font-size: 1rem;
#   }

#   .about ul li {
#     font-size: 1rem;
#   }
# }

#          '''
#     html_content='''
#     <style>{{css}}</style>  
#   <!-- About Section -->
#   <section class="about">
#     <div class="container">
#       <h1>About RARE SYNTAX</h1>
#       <p>RARE SYNTAX is a platform dedicated to providing high-quality tech education in various programming languages. We focus on empowering learners with the skills they need to succeed in the ever-evolving world of software development.</p>

#       <h2>Our Mission</h2>
#       <p>Our mission is to bridge the knowledge gap in the tech industry by providing affordable and accessible education. Whether you're just starting your coding journey or looking to expand your skills, we offer comprehensive courses that cater to all levels of learners.</p>

#       <h2>What We Offer</h2>
#       <p>We specialize in offering courses in:</p>
#       <ul>
#         <li><strong>Python</strong> – Learn one of the most versatile programming languages used in data science, web development, and automation.</li>
#         <li><strong>JavaScript</strong> – Master the language of the web, from front-end development to back-end frameworks like Node.js.</li>
#         <li><strong>Django</strong> – Dive into web development with one of the most popular Python frameworks for building robust applications.</li>
#       </ul>

#       <h2>Why Choose Us?</h2>
#       <p>At RARE SYNTAX, we offer a unique approach to learning that combines theory with practical, real-world projects. Our courses are designed to make learning engaging and interactive, helping you retain knowledge and build confidence in your coding skills.</p>

#       <h2>Our Team</h2>
#       <p>RARE SYNTAX was founded by passionate tech enthusiasts with years of experience in the software industry. Our team is committed to providing the best learning experience, tailored to meet the needs of both beginners and advanced learners.</p>

#       <h2>Contact Us</h2>
#       <p>If you have any questions or need further information about our courses, feel free to reach out to us:</p>
#       <ul>
#         <li>Email: <a href="mailto:raresyntax@gmail.com">raresyntax@gmail.com</a></li>
#         <li>Phone: +91 9731383927</li>
#         <li>Website: <a href="http://www.raresyntax.in">www.raresyntax.in</a></li>
#       </ul>
#     </div>
#   </section>
# '''