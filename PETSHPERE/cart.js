// ── cart.js ── shared cart utilities ──────────────────────────────────────

function getCart() {
  return JSON.parse(localStorage.getItem("petCart") || "[]");
}

function saveCart(cart) {
  localStorage.setItem("petCart", JSON.stringify(cart));
}

function addToCart(pet) {
  const cart = getCart();
  const existing = cart.find(item => item.id === pet.id);
  if (existing) {
    existing.qty = (existing.qty || 1) + 1;
  } else {
    cart.push({ id: pet.id, name: pet.name, price: pet.price, img: pet.img, type: pet.type, qty: 1 });
  }
  saveCart(cart);
  showToast(`${pet.name} added to cart 🛒`);
  updateCartBadge();
}

function removeFromCart(petId) {
  const cart = getCart().filter(item => item.id !== petId);
  saveCart(cart);
  updateCartBadge();
}

function clearCart() {
  localStorage.removeItem("petCart");
  updateCartBadge();
}

function getCartCount() {
  return getCart().reduce((sum, item) => sum + (item.qty || 1), 0);
}

function updateCartBadge() {
  const badge = document.getElementById("cartBadge");
  if (badge) {
    const count = getCartCount();
    badge.textContent = count;
    badge.style.display = count > 0 ? "flex" : "none";
  }
}

// ── Toast notification ────────────────────────────────────────────────────
function showToast(msg) {
  let toast = document.getElementById("cartToast");
  if (!toast) {
    toast = document.createElement("div");
    toast.id = "cartToast";
    toast.style.cssText = `
      position:fixed; bottom:30px; left:50%; transform:translateX(-50%) translateY(80px);
      background:#5d4037; color:#fff; padding:14px 28px; border-radius:40px;
      font-family:Poppins,sans-serif; font-size:14px; font-weight:500;
      box-shadow:0 8px 30px rgba(62,39,35,0.35); z-index:9999;
      transition:transform 0.35s cubic-bezier(.34,1.56,.64,1), opacity 0.3s;
      opacity:0; pointer-events:none;
    `;
    document.body.appendChild(toast);
  }
  toast.textContent = msg;
  toast.style.opacity = "1";
  toast.style.transform = "translateX(-50%) translateY(0)";
  clearTimeout(toast._timer);
  toast._timer = setTimeout(() => {
    toast.style.opacity = "0";
    toast.style.transform = "translateX(-50%) translateY(80px)";
  }, 2500);
}

// Run badge update on load
document.addEventListener("DOMContentLoaded", updateCartBadge);