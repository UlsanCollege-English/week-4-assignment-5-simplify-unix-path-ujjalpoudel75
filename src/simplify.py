# /src/simplify.py

def simplify_path(path: str) -> str:
    """
    Normalizes an absolute path string using a stack.
    Handles '.', '..', and multiple or trailing slashes.
    """
    stack = []
    
    # 1. Split the path by '/', which handles multiple consecutive slashes, 
    #    and filters out empty strings and the special '.' segment.
    segments = path.split('/')

    # 2. Process each segment
    for segment in segments:
        if segment == '..':
            # If '..', pop the last directory name off the stack, 
            # unless the stack is empty (we're at the root).
            if stack:
                stack.pop()
        elif segment == '.' or segment == '':
            # Ignore '.' (current directory) and empty strings (from multiple slashes).
            continue
        else:
            # Valid directory name: push it onto the stack.
            stack.append(segment)

    # 3. Join the stack elements to form the final path
    # The path must always start with a single '/'
    if not stack:
        return "/"
    else:
        # Join the elements with '/' and prepend the root '/'
        return "/" + "/".join(stack)