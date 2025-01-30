**ClickSafe: Phishing Simulation Tool**

**ClickSafe** is a phishing simulation tool developed with **Python**, **Flask**, and **Flask-Mail** to help train users on identifying phishing emails. The tool simulates phishing campaigns and tracks user interactions, offering insights and reports to raise awareness about phishing attacks.

 **Features**
- **Phishing Email Simulation**: Send realistic phishing emails to users.
- **User Interaction Tracking**: Track which users clicked on the phishing link.
- **Report Generation**: Generate detailed reports based on user interactions.
- **Email Customization**: Use customizable email templates for phishing simulations.


**Installation**

Follow these steps to set up **ClickSafe** locally:

**1. Clone the Repository**
Clone the repository to your local machine:

```bash
git clone https://github.com/your-username/ClickSafe.git
```

**2. Set up a Virtual Environment**

To isolate dependencies, create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

- **Windows**:
  ```bash
  venv\Scripts\activate
  ```

- **Mac/Linux**:
  ```bash
  source venv/bin/activate
  ```

### **3. Install Dependencies**

Install the required dependencies using **pip**:

```bash
pip install -r requirements.txt
```

### **4. Set Up Email Credentials**

1. Create a `.env` file in the root of the project and add your email credentials.

```bash
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password
```

2. You will need to create an **App Password** if you are using Gmail for sending emails. Instructions can be found [here](https://support.google.com/accounts/answer/185833).

---

**Usage**

**Running the Application**

To run the application locally, use the following command:

```bash
python clicksafe.py
---

By default, the app will be available at `http://127.0.0.1:5000/`.


Email Simulation
- Navigate to `http://127.0.0.1:5000/send-email` to send a phishing email.
- The app will send an email to the specified recipient with a phishing link.


Report Generation
- Reports will automatically be generated based on user interactions.
- You can view the report output in the terminal or extend it to a more user-friendly format.


License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.
