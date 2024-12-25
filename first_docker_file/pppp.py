from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # Add Oracle logo as a watermark on every page
        self.set_font("Arial", "B", 16)
        self.set_text_color(200, 200, 200)  # Light grey color
        self.image("quantum_watermark.png", x=50, y=70, w=100, h=100)  # Adjust position and size as needed

# Create a PDF document
pdf = PDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# Set title
pdf.set_font("Arial", "B", 16)
pdf.cell(170, 10, txt="Student Grievance Management System", ln=True, align="C")

# Add "Report by" section
pdf.set_font("Arial", "I", 12)
pdf.cell(170, 10, txt="Report by:", ln=True, align="C")
pdf.set_font("Arial", "", 12)
contributors = "1. Ankit Raj  2. Akash Gupta  3. Aniket Saini  4. Prasant Gupta  5. Parmjeet Yadav"
pdf.cell(170, 10, txt=contributors, ln=True, align="C")

# Add a line break
pdf.ln(10)

# Add the Abstract Section
pdf.set_font("Arial", "B", 16)
pdf.cell(170, 10, txt="Abstract", ln=True)
pdf.set_font("Arial", "", 16)
abstract_text = """
The Student Grievance Management System is an innovative solution designed to address the challenges students face in voicing their concerns within educational institutions. 
This system ensures a transparent, efficient, and student-friendly process for managing grievances, which traditional methods often lack. 
The platform offers students a way to submit issues, track resolutions, and provide feedback, thus fostering accountability and improving satisfaction. 
By integrating technology into grievance handling, institutions can bridge the communication gap between students and administrators, ensuring timely and effective resolutions. 
This report delves into the system's framework, highlighting its features, workflow, and potential impact on institutional management.
"""
pdf.multi_cell(0, 10, txt=abstract_text)

# Add a line break
pdf.ln(5)

# Add the Introduction Section
pdf.set_font("Arial", "B", 16)
pdf.cell(170, 10, txt="Introduction", ln=True)
pdf.set_font("Arial", "", 16)
introduction_text = """
The Student Grievance Management System is an innovative solution designed to address the challenges students face in voicing their concerns within educational institutions. 
This system ensures a transparent, efficient, and student-friendly process for managing grievances, which traditional methods often lack. 
The platform offers students a way to submit issues, track resolutions, and provide feedback, thus fostering accountability and improving satisfaction. 
By integrating technology into grievance handling, institutions can bridge the communication gap between students and administrators, ensuring timely and effective resolutions. 
This report delves into the system's framework, highlighting its features, workflow, and potential impact on institutional management.The Student Grievance Management System is 
a web-based platform that addresses these issues. It streamlines the grievance process by providing a centralized solution that empowers students to raise concerns and track resolutions. 
This report aims to provide insights into the system's functionality, its relevance in educational settings, and its ability to improve institutional transparency.
"""
pdf.multi_cell(0, 10, txt=introduction_text)

# Add a line break
pdf.ln(5)

# Add the problem_statement Section
pdf.set_font("Arial", "B", 16)
pdf.cell(170, 10, txt="Problem_statement", ln=True)
pdf.set_font("Arial", "", 16)
problem_statement_text = """
Handling student grievances effectively has always been a challenging task for educational institutions. The traditional methods, often paper-based or reliant on face-to-face 
communication, are inefficient and lack transparency. These processes result in delayed responses, lost grievances, and student frustration, which ultimately harm the institution's 
reputation. Moreover, tracking and managing grievances without a digital solution is cumbersome and prone to errors. Institutions require a streamlined system to address these challenges, 
improve communication, and ensure timely resolutions. The Student Grievance Management System aims to resolve these issues by providing a digital platform that simplifies and enhances grievance 
handling processes.
"""
pdf.multi_cell(0, 10, txt=problem_statement_text)

# Add a line break
pdf.ln(5)

# Add the objectives Section
pdf.set_font("Arial", "B", 16)
pdf.cell(170, 10, txt="Objective", ln=True)
pdf.set_font("Arial", "", 16)
objective_text = """
The objectives of the Student Grievance Management System are as follows:

1. To provide students with an easy-to-use interface for submitting grievances, ensuring accessibility and simplicity.
2. To maintain transparency throughout the grievance process by offering status tracking and regular updates.
3. To enable categorization and prioritization of grievances for more efficient management.
4. To create a centralized system that reduces paperwork and manual intervention.
5. To foster better communication between students and administrators, enhancing trust and satisfaction.
6. By achieving these objectives, the system ensures that grievances are resolved promptly and efficiently, contributing to a positive institutional environment.
"""
pdf.multi_cell(0, 10, txt=objective_text)

# Add a line break
pdf.ln(5)

# Add the system_workflow Section
pdf.set_font("Arial", "B", 16)
pdf.cell(170, 10, txt="System_workflow", ln=True)
pdf.set_font("Arial", "", 16)
system_workflow_text = """
The workflow of the Student Grievance Management System is designed to ensure efficiency and transparency at every step.

1. Login and Authentication: Students log into the system using unique credentials to ensure secure access.
2. Grievance Submission: Students fill out a detailed form to submit grievances, categorizing them under appropriate types such as academic, administrative, or personal issues.
3. Grievance Routing: The system automatically forwards grievances to the relevant department or individual for review.
4. Review and Assignment: The concerned department reviews the grievance and assigns it to the appropriate personnel for resolution.
5. Resolution Update: Once resolved, the status is updated in the system, and the student is notified via email or SMS.
6. Feedback Collection: Students provide feedback on the resolution process, enabling continuous improvement.
"""
pdf.multi_cell(0, 10, txt=system_workflow_text)

# Add a line break
pdf.ln(5)

# Add the main_features Section
pdf.set_font("Arial", "B", 16)
pdf.cell(170, 10, txt="Main_features", ln=True)
pdf.set_font("Arial", "", 16)
main_features_text = """
The Student Grievance Management System includes several key features:

1. User-Friendly Interface: Designed to make grievance submission intuitive and straightforward for students.
2. Grievance Categorization: Automatically categorizes grievances into academic, administrative, or facility-related issues for better organization.
3. Real-Time Tracking: Allows students to monitor the progress of their grievances at any stage.
4. Role-Based Access: Ensures that only authorized personnel can access and manage specific grievances.
5. Feedback Mechanism: Collects student feedback post-resolution to ensure continuous improvement of the process.
6. Data Analytics: Provides administrators with insights into common grievances, helping institutions address recurring issues effectively.
"""
pdf.multi_cell(0, 10, txt=main_features_text)

# Add a line break
pdf.ln(5)

# Add the use_cases Section
pdf.set_font("Arial", "B", 16)
pdf.cell(170, 10, txt="Use_cases", ln=True)
pdf.set_font("Arial", "", 16)
use_cases_text = """
The Student Grievance Management System can be applied in multiple scenarios:

1. Academic Concerns: A student submits a grievance regarding a scheduling conflict with exams. The academic department addresses the issue promptly.
2. Facility Maintenance: A student reports a broken air conditioner in a lecture hall. The grievance is forwarded to the maintenance department for quick resolution.
3. Administrative Issues: A student raises a concern about delays in receiving official documents, which the administrative staff resolves efficiently.
4. Disciplinary Actions: A student feels unfairly treated during a disciplinary hearing and submits a grievance for review by higher authorities.
"""
pdf.multi_cell(0, 10, txt=use_cases_text)

# Add a line break
pdf.ln(5)

# Add the technological_stact Section
pdf.set_font("Arial", "B", 16)
pdf.cell(170, 10, txt="Technological_stact", ln=True)
pdf.set_font("Arial", "", 16)
technological_stack_text = """
The system leverages modern technologies to provide a robust and scalable platform:

1. Frontend: HTML, CSS, and JavaScript are used to create a responsive and visually appealing user interface.
2. Backend: Python with the Django framework handles server-side operations and database interactions.
3. Database: MySQL provides secure and efficient storage for grievance data.
4. Hosting: Cloud platforms such as AWS or Google Cloud ensure reliable deployment and scalability.
5. Authentication: OAuth or similar protocols are implemented for secure user login and data access.
"""
pdf.multi_cell(0, 10, txt=technological_stack_text)

# Add a line break
pdf.ln(5)

# Add the future_scope Section
pdf.set_font("Arial", "B", 16)
pdf.cell(170, 10, txt="Future_scope", ln=True)
pdf.set_font("Arial", "", 16)
future_scope_text = """
The Student Grievance Management System has immense potential for growth:

1. Mobile Integration: Development of a dedicated mobile app for seamless access to the system.
2. AI-Powered Insights: Implementation of AI tools to predict grievance resolution times and provide automated responses for common queries.
3. Multi-Language Support: Catering to students from diverse linguistic backgrounds by offering multi-language options.
4. Advanced Analytics: Integration of analytics dashboards to help administrators identify trends and take proactive measures.
5. Integration with ERP Systems: Connecting the grievance system with existing institutional ERP systems for better synchronization and data management.
"""
pdf.multi_cell(0, 10, txt=future_scope_text)

# Add a line break
pdf.ln(5)

# Add the conclusion Section
pdf.set_font("Arial", "B", 16)
pdf.cell(170, 10, txt="Conclusion", ln=True)
pdf.set_font("Arial", "", 16)
conclusion_text = """
The Student Grievance Management System revolutionizes the traditional methods of handling student grievances. By providing a centralized, 
transparent, and efficient platform, it empowers students and enhances institutional accountability. The system not only resolves grievances 
faster but also builds trust between students and administrators. With its advanced features and potential for future enhancements, it is a step 
toward modernizing grievance management in educational institutions. This system is a testament to how technology can be leveraged to improve processes 
and create a positive academic environment.
"""
pdf.multi_cell(0, 10, txt=conclusion_text)

# Add a line break
pdf.ln(5)

# Add the refrence Section
pdf.set_font("Arial", "B", 16)
pdf.cell(170, 10, txt="Reference", ln=True)
pdf.set_font("Arial", "", 16)
reference_text = """
1. Online Grievance Management System: Enhancing Transparency and Accountability in Educational Institutions.
2. Best Practices for Building Student-Centric Applications, published by TechEd Journal.
3. Official documentation of Django framework and MySQL database.
4. Articles on grievance management trends in educational institutions, TechRadar Insights.
"""
pdf.multi_cell(0, 10, txt=reference_text)

#save the pdf to a file
<<<<<<< HEAD
pdf_output_path = "E:\\Ankitt\\student.pdf"

=======
pdf_output_path = r"E:\Ankitt\student.pdf"
>>>>>>> e9dc8f26904ebda5edb544fe373523010adddc92
pdf.output(pdf_output_path)

pdf_output_path
