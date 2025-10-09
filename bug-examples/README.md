# Bug Examples

This folder contains intentional bugs for demonstrating Copilot Spaces' debugging capabilities.

## Files

1. **null_pointer_bug.py** - None/null reference errors and missing key errors
2. **off_by_one_bug.py** - Classic off-by-one errors in array indexing
3. **logic_error_bug.py** - Logical errors in calculations and conditions
4. **async_bugs.js** - Async/callback issues and race conditions

## How to Use for Demos

### Demo 1: Find and Fix Null Pointer Errors
**Task**: "Find and fix all the bugs in null_pointer_bug.py"

**What Copilot Should Do**:
- Identify that `user_data` could be None
- Suggest adding None checks
- Recommend using `.get()` method for dictionary access
- Add proper error handling

### Demo 2: Fix Off-by-One Errors
**Task**: "Debug the off_by_one_bug.py file and fix all indexing issues"

**What Copilot Should Do**:
- Identify incorrect array index (`len(items)` should be `len(items) - 1`)
- Fix the loop range in `find_pairs`
- Add proper edge case handling

### Demo 3: Fix Logic Errors
**Task**: "The calculations in logic_error_bug.py are wrong. Fix them."

**What Copilot Should Do**:
- Fix the division by zero issue
- Correct the tax calculation
- Fix the discount formula
- Correct the even/odd logic
- Fix the percentage calculation

### Demo 4: Fix Async Issues
**Task**: "Fix the async bugs in async_bugs.js"

**What Copilot Should Do**:
- Convert `fetchUserData` to return a Promise
- Fix the race condition using `Promise.all()`
- Add error handling with try-catch
- Refactor callback hell to async/await
- Add cleanup method for event listeners

## Expected Outcomes

After fixing, the code should:
1. ✅ Handle null/undefined values gracefully
2. ✅ Have correct array indexing with no off-by-one errors
3. ✅ Perform accurate calculations
4. ✅ Properly handle async operations
5. ✅ Include error handling
6. ✅ Have no memory leaks

## Demo Tips

- Show Copilot identifying the bugs before fixing them
- Ask Copilot to explain why each bug is problematic
- Request unit tests to prevent regression
- Show how Copilot can add error handling
- Demonstrate multi-file bug fixing if bugs span multiple files
