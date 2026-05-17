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

  const users =
    JSON.parse(localStorage.getItem("users") || "[]");

  const user = users.find(
    (u) =>
      u.email === email &&
      u.password === password
  );

  // Successful Login
  if (user) {

    currentUser = {
      name: user.name,
      email: user.email
    };

    localStorage.setItem(
      "currentUser",
      JSON.stringify(currentUser)
    );

    updateNav();

    showHome();

    e.target.reset();
  }

  // Failed Login
  else {

    alert("Invalid email or password!");
  }
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

  const users =
    JSON.parse(localStorage.getItem("users") || "[]");

  // Check Existing User
  if (
    users.some((u) => u.email === newUser.email)
  ) {

    alert("Email already registered!");

    return;
  }

  // Save User
  users.push(newUser);

  localStorage.setItem(
    "users",
    JSON.stringify(users)
  );

  alert("Account created successfully! Please login.");

  showLogin();

  e.target.reset();
}

// =========================
// LOGOUT FUNCTION
// =========================
function logout() {

  currentUser = null;

  localStorage.removeItem("currentUser");

  updateNav();

  showHome();
}