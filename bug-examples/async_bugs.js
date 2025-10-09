/**
 * Bug Example 4: Async/Callback Issues (JavaScript)
 * This code has common async bugs and race conditions
 */

// Bug 1: Not handling async properly
function fetchUserData(userId) {
    let userData = null;
    
    // Simulating an API call
    setTimeout(() => {
        userData = {
            id: userId,
            name: 'John Doe',
            email: 'john@example.com'
        };
    }, 100);
    
    // Bug: Returns null because setTimeout hasn't executed yet
    return userData;
}

// Bug 2: Race condition in concurrent operations
async function processMultipleUsers(userIds) {
    let results = [];
    
    // Bug: All requests start simultaneously, but results may be in wrong order
    for (let id of userIds) {
        fetch(`https://api.example.com/users/${id}`)
            .then(response => response.json())
            .then(data => {
                results.push(data);  // Bug: Results may not be in order
            });
    }
    
    return results;  // Bug: Returns immediately, before any fetch completes
}

// Bug 3: Missing error handling
async function saveUserData(user) {
    // Bug: No try-catch, will crash if API call fails
    const response = await fetch('https://api.example.com/users', {
        method: 'POST',
        body: JSON.stringify(user)
    });
    
    const data = await response.json();
    return data;
}

// Bug 4: Callback hell with errors
function complexOperation(callback) {
    setTimeout(() => {
        const data1 = { value: 10 };
        
        setTimeout(() => {
            const data2 = { value: data1.value + 20 };
            
            setTimeout(() => {
                const data3 = { value: data2.value + 30 };
                
                // Bug: What if any of these operations fail?
                // No error handling in the nested callbacks
                callback(data3);
            }, 100);
        }, 100);
    }, 100);
}

// Bug 5: Memory leak with event listeners
class DataManager {
    constructor() {
        this.data = [];
        this.listeners = [];
    }
    
    addListener(callback) {
        this.listeners.push(callback);
        
        // Bug: No way to remove listeners, causing memory leaks
        setInterval(() => {
            callback(this.data);
        }, 1000);
    }
    
    addData(item) {
        this.data.push(item);
    }
}

// Test cases
console.log('Testing async bugs...');

// Test 1: Will return null instead of user data
const user = fetchUserData(123);
console.log('User data:', user);  // Prints: User data: null

// Test 2: Will return empty array
processMultipleUsers([1, 2, 3]).then(results => {
    console.log('Results:', results);  // Prints: Results: []
});

// Test 3: Create memory leaks
const manager = new DataManager();
for (let i = 0; i < 100; i++) {
    manager.addListener((data) => {
        console.log('Data updated:', data.length);
    });
}
