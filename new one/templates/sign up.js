document.getElementById('sign-up-form').addEventListener('submit', function(event) {
    event.preventDefault();
    validateSignUpForm();
});

function validateSignUpForm() {
    clearErrors();
    const username = document.getElementById('sign-up-username').value;
    const email = document.getElementById('sign-up-email').value;
    const password = document.getElementById('sign-up-password').value;
    const confirmPassword = document.getElementById('confirm-password').value;
    let valid = true;

    if (!validateUsername(username)) {
        showError('sign-up-username-error', 'Username must be at least 3 characters and contain only letters and numbers');
        valid = false;
    }

    if (!validateEmail(email)) {
        showError('sign-up-email-error', 'Invalid email format');
        valid = false;
    }

    if (password.length < 6) {
        showError('sign-up-password-error', 'Password must be at least 6 characters');
        valid = false;
    }

    if (password !== confirmPassword) {
        showError('confirm-password-error', 'Passwords do not match');
        valid = false;
    }

    if (valid) {
        alert('Sign Up Successful');
    }
}

function validateUsername(username) {
    const re = /^[a-zA-Z0-9]{3,}$/;
    return re.test(username);
}

function validateEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
}

function showError(elementId, message) {
    const errorElement = document.getElementById(elementId);
    errorElement.innerText = message;
}

function clearErrors() {
    const errorElements = document.querySelectorAll('.error');
    errorElements.forEach(element => element.innerText = '');
}
