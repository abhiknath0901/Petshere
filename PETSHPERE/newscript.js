let currentUser = null;

// Initialize on page load
document.addEventListener("DOMContentLoaded", init);

function init() {
  const savedUser = localStorage.getItem("currentUser");

  if (savedUser) {
    currentUser = JSON.parse(savedUser);
    updateNav();
  }

  setupEventListeners();
}

// =========================
// EVENT LISTENERS
// =========================
function setupEventListeners() {

  // Navigation buttons
  document.getElementById("homeNav")?.addEventListener("click", showHome);
  document.getElementById("loginNav")?.addEventListener("click", showLogin);
  document.getElementById("signupNav")?.addEventListener("click", showSignup);

  // Login form
  document
    .getElementById("loginForm")
    ?.addEventListener("submit", handleLogin);

  // Signup form
  document
    .getElementById("signupForm")
    ?.addEventListener("submit", handleSignup);
}

// =========================
// PAGE NAVIGATION
// =========================
function showPage(pageId) {

  document.querySelectorAll(".page").forEach((page) => {
    page.classList.remove("active");
  });

  document.getElementById(pageId)?.classList.add("active");
}

function showHome() {
  showPage("homePage");
}

function showLogin() {
  showPage("loginPage");
}

function showSignup() {
  showPage("signupPage");
}

// =========================
// NAVBAR UPDATE
// =========================
function updateNav() {

  const navAuth = document.getElementById("navAuth");

  if (!navAuth) return;

  // User Logged In
  if (currentUser) {

    navAuth.innerHTML = `
      <div class="user-info">
        <span class="user-name">
          👤 ${currentUser.name}
        </span>

        <button 
          class="logout-btn" 
          onclick="logout()"
        >
          Logout
        </button>
      </div>
    `;

  }

  // User Logged Out
  else {

    navAuth.innerHTML = `
      <button 
        class="nav-btn" 
        onclick="showLogin()"
      >
        Login
      </button>

      <button 
        class="nav-btn" 
        onclick="showSignup()"
      >
        Signup
      </button>
    `;
  }
}

// =========================
// LOGIN FUNCTION
// =========================


function handleLogin(e) {

  e.preventDefault();

  const email =
    document.getElementById("loginEmail").value;

  const password =
    document.getElementById("loginPassword").value;

  fetch(`${API_URL}/petshpere/login/`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ email, password })
  })
    .then(response => response.json())
    .then(data => {

      if (data.access && data.refresh && data.user) {
        localStorage.setItem("access", data.access);
        localStorage.setItem("refresh", data.refresh);
        localStorage.setItem("currentUser", JSON.stringify(data.user));
        console.log("Logged In");
        currentUser = data.user;
        updateNav();

        showHome();

        e.target.reset();

      } else {
        console.log(data.error);
        alert("Login failed: " + data.error);

      }
    }).catch(error => {
      console.log(error);

    })

}



// =========================
// SIGNUP FUNCTION
// =========================
function handleSignup(e) {

  e.preventDefault();

  const newUser = {

    name:
      document.getElementById("signupName").value,

    email:
      document.getElementById("signupEmail").value,

    password:
      document.getElementById("signupPassword").value,

    phone:
      document.getElementById("signupPhone").value,
  };

  fetch(`${API_URL}/petshpere/signup/`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(newUser)
  })
    .then(response => response.json())
    .then(data => {
      if (data.error) {

        console.log(data.error);
        alert("Signup failed: " + data.error);
        return

      }
      console.log(data.message);
      alert(data.message + " Please login to continue.");
      showLogin();
      e.target.reset();
    }).catch(error => {
      console.log(error);
    })


}

// =========================
// LOGOUT FUNCTION
// =========================
function logout() {
  const refresh = localStorage.getItem('refresh');
  const access = localStorage.getItem('access');
  fetch(`${API_URL}/petshpere/logout/`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${access}`
    },
    body: JSON.stringify({ refresh })
  })
    .then(response => response.json())
    .then(data => {
      if (data.error) {
        console.log(data.error);
        alert("Logout failed: " + data.error);
        return;
      }
      console.log(data.message);
      
      currentUser = null;

      localStorage.removeItem("currentUser");
      localStorage.removeItem("access");
      localStorage.removeItem("refresh");
      alert(data.message);

      updateNav();

      showHome();
    })
    .catch(error => {
      console.log(error);
    });


}