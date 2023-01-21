function getCommonOptions() {
    const authToken = localStorage.getItem("authToken");

    // If no token return empty object
    if (!authToken) {
        return {};
    }

    return {
        headers: {
            Authorization: `Token ${authToken}`
        }
    }
}

export default getCommonOptions;