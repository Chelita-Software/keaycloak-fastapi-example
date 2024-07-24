async function callVerifyAuth() {
    const response = await fetch("http://fast-api:8001/auth/verify", {
        method: "GET",
        credentials: "include", // This might not be needed in production
        headers:{
            "Content-Type": "application/json",
        },
    });
    const result = await response.json();
    console.log(response);
    if (!response.ok) {
        throw new Error(response.statusText);
    }
    return result;
}

export { callVerifyAuth };