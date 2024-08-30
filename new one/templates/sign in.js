document.getElementById('sign-in-form').addEventListener('submit', function(event) {
    event.preventDefault();
    validateSignInForm();
});

function validateSignInForm() {
    clearErrors();
    const username = document.getElementById('sign-in-username').value;
    const password = document.getElementById('sign-in-password').value;
    let valid = true;

    if (!validateUsername(username)) {
        showError('sign-in-username-error', 'Username must be at least 3 characters and contain only letters and numbers');
        valid = false;
    }

    if (password.length < 6) {
        showError('sign-in-password-error', 'Password must be at least 6 characters');
        valid = false;
    }

    if (valid) {
        alert('Sign In Successful');
    }
}

function validateUsername(username) {
    const re = /^[a-zA-Z0-9]{3,}$/;
    return re.test(username);
}

function showError(elementId, message) {
    const errorElement = document.getElementById(elementId);
    errorElement.innerText = message;
}

function clearErrors() {
    const errorElements = document.querySelectorAll('.error');
    errorElements.forEach(element => element.innerText = '');
}
