// Basic JavaScript for Hotel Management System
const API_BASE_URL = 'http://localhost:8000/api/v1';

// DOM Elements
const loginForm = document.getElementById('login-form');
const pages = document.querySelectorAll('.page');

// State
let currentUser = null;
let authToken = null;

// Show a specific page and hide others
function showPage(pageId) {
    pages.forEach(page => {
        if (page.id === pageId) {
            page.classList.remove('hidden');
        } else {
            page.classList.add('hidden');
        }
    });
}

// Handle login form submission
loginForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    
    try {
        const response = await fetch(`${API_BASE_URL}/auth/login`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: `username=${encodeURIComponent(username)}&password=${encodeURIComponent(password)}`
        });
        
        if (response.ok) {
            const data = await response.json();
            authToken = data.access_token;
            currentUser = { username, role: data.role };
            
            // Update UI
            document.getElementById('user-info').innerHTML = `
                <p>Welcome, ${username}!</p>
                <p>Role: ${data.role}</p>
                <button id="logout-btn">Logout</button>
            `;
            
            document.getElementById('logout-btn').addEventListener('click', logout);
            
            // Show dashboard
            showPage('dashboard');
            
            // Load dashboard data
            loadDashboardData();
        } else {
            alert('Login failed. Please check your credentials.');
        }
    } catch (error) {
        console.error('Login error:', error);
        alert('An error occurred during login.');
    }
});

// Logout function
function logout() {
    authToken = null;
    currentUser = null;
    showPage('login');
    document.getElementById('login-form').reset();
}

// Load dashboard data
async function loadDashboardData() {
    if (!authToken) return;
    
    try {
        // Fetch counts for rooms, guests, and orders
        const [roomsResponse, guestsResponse, ordersResponse] = await Promise.all([
            fetch(`${API_BASE_URL}/rooms`, {
                headers: { 'Authorization': `Bearer ${authToken}` }
            }),
            fetch(`${API_BASE_URL}/guests`, {
                headers: { 'Authorization': `Bearer ${authToken}` }
            }),
            fetch(`${API_BASE_URL}/orders`, {
                headers: { 'Authorization': `Bearer ${authToken}` }
            })
        ]);
        
        if (roomsResponse.ok && guestsResponse.ok && ordersResponse.ok) {
            const rooms = await roomsResponse.json();
            const guests = await guestsResponse.json();
            const orders = await ordersResponse.json();
            
            document.getElementById('room-count').textContent = rooms.length;
            document.getElementById('guest-count').textContent = guests.length;
            document.getElementById('order-count').textContent = orders.length;
        }
    } catch (error) {
        console.error('Error loading dashboard data:', error);
    }
}

// Initialize the app
document.addEventListener('DOMContentLoaded', () => {
    showPage('login');
});